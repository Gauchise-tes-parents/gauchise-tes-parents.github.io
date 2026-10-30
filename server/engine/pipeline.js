// Orchestration : recherche (phase 1) → vérification des preuves → stratégie (phase 2) → présentation.
// Gère aussi : cache des dossiers, mémoire des analyses (changement de mode sans tout relancer),
// budget financier mesuré, et dossiers construits à partir des fiches de la bibliothèque.
import { randomUUID, createHash } from 'node:crypto';
import { runResearch } from './research.js';
import { runStrategy } from './strategy.js';
import { runSpeech, runRephrase } from './speech.js';
import { sumCosts } from './cost.js';
import { EngineError, frToday, isoToday } from './util.js';
import { VERDICTS } from '../../public/js/taxonomy.js';
import { searchLibrary } from '../library.js';
import { compareWithFiche, recordProposal } from './knowledge.js';

/** Petit cache clé → valeur avec durée de vie et taille maximale (le plus ancien sort en premier). */
export class TtlStore {
  constructor({ ttlMs, max = 300, now = () => Date.now() }) {
    this.ttlMs = ttlMs;
    this.max = max;
    this.now = now;
    this.map = new Map();
  }

  get(key) {
    const e = this.map.get(key);
    if (!e) return undefined;
    if (this.now() - e.t > this.ttlMs) { this.map.delete(key); return undefined; }
    return e.v;
  }

  set(key, v) {
    this.map.delete(key);
    this.map.set(key, { v, t: this.now() });
    while (this.map.size > this.max) this.map.delete(this.map.keys().next().value);
  }
}

const normClaim = (s) => s.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/[^a-z0-9]+/g, ' ').trim();
export const researchKey = (req) => createHash('sha256').update(JSON.stringify([normClaim(req.claim), req.volet, req.sousTheme || '', Boolean(req.express)])).digest('base64url').slice(0, 22);

/** Dossier vérifié construit à partir d'une fiche de bibliothèque (sources déjà consultées par l'équipe). */
export function dossierFromFiche(fiche) {
  const sources = fiche.sources.map((s, i) => ({
    id: `S${i + 1}`, titre: s.titre, organisme: s.organisme, date_publication: s.date_publication, periode_couverte: s.periode_couverte || null,
    type: s.type || null, url: s.url, acces: s.consultee ? 'document_consulte' : 'non_consulte',
    acces_detail: s.consultee ? `Consultée par l'équipe lors de la vérification du ${fiche.derniere_verification}` : 'Non lue directement : à consulter pour vérification',
    extraits_cites: [], passage: s.passage || null, pertinence: s.pertinence || null, consultee: Boolean(s.consultee),
  }));
  return {
    reformulation: fiche.affirmation,
    verifiable: true,
    verdict: fiche.verdict || null,
    verdict_label: fiche.verdict ? VERDICTS[fiche.verdict] : null,
    fiabilite: fiche.fiabilite || null,
    stabilite: fiche.stabilite || null,
    objections_legitimes: fiche.objections_legitimes || [],
    citations: (fiche.citations || []).map((c) => ({ auteur: c.auteur, texte: c.texte, date: c.date, contexte: c.contexte || null, source: sources[c.source]?.id || null })),
    resume: fiche.resume,
    faits: fiche.faits.map((f, i) => ({
      id: `F${i + 1}`, fait: f.fait, chiffre: f.chiffre || null, periode: f.periode || null, perimetre: f.perimetre || null,
      montre: f.explication || null, ne_montre_pas: null, sens: 'contexte',
      source: sources[f.source]?.consultee ? sources[f.source].id : null, source_verifiee: Boolean(sources[f.source]?.consultee),
      controle_chiffre: { statut: 'fiche', detail: 'Chiffre relevé à la main dans la source lors de la vérification de la fiche.' },
    })),
    contradictions: [],
    alerte: null,
    jugements_de_valeur: [],
    manques: [],
    limites: fiche.limites || [],
    sources,
    sources_rejetees: [],
    avertissements: [],
    recherche: null,
    date_verification: fiche.derniere_verification,
  };
}

export function createEngine({ config, provider, library = [], ledger, logger = console }) {
  const dossiers = new TtlStore({ ttlMs: config.cacheTtlHours * 3600e3, max: 300 }); // clé de recherche → analyse
  const analyses = new TtlStore({ ttlMs: Math.max(config.cacheTtlHours, 6) * 3600e3, max: 500 }); // id → analyse

  const ensureBudget = (estimate) => {
    if (!ledger.canSpend(estimate)) {
      throw new EngineError('budget', "Le budget de ce serveur pour la période est atteint (plafond fixé pour maîtriser les coûts). La bibliothèque reste consultable ; réessaie plus tard.", 503);
    }
  };
  const bill = (requests, label) => {
    const c = sumCosts(requests, config.pricing, config.fallbackPricing);
    ledger.record(c.usd);
    logger.info?.(`[coût] ${label} ${c.usd.toFixed(4)} $ — recherches=${c.web_search_requests} consultations=${c.web_fetch_requests} jetons=${c.input_tokens}+${c.output_tokens}`);
    return c;
  };

  async function strategyFor(entry, { mode, profil, contexte, interlocuteur = null }) {
    const key = `${mode}|${profil}|${contexte}|${interlocuteur && !interlocuteur.inconnu ? JSON.stringify(interlocuteur) : ''}`;
    if (entry.strategies[key]) return { strategy: entry.strategies[key], cached: true };
    ensureBudget(config.estimateStrategyUsd);
    const { strategy, requests } = await runStrategy({
      provider, config, mode, dossier: entry.dossier, claim: entry.request.claim, profil, contexte, volet: entry.request.volet, express: entry.request.express, interlocuteur,
    });
    const cost = bill(requests, `stratégie:${mode}`);
    entry.couts.push({ etape: `strategie_${mode}`, ...cost });
    entry.strategies[key] = strategy;
    return { strategy, cached: false };
  }

  function present(entry, strategy, { cached = false } = {}) {
    const total = entry.couts.reduce((a, c) => a + c.usd, 0);
    return {
      mode: 'live',
      analyse_id: entry.id,
      origine: entry.origine,
      fiche_id: entry.ficheId || null,
      affirmation: entry.request.claim,
      volet: entry.request.volet,
      sous_theme: entry.request.sousTheme || null,
      express: Boolean(entry.request.express),
      comparaison_fiche: entry.comparaison || null,
      dossier: entry.dossier,
      strategie: strategy,
      cache: cached ? { depuis: entry.createdAt } : null,
      technique: {
        modele_recherche: entry.origine === 'recherche' ? config.researchModel : null,
        modele_strategie: config.strategyModel,
        cout_usd: Number(total.toFixed(4)),
        couts: entry.couts.map((c) => ({ etape: c.etape, usd: Number(c.usd.toFixed(4)), recherches: c.web_search_requests, consultations: c.web_fetch_requests })),
      },
    };
  }

  return {
    /** Analyse complète : réutilise un dossier récent identique si disponible (sauf recherche fraîche). */
    async analyse(req, { fiche = null } = {}) {
      const key = researchKey(req);
      let entry = req.fraiche ? undefined : dossiers.get(key);
      let cachedDossier = Boolean(entry);
      if (!entry) {
        ensureBudget(config.estimateResearchUsd + config.estimateStrategyUsd);
        // Pistes : les sources déjà vérifiées de la fiche correspondante (ou des fiches voisines).
        const proches = fiche ? [fiche] : searchLibrary(library, req.claim, null, null, { min: 3 }).slice(0, 2);
        const pistes = proches.flatMap((f) => f.sources.filter((s) => s.consultee).map((s) => s.url)).slice(0, 4);
        const { dossier, requests } = await runResearch({ provider, config, req, pistes, today: frToday(), isoDate: isoToday() });
        const cost = bill(requests, 'recherche');
        entry = { id: randomUUID(), createdAt: new Date().toISOString(), origine: 'recherche', request: req, dossier, strategies: {}, couts: [{ etape: 'recherche', ...cost }] };
        if (fiche) {
          // Comparaison web ↔ fiche : les écarts sont signalés et consignés, jamais appliqués automatiquement.
          entry.ficheId = fiche.id;
          entry.comparaison = compareWithFiche(dossier, fiche);
          if (entry.comparaison.mise_a_jour_proposee && config.storeUpdates && config.updatesFile) {
            await recordProposal(config.updatesFile, entry.comparaison, req.claim).catch((err) => logger.warn?.(`[base] proposition non enregistrée : ${err.message}`));
          }
        }
        dossiers.set(key, entry);
        analyses.set(entry.id, entry);
        cachedDossier = false;
      }
      const { strategy } = await strategyFor(entry, req);
      return present(entry, strategy, { cached: cachedDossier });
    },

    /** Changement de mode (ou d'interlocuteur) sans relancer la recherche. */
    async switchStrategy(id, opts) {
      const entry = analyses.get(id);
      if (!entry) throw new EngineError('expired', "Cette analyse n'est plus en mémoire (elle a expiré). Relance la vérification : tes choix sont conservés.", 410);
      const { strategy, cached } = await strategyFor(entry, opts);
      return present(entry, strategy, { cached });
    },

    /** Stratégie construite sur une fiche de bibliothèque (pas de recherche : sources déjà vérifiées). */
    async fromFiche(fiche, opts) {
      const id = `fiche-${fiche.id}-${fiche.derniere_verification}`;
      let entry = analyses.get(id);
      if (!entry) {
        entry = {
          id, ficheId: fiche.id, createdAt: new Date().toISOString(), origine: 'bibliotheque',
          request: { claim: fiche.affirmation, volet: fiche.volet, sousTheme: fiche.sous_theme, express: false },
          dossier: dossierFromFiche(fiche), strategies: {}, couts: [],
        };
        analyses.set(id, entry);
      }
      const { strategy, cached } = await strategyFor(entry, opts);
      return present(entry, strategy, { cached });
    },

    async rephrase(id, { variante, mode, profil, contexte, replique }) {
      const entry = analyses.get(id);
      if (!entry) throw new EngineError('expired', "Cette analyse n'est plus en mémoire. Relance la vérification.", 410);
      const { strategy } = await strategyFor(entry, { mode, profil, contexte });
      ensureBudget(config.estimateStrategyUsd);
      const r = await runRephrase({ provider, config, variante, replique: replique || strategy.replique, dossier: entry.dossier, claim: entry.request.claim });
      const cost = bill(r.requests, 'reformulation');
      entry.couts.push({ etape: `reformulation_${variante}`, ...cost });
      return { replique: r.replique };
    },

    async speech(id, { duree, mode, profil, contexte }) {
      const entry = analyses.get(id);
      if (!entry) throw new EngineError('expired', "Cette analyse n'est plus en mémoire. Relance la vérification.", 410);
      const { strategy } = await strategyFor(entry, { mode, profil, contexte });
      const key = `speech|${mode}|${duree}`;
      if (entry.strategies[key]) return entry.strategies[key];
      ensureBudget(config.estimateStrategyUsd);
      const { speech, requests } = await runSpeech({ provider, config, duree, mode, dossier: entry.dossier, strategy, claim: entry.request.claim });
      const cost = bill(requests, 'demonstration');
      entry.couts.push({ etape: `demonstration_${duree}s`, ...cost });
      entry.strategies[key] = speech;
      return speech;
    },
  };
}
