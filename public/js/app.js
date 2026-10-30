// Application monopage « Gauchise tes parents » — conçue d'abord pour le téléphone.
import { api } from './api.js';
import { store } from './store.js';
import { kb } from './kbstore.js';
import { nettoyerProfil, profilSimple, resumeProfil, strategieProfil } from './profile.js';
import { composer, questionsUtiles } from './composer.js';
import { suggestionsPour } from './suggestions.js';
import { nouvelleConversation, repondreConversation, enregistrerTour, analyserMessage, terminerConversation, basculerSujet, revenirSujetInitial, corrigerHypotheses, chargeServeur, phaseConversation, CV_RACCOURCIS, CV_TYPES } from './conversation.js';
import { kbMatch, kbFreshness, kbNormalize, kbDataAge } from './kbsearch.js';
import { analyserPhrase } from './analyse.js';
import { LOGO_SVG } from './logo-data.js';
import {
  heroScene, mascotSvg, profileSvg, VOLET_ICONS, TAB_ICONS, modeArtGagner, modeArtConvaincre, duoArt,
} from './art.js';
import {
  TIPEEE_URL, MODES, VOLETS, voletById, PROFILS, CONTEXTES, DUREES, VERDICTS, NATURES, LIMITS,
  RUBRIQUES, rubriqueById, FIABILITES, STABILITES, TYPES_FICHE, FICHE_TABS, INTERLOCUTEUR, ROBUSTESSES,
} from './taxonomy.js';
import { QUIPS, LOADING, LOADING_STRATEGY, STEPS_RESEARCH, pick } from './copy.js';

// ---------------------------------------------------------------- utilitaires
const $ = (sel, root = document) => root.querySelector(sel);
const $$ = (sel, root = document) => [...root.querySelectorAll(sel)];
const ESC = { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' };
const h = (v) => String(v ?? '').replace(/[&<>"']/g, (c) => ESC[c]);
const safeUrl = (u) => (/^https?:\/\//i.test(String(u || '')) ? String(u) : null);
const reduceMotion = () => window.matchMedia('(prefers-reduced-motion: reduce)').matches;
const frDate = (iso) => {
  if (!iso || !/^\d{4}-\d{2}-\d{2}/.test(iso)) return iso || '';
  const [y, m, d] = iso.slice(0, 10).split('-').map(Number);
  return new Date(Date.UTC(y, m - 1, d)).toLocaleDateString('fr-FR', { day: 'numeric', month: 'long', year: 'numeric', timeZone: 'UTC' });
};
const paras = (t) => h(t).split(/\n{2,}/).map((p) => `<p>${p}</p>`).join('');

function toast(msg) {
  const t = $('#toast');
  t.textContent = msg;
  t.classList.add('is-visible');
  clearTimeout(toast.timer);
  toast.timer = setTimeout(() => t.classList.remove('is-visible'), 2600);
}

async function copyText(text, okMsg = 'Copié !') {
  try {
    await navigator.clipboard.writeText(text);
    toast(okMsg);
  } catch {
    const ta = document.createElement('textarea');
    ta.value = text;
    ta.setAttribute('readonly', '');
    ta.className = 'visually-hidden';
    document.body.appendChild(ta);
    ta.select();
    const ok = document.execCommand && document.execCommand('copy');
    ta.remove();
    toast(ok ? okMsg : 'Copie automatique impossible : sélectionne le texte à la main.');
  }
}

// ---------------------------------------------------------------- état (conservé pendant la session)
const freshWizard = () => ({ step: 1, mode: null, volet: null, sousTheme: null, affirmation: '', profil: 'mystere', contexte: 'repas', interlocuteur: { inconnu: true } });
const state = {
  status: null,
  wizard: freshWizard(),
  express: { mode: 'gagner', volet: 'autre', affirmation: '' },
  result: null, // réponse /api/analyse ou /api/strategie
  request: null, // dernière requête d'analyse (pour relancer)
  currentFiche: null,
  speech: {},
  compo: null, // argumentaire composé localement : { fiche, profil, vue, session, conv (conversation continue) }
};
try {
  const saved = JSON.parse(sessionStorage.getItem('gtp-parcours') || 'null');
  if (saved?.wizard) Object.assign(state.wizard, saved.wizard);
  if (saved?.express) Object.assign(state.express, saved.express);
} catch { /* stockage indisponible : on garde l'état en mémoire */ }
function persist() {
  try { sessionStorage.setItem('gtp-parcours', JSON.stringify({ wizard: state.wizard, express: state.express })); } catch { /* ignoré */ }
}
// Deux modes : « autonome » (aucune connexion nécessaire) et « connecté » (serveur facultatif).
const appMode = () => store.reglages().mode === 'connecte' ? 'connecte' : 'autonome';
const isLive = () => appMode() === 'connecte' && state.status?.mode === 'live';
const serverLabel = () => {
  if (appMode() === 'autonome') return 'Mode autonome — sans Internet';
  if (state.status?.mode === 'live') return 'Mode connecté — recherche web active';
  if (state.status?.mode === 'demo') return 'Mode connecté — recherche web non configurée';
  return 'Mode connecté — serveur non configuré';
};

// ---------------------------------------------------------------- composants partagés
function supportCard(variant = 'main', idSuffix = '') {
  const home = variant === 'home';
  const id = `support-${variant}${idSuffix}`;
  return `<section class="support-card" aria-labelledby="${id}">
    <div class="support-art" aria-hidden="true">${mascotSvg('confirme', '', 84)}</div>
    <div class="support-body">
      <h2 id="${id}">${home ? 'Soutiens l’éducation populaire' : 'T’AIMES LES FAITS ? SOUTIENS LE PROJET !'}</h2>
      <p>${home
    ? 'Derrière cet outil, il y a un travail indépendant de création de contenu et de vulgarisation. Ton soutien finance de nouveaux outils gratuits pour l’esprit critique, à partir de 1 €.'
    : 'Gauchise tes parents est un outil d’éducation populaire gratuit. Si tu veux soutenir mon travail de création de contenu et le développement de nouveaux outils, tu peux contribuer à partir de 1 €. Merci de faire vivre l’esprit critique !'}</p>
      <a class="btn btn-primary" href="${TIPEEE_URL}" target="_blank" rel="noopener noreferrer" data-tipeee>${home ? 'Soutenir sur Tipeee' : 'JE SOUTIENS SUR TIPEEE'}<span class="visually-hidden"> (ouvre un nouvel onglet)</span></a>
    </div>
  </section>`;
}

function verdictBadge(code, small = false) {
  if (!code) return `<span class="verdict-badge verdict-badge--debat ${small ? 'is-small' : ''}"><span class="verdict-dot" aria-hidden="true"></span>Pas de verdict binaire</span>`;
  return `<span class="verdict-badge verdict-badge--${h(code)} ${small ? 'is-small' : ''}"><span class="verdict-dot" aria-hidden="true"></span>${h(VERDICTS[code] || VERDICTS.inverifiable)}</span>`;
}

function freshBadge(f) {
  if (!f?.fraicheur) return '';
  return f.fraicheur.statut === 'a_actualiser'
    ? `<span class="fresh-badge is-stale">À actualiser</span>`
    : `<span class="fresh-badge">À jour</span>`;
}

const fiabBadge = (code) => (code ? `<span class="fiab-badge fiab-badge--${h(code)}" title="Niveau de fiabilité">${h(FIABILITES[code] || code)}</span>` : '');

function ficheCard(f) {
  const rubs = (f.rubriques || []).map(rubriqueById).filter(Boolean);
  return `<a class="fiche-card ${f.force === 'forte' ? 'is-strong' : ''}" href="#/bibliotheque/${h(f.id)}">
    <span class="fiche-top"><span class="fiche-icon" aria-hidden="true">${VOLET_ICONS[f.volet] || VOLET_ICONS.autre}</span><span class="fiche-cat">${h(voletById(f.volet).court)}${f.sous_theme ? ` · ${h(f.sous_theme)}` : ''}</span></span>
    ${f.force ? `<span class="match-badge match-badge--${h(f.force)}">${f.force === 'forte' ? 'Correspond à ta question' : 'Sujet voisin'}</span>` : ''}
    <span class="fiche-claim">« ${h(f.affirmation)} »</span>
    ${rubs.length ? `<span class="rub-chips">${rubs.map((r) => `<span class="rub-chip">${h(r.court)}</span>`).join('')}</span>` : ''}
    <span class="fiche-badges">${verdictBadge(f.verdict, true)}${fiabBadge(f.fiabilite)}${freshBadge(f)}</span>
    <span class="fiche-date">Vérifiée le ${h(frDate(f.derniere_verification))}</span>
  </a>`;
}

/** Résultats instantanés de la base locale (affichés pendant la recherche, puis en tête du résultat). */
function baseLocaleBlock(b, { titre = 'Déjà dans la base locale' } = {}) {
  if (!b || !b.correspondances?.length) return '';
  return `<section class="block kb-block" aria-labelledby="kb-title">
    <h2 id="kb-title" class="block-title">${h(titre)}</h2>
    ${b.decision?.raison ? `<p class="kb-decision ${b.decision.web_complementaire ? 'is-web' : 'is-local'}">${h(b.decision.raison)}</p>` : ''}
    <div class="fiche-grid">${b.correspondances.map(ficheCard).join('')}</div>
  </section>`;
}

/** Comparaison entre la recherche web récente et la fiche locale correspondante. */
function comparaisonBlock(c) {
  if (!c) return '';
  return `<section class="block compare-block" aria-labelledby="compare-title">
    <h2 id="compare-title" class="block-title">Fiche locale et recherche récente</h2>
    <p>Comparaison avec la fiche <a href="#/bibliotheque/${h(c.fiche_id)}">« ${h(c.fiche_affirmation)} »</a>, vérifiée le ${h(frDate(c.fiche_verifiee_le))}.</p>
    ${c.signaux.length ? `<ul class="compare-signals">${c.signaux.map((x) => `<li>${h(x)}</li>`).join('')}</ul>` : '<p class="kb-decision is-local">Pas d’écart notable entre la fiche et les résultats récents.</p>'}
    ${c.chiffres_fiche_absents.length ? `<details class="acc"><summary><span>Chiffres de la fiche non retrouvés (${c.chiffres_fiche_absents.length})</span></summary><div class="acc-body"><ul>${c.chiffres_fiche_absents.map((x) => `<li>${h(x.chiffre)}${x.periode ? ` (${h(x.periode)})` : ''} — ${h(x.fait)}</li>`).join('')}</ul><p class="hint">Un chiffre absent n’est pas forcément faux : il peut simplement ne pas avoir été repris par la recherche.</p></div></details>` : ''}
    ${c.mise_a_jour_proposee ? '<p class="hint">Une proposition de mise à jour a été transmise à l’équipe. La fiche ne change qu’après relecture humaine.</p>' : ''}
  </section>`;
}

function errorBox(message, { retry = false } = {}) {
  return `<div class="error-box" role="alert">
    <div class="error-art" aria-hidden="true">${mascotSvg('inverifiable', '', 80)}</div>
    <div><h2>Ça n’a pas marché</h2><p>${h(message)}</p>
    <div class="btn-row">${retry ? '<button class="btn btn-primary" type="button" data-action="retry">Relancer</button>' : ''}
    <a class="btn btn-ghost" href="#/bibliotheque">Voir la bibliothèque</a></div></div>
  </div>`;
}

function modeCard(id, { selectable = false, selected = false } = {}) {
  const m = MODES[id];
  const art = id === 'gagner' ? modeArtGagner() : modeArtConvaincre();
  const body = `<span class="mode-art">${art}</span>
    <span class="mode-title">${h(selectable ? m.label : m.carte)}</span>
    <span class="mode-sub">${h(m.sousTitre)}</span>
    <span class="mode-desc">${h(m.description)}</span>`;
  if (selectable) {
    return `<button type="button" role="radio" aria-checked="${selected}" class="mode-card mode-card--${id} ${selected ? 'is-selected' : ''}" data-pick-mode="${id}">${body}</button>`;
  }
  return `<article class="mode-card mode-card--${id}">${body}<a class="btn btn-primary btn-block" href="#/debat?mode=${id}" data-start-mode="${id}">${h(m.bouton)}</a></article>`;
}

// ---------------------------------------------------------------- accueil
function viewHome() {
  return `
  <section class="home-hero">
    <div class="wrap">
      <h1 class="hero-title"><span>ENVIE DE GAUCHISER</span> <span>LE REPAS</span> <span>DE FAMILLE ?</span></h1>
      <p class="hero-lede">Ton oncle vient de sortir une énormité ? Choisis ta stratégie : on cherche les sources en direct et on te prépare la réponse.</p>
    </div>
  </section>

  <section class="section section--tight" aria-labelledby="modes-title">
    <div class="wrap">
      <h2 id="modes-title" class="visually-hidden">Choisis ton objectif</h2>
      <div class="mode-grid">${modeCard('gagner')}${modeCard('convaincre')}</div>
      <p class="hero-note">Gratuit. Sources consultables. Esprit critique obligatoire.</p>
    </div>
  </section>

  <section class="section section--tight" aria-labelledby="express-title">
    <div class="wrap">
      <form class="panel express-mini" id="express-mini">
        <h2 id="express-title" class="express-title"><span aria-hidden="true">${TAB_ICONS.express}</span> Réponse express</h2>
        <p class="hint">En pleine conversation ? Colle la phrase, on te donne une réplique sourcée à copier.</p>
        <label class="visually-hidden" for="express-mini-text">Affirmation à vérifier</label>
        <textarea id="express-mini-text" rows="2" maxlength="${LIMITS.claimMax}" placeholder="Ex. : les chômeurs ne veulent pas travailler">${h(state.express.affirmation)}</textarea>
        <button class="btn btn-primary btn-block" type="submit">Sortir une réplique</button>
      </form>
    </div>
  </section>

  <section class="section section--tint" aria-labelledby="volets-title">
    <div class="wrap">
      <h2 id="volets-title" class="section-title">Les grands sujets</h2>
      <div class="volet-chips">${VOLETS.filter((v) => v.id !== 'autre').map((v) => `<a class="volet-chip" href="#/thematiques/${v.id}"><span aria-hidden="true">${VOLET_ICONS[v.id]}</span>${h(v.court)}</a>`).join('')}</div>
      <p><a class="link-strong" href="#/thematiques">Voir tous les volets et sous-thèmes</a></p>
    </div>
  </section>

  <section class="section" id="comment" aria-labelledby="comment-title">
    <div class="wrap">
      <h2 id="comment-title" class="section-title">Comment ça marche ?</h2>
      <div class="hero-art">${heroScene()}</div>
      <ol class="how">
        <li><strong>Tu choisis ta stratégie.</strong> Gagner devant la table, ou convaincre sans braquer.</li>
        <li><strong>On cherche en direct.</strong> Recherche Web, documents officiels ouverts et lus, chiffres contrôlés.</li>
        <li><strong>Tu as ta réponse.</strong> Une réplique courte, trois arguments, les sources, et le reste en détail.</li>
      </ol>
      <div class="honesty">
        <div class="honesty-art">${duoArt()}</div>
        <div>
          <h3>La règle de la maison</h3>
          <p>On assume une ligne de gauche, mais on ne triche pas avec les faits : aucun chiffre ni aucune source inventés, et si les données donnent raison à ton oncle, on te le dit et on t’aide à reformuler sur des bases solides.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--tight" aria-label="Soutien">
    <div class="wrap">${supportCard('home')}</div>
  </section>`;
}

// ---------------------------------------------------------------- questionnaire « interlocuteur »
function dimField(d, p, ctx) {
  return `<fieldset class="dim"><legend class="field-label">${h(d.label)}</legend><div class="chips">${d.options.map(([k, lab]) => {
    const on = Array.isArray(p[d.id]) ? p[d.id].includes(k) : p[d.id] === k;
    return `<button type="button" class="chip chip--small ${on ? 'is-on' : ''}" aria-pressed="${on}" data-dim="${d.id}" data-val="${k}" data-ctx="${ctx}">${h(lab)}</button>`;
  }).join('')}</div></fieldset>`;
}

/** Fiches de référence pour estimer quelles questions changeraient le plus la réponse. */
function fichesReference(ctx) {
  if (ctx === 'compo' && state.compo) return [state.compo.fiche];
  const v = state.wizard.volet;
  const pool = kb.fiches.filter((f) => f.type !== 'science' && (!v || v === 'autre' || f.volet === v));
  return (pool.length ? pool : kb.fiches.filter((f) => f.type !== 'science')).slice(0, 6);
}

// Questionnaire progressif : les questions essentielles, puis celles qui changeraient le plus la réponse ;
// le reste est replié. Rien n'est obligatoire.
function interlocuteurForm(p0, ctx) {
  const p = nettoyerProfil(p0 || { inconnu: true });
  const saved = store.profils();
  const refs = kb.loaded() ? fichesReference(ctx) : [];
  const utiles = refs.length ? questionsUtiles(refs, p, { max: 3 }) : [];
  const answered = INTERLOCUTEUR.filter((d) => !p.inconnu && p[d.id]).map((d) => d.id);
  const prio = [...new Set([...INTERLOCUTEUR.filter((d) => d.essentiel).map((d) => d.id), ...utiles.filter((u) => u.impact > 0).map((u) => u.id), ...answered])];
  const first = INTERLOCUTEUR.filter((d) => prio.includes(d.id));
  const rest = INTERLOCUTEUR.filter((d) => !prio.includes(d.id));
  const suggestion = utiles.find((u) => u.impact > 0 && !answered.includes(u.id));
  return `<div class="interloc" data-interloc="${ctx}">
    <p class="hint">Des hypothèses de travail pour adapter la stratégie, pas un diagnostic. Tout est facultatif et modifiable à tout moment.</p>
    <button type="button" class="chip chip--unknown ${p.inconnu ? 'is-on' : ''}" aria-pressed="${p.inconnu}" data-inconnu="${ctx}">Je ne connais pas assez cette personne</button>
    ${suggestion ? `<p class="hint interloc-suggestion">La question qui changerait le plus la réponse maintenant : <strong>${h(suggestion.label)}</strong>.</p>` : ''}
    ${saved.length ? `<div class="saved-profiles"><p class="field-label">Profils enregistrés sur cet appareil</p><div class="chips">${saved.map((sp) => `<button type="button" class="chip" data-use-profile="${h(sp.id)}" data-ctx="${ctx}">${h(sp.nom)}</button>`).join('')}</div></div>` : ''}
    ${first.map((d) => dimField(d, p, ctx)).join('')}
    ${rest.length ? `<details class="dims-more" ${state[`plus_${ctx}`] ? 'open' : ''} data-more="${ctx}"><summary>Préciser davantage (${rest.length} questions facultatives)</summary>${rest.map((d) => dimField(d, p, ctx)).join('')}</details>` : ''}
    <div class="save-profile">
      <label class="field"><span class="field-label">Enregistrer ce profil sur cet appareil (facultatif)</span>
        <input type="text" id="profile-name-${ctx}" maxlength="40" placeholder="Ex. : Tonton du dimanche (évite les vrais noms)"></label>
      <button type="button" class="btn btn-secondary btn-small" data-save-profile="${ctx}" ${p.inconnu ? 'disabled' : ''}>Enregistrer le profil</button>
    </div>
  </div>`;
}

function profilOf(ctx) {
  if (ctx === 'compo') return state.compo?.profil || { inconnu: true };
  return state.wizard.interlocuteur || { inconnu: true };
}
function setProfil(ctx, p) {
  const clean = nettoyerProfil(p);
  if (ctx === 'compo' && state.compo) { state.compo.profil = clean; state.compo.profilOuvert = true; if (state.compo.conv && !state.compo.conv.terminee) { corrigerHypotheses(state.compo.conv, clean); sauverConv(); } } else { state.wizard.interlocuteur = clean; persist(); }
  const box = document.querySelector(`[data-interloc="${ctx}"]`);
  if (box) box.outerHTML = interlocuteurForm(clean, ctx);
  if (ctx === 'compo') refreshCompo();
  if (ctx === 'wizard') rafraichirSugg('wizard', 'affirmation');
}

// ---------------------------------------------------------------- parcours « Débat »
const STEP_NAMES = ['Objectif', 'Sujet', 'Affirmation'];

function progress(step) {
  return `<ol class="progress" aria-label="Progression">${STEP_NAMES.map((n, i) => {
    const s = i + 1;
    const cls = s < step ? 'is-done' : s === step ? 'is-current' : '';
    const inner = `<span class="progress-num">${s}</span><span class="progress-label">${n}</span>`;
    return `<li class="${cls}">${s < step ? `<button type="button" data-goto="${s}" aria-label="Revenir à l’étape ${s} : ${n}">${inner}</button>` : `<span ${s === step ? 'aria-current="step"' : ''}>${inner}</span>`}</li>`;
  }).join('')}</ol>`;
}

function voletPicker(w) {
  return `<div class="volet-list" role="radiogroup" aria-label="Volet thématique">${VOLETS.map((v) => {
    const on = w.volet === v.id;
    return `<div class="volet-item ${on ? 'is-selected' : ''}">
      <button type="button" role="radio" aria-checked="${on}" class="volet-card" data-pick-volet="${v.id}">
        <span class="volet-icon" aria-hidden="true">${VOLET_ICONS[v.id]}</span><span class="volet-name">${h(v.label)}</span>
      </button>
      ${on && v.sousThemes.length ? `<div class="sub-chips" role="group" aria-label="Sous-thème (facultatif)">
        <p class="hint">Préciser (facultatif) :</p>
        ${v.sousThemes.map((st) => `<button type="button" class="chip ${w.sousTheme === st ? 'is-on' : ''}" aria-pressed="${w.sousTheme === st}" data-pick-sub="${h(st)}">${h(st)}</button>`).join('')}
      </div>` : ''}
    </div>`;
  }).join('')}</div>`;
}

// ── Suggestions d'affirmations adaptées au parcours (bibliothèque locale, hors ligne) ──
// L'état reste en mémoire : les suggestions déjà vues ne reviennent qu'après avoir épuisé la liste.
const suggEtat = {};
function suggCtx(key) {
  if (key === 'express') return { volet: state.express.volet, sousTheme: null, mode: state.express.mode, interlocuteur: {} };
  const w = state.wizard;
  return { volet: w.volet, sousTheme: w.sousTheme, mode: w.mode, interlocuteur: w.interlocuteur && !w.interlocuteur.inconnu ? w.interlocuteur : {} };
}
function suggTirage(key, { renouveler = false } = {}) {
  const ctx = suggCtx(key);
  const cle = JSON.stringify([ctx.volet, ctx.sousTheme, ctx.mode, ctx.interlocuteur]);
  let e = suggEtat[key];
  if (!e || e.cle !== cle) e = suggEtat[key] = { cle, vues: [], actuelles: null };
  if (!e.actuelles || renouveler) {
    const r = suggestionsPour({ ...ctx, vues: e.vues }, 3);
    if (r.cycle) e.vues = [];
    e.actuelles = r.suggestions;
    e.total = r.total;
    for (const x of r.suggestions) if (!e.vues.includes(x.texte)) e.vues.push(x.texte);
  }
  return e;
}
function suggestionsHtml(key, cible) {
  const e = suggTirage(key);
  if (!e.actuelles?.length) return '';
  const couverte = (t) => (kb.fiches?.length ? kbMatch(kb.fiches.filter((f) => f.type !== 'science'), t)[0]?.force === 'forte' : false);
  return `<div class="sugg-box" id="sugg-${key}">
    <p class="field-label">Souvent entendu, à examiner :</p>
    <div class="chips sugg-chips">${e.actuelles.map((x) => `<button type="button" class="chip sugg-chip" data-example-fill="${h(x.texte)}" data-sugg-cible="${cible}">« ${h(x.texte)} »${couverte(x.texte) ? '<span class="sugg-tag">fiche vérifiée</span>' : ''}</button>`).join('')}</div>
    <div class="sugg-actions"><button type="button" class="link-btn" data-sugg-autres="${key}">Autres affirmations</button><span class="hint">${e.total} suggestion${e.total > 1 ? 's' : ''} pour ce sujet · formulations génériques, attribuées à personne</span></div>
  </div>`;
}
function rafraichirSugg(key, cible, opts) {
  const box = document.getElementById(`sugg-${key}`);
  if (opts?.renouveler) suggTirage(key, { renouveler: true });
  if (box) box.outerHTML = suggestionsHtml(key, cible);
}

function wizardBody(w) {
  if (w.step === 1) {
    return `<h1 class="step-title">Quel est ton objectif ?</h1>
      <div class="mode-grid" role="radiogroup" aria-label="Objectif">${modeCard('gagner', { selectable: true, selected: w.mode === 'gagner' })}${modeCard('convaincre', { selectable: true, selected: w.mode === 'convaincre' })}</div>`;
  }
  if (w.step === 2) {
    return `<h1 class="step-title">De quoi ça parle ?</h1>${voletPicker(w)}`;
  }
  const v = voletById(w.volet);
  return `<h1 class="step-title">Alors, qu’est-ce qu’il a encore raconté ?</h1>
    <p class="step-help">${h(MODES[w.mode].court)} · ${h(v.court)}${w.sousTheme ? ` · ${h(w.sousTheme)}` : ''}</p>
    <label class="field">
      <span class="field-label">L’affirmation, la question ou le lien d’un article</span>
      <textarea id="affirmation" rows="4" maxlength="${LIMITS.claimMax}" placeholder="Écris ici l’affirmation à vérifier…">${h(w.affirmation)}</textarea>
      <span class="field-count" id="aff-count">${w.affirmation.length} / ${LIMITS.claimMax}</span>
    </label>
    ${suggestionsHtml('wizard', 'affirmation')}
    <details class="tune" ${w.interlocuteur && !w.interlocuteur.inconnu ? 'open' : ''}>
      <summary>Décrire la personne en face (facultatif)</summary>
      ${interlocuteurForm(w.interlocuteur, 'wizard')}
    </details>`;
}

function viewWizard() {
  const w = state.wizard;
  return `<section class="section wizard">
    <div class="wrap wrap--narrow">
      ${progress(w.step)}
      <form class="wizard-panel" id="wizard-form" novalidate>
        <div id="wizard-body">${wizardBody(w)}</div>
        <p class="form-error" id="wizard-error" role="alert"></p>
        <div class="action-bar">
          ${w.step > 1 ? '<button type="button" class="btn btn-ghost" data-action="prev">Retour</button>' : '<a class="btn btn-ghost" href="#/express">Réponse express</a>'}
          ${w.step < 3 ? '<button type="submit" class="btn btn-primary btn-grow">Continuer</button>' : '<button type="submit" class="btn btn-go btn-grow">OK, SORS LES SOURCES !</button>'}
        </div>
      </form>
    </div>
  </section>`;
}

function validateStep(w) {
  if (w.step === 1 && !w.mode) return 'Choisis ton objectif : gagner le débat ou convaincre sans braquer.';
  if (w.step === 2 && !w.volet) return 'Choisis un volet (ou « Autre sujet »).';
  if (w.step === 3 && w.affirmation.trim().length < 5) return 'Écris l’affirmation à vérifier (au moins quelques mots).';
  return '';
}

// ---------------------------------------------------------------- réponse express
function viewExpress() {
  const e = state.express;
  return `<section class="section">
    <div class="wrap wrap--narrow">
      <h1 class="page-title"><span class="title-icon" aria-hidden="true">${TAB_ICONS.express}</span> Réponse express</h1>
      <p class="section-lede">Moins de recherches, même exigence de preuve. Tu lis la réplique, tu la copies, tu la dis.</p>
      <form class="wizard-panel" id="express-form" novalidate>
        <div class="segmented" role="radiogroup" aria-label="Objectif">
          ${Object.entries(MODES).map(([id, m]) => `<button type="button" role="radio" aria-checked="${e.mode === id}" class="${e.mode === id ? 'is-on' : ''}" data-express-mode="${id}">${h(m.court)}</button>`).join('')}
        </div>
        <label class="field"><span class="field-label">Sujet</span>
          <select id="express-volet">${VOLETS.map((v) => `<option value="${v.id}" ${e.volet === v.id ? 'selected' : ''}>${h(v.label)}</option>`).join('')}</select></label>
        <label class="field"><span class="field-label">Ce qu’il vient de dire</span>
          <textarea id="express-text" rows="3" maxlength="${LIMITS.claimMax}" placeholder="Écris ou colle l’affirmation…">${h(e.affirmation)}</textarea></label>
        ${suggestionsHtml('express', 'express-text')}
        <p class="form-error" id="express-error" role="alert"></p>
        <div class="action-bar"><button type="submit" class="btn btn-go btn-grow">Sortir une réplique</button></div>
      </form>
    </div>
  </section>`;
}

// ---------------------------------------------------------------- chargement
function viewLoading(text, { strategy = false } = {}) {
  return `<section class="section loading" aria-busy="true">
    <div class="wrap wrap--narrow center">
      <div class="loading-stage">
        <div class="loading-claim">« ${h(text)} »</div>
        <div class="loading-mascot">${mascotSvg('search', 'La mascotte examine l’affirmation à la loupe', 130)}</div>
      </div>
      <p class="loading-quip" aria-live="polite">${h(pick(strategy ? LOADING_STRATEGY : LOADING))}</p>
      ${strategy ? '' : `<div id="kb-instant" class="kb-instant" aria-live="polite"></div>
      <ol class="loading-steps" aria-label="Étapes de l’analyse (indicatives)">${STEPS_RESEARCH.map((s, i) => `<li data-ls="${i}">${h(s)}</li>`).join('')}</ol>
      <p class="hint">Recherche en direct : compte en général entre 30 secondes et 2 minutes.</p>`}
    </div>
  </section>`;
}
function animateLoading() {
  const items = $$('.loading-steps li');
  const quip = $('.loading-quip');
  let i = 0;
  const tick = () => {
    if (!items[0] || !document.body.contains(items[0])) return;
    items.forEach((el, k) => { el.classList.toggle('is-done', k < i); el.classList.toggle('is-current', k === i); });
    if (i > 0 && quip) quip.textContent = LOADING[i % LOADING.length];
    if (i < items.length - 1) { i += 1; setTimeout(tick, 8000 + i * 3000); }
  };
  tick();
}

// ---------------------------------------------------------------- résultats
const accessLabel = (s) => ({
  document_consulte: 'Document consulté',
  extrait_recherche: 'Extrait de recherche seulement',
  non_consulte: 'Non lue directement',
}[s.acces] || 'Source');

function factRef(dossier, id) {
  const f = dossier.faits.find((x) => x.id === id);
  if (!f) return '';
  const s = dossier.sources.find((x) => x.id === f.source);
  return `<a class="ref" href="#fait-${h(f.id)}" data-open="fait-${h(f.id)}" title="${h(f.fait)}">${h(f.id)}${s ? ` · ${h(s.organisme || s.id)}` : ''}</a>`;
}
const refs = (dossier, list) => (list || []).map((id) => factRef(dossier, id)).join(' ');
const natureBadge = (n) => (n ? `<span class="nature nature--${h(n)}">${h(NATURES[n] || n)}</span>` : '');
const numWarn = (x) => (x?.chiffres_non_sources?.length ? `<p class="num-warn">Chiffre absent du dossier vérifié : ${h(x.chiffres_non_sources.join(', '))}. Ne l’utilise pas sans vérifier.</p>` : '');

function factCard(f, dossier) {
  const s = dossier.sources.find((x) => x.id === f.source);
  const ctl = f.controle_chiffre || {};
  const ctlLabel = { retrouve: 'Chiffre retrouvé dans le document', non_retrouve: 'Chiffre non retrouvé tel quel', non_verifiable: 'Contrôle automatique impossible', fiche: 'Relevé à la main (fiche)' }[ctl.statut];
  return `<article class="fact" id="fait-${h(f.id)}" tabindex="-1">
    <p class="fact-id">${h(f.id)}${f.sens === 'soutient_affirmation' ? ' · <span class="sens-pro">va dans le sens de l’affirmation</span>' : ''}</p>
    ${f.chiffre ? `<p class="fact-figure">${h(f.chiffre)}</p>` : ''}
    <h4 class="fact-text">${h(f.fait)}</h4>
    <dl class="fact-meta">${f.periode ? `<div><dt>Période</dt><dd>${h(f.periode)}</dd></div>` : ''}${f.perimetre ? `<div><dt>Périmètre</dt><dd>${h(f.perimetre)}</dd></div>` : ''}</dl>
    ${f.montre ? `<p class="fact-expl"><strong>Ce que ça montre :</strong> ${h(f.montre)}</p>` : ''}
    ${f.ne_montre_pas ? `<p class="fact-expl"><strong>Ce que ça ne montre pas :</strong> ${h(f.ne_montre_pas)}</p>` : ''}
    ${ctlLabel && ctl.statut !== 'sans_chiffre' ? `<p class="ctl ctl--${h(ctl.statut)}" title="${h(ctl.detail || '')}">${h(ctlLabel)}</p>` : ''}
    ${s ? `<a class="fact-source" href="#source-${h(s.id)}" data-open="source-${h(s.id)}">Source ${h(s.id)} : ${h(s.organisme || s.titre)}</a>` : '<p class="fact-warning">Aucune source consultée ne soutient ce point : prudence.</p>'}
  </article>`;
}

function sourceCard(s) {
  const url = safeUrl(s.url);
  return `<article class="source-card ${s.acces === 'document_consulte' ? '' : 'is-partial'}" id="source-${h(s.id)}" tabindex="-1">
    <header>
      <span class="source-num" aria-hidden="true">${h(s.id)}</span>
      <div class="source-head">
        <p class="source-org">${h(s.organisme || 'Organisme non précisé')}</p>
        <h4 class="source-title">${url ? `<a href="${h(url)}" target="_blank" rel="noopener noreferrer">${h(s.titre)}<span class="visually-hidden"> (ouvre un nouvel onglet)</span></a>` : h(s.titre)}</h4>
        <p class="source-meta">${s.date_publication ? `Publié : ${h(s.date_publication)}` : 'Date de publication non précisée'}${s.periode_couverte ? ` · Données : ${h(s.periode_couverte)}` : ''}${s.type ? ` · ${h(s.type)}` : ''}</p>
        <p class="access access--${h(s.acces)}">${h(accessLabel(s))}</p>
      </div>
    </header>
    <details class="source-details">
      <summary>Voir les données utilisées</summary>
      <div class="source-details-body">
        <p class="hint">${h(s.acces_detail || '')}</p>
        ${s.passage ? `<p class="source-passage-label">Données utilisées${s.acces ? ' (résumé : à vérifier dans le document)' : ''}</p><p class="source-passage">${h(s.passage)}</p>` : ''}
        ${(s.extraits_cites || []).length ? `<p class="source-passage-label">Extraits exacts cités par la recherche</p>${s.extraits_cites.map((c) => `<blockquote>${h(c)}</blockquote>`).join('')}` : ''}
        ${s.pertinence ? `<p><strong>Pourquoi cette source :</strong> ${h(s.pertinence)}</p>` : ''}
        ${url ? `<p class="source-url">${h(url)}</p>` : ''}
        ${peutEnvoyer() ? `<button type="button" class="link-btn" data-report-source="${h(s.id)}">Signaler une source incorrecte</button>` : ''}
        <div class="report-slot" id="report-${h(s.id)}"></div>
      </div>
    </details>
  </article>`;
}

function acc(id, title, inner, { open = false } = {}) {
  if (!inner) return '';
  return `<details class="acc" id="${id}" ${open ? 'open' : ''}><summary><span>${title}</span></summary><div class="acc-body">${inner}</div></details>`;
}

function referencesText(dossier) {
  return dossier.sources.map((s) => `[${s.id}] ${s.organisme ? `${s.organisme}, ` : ''}« ${s.titre} »${s.date_publication ? `, ${s.date_publication}` : ''}. ${s.url}`).join('\n');
}

function shareText(r) {
  const d = r.dossier;
  return [
    `« ${r.affirmation} »`,
    d.verdict ? `Verdict documentaire : ${VERDICTS[d.verdict]}` : 'Sujet débattu : pas de verdict binaire',
    r.strategie?.replique ? `\n${$('#replique-text')?.textContent || r.strategie.replique}` : `\n${d.resume}`,
    d.sources.length ? `\nSources :\n${referencesText(d)}` : '',
    `\nVérifié avec Gauchise tes parents${d.date_verification ? ` le ${frDate(d.date_verification)}` : ''}.`,
  ].filter(Boolean).join('\n');
}

function strategyMain(r) {
  const s = r.strategie;
  const d = r.dossier;
  if (!s) return '';
  if (s.mode === 'convaincre') {
    return `<section class="block" aria-labelledby="args-title">
      <h2 id="args-title" class="block-title">Les faits, un par un</h2>
      ${s.reconnaissance ? `<p class="lead-in">${h(s.reconnaissance)}</p>` : ''}
      <ol class="args">${s.faits_progressifs.map((f) => `<li class="arg"><p class="arg-main">${h(d.faits.find((x) => x.id === f.fait)?.fait || '')}</p><p>${h(f.explication)}</p>${f.pourquoi ? `<p class="arg-why">${h(f.pourquoi)}</p>` : ''}<p class="arg-refs">${factRef(d, f.fait)}</p>${numWarn(f)}</li>`).join('')}</ol>
    </section>`;
  }
  return `<section class="block" aria-labelledby="args-title">
    <h2 id="args-title" class="block-title">La démonstration en 3 points</h2>
    ${s.these ? `<p class="these">${h(s.these)}</p>` : ''}
    <ol class="args">${s.demonstration.map((a) => `<li class="arg">${natureBadge(a.nature)}<p class="arg-main">${h(a.argument)}</p>${a.pourquoi ? `<p>${h(a.pourquoi)}</p>` : ''}${a.comment_le_dire ? `<p class="arg-why"><strong>Comment le dire :</strong> ${h(a.comment_le_dire)}</p>` : ''}${a.faits?.length ? `<p class="arg-refs">${refs(d, a.faits)}</p>` : ''}${numWarn(a)}</li>`).join('')}</ol>
  </section>`;
}

function strategyDetails(r) {
  const s = r.strategie;
  const d = r.dossier;
  if (!s) return '';
  const speech = `<div class="speech-tool" id="speech-tool">
      <p class="hint">Un texte naturel à dire, et une version en points clés pour parler avec tes mots.</p>
      <div class="segmented" role="group" aria-label="Durée">${DUREES.map(([sec, lab]) => `<button type="button" data-speech="${sec}">${h(lab)}</button>`).join('')}</div>
      <div id="speech-out" aria-live="polite"></div>
    </div>`;
  if (s.mode === 'convaincre') {
    return [
      acc('d-preoc', 'Ce qui se cache peut-être derrière', s.preoccupation.length ? `<p class="hint">Ce sont des hypothèses, pas un diagnostic : vérifie-les en écoutant.</p><ul>${s.preoccupation.map((x) => `<li>${h(x)}</li>`).join('')}</ul>` : ''),
      acc('d-terrain', 'Trouver un terrain d’accord', s.terrain_commun.length ? `<p class="hint">Ces valeurs ne sont pas forcément partagées : à tester.</p><ul>${s.terrain_commun.map((t) => `<li><strong>${h(t.valeur)}</strong> — ${h(t.formulation)}</li>`).join('')}</ul>` : ''),
      acc('d-pont', 'Construire un pont', s.pont ? `<p>${h(s.pont)}</p>` : ''),
      acc('d-solutions', 'Proposer une solution', s.solutions.length ? s.solutions.map((x) => `<div class="solution">${natureBadge(x.nature)}<p class="arg-main">${h(x.solution)}</p><p><strong>Avantages :</strong> ${h(x.avantages)}</p><p><strong>Limites :</strong> ${h(x.limites)}</p><p><strong>Conditions :</strong> ${h(x.conditions)}</p>${x.faits?.length ? `<p class="arg-refs">${refs(d, x.faits)}</p>` : ''}${numWarn(x)}</div>`).join('') : ''),
      acc('d-question', 'La question ouverte', s.question_ouverte ? `<p class="big-q">${h(s.question_ouverte)}</p>` : ''),
      acc('d-sortie', 'Savoir s’arrêter', s.sortie ? `<p>${h(s.sortie)}</p>` : ''),
      acc('d-speech', 'Préparer ma démonstration', speech),
    ].join('');
  }
  return [
    acc('d-donnees', 'Les données qui marquent', s.donnees.length ? s.donnees.map((x) => { const f = d.faits.find((y) => y.id === x.fait); return `<div class="donnee"><p class="fact-figure">${h(f?.chiffre || f?.fait || '')}</p><p><strong>Ça montre :</strong> ${h(x.montre)}</p><p><strong>Ça ne montre pas :</strong> ${h(x.ne_montre_pas)}</p><p class="arg-refs">${factRef(d, x.fait)}</p>${numWarn(x)}</div>`; }).join('') : ''),
    acc('d-objections', 'Les réponses aux objections', s.objections.length ? s.objections.map((o) => `<div class="objection"><p class="objection-q">« ${h(o.objection)} »</p><p>${h(o.reponse)}</p>${o.faits?.length ? `<p class="arg-refs">${refs(d, o.faits)}</p>` : ''}${numWarn(o)}</div>`).join('') : ''),
    acc('d-sophismes', 'Les raisonnements fallacieux', s.sophismes.length ? s.sophismes.map((x) => `<div class="sophisme"><p><span class="nature">${h(x.type)}</span></p>${x.passage ? `<p class="objection-q">« ${h(x.passage)} »</p>` : ''}<p>${h(x.explication)}</p></div>`).join('') : '<p>Aucun raisonnement fallacieux net : c’est un désaccord, pas un sophisme.</p>'),
    acc('d-questions', 'Les questions qui renversent la perspective', s.questions.length ? `<ul class="questions">${s.questions.map((q) => `<li>${h(q)}</li>`).join('')}</ul>` : ''),
    acc('d-conclusion', 'La conclusion mémorable', s.conclusion ? `<p class="big-q">${h(s.conclusion)}</p>${s.conclusion_chiffres_non_sources ? numWarn({ chiffres_non_sources: s.conclusion_chiffres_non_sources }) : ''}` : ''),
    acc('d-speech', 'Préparer ma démonstration', speech),
  ].join('');
}

function renderResult(r, { origin = 'live' } = {}) {
  const d = r.dossier;
  const s = r.strategie;
  const vkey = d.verdict || 'debat';
  const vlabel = d.verdict ? VERDICTS[d.verdict] : 'Pas de verdict binaire';
  const quip = pick(QUIPS[vkey] || QUIPS.inverifiable);
  const fromFiche = r.origine === 'bibliotheque' || origin === 'fiche';
  const canAi = isLive();
  const mode = s?.mode || r.mode_debat || state.wizard.mode || 'gagner';
  const warnings = [...(d.avertissements || []), ...(s?.avertissements || [])];

  return `<section class="section result">
    <div class="wrap wrap--narrow">
      ${fromFiche ? `<p class="crumb"><a href="#/bibliotheque">Bibliothèque</a></p>` : ''}
      ${!fromFiche || s ? `<div class="segmented mode-switch" role="radiogroup" aria-label="Changer de stratégie">
        ${Object.entries(MODES).map(([id, m]) => `<button type="button" role="radio" aria-checked="${mode === id && Boolean(s)}" class="${mode === id && s ? 'is-on' : ''}" data-switch-mode="${id}" ${canAi ? '' : 'disabled'}>${h(m.court)}</button>`).join('')}
      </div>` : ''}

      <div class="claim-bubble"><span class="claim-label">${fromFiche ? 'L’idée reçue' : 'L’affirmation examinée'}</span><p>« ${h(r.affirmation)} »</p>
        ${d.reformulation && d.reformulation !== r.affirmation ? `<p class="claim-reform">Reformulée : ${h(d.reformulation)}</p>` : ''}</div>

      <article class="verdict-card verdict-card--${h(vkey)}" aria-labelledby="verdict-title">
        <div class="verdict-mascot">${mascotSvg(d.verdict || 'opinion', `Doc Source réagit : ${vlabel}`, 96)}</div>
        <div class="verdict-body">
          <h1 id="verdict-title" class="verdict-h">${verdictBadge(d.verdict)}</h1>
          <p class="verdict-quip">${h(quip)}</p>
          <p class="verdict-summary">${h(d.resume)}</p>
          <p class="verdict-meta">
            ${d.date_verification ? `<span>Vérifié le ${h(frDate(d.date_verification))}</span>` : ''}
            ${d.sources.length ? `<a href="#sources" data-open="sources">${d.sources.length} source${d.sources.length > 1 ? 's' : ''}</a>` : '<span>Aucune source consultée</span>'}
            ${r.cache ? `<span>Dossier réutilisé (recherche du ${h(frDate(r.cache.depuis))})</span>` : ''}
            ${r.fraicheur?.statut === 'a_actualiser' ? '<span class="fresh-badge is-stale">Fiche à actualiser</span>' : ''}
          </p>
        </div>
      </article>

      ${r.base_locale?.decision && r.origine === 'bibliotheque' && r.fiche_id ? `<p class="kb-decision is-local">Réponse construite à partir de la fiche vérifiée <a href="#/bibliotheque/${h(r.fiche_id)}">« ${h(d.reformulation)} »</a>. ${h(r.base_locale.decision.raison)}</p>` : ''}
      ${d.alerte ? `<aside class="alert-box" role="note"><h2>Attention : les données donnent en partie raison à ton interlocuteur</h2><p>${h(d.alerte.constat)}</p>${d.alerte.reformulation_solide ? `<p><strong>Reformule plutôt ainsi :</strong> ${h(d.alerte.reformulation_solide)}</p>` : ''}</aside>` : ''}
      ${r.fraicheur?.statut === 'a_actualiser' ? `<aside class="notice" role="note"><p><strong>Cette fiche doit être actualisée.</strong> ${h(r.fraicheur.raison)}</p></aside>` : ''}

      ${s?.replique ? `<section class="block replique" aria-labelledby="replique-title">
        <h2 id="replique-title" class="block-title">LA RÉPLIQUE EN 20 SECONDES</h2>
        <div class="speech"><p id="replique-text">${h(s.replique)}</p></div>
        ${s.replique_chiffres_non_sources ? numWarn({ chiffres_non_sources: s.replique_chiffres_non_sources }) : ''}
        <div class="btn-row">
          <button type="button" class="btn btn-primary" data-action="copy-replique">Copier la réponse</button>
          <button type="button" class="btn btn-secondary" data-action="share">Partager</button>
        </div>
        <div class="btn-row btn-row--small">
          <button type="button" class="btn btn-ghost btn-small" data-action="rephrase" data-variante="variante" ${canAi ? '' : 'disabled'}>Autre formulation</button>
          <button type="button" class="btn btn-ghost btn-small" data-action="rephrase" data-variante="pedagogique" ${canAi ? '' : 'disabled'}>Plus pédagogique</button>
        </div>
      </section>` : ''}

      ${!s && fromFiche ? `<section class="block build-from-fiche">
        <h2 class="block-title">Construire ma réponse</h2>
        <p>À partir de cette fiche déjà vérifiée, sans nouvelle recherche :</p>
        <div class="btn-row">${Object.entries(MODES).map(([id, m]) => `<button type="button" class="btn btn-primary" data-fiche-mode="${id}" ${canAi ? '' : 'disabled'}>${h(m.bouton)}</button>`).join('')}</div>
        ${canAi ? '' : '<p class="hint">Disponible quand le moteur est configuré. En attendant, la réplique de la fiche est ci-dessous.</p>'}
      </section>` : ''}

      ${!s && r.replique ? `<section class="block replique"><h2 class="block-title">LA RÉPLIQUE EN 20 SECONDES</h2><div class="speech"><p id="replique-text">${h(r.replique)}</p></div>
        <div class="btn-row"><button type="button" class="btn btn-primary" data-action="copy-replique">Copier la réponse</button><button type="button" class="btn btn-secondary" data-action="share">Partager</button></div></section>` : ''}

      ${warnings.length ? `<aside class="notice" role="note"><ul>${warnings.map((a) => `<li>${h(a)}</li>`).join('')}</ul></aside>` : ''}
      ${strategyMain(r)}

      ${d.sources.length ? `<section class="block" id="sources" aria-labelledby="sources-title" tabindex="-1">
        <h2 id="sources-title" class="block-title">Les sources</h2>
        <div class="sources">${d.sources.map(sourceCard).join('')}</div>
      </section>` : ''}

      ${comparaisonBlock(r.comparaison_fiche)}
      ${r.origine === 'bibliotheque' ? '' : baseLocaleBlock(r.base_locale, { titre: 'Dans la base locale' })}

      <section class="block details" aria-labelledby="details-title">
        <h2 id="details-title" class="block-title">Pour aller plus loin</h2>
        ${strategyDetails(r)}
        ${acc('d-faits', `Tous les faits vérifiés (${d.faits.length})`, d.faits.length ? `<div class="facts">${d.faits.map((f) => factCard(f, d)).join('')}</div>` : '')}
        ${acc('d-contra', 'Ce qui complique notre argument', d.contradictions.length ? `<p class="hint">On ne cache rien : voici les données qui vont en sens contraire ou nuancent.</p><ul>${d.contradictions.map((c) => `<li>${h(c.element)}${c.source ? ` <a class="ref" href="#source-${h(c.source)}" data-open="source-${h(c.source)}">${h(c.source)}</a>` : ' <span class="fact-warning-inline">(non sourcé)</span>'}</li>`).join('')}</ul>` : '')}
        ${acc('d-valeurs', 'Ce qui relève des valeurs', d.jugements_de_valeur.length ? `<p class="hint">Ici, les chiffres éclairent mais ne tranchent pas.</p><ul>${d.jugements_de_valeur.map((x) => `<li>${h(x)}</li>`).join('')}</ul>` : '')}
        ${acc('d-limites', 'CE QU’ON NE SAIT PAS ENCORE', (d.limites.length || d.manques.length) ? `<ul>${[...d.manques, ...d.limites].map((x) => `<li>${h(x)}</li>`).join('')}</ul>` : '')}
        ${acc('d-rejetees', `Références écartées (${d.sources_rejetees.length})`, d.sources_rejetees.length ? `<p>L’IA a proposé ces liens, mais ils ne figuraient pas dans les résultats réellement obtenus : ils ne sont pas présentés comme des sources.</p><ul>${d.sources_rejetees.map((x) => `<li class="break">${h(x.url)} — ${h(x.raison)}</li>`).join('')}</ul>` : '')}
        ${acc('d-tech', 'Coulisses de la recherche', d.recherche ? `<ul>${d.recherche.requetes.map((q) => `<li>Recherche : ${h(q)}</li>`).join('')}</ul><p>${d.recherche.nb_resultats} résultat(s), ${d.recherche.documents_ouverts} document(s) ouvert(s)${d.recherche.erreurs.length ? `, incidents : ${h(d.recherche.erreurs.join(', '))}` : ''}.</p>${r.technique ? `<p>Coût mesuré de cette analyse : ${h(r.technique.cout_usd.toFixed(3))} $ (modèles : ${h([r.technique.modele_recherche, r.technique.modele_strategie].filter(Boolean).join(' / '))}).</p>` : ''}` : '')}
      </section>

      <section class="block actions" aria-label="Actions">
        <div class="btn-row">
          ${d.sources.length ? '<button type="button" class="btn btn-secondary" data-action="copy-refs">Copier les références</button>' : ''}
          ${!fromFiche ? `<button type="button" class="btn btn-secondary" data-action="fresh" ${canAi ? '' : 'disabled'}>Relancer une recherche fraîche</button>` : `<a class="btn btn-secondary" href="#/debat" data-prefill-fiche>Revérifier en direct</a>`}
          <a class="btn btn-ghost" href="#/debat" data-action="new">Nouvelle affirmation</a>
        </div>
        <p class="hint">Le partage contient l’affirmation, le verdict, la réplique et les liens : rien sur toi ni sur ton interlocuteur.</p>
      </section>

      ${feedbackForm(fromFiche)}
    </div>
  </section>`;
}

function renderDemo(r) {
  const local = r.base_locale?.correspondances || [];
  const sugg = [...local, ...(r.suggestions_bibliotheque || []).filter((e) => !local.some((l) => l.id === e.id))].slice(0, 4);
  return `<section class="section result">
    <div class="wrap wrap--narrow">
      <div class="claim-bubble"><span class="claim-label">L’affirmation</span><p>« ${h(r.affirmation)} »</p></div>
      <article class="verdict-card verdict-card--inverifiable">
        <div class="verdict-mascot">${mascotSvg('demo', 'Mascotte en mode démonstration', 96)}</div>
        <div class="verdict-body">
          <h1 class="verdict-h">Mode démonstration</h1>
          <p class="verdict-quip">Pas de recherche web, pas de verdict inventé. On ne joue pas aux devinettes.</p>
          <p class="verdict-summary">${h(r.message)}</p>
        </div>
      </article>
      <section class="block">
        <h2 class="block-title">Déjà vérifié par l’équipe</h2>
        ${r.base_locale?.decision?.raison && local.length ? `<p class="kb-decision ${local[0].force === 'forte' ? 'is-local' : 'is-web'}">${h(local[0].force === 'forte' ? 'Une fiche de la base locale traite cette affirmation : ouvre-la pour la réponse en 15 secondes, en 1 minute ou en 3 minutes.' : 'Les fiches ci-dessous traitent un sujet voisin.')}</p>` : ''}
        ${sugg.length ? `<div class="fiche-grid">${sugg.map(ficheCard).join('')}</div>` : '<p>Aucune fiche ne correspond pour l’instant. <a href="#/bibliotheque">Voir toute la bibliothèque</a></p>'}
      </section>
    </div>
  </section>`;
}

// Les retours et signalements ont besoin du serveur : sans lui, on ne propose pas un formulaire qui échouerait.
const peutEnvoyer = () => appMode() === 'connecte' && Boolean(state.status) && state.status.mode !== 'absent';

function feedbackForm(fromFiche) {
  if (!peutEnvoyer()) return `<section class="block feedback"><p class="hint">Une erreur dans cette fiche ? Les signalements passent par le serveur du mode connecté (non disponible ici). Tu peux noter la fiche et la source concernées et les transmettre au projet.</p></section>`;
  return `<section class="block feedback">
    <form class="panel feedback-form" id="feedback-form">
      <h2 class="block-title">Cette analyse t’a-t-elle été utile ?</h2>
      <fieldset class="fb-options"><legend class="visually-hidden">Ton avis</legend>
        <label><input type="radio" name="note" value="oui"> <span>Oui, carrément !</span></label>
        <label><input type="radio" name="note" value="partiel"> <span>Oui, mais il manque des choses.</span></label>
        <label><input type="radio" name="note" value="non"> <span>Non, il faut revoir ça.</span></label>
      </fieldset>
      <label class="field"><span class="field-label">Qu’est-ce qu’on pourrait améliorer ? (facultatif)</span>
        <textarea name="commentaire" id="fb-comment" rows="3" maxlength="1000"></textarea></label>
      ${fromFiche ? '' : '<label class="check"><input type="checkbox" name="joindre" id="fb-joindre"> Joindre l’affirmation analysée (pour aider à corriger une erreur)</label>'}
      <p class="hint">Aucune donnée personnelle enregistrée : ni adresse IP, ni profil d’interlocuteur.</p>
      <button type="submit" class="btn btn-primary">Envoyer mon avis</button>
      <p class="form-msg" role="status"></p>
    </form>
  </section>`;
}

// ---- fiche de bibliothèque → même format que le dossier vérifié
function ficheToResult(f) {
  const sources = f.sources.map((s, i) => ({
    id: `S${i + 1}`, titre: s.titre, organisme: s.organisme, date_publication: s.date_publication, periode_couverte: s.periode_couverte || null,
    type: s.type, url: s.url, acces: s.consultee ? 'document_consulte' : 'non_consulte',
    acces_detail: s.consultee ? `Consultée par l’équipe lors de la vérification du ${frDate(f.derniere_verification)}.` : 'Non lue directement : à consulter pour vérification.',
    extraits_cites: [], passage: s.passage, pertinence: s.pertinence,
  }));
  return {
    origine: 'bibliotheque',
    fiche_id: f.id,
    affirmation: f.affirmation,
    volet: f.volet,
    replique: f.argumentaires?.court || f.replique,
    fraicheur: f.fraicheur,
    dossier: {
      reformulation: f.affirmation, verdict: f.verdict || null, resume: f.resume,
      faits: f.faits.map((x, i) => ({
        id: `F${i + 1}`, fait: x.fait, chiffre: x.chiffre, periode: x.periode, perimetre: x.perimetre, montre: x.explication, ne_montre_pas: null,
        sens: 'contexte', source: sources[x.source]?.id, source_verifiee: true, controle_chiffre: { statut: 'fiche' }, fiabilite: x.fiabilite || null,
      })),
      contradictions: [], alerte: null, jugements_de_valeur: [], manques: [], limites: f.limites || [],
      sources, sources_rejetees: [], avertissements: [], recherche: null, date_verification: f.derniere_verification,
    },
    strategie: null,
    questions: f.questions,
  };
}

const TAB_IDS = FICHE_TABS.map(([id]) => id);
const PARTS = [
  ['reproche', '1. Le reproche'], ['sources', '2. Les faits'], ['moyen', '3. La réponse'], ['contre', '4. Objections légitimes'], ['court', '5. À table'],
];

function stabiliteNote(f) {
  if (f.fraicheur?.statut === 'a_actualiser') return `<aside class="notice notice--stale" role="note"><p><strong>Fiche à actualiser.</strong> ${h(f.fraicheur.raison)} Les chiffres doivent être revérifiés avant usage.</p></aside>`;
  const txt = {
    historique: 'Fait historique : les éléments de cette fiche ne changent pas d’une année sur l’autre.',
    evolutive: `Donnée qui évolue : vérifiée le ${frDate(f.derniere_verification)}, à revoir le ${frDate(f.a_actualiser_le)}.`,
    actualite: `Sujet d’actualité : vérifié le ${frDate(f.derniere_verification)}. Une recherche récente peut compléter cette fiche.`,
  }[f.stabilite];
  return txt ? `<p class="stab-note stab-note--${h(f.stabilite)}">${h(txt)}</p>` : '';
}

function citationsBlock(f, sources) {
  if (!f.citations?.length) return '';
  return `<h3 class="sub-title">Citations vérifiées</h3>
    <ul class="quotes">${f.citations.map((c) => {
    const s = sources[c.source];
    return `<li><blockquote>« ${h(c.texte)} »</blockquote><p class="quote-meta"><strong>${h(c.auteur)}</strong>, ${h(c.date)}${c.contexte ? ` — ${h(c.contexte)}` : ''}${s ? ` <a class="ref" href="#source-${h(s.id)}" data-open="source-${h(s.id)}">${h(s.id)} · ${h(s.organisme)}</a>` : ''}</p></li>`;
  }).join('')}</ul>`;
}

function fichePanel(f, r, id) {
  const A = f.argumentaires || {};
  const d = r.dossier;
  const copyBtn = (key, label = 'Copier') => `<button type="button" class="btn btn-secondary btn-small" data-copy-tab="${key}">${label}</button>`;
  switch (id) {
    case 'court':
      return `<div class="speech"><p id="replique-text">${h(A.court)}</p></div>
        <div class="btn-row"><button type="button" class="btn btn-primary" data-action="copy-replique">Copier la réponse</button><button type="button" class="btn btn-secondary" data-action="share">Partager</button></div>
        <p class="hint">À dire en 15 secondes environ. Les faits et les sources sont dans l’onglet « Sources et preuves ».</p>`;
    case 'moyen':
      return `<div class="prose">${paras(A.moyen)}</div>${copyBtn('moyen')}<p class="hint">Environ 1 minute à l’oral.</p>`;
    case 'detaille':
      return `<div class="prose">${paras(A.detaille)}</div>${copyBtn('detaille')}<p class="hint">Environ 3 minutes à l’oral.</p>`;
    case 'sources':
      return `${citationsBlock(f, d.sources)}
        <h3 class="sub-title">Les faits vérifiés (${d.faits.length})</h3>
        <div class="facts">${d.faits.map((x) => factCard(x, d)).join('')}</div>
        <h3 class="sub-title" id="sources" tabindex="-1">Les sources (${d.sources.length})</h3>
        <div class="sources">${d.sources.map(sourceCard).join('')}</div>
        <div class="btn-row"><button type="button" class="btn btn-secondary" data-action="copy-refs">Copier les références</button></div>`;
    case 'contre':
      return `${f.objections_legitimes?.length ? `<div class="legit"><h3 class="sub-title">Ce qu’il faut reconnaître</h3><p class="hint">Des critiques légitimes, à ne pas balayer : les reconnaître rend la réponse plus crédible.</p><ul>${f.objections_legitimes.map((x) => `<li>${h(x)}</li>`).join('')}</ul></div>` : ''}
        <h3 class="sub-title">Si on te répond…</h3>
        ${(f.contre_arguments || []).map((c) => `<div class="objection"><p class="objection-q">« ${h(c.objection)} »</p><p>${h(c.reponse)}</p></div>`).join('')}
        ${f.questions?.length ? `<h3 class="sub-title">Les questions qui font réfléchir</h3><ul class="questions">${f.questions.map((q) => `<li>${h(q)}</li>`).join('')}</ul>` : ''}`;
    case 'contexte': {
      const rubs = (f.rubriques || []).map(rubriqueById).filter(Boolean);
      return `<div class="prose">${paras(f.contexte || '')}</div>
        ${f.explication ? `<h3 class="sub-title">En clair</h3><div class="prose">${paras(f.explication)}</div>` : ''}
        ${f.limites?.length ? `<h3 class="sub-title">Ce qu’on ne sait pas encore</h3><ul>${f.limites.map((x) => `<li>${h(x)}</li>`).join('')}</ul>` : ''}
        ${rubs.map((rb) => `<aside class="notice" role="note"><p><strong>${h(rb.court)} :</strong> ${h(rb.avertissement)}</p></aside>`).join('')}`;
    }
    case 'empathie':
      return `<div class="speech speech--soft"><p>${h(A.empathie)}</p></div>${copyBtn('empathie', 'Copier la réponse')}
        <p class="hint">Pour quelqu’un d’inquiet ou de sincère : on part de ce qui le préoccupe, sans flatterie ni manipulation.</p>`;
    default:
      return '';
  }
}

function viewFiche(f, tab = 'court') {
  if (!TAB_IDS.includes(tab)) tab = 'court';
  const r = ficheToResult(f);
  const canAi = isLive();
  const vkey = f.verdict || 'debat';
  const rubs = (f.rubriques || []).map(rubriqueById).filter(Boolean);
  const isCrit = f.type === 'reponse_critique';
  return `<section class="section result fiche-view">
    <div class="wrap wrap--narrow">
      <p class="crumb"><a href="#/bibliotheque">Bibliothèque</a>${rubs.length ? ` · ${rubs.map((rb) => `<a href="#/rubriques/${h(rb.id)}">${h(rb.court)}</a>`).join(' · ')}` : ''}</p>
      <div class="claim-bubble"><span class="claim-label">${h(TYPES_FICHE[f.type] || 'Idée reçue')}</span><p>« ${h(f.affirmation)} »</p></div>

      <article class="verdict-card verdict-card--${h(vkey)}" aria-labelledby="verdict-title">
        <div class="verdict-mascot">${mascotSvg(f.verdict || 'opinion', 'Doc Source a vérifié la fiche', 96)}</div>
        <div class="verdict-body">
          <h1 id="verdict-title" class="verdict-h">${verdictBadge(f.verdict)}</h1>
          <p class="fiche-badges">${fiabBadge(f.fiabilite)}${freshBadge(f)}</p>
          <p class="verdict-summary">${h(f.resume)}</p>
          <p class="verdict-meta"><span>Vérifiée le ${h(frDate(f.derniere_verification))}</span><a href="#sources" data-tab-open="sources">${f.sources.length} source${f.sources.length > 1 ? 's' : ''}</a></p>
        </div>
      </article>
      ${stabiliteNote(f)}

      ${isCrit && f.reproche ? `<section class="block reproche" aria-labelledby="reproche-title">
        <h2 id="reproche-title" class="block-title">Ce qui est reproché</h2>
        <p>${h(f.reproche)}</p>
        <nav class="parts" aria-label="Les cinq parties de la fiche">${PARTS.slice(1).map(([id, label]) => `<button type="button" class="part-chip" data-tab-open="${id}">${h(label)}</button>`).join('')}</nav>
      </section>` : ''}

      <section class="block fiche-tabs-block">
        <div class="fiche-tabs" role="tablist" aria-label="Formats de réponse">
          ${FICHE_TABS.map(([id, label]) => `<button type="button" role="tab" id="tab-${id}" aria-controls="panel-${id}" aria-selected="${id === tab}" tabindex="${id === tab ? 0 : -1}" class="fiche-tab ${id === tab ? 'is-on' : ''}" data-tab="${id}">${h(label)}</button>`).join('')}
        </div>
        ${FICHE_TABS.map(([id]) => `<div class="fiche-panel" role="tabpanel" id="panel-${id}" aria-labelledby="tab-${id}" tabindex="0" ${id === tab ? '' : 'hidden'}>${fichePanel(f, r, id)}</div>`).join('')}
      </section>

      ${f.type === 'science' && f.reference ? `<section class="block"><h2 class="block-title">Référentiel scientifique</h2><dl class="ref-sci">
        <dt>Référence principale</dt><dd>${h(f.reference.titre)}${f.reference.url ? ` — <a href="${h(f.reference.url)}" target="_blank" rel="noopener noreferrer">consulter</a>` : ''}</dd>
        <dt>Auteurs, année</dt><dd>${h(f.reference.auteurs)}, ${h(String(f.reference.annee))}</dd>
        ${f.conditions ? `<dt>Conditions d’application</dt><dd>${h(f.conditions)}</dd>` : ''}
        ${f.limites_methodo ? `<dt>Limites</dt><dd>${h(f.limites_methodo)}</dd>` : ''}
        ${f.confiance ? `<dt>Niveau de confiance</dt><dd>${h({ elevee: 'Élevé', moyenne: 'Moyen', faible: 'Faible' }[f.confiance] || f.confiance)}</dd>` : ''}
      </dl><p class="hint">Aucune de ces notions n’est une loi universelle : les effets observés sont en moyenne modestes et dépendent du contexte.</p></section>` : ''}
      ${f.type === 'science' && f.application?.length ? `<section class="block"><h2 class="block-title">Dans l’application</h2><p class="hint">${h(ROBUSTESSES[f.robustesse] || '')}. Comment ce résultat oriente les stratégies proposées :</p><ul>${f.application.map((x) => `<li><strong>${h(x.situation)} :</strong> ${h(x.tactique)}</li>`).join('')}</ul></section>` : ''}
      ${f.type !== 'science' ? `<section class="block build-from-fiche">
        <h2 class="block-title">Adapter à mon interlocuteur</h2>
        <p>Les deux stratégies, adaptées à la personne en face, composées à partir de cette fiche :</p>
        <div class="btn-row"><a class="btn btn-primary" href="#/argumentaire/${h(f.id)}">Composer mon argumentaire</a></div>
        <p class="hint">Fonctionne sans Internet.${canAi ? '' : ''}</p>
        ${canAi ? `<p class="hint">Mode connecté : version rédigée par l’IA à partir de cette fiche.</p><div class="btn-row">${Object.entries(MODES).map(([id, m]) => `<button type="button" class="btn btn-secondary" data-fiche-mode="${id}">${h(m.bouton)}</button>`).join('')}</div>` : ''}
      </section>` : ''}

      <section class="block actions" aria-label="Actions">
        <div class="btn-row">
          <a class="btn btn-secondary" href="#/debat" data-prefill-fiche>${isLive() ? 'Revérifier en direct' : 'Préparer un débat sur ce sujet'}</a>
          <a class="btn btn-ghost" href="#/debat" data-action="new">Nouvelle affirmation</a>
        </div>
      </section>
      ${feedbackForm(true)}
    </div>
  </section>`;
}

function selectFicheTab(id, { focus = false } = {}) {
  if (!TAB_IDS.includes(id)) return;
  $$('.fiche-tab').forEach((b) => { const on = b.dataset.tab === id; b.classList.toggle('is-on', on); b.setAttribute('aria-selected', String(on)); b.tabIndex = on ? 0 : -1; });
  $$('.fiche-panel').forEach((p) => { p.hidden = p.id !== `panel-${id}`; });
  if (focus) $(`#tab-${id}`)?.focus();
  try { sessionStorage.setItem('gtp-onglet', id); } catch { /* ignoré */ }
}

// ---------------------------------------------------------------- argumentaire composé hors ligne
function nouvelleCompo(fiche, { question = null, force = null, profil = null, vue = null, autres = [] } = {}) {
  state.compo = {
    fiche, question, force, autres,
    profil: nettoyerProfil(profil || state.wizard.interlocuteur || { inconnu: true }),
    vue: vue || (state.wizard.mode === 'convaincre' ? 'convaincre' : 'gagner'),
    session: { utilises: [], objectionsVues: [], questionsPosees: [], retours: [] },
  };
  state.compo.conv = nouvelleConversation(fiche, { mode: state.compo.vue, profil: state.compo.profil, question });
  sauverConv();
  try {
    const r = JSON.parse(sessionStorage.getItem('gtp-recents') || '[]');
    sessionStorage.setItem('gtp-recents', JSON.stringify([fiche.id, ...r.filter((x) => x !== fiche.id)].slice(0, 8)));
  } catch { /* sans stockage de session */ }
}
// ── Conversation en cours : gardée dans l'onglet (sessionStorage) pour survivre à un rechargement ou à une
// interruption ; effacée à la fermeture de l'onglet. Rien n'est envoyé ailleurs en mode autonome.
const CONV_KEY = 'gtp-conversation';
function sauverConv() {
  const c = state.compo;
  if (!c?.conv) return;
  try { sessionStorage.setItem(CONV_KEY, JSON.stringify({ fiche_id: c.fiche.id, question: c.question, force: c.force, profil: c.profil, vue: c.vue, session: c.session, conv: c.conv })); } catch { /* stockage plein ou refusé : la conversation reste en mémoire */ }
}
function restaurerConv(fiches) {
  try {
    const d = JSON.parse(sessionStorage.getItem(CONV_KEY) || 'null');
    const f = d && fiches.find((x) => x.id === d.fiche_id);
    if (!f || !d.conv) return false;
    state.compo = { fiche: f, question: d.question, force: d.force, autres: [], profil: nettoyerProfil(d.profil), vue: d.vue === 'convaincre' ? 'convaincre' : 'gagner', session: d.session || { utilises: [], objectionsVues: [], questionsPosees: [], retours: [] }, conv: d.conv };
    return true;
  } catch { return false; }
}
const recents = () => { try { return JSON.parse(sessionStorage.getItem('gtp-recents') || '[]').slice(1); } catch { return []; } };

const srcLink = (s) => (s ? `<a class="src-inline" href="${h(safeUrl(s.url) || '#')}" target="_blank" rel="noopener noreferrer">${h(s.organisme)}, ${h(s.date)}<span class="visually-hidden"> (ouvre un nouvel onglet)</span></a>` : '<span class="fact-warning-inline">(source manquante)</span>');

function preuveItem(pr, label = '') {
  return `<li class="preuve">${label ? `<span class="preuve-label">${h(label)}</span>` : ''}
    ${pr.chiffre ? `<span class="preuve-chiffre">${h(pr.chiffre)}</span>` : ''}
    <p>${h(pr.texte)}</p>
    ${pr.methode ? `<p class="preuve-methode">${h(pr.methode)}</p>` : ''}
    <p class="preuve-src">Source : ${srcLink(pr.source)}${pr.fiabilite ? ` · ${h(FIABILITES[pr.fiabilite] || '')}` : ''}</p>
  </li>`;
}

const ORDINAUX = ['Un premier élément', 'Ensuite', 'Enfin', 'Et encore'];
function blocHtml(b, mode) {
  switch (b.type) {
    case 'ton': return `<p class="ton-note"><strong>${h(b.titre)} :</strong> ${h(b.texte)}</p>`;
    case 'replique': return `<h3 class="sub-title">${h(b.titre)}</h3><div class="speech"><p id="replique-text">${h(b.texte)}</p></div>
      <div class="btn-row"><button type="button" class="btn btn-primary" data-action="copy-replique">Copier la réponse</button><button type="button" class="btn btn-secondary" data-action="share-compo">Partager</button></div>`;
    case 'preuves': return `<h3 class="sub-title">${h(b.titre)}</h3>${b.concordantes ? `<p class="hint">Sources de plusieurs organismes : ${h(b.concordantes.join(', '))}.</p>` : ''}<ul class="preuves">${b.items.map((pr, i) => preuveItem(pr, mode === 'convaincre' && b.items.length > 1 ? ORDINAUX[i] : '')).join('')}</ul>`;
    case 'questions': return `<h3 class="sub-title">${h(b.titre)}</h3><ul class="questions">${b.items.map((q) => `<li>${h(q)}</li>`).join('')}</ul>`;
    case 'objection': return `<h3 class="sub-title">${h(b.titre)}</h3><div class="objection"><p class="objection-q">« ${h(b.objection)} »</p><p>${h(b.reponse)}</p></div>`;
    case 'developpement': return `<h3 class="sub-title">${h(b.titre)}</h3><div class="prose">${b.paragraphes.map((x) => `<p>${h(x)}</p>`).join('')}</div>`;
    case 'liste': return `<div class="legit"><h3 class="sub-title">${h(b.titre)}</h3><ul>${b.items.map((x) => `<li>${h(x)}</li>`).join('')}</ul></div>`;
    case 'empathie': return `<h3 class="sub-title">${h(b.titre)}</h3><div class="speech speech--soft"><p ${mode === 'convaincre' ? 'id="empathie-text"' : ''}>${h(b.texte)}</p></div>`;
    case 'conclusion': return `<h3 class="sub-title">${h(b.titre)}</h3><p class="big-q">${h(b.texte)}</p>`;
    case 'entree': case 'texte': default: return `<h3 class="sub-title">${h(b.titre)}</h3><p>${h(b.texte)}</p>`;
  }
}

function planResume(pl) {
  const ENTREES = { correction: 'correction expliquée', fait: 'un fait d’abord', cadre: 'poser le cadre', concession: 'reconnaître un point', preoccupation: 'partir de sa préoccupation', exemple: 'un exemple concret', vecu: 'reconnaître son vécu', accord: 'ce qui nous rassemble', reformulation: 'reformuler', question: 'une question ouverte' };
  return `<p class="plan-resume"><strong>Stratégie :</strong> ${h(pl.approche_titre.toLowerCase())} · entrée : ${h(ENTREES[pl.entree] || pl.entree)} · détail : ${h(pl.detail)} · ${pl.preuves.length} preuve${pl.preuves.length > 1 ? 's' : ''}</p>`;
}

function viewArgumentaire() {
  const c = state.compo;
  if (!c) return `<section class="section"><div class="wrap wrap--narrow center"><h1 class="page-title">Aucun argumentaire en cours</h1><a class="btn btn-primary" href="#/debat">Préparer un débat</a></div></section>`;
  const f = c.fiche;
  const a = composer(f, c.profil, { bibliotheque: kb.fiches, recents: recents(), force: c.force, deja: c.session.utilises, objectionsVues: c.session.objectionsVues, questionsPosees: c.session.questionsPosees });
  c.last = a;
  const pl = a.plans[c.vue];
  const tab = (id, label) => `<button type="button" role="tab" id="strat-${id}" aria-controls="strat-panel-${id}" aria-selected="${c.vue === id}" tabindex="${c.vue === id ? 0 : -1}" class="fiche-tab ${c.vue === id ? 'is-on' : ''}" data-strat="${id}">${h(label)}</button>`;
  const sameQ = !c.question || kbNormalize(c.question).replace(/[^a-z0-9]+/g, '') === kbNormalize(f.affirmation).replace(/[^a-z0-9]+/g, '');
  const incert = [...new Set([kbDataAge(f).texte, ...a.plans.gagner.incertitudes, ...a.plans.convaincre.incertitudes])].map((t) => t.replace(/\d{4}-\d{2}-\d{2}/g, (d) => frDate(d)));
  const panel = (mode) => {
    const p2 = a.plans[mode];
    return `<div class="fiche-panel" role="tabpanel" id="strat-panel-${mode}" aria-labelledby="strat-${mode}" tabindex="0" ${c.vue === mode ? '' : 'hidden'}>
      <p class="hint">${mode === 'gagner' ? h(MODES.gagner.sousTitre) : 'Une réponse progressive : questions ouvertes, valeurs communes, faits présentés sans braquer.'}</p>
      ${planResume(p2)}
      ${a[mode].blocs.map((b) => blocHtml(b, mode)).join('')}
      ${p2.prochaine.length ? `<h3 class="sub-title">Et ensuite</h3><ul class="prochaine">${p2.prochaine.map((x) => `<li>${h(x.texte)}</li>`).join('')}</ul>` : ''}
    </div>`;
  };
  return `<section class="section result compo-view">
    <div class="wrap wrap--narrow">
      <p class="crumb"><a href="#/bibliotheque/${h(f.id)}">Fiche complète</a></p>
      <div class="claim-bubble"><span class="claim-label">${!sameQ ? 'Ta question' : 'L’affirmation'}</span><p>« ${h(c.question || f.affirmation)} »</p>
        ${!sameQ ? `<p class="claim-reform">Fiche utilisée : « ${h(f.affirmation)} »${c.force === 'partielle' ? ' (sujet voisin)' : ''}</p>` : ''}</div>
      <p class="offline-badge">Composé à partir de la bibliothèque locale — sans recherche web ni IA.</p>
      ${c.analyse ? analyseHtml(c.analyse.mode === c.vue ? c.analyse : (c.analyse = analyserPhrase(c.analyse.texte, { bibliotheque: kb.fiches, mode: c.vue })), f.id, c.vue) : ''}
      ${incert.length ? `<aside class="notice notice--soft" role="note"><p><strong>À garder en tête :</strong></p><ul>${incert.map((x) => `<li>${h(x)}</li>`).join('')}</ul></aside>` : ''}
      ${a.profil.inconnu ? '' : `<p class="hyp-note"><strong>Hypothèses retenues sur la personne</strong> (tu peux les corriger ci-dessous) : ${h(resumeProfil(a.profil))}.</p>`}

      <section class="block steelman" aria-labelledby="steel-title">
        <h2 id="steel-title" class="block-title">L’argument d’en face, version solide</h2>
        <p>${h(a.version_solide)}</p>
      </section>

      <section class="block">
        <div class="fiche-tabs" role="tablist" aria-label="Deux stratégies">${tab('gagner', MODES.gagner.label)}${tab('convaincre', MODES.convaincre.carte)}</div>
        ${panel('gagner')}${panel('convaincre')}
      </section>

      <section class="block">
        <details class="acc" id="compo-profil" ${c.profilOuvert ? 'open' : ''}><summary><span>Corriger les hypothèses sur la personne${a.profil.inconnu ? '' : ` : ${h(resumeProfil(a.profil))}`}</span></summary><div class="acc-body">${interlocuteurForm(c.profil, 'compo')}</div></details>
        <details class="acc" id="compo-deja" ${c.dejaOuvert ? 'open' : ''}><summary><span>Arguments déjà avancés (${c.session.utilises.length})</span></summary><div class="acc-body">
          <p class="hint">Coche ce que tu as déjà dit : le moteur choisira d’autres preuves.</p>
          <div class="chips">${f.faits.map((x, i) => `<button type="button" class="chip chip--small ${c.session.utilises.includes(i) ? 'is-on' : ''}" aria-pressed="${c.session.utilises.includes(i)}" data-deja="${i}">${h(x.chiffre || x.fait.slice(0, 60) + (x.fait.length > 60 ? '…' : ''))}</button>`).join('')}</div>
        </div></details>
        ${a.approches.length > 1 ? `<details class="acc" ${c.approchesOuvert || a.profil.politique === 'ouvert' ? 'open' : ''}><summary><span>Comparer ${a.approches.length} approches</span></summary><div class="acc-body">
          <p class="hint">Aucune approche ne garantit de convaincre : ce sont des estimations qualitatives, pas des prédictions.</p>
          ${a.approches.map((ap) => `<article class="approche ${ap.approche === pl.approche ? 'is-chosen' : ''}"><h3 class="sub-title">${h(ap.titre)}${ap.approche === a.plans[c.vue].approche ? ' (retenue)' : ''}</h3>
            <p><strong>Pour qui :</strong> ${h(ap.profil)}</p><p><strong>Pourquoi :</strong> ${h(ap.pourquoi)}</p>
            ${ap.preuves.length ? `<ul class="preuves">${ap.preuves.map((pr) => preuveItem(pr)).join('')}</ul>` : ''}
            ${ap.exemple_lie ? `<p><strong>Exemple historique lié :</strong> <a href="#/bibliotheque/${h(ap.exemple_lie.id)}">« ${h(ap.exemple_lie.affirmation)} »</a> — ${h(ap.exemple_lie.resume)}</p>` : ''}
            <p><strong>Risque de malentendu :</strong> ${h(ap.risques)}</p>
            ${ap.limites.length ? `<p><strong>Limites :</strong> ${h(ap.limites.join(' '))}</p>` : ''}
            <p><strong>Pour poursuivre :</strong> ${h(ap.questions.join(' '))}</p></article>`).join('')}
        </div></details>` : ''}
        <details class="acc"><summary><span>Pourquoi cette stratégie</span></summary><div class="acc-body">
          <ul class="regles">${pl.pourquoi.map((r) => `<li><strong>${h(r.choix)} :</strong> ${h(r.raison)}${r.fiche ? ` <a href="#/bibliotheque/${h(r.fiche)}">La recherche</a>` : ''}</li>`).join('')}</ul>
          <p class="hint">Consignes appliquées (« recherche » : appuyée sur des études ; « pratique » : choix de communication sans démonstration directe) :</p>
          <ul class="regles">${a.regles.map((r) => `<li><strong>${h(r.titre)}.</strong> ${h(r.consigne)} <span class="tag">${r.fondement === 'recherche' ? 'recherche' : 'pratique'}</span> <a href="#/bibliotheque/${h(r.fiche)}">Fiche</a></li>`).join('')}</ul>
        </div></details>
        ${a.sources ? `<details class="acc"><summary><span>Toutes les sources consultées (${a.sources.length})</span></summary><div class="acc-body"><ul>${a.sources.map((x) => `<li>${srcLink(x)} — ${h(x.titre)}</li>`).join('')}</ul></div></details>` : ''}
        ${a.limites.length ? `<details class="acc"><summary><span>Ce qu’on ne sait pas encore</span></summary><div class="acc-body"><ul>${a.limites.map((x) => `<li>${h(x)}</li>`).join('')}</ul></div></details>` : ''}
      </section>

      ${conversationHtml(c)}

      <section class="block actions">
        <div class="btn-row">
          <button type="button" class="btn btn-primary" data-action="save-compo">Enregistrer cet argumentaire</button>
          <a class="btn btn-secondary" href="#/bibliotheque/${h(f.id)}">Ouvrir la fiche complète</a>
          ${isLive() ? '<button type="button" class="btn btn-secondary" data-action="web-compo">Compléter par une recherche web</button>' : ''}
          <a class="btn btn-ghost" href="#/debat" data-action="new">Nouvelle question</a>
        </div>
        ${c.autres?.length ? `<p class="hint">Autres fiches proches : ${c.autres.map((x) => `<a href="#/argumentaire/${h(x.id)}">« ${h(x.affirmation)} »</a>`).join(' · ')}</p>` : ''}
      </section>
    </div>
  </section>`;
}

// ---------------------------------------------------------------- conversation continue
const PHASES = { ouverture: 'début de la discussion', approfondissement: 'on approfondit', tension: 'ça se tend', essoufflement: 'ça s’essouffle', convergence: 'des points communs apparaissent' };

function convTourHtml(t) {
  const i = t.intervention;
  const rac = t.raccourci ? CV_RACCOURCIS.find(([k]) => k === t.raccourci)?.[1] : null;
  return `<li class="conv-tour" id="conv-tour-${t.n}">
    <p class="conv-num">Échange ${t.n}</p>
    <div class="bulle bulle--autre"><span class="bulle-qui">Il ou elle a répondu${rac ? ` · ${h(rac)}` : ''}</span>${t.message ? `<p>« ${h(t.message)} »</p>` : `<p class="hint">(sans précision)</p>`}</div>
    <p class="conv-lecture"><strong>Ce que je comprends :</strong> ${h(i.lecture || CV_TYPES[t.analyse.type] || '')} <span class="hint">— lecture approximative${t.origine === 'connecte' ? ' (mode connecté)' : ''}, à corriger si besoin.</span></p>
    <div class="bulle bulle--toi"><span class="bulle-qui">Tu peux répondre</span><p>${h(i.texte)}</p>
      <button type="button" class="link-btn" data-conv-copier="${t.n}">Copier</button></div>
    ${i.complement ? `<p>${h(i.complement)}</p>` : ''}
    ${t.analyse?.lecture_phrase?.emotions?.length ? `<p class="conv-ressenti"><strong>Derrière la phrase, peut-être :</strong> ${h(t.analyse.lecture_phrase.emotions[0].label.toLowerCase())}. ${h(t.analyse.lecture_phrase.emotions[0].reponse)}</p>` : ''}
    ${t.analyse?.lacune_sujet ? `<p class="fact-warning">Pas encore de fiche sur « ${h(t.analyse.lacune_sujet)} » : aucune fiche voisine n’est présentée à la place.</p>` : ''}
    ${i.preuve?.source ? `<ul class="preuves">${preuveItem(i.preuve)}</ul>` : ''}
    ${i.question ? `<p class="conv-question"><strong>Question à poser :</strong> ${h(i.question)}</p>` : ''}
    ${i.avertissement ? `<p class="fact-warning">${h(i.avertissement)}</p>` : ''}
    ${(i.options || []).length ? `<div class="btn-row conv-options">${i.options.map((o) => `<button type="button" class="btn btn-secondary btn-small" data-conv-option="${h(o.action)}${o.fiche_id ? `:${h(o.fiche_id)}` : ''}">${h(o.label)}</button>`).join('')}</div>` : ''}
    <p class="hint"><strong>Pourquoi :</strong> ${h(i.strategie || '')}${i.fiche_science ? ` <a href="#/bibliotheque/${h(i.fiche_science)}">La recherche</a>` : ''}</p>
    ${i.conclusion_possible ? '<p class="hint conv-conclure">C’est peut-être un bon moment pour conclure… seulement si tu le souhaites.</p>' : ''}
  </li>`;
}

function bilanHtml(c) {
  const b = c.conv.bilan;
  const liste = (arr, vide) => (arr.length ? `<ul>${arr.map((x) => `<li>${h(x)}</li>`).join('')}</ul>` : `<p class="hint">${h(vide)}</p>`);
  return `<section class="block conv-bilan" id="conv-bilan" aria-labelledby="bilan-title">
    <div class="bilan-head">${mascotSvg('happy', 'La mascotte applaudit', 88)}<h2 id="bilan-title" class="block-title">Conversation terminée</h2></div>
    <p class="bilan-message">${h(b.message)}</p>
    <h3 class="sub-title">Les arguments abordés (${b.arguments.length})</h3>
    ${liste(b.arguments.map((a) => a.texte), 'Aucun fait n’a été présenté pendant la conversation.')}
    <h3 class="sub-title">Points d’accord</h3>
    ${liste(b.accords, 'Aucun point d’accord identifiable dans ce que tu as rapporté.')}
    <h3 class="sub-title">Points de désaccord</h3>
    ${liste(b.desaccords, 'Aucun désaccord identifiable dans ce que tu as rapporté.')}
    <h3 class="sub-title">Les sources utilisées (${b.sources.length})</h3>
    ${b.sources.length ? `<ul>${b.sources.map((x) => `<li>${srcLink(x)} — ${h(x.titre)}</li>`).join('')}</ul>` : '<p class="hint">Aucune source citée pendant la conversation.</p>'}
    <details class="acc"><summary><span>Revoir les ${b.nb_echanges} échanges</span></summary><div class="acc-body"><ol class="conv-fil">${c.conv.tours.map(convTourHtml).join('')}</ol></div></details>
    <div class="btn-row">
      <button type="button" class="btn btn-primary" data-action="conv-nouvelle">Nouvelle conversation sur ce sujet</button>
      <a class="btn btn-secondary" href="#/debat" data-action="new">Nouveau sujet</a>
      <button type="button" class="btn btn-ghost btn-small" data-action="conv-reprendre">Finalement, reprendre la conversation</button>
    </div>
    <p class="hint">Ce bilan reste disponible tant que l’onglet est ouvert ou jusqu’à ce que tu commences une nouvelle conversation.</p>
  </section>`;
}

function conversationHtml(c) {
  const cv = c.conv;
  if (!cv) return '';
  if (cv.terminee && cv.bilan) return bilanHtml(c);
  const err = c.convErreur;
  return `<section class="block conv-block" id="conversation" aria-labelledby="conv-title">
    <h2 id="conv-title" class="block-title">La conversation continue</h2>
    <p class="hint">Après chaque réponse de ton interlocuteur, raconte-la ici : je propose la suite en tenant compte de tout ce qui a déjà été dit. Il n’y a pas de limite d’échanges ; c’est toi qui décides quand c’est fini.</p>
    <p class="conv-etat"><span class="tag">${cv.mode === 'gagner' ? 'Gagner le débat' : 'Convaincre avec empathie'}</span> <span class="tag">${cv.tours.length} échange${cv.tours.length > 1 ? 's' : ''}</span> <span class="tag">${h(PHASES[phaseConversation(cv)])}</span>${cv.courante !== cv.sujet.fiche_id ? ` <span class="tag">sujet voisin en cours</span> <button type="button" class="link-btn" data-conv-option="rester">revenir au sujet initial</button>` : ''}</p>
    <ol class="conv-fil" id="conv-fil">${cv.tours.map(convTourHtml).join('')}</ol>
    ${c.convPending ? `<p class="conv-attente" role="status">${mascotSvg('search', 'La mascotte réfléchit', 40)} Je réfléchis à la suite…</p>` : ''}
    ${err ? `<div class="notice notice--error" role="alert"><p><strong>La suite n’a pas pu être préparée :</strong> ${h(err.message)}</p><p class="hint">Ta conversation est conservée, rien n’est perdu.</p>
      <div class="btn-row">${err.retry !== false ? '<button type="button" class="btn btn-primary btn-small" data-action="conv-reessayer">Réessayer</button>' : ''}<button type="button" class="btn btn-secondary btn-small" data-action="conv-local">Continuer avec le moteur hors ligne</button></div></div>` : ''}
    <form class="conv-form" id="conv-form">
      <label class="field"><span class="field-label">Ce qu’il ou elle t’a répondu (avec tes mots)</span>
        <textarea id="conv-msg" rows="3" maxlength="1000" placeholder="Ex. : « Tes chiffres, c’est l’Insee : c’est truqué. »" ${c.convPending ? 'disabled' : ''}>${h(c.convBrouillon || '')}</textarea></label>
      <p class="field-label small">Raccourcis facultatifs (ils complètent ton texte) :</p>
      <div class="chips conv-raccourcis">${CV_RACCOURCIS.map(([k, lab]) => `<button type="button" class="chip chip--small" data-conv-raccourci="${k}" ${c.convPending ? 'disabled' : ''}>${h(lab)}</button>`).join('')}</div>
      <div class="btn-row"><button class="btn btn-primary" type="submit" ${c.convPending ? 'disabled' : ''}>Il ou elle m’a répondu…</button></div>
      <p class="form-msg" id="conv-statut" role="status">${h(c.convStatut || '')}</p>
      ${c.convDoublon ? '<button type="button" class="btn btn-secondary btn-small" data-action="conv-forcer">Oui, c’est une nouvelle réaction</button>' : ''}
    </form>
    ${cv.tours.length ? `<details class="acc" id="conv-resume"><summary><span>Où en est la discussion</span></summary><div class="acc-body"><p class="conv-resume-txt">${h(cv.resume).replace(/\n/g, '<br>')}</p><p class="hint">Les hypothèses sur la personne viennent de toi ; les propos rapportés sont ce que tu as écrit ; seuls les faits sourcés viennent de la bibliothèque.</p></div></details>` : ''}
    <div class="conv-fin"><button type="button" class="btn btn-ghost btn-small" data-action="conv-terminer">Conversation terminée</button><span class="hint">Quand tu veux : rien ne s’arrête tout seul.</span></div>
  </section>`;
}

const convConnecte = () => isLive() && store.reglages().mode === 'connecte';

/** Envoie un nouveau propos rapporté. Une seule requête à la fois (protection contre les boucles). */
async function envoyerConv(texte, raccourci = null, { force = false, local = false } = {}) {
  const c = state.compo;
  if (!c?.conv || c.convPending || c.conv.terminee) return;
  const msg = String(texte || '').trim();
  if (!msg && !raccourci) { c.convStatut = 'Écris ce que ton interlocuteur a répondu, ou choisis un raccourci.'; refreshCompo(); return; }
  c.convStatut = '';
  c.convDoublon = null;
  if (convConnecte() && !local) {
    c.convPending = true;
    c.convErreur = null;
    c.convBrouillon = msg;
    refreshCompo();
    try {
      const r = await api.conversation({ ...chargeServeur(c.conv, msg, { raccourci }), interlocuteur: c.conv.hypotheses, mode: c.conv.mode });
      const analyse = { ...analyserMessage(c.conv, msg, { raccourci, bibliotheque: kb.fiches }), type: r.intervention.type };
      enregistrerTour(c.conv, { message: msg, raccourci, analyse, intervention: r.intervention, origine: 'connecte' });
      c.convBrouillon = '';
    } catch (e) {
      c.convErreur = { message: e.message, retry: e.status === 429 || e.status >= 500 || e.data?.relancer === true, texte: msg, raccourci };
    } finally {
      c.convPending = false;
    }
  } else {
    const r = repondreConversation(c.conv, msg, { raccourci, bibliotheque: kb.fiches, force });
    if (r.doublon) { c.convStatut = r.message; c.convDoublon = { texte: msg, raccourci }; c.convBrouillon = msg; refreshCompo(); return; }
    if (r.erreur) { c.convStatut = r.erreur; refreshCompo(); return; }
    c.convErreur = null;
    c.convBrouillon = '';
  }
  sauverConv();
  refreshCompo();
  const last = document.querySelector('#conv-fil .conv-tour:last-child');
  if (last) last.scrollIntoView({ behavior: reduceMotion() ? 'auto' : 'smooth', block: 'start' });
}

function refreshCompo() {
  if (!parseRoute().path.startsWith('/argumentaire')) return;
  const y = window.scrollY;
  $('#app').innerHTML = viewArgumentaire();
  window.scrollTo(0, y);
}

// Panneau « Ce que contient la phrase » : arguments repérés (et fiche qui répond à chacun, ou lacune),
// liens de cause affirmés, émotions possibles, procédés, formule et question, fiches écartées et pourquoi.
function analyseHtml(an, ficheCourante, vue) {
  const ficheDe = (id) => kb.fiches.find((x) => x.id === id);
  const preuveDe = (f) => {
    const fa = (f?.faits || []).find((x) => x.source != null && f.sources?.[x.source]);
    if (!fa) return '';
    const so = f.sources[fa.source];
    return `<p class="an-preuve">${fa.chiffre ? `<strong>${h(fa.chiffre)}</strong> — ` : ''}${h(fa.fait)} <span class="an-src">Source : <a href="${h(safeUrl(so.url) || '#')}" target="_blank" rel="noopener noreferrer">${h(so.organisme)}, ${h(so.date_publication || '')}<span class="visually-hidden"> (ouvre un nouvel onglet)</span></a></span></p>`;
  };
  const carte = (a, i) => {
    const f = a.fiche && ficheDe(a.fiche.id);
    const ici = a.fiche?.id === ficheCourante;
    return `<li class="an-arg ${a.lacune ? 'an-arg--lacune' : ''}">
      <p class="an-arg-head"><span class="an-rang">${i === 0 ? 'Argument principal' : 'Argument secondaire'}</span> ${h(a.label)}</p>
      ${an.arguments.length > 1 ? `<p class="an-seg">« ${h(a.segment)} »</p>` : ''}
      ${a.lacune ? '<p class="an-lacune">Pas encore de fiche qui réponde précisément à ce point : aucune fiche voisine n’est présentée à la place.</p>'
        : ici ? `<p class="hint">Traité en détail ci-dessous${a.pertinence === 'partielle' ? ' (la fiche n’y répond qu’en partie)' : ''}.</p>`
        : `<p>${h(a.fiche.court || '')}</p>${preuveDe(f)}<p><a class="link-btn" href="#/bibliotheque/${h(a.fiche.id)}">Voir la fiche « ${h(a.fiche.affirmation)} »</a>${a.pertinence === 'partielle' ? ' <span class="hint">(répond en partie)</span>' : ''}</p>`}
      ${a.implicite ? `<p class="an-imp"><strong>Sous-entendu possible :</strong> ${h(a.implicite)}</p>` : ''}
    </li>`;
  };
  const causes = an.causalites.map((x) => `<li>${h(x.cause)} → ${h(x.effet)} <span class="hint">(${h(x.forme)})</span></li>`).join('');
  return `<section class="block analyse" aria-labelledby="an-title">
    <h2 id="an-title" class="block-title">Ce que contient la phrase</h2>
    <p class="hint">Lecture automatique et approximative, à partir de règles explicites. Les émotions et procédés sont des hypothèses, pas des étiquettes.</p>
    <ol class="an-args">${an.arguments.map(carte).join('')}</ol>
    ${an.emotions.length ? `<div class="an-emo"><h3 class="sub-title">Ce qui peut se jouer derrière</h3><ul>${an.emotions.map((e) => `<li><strong>${h(e.label)} :</strong> ${h(e.reponse)}</li>`).join('')}</ul></div>` : ''}
    <div class="an-phrase"><p class="an-phrase-label">${vue === 'convaincre' ? 'Pour ouvrir la discussion' : 'La phrase qui marque'}</p><p class="big-q">${h(an.phrase)}</p>
      <p><strong>Question à poser :</strong> ${h(an.question)}</p></div>
    ${an.procedes.length || causes || an.aVerifier.length ? `<details class="acc"><summary><span>Comment l’argument est construit${an.procedes.length ? ` (${an.procedes.length} procédé${an.procedes.length > 1 ? 's' : ''} possible${an.procedes.length > 1 ? 's' : ''})` : ''}</span></summary><div class="acc-body">
      ${causes ? `<h3 class="sub-title">Lien de cause affirmé</h3><ul>${causes}</ul>` : ''}
      ${an.procedes.map((p) => `<article class="an-proc"><h3 class="sub-title">${h(p.label)} ?</h3><p>${h(p.explication)}</p><p><strong>À vérifier :</strong> ${h(p.verifier)}</p><p><strong>Question :</strong> ${h(p.question)}</p></article>`).join('')}
      ${an.aVerifier.length ? `<h3 class="sub-title">Ce qu’il faudrait vérifier</h3><ul>${an.aVerifier.map((x) => `<li>${h(x)}</li>`).join('')}</ul>` : ''}
    </div></details>` : ''}
    ${an.ecartees.length ? `<details class="acc an-ecartees"><summary><span>Fiches écartées (${an.ecartees.length})</span></summary><div class="acc-body">
      <p class="hint">Ces fiches partagent des mots avec la phrase mais ne répondent pas à l’argument.</p>
      <ul>${an.ecartees.map((e) => `<li><a href="#/bibliotheque/${h(e.id)}">« ${h(e.affirmation)} »</a> — ${h(e.raison)}.</li>`).join('')}</ul>
    </div></details>` : ''}
  </section>`;
}

function viewPasDansLaBase(payload) {
  const proches = payload.volet && payload.volet !== 'autre' ? kb.fiches.filter((f) => f.volet === payload.volet).slice(0, 4) : [];
  return `<section class="section result">
    <div class="wrap wrap--narrow">
      <div class="claim-bubble"><span class="claim-label">Ta question</span><p>« ${h(payload.affirmation)} »</p></div>
      <article class="verdict-card verdict-card--debat">
        <div class="verdict-mascot">${mascotSvg('search', 'La mascotte cherche dans la bibliothèque', 96)}</div>
        <div class="verdict-body">
          <h1 class="verdict-h">Pas encore dans la bibliothèque</h1>
          <p class="verdict-summary">${payload.analyse?.principal ? `J’ai compris l’argument (« ${h(payload.analyse.principal.label.toLowerCase())} »), mais la bibliothèque ne contient pas encore de fiche qui y réponde. Plutôt que de présenter une fiche voisine comme une réponse, je le dis.` : 'La bibliothèque locale ne contient pas encore cette information. Rien n’est inventé à la place.'}</p>
          ${isLive() ? '<button type="button" class="btn btn-primary" data-action="web-search-local">Lancer une recherche web</button>' : ''}
        </div>
      </article>
      ${payload.analyse ? analyseHtml(payload.analyse, null, payload.mode === 'convaincre' ? 'convaincre' : 'gagner') : ''}
      ${proches.length && !payload.analyse ? `<section class="block"><h2 class="block-title">Dans le même volet</h2><div class="fiche-grid">${proches.map((f) => ficheCard(withFresh(f))).join('')}</div></section>` : ''}
      <p><a class="btn btn-secondary" href="#/bibliotheque">Chercher dans la bibliothèque</a></p>
    </div>
  </section>`;
}

const withFresh = (f) => (f.fraicheur ? f : { ...f, fraicheur: kbFreshness(f) });

async function launchLocal(payload) {
  state.request = payload;
  try { await kb.load(); } catch {
    $('#app').innerHTML = `<section class="section"><div class="wrap wrap--narrow">${errorBox('La bibliothèque locale n’a pas pu être chargée sur cet appareil. Recharge la page une fois connecté pour l’enregistrer.')}</div></section>`;
    return;
  }
  // 1. Analyse argumentative : concepts → arguments → fiches qui y répondent vraiment (sinon, lacune reconnue).
  const an = analyserPhrase(payload.affirmation, { bibliotheque: kb.fiches, mode: payload.mode === 'convaincre' ? 'convaincre' : 'gagner' });
  if (an.arguments.length) {
    const avecFiche = an.arguments.filter((x) => x.fiche);
    if (!avecFiche.length) {
      state.compo = null;
      state.pasTrouve = { ...payload, analyse: an };
      if (location.hash !== '#/introuvable') location.hash = '#/introuvable'; else render();
      return;
    }
    const pr = avecFiche[0];
    const fiche = kb.fiches.find((f) => f.id === pr.fiche.id);
    nouvelleCompo(fiche, { question: payload.affirmation, force: pr.pertinence === 'partielle' ? 'partielle' : 'forte', profil: payload.interlocuteur, vue: payload.mode === 'convaincre' ? 'convaincre' : 'gagner', autres: avecFiche.slice(1).map((x) => kb.fiches.find((f) => f.id === x.fiche.id)).filter(Boolean) });
    state.compo.analyse = an;
    if (location.hash !== '#/argumentaire') location.hash = '#/argumentaire'; else render();
    return;
  }
  // 2. Aucun argument reconnu : correspondance textuelle (le volet et le sous-thème départagent).
  const m = kbMatch(kb.fiches.filter((f) => f.type !== 'science' || payload.volet === 'autre'), payload.affirmation, { limit: 6 })
    .map((x) => ({ ...x, adj: x.score + (payload.volet && x.fiche.volet === payload.volet ? 2 : 0) + (payload.sous_theme && x.fiche.sous_theme === payload.sous_theme ? 1 : 0) }))
    .sort((x, y) => y.adj - x.adj)
    .slice(0, 3);
  if (!m.length) {
    state.compo = null;
    state.pasTrouve = payload;
    if (location.hash !== '#/introuvable') location.hash = '#/introuvable'; else render();
    return;
  }
  nouvelleCompo(m[0].fiche, { question: payload.affirmation, force: m[0].force, profil: payload.interlocuteur, vue: payload.mode === 'convaincre' ? 'convaincre' : 'gagner', autres: m.slice(1).map((x) => x.fiche) });
  if (location.hash !== '#/argumentaire') location.hash = '#/argumentaire'; else render();
}

// ---------------------------------------------------------------- thématiques
function viewThemes() {
  return `<section class="section">
    <div class="wrap wrap--narrow">
      <h1 class="page-title">Thématiques</h1>
      <p class="section-lede">Cinq rubriques à la une, puis dix grands volets. Choisis-en un pour voir ses fiches ou préparer un débat.</p>
      <h2 class="section-title small">Rubriques</h2>
      <div class="rub-list">${RUBRIQUES.map((r) => `<a class="rub-card rub-card--${r.id}" href="#/rubriques/${r.id}">
        <span class="rub-name">${h(r.label)}</span>
        <span class="rub-desc">${h(r.description)}</span>
        <span class="rub-go">Voir les fiches</span>
      </a>`).join('')}</div>
      <h2 class="section-title small">Les dix volets</h2>
      <div class="volet-list">${VOLETS.map((v) => `<a class="volet-card volet-link" href="#/thematiques/${v.id}">
        <span class="volet-icon" aria-hidden="true">${VOLET_ICONS[v.id]}</span>
        <span class="volet-name">${h(v.label)}</span>
        <span class="volet-count">${v.sousThemes.length ? `${v.sousThemes.length} sous-thèmes` : 'Saisie libre'}</span>
      </a>`).join('')}</div>
    </div>
  </section>`;
}

function viewTheme(id) {
  const v = VOLETS.find((x) => x.id === id);
  if (!v) return viewNotFound();
  return `<section class="section">
    <div class="wrap wrap--narrow">
      <p class="crumb"><a href="#/thematiques">Thématiques</a></p>
      <h1 class="page-title"><span class="title-icon" aria-hidden="true">${VOLET_ICONS[v.id]}</span> ${h(v.label)}</h1>
      <a class="btn btn-primary btn-block" href="#/debat" data-start-volet="${v.id}">Préparer un débat sur ce volet</a>
      ${v.sousThemes.length ? `<h2 class="section-title small">Sous-thèmes</h2>
      <ul class="sub-list">${v.sousThemes.map((st) => `<li><button type="button" class="sub-item" data-start-volet="${v.id}" data-start-sub="${h(st)}"><span>${h(st)}</span><span class="sub-go">Préparer</span></button></li>`).join('')}</ul>` : '<p>Pour tout autre sujet, écris librement l’affirmation : le moteur la traitera.</p>'}
      <h2 class="section-title small">Fiches vérifiées de ce volet</h2>
      <div id="theme-fiches" class="fiche-grid"><p class="hint">Chargement…</p></div>
    </div>
  </section>`;
}

function viewRubrique(id) {
  const r = rubriqueById(id);
  if (!r) return viewNotFound();
  return `<section class="section">
    <div class="wrap wrap--narrow">
      <p class="crumb"><a href="#/thematiques">Thématiques</a></p>
      <h1 class="page-title">${h(r.label)}</h1>
      <p class="section-lede">${h(r.description)}</p>
      <aside class="notice" role="note"><p>${h(r.avertissement)}</p></aside>
      <h2 class="section-title small">Les fiches</h2>
      <div id="rubrique-fiches" class="fiche-grid"><p class="hint">Chargement…</p></div>
    </div>
  </section>`;
}

// ---------------------------------------------------------------- bibliothèque
function viewLibrary(params) {
  const q = params.get('q') || '';
  const volet = params.get('volet') || '';
  const rubrique = params.get('rubrique') || '';
  const fiab = params.get('fiabilite') || '';
  return `<section class="section">
    <div class="wrap wrap--narrow">
      <h1 class="page-title">Bibliothèque</h1>
      <p class="section-lede">La base de connaissances : idées reçues, fiches historiques et réponses aux critiques, avec leurs sources, leur niveau de fiabilité et leur date de vérification. Une fiche ancienne est signalée « À actualiser ».</p>
      <form class="library-search" id="library-search" role="search">
        <label class="visually-hidden" for="lib-q">Rechercher</label>
        <input id="lib-q" type="search" placeholder="RSA, délinquance, impôts…" value="${h(q)}">
        <label class="visually-hidden" for="lib-volet">Volet</label>
        <select id="lib-volet"><option value="">Tous les volets</option>${VOLETS.filter((v) => v.id !== 'autre').map((v) => `<option value="${v.id}" ${volet === v.id ? 'selected' : ''}>${h(v.court)}</option>`).join('')}</select>
        <label class="visually-hidden" for="lib-rubrique">Rubrique</label>
        <select id="lib-rubrique"><option value="">Toutes les rubriques</option>${RUBRIQUES.map((r) => `<option value="${r.id}" ${rubrique === r.id ? 'selected' : ''}>${h(r.court)}</option>`).join('')}</select>
        <label class="visually-hidden" for="lib-fiab">Fiabilité</label>
        <select id="lib-fiab"><option value="">Toute fiabilité</option>${Object.entries(FIABILITES).map(([k, v]) => `<option value="${k}" ${fiab === k ? 'selected' : ''}>${h(v)}</option>`).join('')}</select>
        <button class="btn btn-primary" type="submit">Rechercher</button>
      </form>
      <div id="library-results" class="fiche-grid"><p class="hint">Chargement des fiches…</p></div>
    </div>
  </section>`;
}

async function loadFiches(box, query, emptyLink = true) {
  try {
    const { fiches } = await api.library(query);
    if (!box.isConnected) return;
    const count = box.id === 'library-results' ? `<p class="lib-count" role="status">${fiches.length} fiche${fiches.length > 1 ? 's' : ''}</p>` : '';
    box.innerHTML = fiches.length ? count + fiches.map(ficheCard).join('') : `<div class="empty"><p>Aucune fiche ne correspond pour l’instant.</p>${emptyLink ? `<a class="btn btn-primary" href="#/debat" data-prefill-text="${h(query.q || '')}">Vérifier en direct</a>` : ''}</div>`;
  } catch (e) {
    box.innerHTML = errorBox(e.message);
  }
}

// ---------------------------------------------------------------- mode, données locales, publication, veille
function viewMode() {
  const m = appMode();
  const meta = kb.meta || {};
  const st = state.status;
  return `<section class="section">
    <div class="wrap wrap--narrow prose-page">
      <h1 class="page-title">Mode et hors-ligne</h1>
      <div class="segmented mode-pick" role="radiogroup" aria-label="Mode de fonctionnement">
        <button type="button" role="radio" aria-checked="${m === 'autonome'}" class="${m === 'autonome' ? 'is-on' : ''}" data-set-mode="autonome">Autonome — sans Internet</button>
        <button type="button" role="radio" aria-checked="${m === 'connecte'}" class="${m === 'connecte' ? 'is-on' : ''}" data-set-mode="connecte">Connecté</button>
      </div>
      <h2>Mode autonome</h2>
      <ul>
        <li><strong>Disponible sans connexion</strong> (après une première visite) : la bibliothèque (${kb.fiches.length || meta.nb || '…'} fiches), la recherche locale, les fiches à sept onglets, le questionnaire sur l’interlocuteur, les deux stratégies composées à partir des fiches, l’adaptation après chaque échange, l’historique et les argumentaires enregistrés.</li>
        <li><strong>Comment c’est composé :</strong> par un moteur de règles qui assemble des éléments déjà vérifiés de la bibliothèque (faits, sources, contre-arguments, formulations) selon le profil choisi. <strong>Il n’y a pas de modèle d’IA embarqué</strong> : aucun texte libre n’est généré, et aucun fait n’est inventé.</li>
        <li><strong>Ce qui n’est pas disponible :</strong> la recherche web, les informations postérieures à la dernière mise à jour de la base, les reformulations libres. Si une question n’est pas couverte, l’application le dit.</li>
      </ul>
      <h2>Mode connecté</h2>
      <p>Facultatif. Il ajoute la recherche web en direct et la rédaction assistée par IA, quand un serveur est configuré. État actuel : <strong>${h(st?.mode === 'live' ? 'serveur configuré, recherche web active' : st?.mode === 'demo' ? 'serveur présent, recherche web non configurée' : 'aucun serveur configuré pour ce site')}</strong>. Le mode autonome reste utilisable dans tous les cas.</p>
      <h2>La base de connaissances sur cet appareil</h2>
      <dl class="kb-meta">
        <div><dt>Version</dt><dd>${h(meta.version || 'non encore enregistrée')}</dd></div>
        <div><dt>Fiches</dt><dd>${h(String(kb.fiches.length || meta.nb || '—'))}</dd></div>
        <div><dt>Dernière actualisation reçue</dt><dd>${meta.date ? h(frDate(meta.date.slice(0, 10))) : '—'}</dd></div>
        <div><dt>Hors-ligne</dt><dd>${'serviceWorker' in navigator && location.protocol !== 'file:' ? 'activé après la première visite' : 'non disponible dans ce contexte (aperçu ou fichier local)'}</dd></div>
      </dl>
      <label class="check"><input type="checkbox" id="maj-auto" ${store.reglages().majAuto ? 'checked' : ''}> Installer automatiquement les nouvelles versions de la base (après vérification de leur intégrité)</label>
      <div class="btn-row"><button type="button" class="btn btn-secondary" data-action="check-kb">Vérifier les mises à jour</button><a class="btn btn-ghost" href="#/mes-donnees">Mes données</a></div>
      <p class="form-msg" id="kb-msg" role="status"></p>
      ${store.persistant() ? '' : '<p class="notice">Ce navigateur refuse le stockage local : l’historique et les argumentaires ne pourront pas être conservés.</p>'}
    </div>
  </section>`;
}

function viewMesDonnees() {
  const hist = store.historique();
  const args = store.argumentaires();
  const profs = store.profils();
  return `<section class="section">
    <div class="wrap wrap--narrow prose-page">
      <h1 class="page-title">Mes données</h1>
      <p class="lead">Tout ce qui est ici reste sur cet appareil. Rien n’est envoyé à un serveur.</p>
      <h2>Argumentaires enregistrés (${args.length})</h2>
      ${args.length ? `<ul class="data-list">${args.map((a) => `<li><a href="#/argumentaire/${h(a.fiche_id)}?enr=${h(a.id)}">« ${h(a.affirmation)} »</a><span class="hint"> ${h(frDate(a.date.slice(0, 10)))} · ${h(a.resume_profil || '')}</span> <button type="button" class="link-btn" data-del-arg="${h(a.id)}">Supprimer</button></li>`).join('')}</ul>` : '<p>Aucun argumentaire enregistré.</p>'}
      <h2>Fiches consultées (${hist.length})</h2>
      ${hist.length ? `<ul class="data-list">${hist.map((x) => `<li><a href="#/bibliotheque/${h(x.id)}">« ${h(x.affirmation)} »</a><span class="hint"> ${h(frDate(x.date.slice(0, 10)))}</span></li>`).join('')}</ul><button type="button" class="link-btn" data-clear="historique">Effacer l’historique</button>` : '<p>Aucune fiche consultée.</p>'}
      <h2>Profils d’interlocuteur (${profs.length})</h2>
      <p class="hint">Facultatifs, modifiables et supprimables. Évite d’y mettre de vrais noms.</p>
      ${profs.length ? `<ul class="data-list">${profs.map((x) => `<li><strong>${h(x.nom)}</strong><span class="hint"> ${h(resumeProfil(x.profil))}</span> <button type="button" class="link-btn" data-del-profile="${h(x.id)}">Supprimer</button></li>`).join('')}</ul>` : '<p>Aucun profil enregistré.</p>'}
      <p><button type="button" class="btn btn-ghost" data-clear="tout">Tout effacer sur cet appareil</button></p>
    </div>
  </section>`;
}

function viewPublier() {
  const here = location.href.split('#')[0];
  const local = /^(file:|https?:\/\/(localhost|127\.|\[::1\]))/.test(here) || /claude|artifact/.test(location.host);
  return `<section class="section">
    <div class="wrap wrap--narrow prose-page">
      <h1 class="page-title">Publier et partager</h1>
      <p class="lead">Rendre l’application accessible à tout le monde avec un lien. Le guide complet pour le développeur est dans le fichier <code>PUBLIER.md</code> du projet.</p>
      <h2>Le lien de cette page</h2>
      ${local ? '<p class="notice">Tu consultes une version locale ou un aperçu : ce lien ne fonctionnera pas sur un autre appareil. Il faut d’abord publier le site (étapes ci-dessous).</p>' : ''}
      <div class="copy-url"><input type="text" readonly value="${h(here)}" id="share-url" aria-label="Adresse du site"><button type="button" class="btn btn-secondary btn-small" data-action="copy-url">Copier</button>${'share' in navigator ? '<button type="button" class="btn btn-secondary btn-small" data-action="share-site">Partager</button>' : ''}</div>
      <h2>Deux façons de publier</h2>
      <ol>
        <li><strong>Mode autonome seul, gratuit : GitHub Pages ou Cloudflare Pages.</strong> Le site statique (bibliothèque, compositeur, hors-ligne) se publie sans serveur. La commande <code>npm run build:static</code> produit le dossier <code>dist/site</code> ; un flux GitHub Actions fourni (<code>.github/workflows/pages.yml</code>) le publie automatiquement à chaque modification.</li>
        <li><strong>Mode connecté : un serveur Node en plus.</strong> La recherche web et l’IA ont besoin du serveur (clé API secrète). Il s’héberge sur un service compatible Node (Render, Railway, Fly.io, un petit VPS…), avec les plafonds de dépenses déjà prévus dans le projet.</li>
      </ol>
      <h2>Avant de partager : la checklist</h2>
      <ul class="checklist">
        <li>Le site s’ouvre sur un téléphone, sur un autre réseau (4G).</li>
        <li>Après une première visite, il fonctionne en mode avion (bibliothèque, fiches, argumentaires).</li>
        <li>Les liens des sources s’ouvrent.</li>
        <li>Les deux stratégies (« Gagner le débat » et « Convaincre avec empathie ») s’affichent pour une question couverte.</li>
        <li>Aucun message d’erreur n’apparaît à cause d’un serveur volontairement absent.</li>
        <li>Aucune clé API ni fichier <code>.env</code> dans le dépôt public ; plafonds de dépenses réglés côté fournisseur et côté serveur.</li>
      </ul>
      <h2>Coûts, en bref</h2>
      <p>Hébergement statique : gratuit dans les limites des offres (à vérifier au moment de publier). Nom de domaine : facultatif et payant (environ une dizaine d’euros par an selon l’extension). Recherche web et IA : facturées à l’usage par le fournisseur d’IA ; le serveur applique des plafonds journaliers et mensuels. Détails et précautions : <code>PUBLIER.md</code>.</p>
    </div>
  </section>`;
}

function viewVeille() {
  return `<section class="section">
    <div class="wrap wrap--narrow prose-page">
      <h1 class="page-title">Veille et actualisations</h1>
      <p class="lead">Un système de veille cherche, toutes les 24 à 48 heures, les évolutions qui changent vraiment les arguments de la bibliothèque, puis propose des mises à jour vérifiées.</p>
      <div id="veille-box"><p class="hint">Chargement de l’état de la veille…</p></div>
    </div>
  </section>`;
}

function veilleHtml(v) {
  if (!v || v.statut === 'indisponible' || (v.statut !== 'actif' && !v.derniere_tentative)) {
    return `<aside class="notice" role="note"><p><strong>Aucune planification active pour ce site.</strong> La veille s’exécute sur un serveur ou une tâche planifiée (GitHub Actions) ; elle n’est pas encore configurée ici. La bibliothèque locale reste utilisable.</p></aside>
      <p class="hint">Activation : voir « Veille automatique » dans <code>PUBLIER.md</code>.</p>`;
  }
  const r = v.dernier_rapport || {};
  const n = r.compteurs || {};
  return `${v.statut !== 'actif' ? '<aside class="notice" role="note"><p><strong>Aucune planification active pour ce site.</strong> Les résultats ci-dessous viennent du dernier cycle exécuté.</p></aside>' : ''}<dl class="kb-meta">
      <div><dt>Dernière actualisation réussie</dt><dd>${v.derniere_reussite ? h(new Date(v.derniere_reussite).toLocaleString('fr-FR')) : 'aucune pour l’instant'}</dd></div>
      <div><dt>Prochaine actualisation prévue</dt><dd>${v.prochaine ? h(new Date(v.prochaine).toLocaleString('fr-FR')) : 'aucune planification active'}</dd></div>
      <div><dt>Intervalle</dt><dd>${v.intervalle_heures ? `${h(String(v.intervalle_heures))} h` : '—'}</dd></div>
      <div><dt>Planificateur</dt><dd>${h(v.planificateur || 'non configuré')}</dd></div>
    </dl>
    <h2>Dernier cycle</h2>
    <ul class="veille-counts">
      <li><strong>${n.collectees ?? 0}</strong> informations collectées</li>
      <li><strong>${n.verifiees ?? 0}</strong> vérifiées selon les règles</li>
      <li><strong>${n.en_attente ?? 0}</strong> en attente de validation humaine</li>
      <li><strong>${n.rejetees ?? 0}</strong> rejetées (source non obtenue, date invalide, doublon…)</li>
      <li><strong>${n.nouvelles_fiches ?? 0}</strong> nouvelles fiches proposées</li>
      <li><strong>${n.fiches_actualisees ?? 0}</strong> fiches actualisées</li>
      <li><strong>${n.statistiques_remplacees ?? 0}</strong> statistiques remplacées</li>
      <li><strong>${n.sources_ajoutees ?? 0}</strong> sources ajoutées</li>
      <li><strong>${(r.fiches_obsoletes || []).length}</strong> fiches signalées comme potentiellement obsolètes</li>
      <li><strong>${(r.erreurs || []).length}</strong> erreurs de collecte ou de validation</li>
      <li>Coût estimé : ${r.cout_usd != null ? `${h(Number(r.cout_usd).toFixed(3))} $` : 'non disponible'}</li>
    </ul>
    ${(r.fiches_obsoletes || []).length ? `<h3 class="sub-title">Fiches à revoir</h3><ul>${r.fiches_obsoletes.map((x) => `<li><a href="#/bibliotheque/${h(x.fiche_id)}">${h(x.fiche_id)}</a> — ${h(x.raison)}</li>`).join('')}</ul>` : ''}
    ${(r.erreurs || []).length ? `<h3 class="sub-title">Erreurs</h3><ul>${r.erreurs.map((x) => `<li>${h(x)}</li>`).join('')}</ul>` : ''}
    <h2>Actualiser maintenant</h2>
    <p class="hint">Lance un cycle de veille sur le serveur (payant : recherches web). Réservé à l’administrateur, protégé par un jeton.</p>
    <form class="panel" id="veille-run">
      <label class="field"><span class="field-label">Jeton d’administration</span><input type="password" id="veille-token" autocomplete="off" required></label>
      <button class="btn btn-primary" type="submit">Actualiser maintenant</button>
      <p class="form-msg" role="status"></p>
    </form>`;
}

// ---------------------------------------------------------------- à propos & confidentialité
function viewAbout() {
  return `<section class="section">
    <div class="wrap wrap--narrow prose-page">
      <h1 class="page-title">À propos</h1>
      <p class="lead">Gauchise tes parents est un projet indépendant créé par Marty Ducanda pour l’éducation populaire, le fact-checking et l’esprit critique.</p>
      <h2>Notre ligne éditoriale</h2>
      <p>Le projet assume une orientation de gauche : justice sociale, solidarité, égalité, services publics, lutte contre les idées reçues. L’outil aide à défendre des arguments de gauche et à analyser les discours de droite et d’extrême droite. Les partis et les personnalités sont des sujets d’analyse, pas des verdicts écrits d’avance.</p>
      <p>Assumer une ligne, ce n’est pas tricher avec les faits. L’outil distingue toujours les faits vérifiables, les interprétations, les jugements de valeur et les propositions politiques. Si une donnée contredit ton argument, il te le dit et t’aide à le reformuler sur des bases solides.</p>
      <h2>Deux stratégies, une seule exigence de preuve</h2>
      <ul>
        <li><strong>Gagner le débat :</strong> quand l’interlocuteur est campé sur ses positions. Le vrai public, c’est le reste de la table.</li>
        <li><strong>Convaincre sans braquer :</strong> quand le dialogue est possible. On part des inquiétudes, sans flatterie ni manipulation.</li>
      </ul>
      <h2>Comment la recherche fonctionne</h2>
      <ul>
        <li>La base locale d’abord : ta question est comparée aux fiches vérifiées à la main, qui s’affichent tout de suite.</li>
        <li>Si une fiche traite précisément ta question et que ses données sont stables ou encore à jour, la réponse est construite à partir d’elle, sans recherche web.</li>
        <li>Si le sujet est récent, contesté, mal couvert ou si la fiche doit être actualisée, le moteur lance de vraies recherches sur le Web, ouvre les documents les plus importants et compare les données avec la fiche. Les écarts sont signalés ; une fiche n’est modifiée qu’après relecture humaine.</li>
        <li>Le serveur retire toute référence qui n’a pas réellement été obtenue pendant la recherche, et indique si un document a été lu en entier ou seulement aperçu dans les résultats.</li>
        <li>Chaque chiffre est recherché dans le texte réellement consulté : s’il n’y figure pas tel quel, c’est signalé.</li>
        <li>Les arguments sont rédigés ensuite, uniquement à partir de ce dossier vérifié. Un chiffre qui n’y figure pas est signalé.</li>
      </ul>
      <h2>Les limites du moteur</h2>
      <ul>
        <li>Un modèle de langage peut mal interpréter une source ou rater un document récent. Les liens sont là pour être cliqués.</li>
        <li>Certains sites refusent la consultation automatique ; certains PDF ne permettent pas le contrôle automatique des chiffres.</li>
        <li>Sans configuration du moteur, l’application reste en mode démonstration : aucune recherche, aucun verdict, seulement les fiches vérifiées à la main.</li>
      </ul>
      <h2>Signaler une erreur</h2>
      <p>Utilise « Signaler une source incorrecte » sous chaque source, l’avis en bas de chaque analyse, ou ce formulaire.</p>
      ${peutEnvoyer() ? '' : '<p class="notice">Le formulaire de signalement a besoin du serveur du mode connecté, qui n’est pas disponible ici.</p>'}
      <form class="panel" id="report-form" ${peutEnvoyer() ? '' : 'hidden'}>
        <label class="field"><span class="field-label">Ce qui ne va pas</span><textarea name="commentaire" id="report-comment" rows="3" maxlength="1000" required></textarea></label>
        <label class="field"><span class="field-label">Lien concerné (facultatif)</span><input type="url" name="url" id="report-url" placeholder="https://"></label>
        <button class="btn btn-primary" type="submit">Envoyer le signalement</button>
        <p class="form-msg" role="status"></p>
      </form>
      <p><a href="#/confidentialite">Politique de confidentialité</a></p>
      ${supportCard('main', '-about')}
    </div>
  </section>`;
}

function viewPrivacy() {
  return `<section class="section">
    <div class="wrap wrap--narrow prose-page">
      <h1 class="page-title">Confidentialité</h1>
      <p class="lead">On collecte le strict minimum, on ne fait pas de profil politique, et on ne garde pas tes conversations.</p>
      <h2>Ce qui est traité</h2>
      <ul>
        <li><strong>L’affirmation</strong> et tes choix (objectif, volet, interlocuteur, contexte) sont envoyés au serveur puis au fournisseur d’IA (Anthropic) pour produire l’analyse. Le serveur garde le dossier en mémoire vive quelques heures pour permettre de changer de stratégie sans relancer la recherche, puis l’oublie. Rien n’est écrit sur disque.</li>
        <li><strong>Le profil d’interlocuteur</strong> sert uniquement à adapter le ton de la réponse en cours.</li>
        <li><strong>Ton parcours en cours</strong> est gardé dans ton navigateur (stockage de session), pour ne pas tout ressaisir. Il disparaît à la fermeture de l’onglet.</li>
        <li><strong>Les retours</strong> sont enregistrés sans adresse IP ni identifiant, avec la seule date du jour. L’affirmation n’y est jointe que si tu coches la case.</li>
        <li><strong>La limitation anti-abus</strong> utilise ton adresse IP hachée, en mémoire vive, quelques minutes.</li>
      </ul>
      <h2>Ce qui n’est pas fait</h2>
      <ul>
        <li>Pas de compte, pas de cookie de suivi, pas de mesure d’audience, pas de publicité.</li>
        <li>Aucune déduction d’opinions politiques sur toi ou ta famille. Aucun dossier sur tes proches.</li>
        <li>Les retours ne servent jamais à mesurer une « conversion » idéologique.</li>
      </ul>
      <p>N’écris pas de nom ni d’information personnelle dans l’affirmation : elle est transmise au fournisseur d’IA.</p>
      <p>Le lien de soutien ouvre le site Tipeee, qui applique sa propre politique de confidentialité.</p>
    </div>
  </section>`;
}

function viewNotFound() {
  return `<section class="section"><div class="wrap wrap--narrow center">${mascotSvg('inverifiable', 'Mascotte perplexe', 120)}<h1 class="page-title">Page introuvable</h1><p>Cette page n’existe pas, ou plus.</p><a class="btn btn-primary" href="#/">Retour à l’accueil</a></div></section>`;
}

function updateModePill() {
  const pill = $('#mode-pill');
  if (!pill) return;
  pill.textContent = appMode() === 'autonome' ? 'Autonome' : isLive() ? 'Connecté' : 'Connecté · non configuré';
  pill.title = serverLabel();
  pill.dataset.mode = appMode();
}

// ---------------------------------------------------------------- routeur
function parseRoute() {
  const raw = location.hash.replace(/^#/, '');
  const [path, query = ''] = raw.split('?');
  return { path: `/${path.replace(/^\/+|\/+$/g, '')}`, params: new URLSearchParams(query) };
}

const TABS = [
  ['/', 'Accueil', 'accueil', (p) => p === '/' || p === '/comment-ca-marche'],
  ['/debat', 'Débat', 'debat', (p) => ['/debat', '/express', '/resultat', '/argumentaire', '/introuvable'].includes(p) || p.startsWith('/argumentaire/')],
  ['/thematiques', 'Thématiques', 'thematiques', (p) => p.startsWith('/thematiques') || p.startsWith('/rubriques')],
  ['/bibliotheque', 'Bibliothèque', 'bibliotheque', (p) => p.startsWith('/bibliotheque')],
];

function renderTabs(path) {
  $('[data-tabbar]').innerHTML = TABS.map(([href, label, icon, active]) => `<a href="#${href}" class="tab" ${active(path) ? 'aria-current="page"' : ''}>${TAB_ICONS[icon]}<span>${label}</span></a>`).join('');
}

async function render() {
  let { path, params } = parseRoute();
  // anciennes adresses
  if (path === '/verifier') path = '/debat';
  if (path.startsWith('/idees-recues')) path = path.replace('/idees-recues', '/bibliotheque');

  const app = $('#app');
  let html;
  let after = null;
  let scrollTo = null;
  const fiche = path.match(/^\/bibliotheque\/([a-z0-9-]+)$/);
  const theme = path.match(/^\/thematiques\/([a-z]+)$/);
  const rubrique = path.match(/^\/rubriques\/([a-z-]+)$/);
  const argu = path.match(/^\/argumentaire\/([a-z0-9-]+)$/);

  if (path === '/' || path === '/comment-ca-marche') {
    html = viewHome();
    if (path === '/comment-ca-marche') scrollTo = 'comment';
  } else if (path === '/debat') {
    const m = params.get('mode');
    if (MODES[m] && state.wizard.mode !== m) { state.wizard.mode = m; if (state.wizard.step === 1) state.wizard.step = 2; persist(); }
    html = viewWizard();
    after = bindWizardInputs;
  } else if (path === '/express') {
    html = viewExpress();
    after = bindExpressInputs;
  } else if (path === '/resultat') {
    if (!state.result) html = `<section class="section"><div class="wrap wrap--narrow center"><h1 class="page-title">Aucune analyse en cours</h1><a class="btn btn-primary" href="#/debat">Préparer un débat</a></div></section>`;
    else html = state.result.mode === 'demo' ? renderDemo(state.result) : renderResult(state.result);
  } else if (path === '/thematiques') {
    html = viewThemes();
  } else if (theme) {
    html = viewTheme(theme[1]);
    after = () => { const box = $('#theme-fiches'); if (box) loadFiches(box, { volet: theme[1] }, false); };
  } else if (path === '/argumentaire') {
    if (!state.compo) {
      html = viewLoading('Reprise de la conversation', { strategy: true });
      after = async () => {
        await kb.load();
        restaurerConv(kb.fiches);
        if (parseRoute().path === path) { app.innerHTML = viewArgumentaire(); }
      };
    } else html = viewArgumentaire();
  } else if (argu) {
    html = viewLoading('Composition de l’argumentaire', { strategy: true });
    after = async () => {
      try {
        const f = await api.fiche(argu[1]);
        const saved = params.get('enr') ? store.argumentaires().find((x) => x.id === params.get('enr')) : null;
        if (!state.compo && !saved) { await kb.load(); restaurerConv(kb.fiches); }
        if (!state.compo || state.compo.fiche.id !== f.id || saved) nouvelleCompo(f, { profil: saved?.profil, vue: saved?.vue });
        if (parseRoute().path === path) app.innerHTML = viewArgumentaire();
      } catch (e) {
        app.innerHTML = `<section class="section"><div class="wrap wrap--narrow">${errorBox(e.message)}</div></section>`;
      }
    };
  } else if (path === '/introuvable') {
    html = state.pasTrouve ? viewPasDansLaBase(state.pasTrouve) : viewNotFound();
  } else if (path === '/mode') {
    html = viewMode();
  } else if (path === '/mes-donnees') {
    html = viewMesDonnees();
  } else if (path === '/publier') {
    html = viewPublier();
  } else if (path === '/veille') {
    html = viewVeille();
    after = async () => { const v = await api.veille(); const box = $('#veille-box'); if (box) box.innerHTML = veilleHtml(v); };
  } else if (rubrique) {
    html = viewRubrique(rubrique[1]);
    after = () => { const box = $('#rubrique-fiches'); if (box) loadFiches(box, { rubrique: rubrique[1] }, false); };
  } else if (path === '/bibliotheque') {
    html = viewLibrary(params);
    after = () => loadFiches($('#library-results'), { q: params.get('q') || '', volet: params.get('volet') || '', rubrique: params.get('rubrique') || '', fiabilite: params.get('fiabilite') || '' });
  } else if (fiche) {
    html = viewLoading('Ouverture de la fiche', { strategy: true });
    after = async () => {
      try {
        const data = await api.fiche(fiche[1]);
        state.currentFiche = data;
        store.noterConsultation(data);
        if (parseRoute().path === `/bibliotheque/${fiche[1]}` || parseRoute().path === `/idees-recues/${fiche[1]}`) app.innerHTML = viewFiche(data, params.get('onglet') || 'court');
      } catch (e) {
        app.innerHTML = `<section class="section"><div class="wrap wrap--narrow">${errorBox(e.message)}</div></section>`;
      }
    };
  } else if (path === '/a-propos') {
    html = viewAbout();
  } else if (path === '/confidentialite') {
    html = viewPrivacy();
  } else {
    html = viewNotFound();
  }

  app.innerHTML = html;
  renderTabs(path);
  $('[data-about]')?.toggleAttribute('aria-current', path === '/a-propos');
  if (after) await after();
  if (scrollTo) {
    $(`#${scrollTo}`)?.scrollIntoView({ behavior: reduceMotion() ? 'auto' : 'smooth' });
  } else {
    window.scrollTo(0, 0);
    $('#main').focus({ preventScroll: true });
  }
}

// ---------------------------------------------------------------- parcours : saisies
function bindWizardInputs() {
  const w = state.wizard;
  const aff = $('#affirmation');
  if (aff) {
    aff.addEventListener('input', (e) => {
      w.affirmation = e.target.value;
      $('#aff-count').textContent = `${w.affirmation.length} / ${LIMITS.claimMax}`;
      persist();
    });
  }
  $('#contexte')?.addEventListener('change', (e) => { w.contexte = e.target.value; persist(); });
}

function bindExpressInputs() {
  const e = state.express;
  $('#express-text')?.addEventListener('input', (ev) => { e.affirmation = ev.target.value; persist(); });
  $('#express-volet')?.addEventListener('change', (ev) => { e.volet = ev.target.value; persist(); rafraichirSugg('express', 'express-text'); });
}

function rerenderWizard() {
  $('#app').innerHTML = viewWizard();
  bindWizardInputs();
  const t = $('.step-title');
  t?.setAttribute('tabindex', '-1');
  t?.focus();
  window.scrollTo(0, 0);
}

async function launchAnalyse(payload) {
  state.request = payload;
  $('#app').innerHTML = viewLoading(payload.affirmation);
  window.scrollTo(0, 0);
  animateLoading();
  // Base locale d'abord : les fiches correspondantes s'affichent pendant que l'analyse tourne.
  api.kbSearch(payload.affirmation).then((b) => {
    const box = $('#kb-instant');
    if (box && b.correspondances?.length) box.innerHTML = `<div class="kb-instant-in"><p class="kb-instant-title">En attendant, déjà dans la base locale :</p><div class="fiche-grid">${b.correspondances.map(ficheCard).join('')}</div><p class="hint">${h(b.decision.raison)}</p></div>`;
  }).catch(() => { /* la base locale est un bonus : l'analyse continue */ });
  try {
    const data = await api.analyse(payload);
    state.result = data;
    state.speech = {};
    if (location.hash !== '#/resultat') location.hash = '#/resultat';
    else render();
  } catch (e) {
    $('#app').innerHTML = `<section class="section"><div class="wrap wrap--narrow">${errorBox(e.message, { retry: e.data?.relancer || e.status === 0 })}</div></section>`;
    state.retry = () => launchAnalyse(payload);
  }
}

async function switchStrategy(payload, label) {
  const keep = window.scrollY;
  $('#app').innerHTML = viewLoading(label, { strategy: true });
  try {
    state.result = await api.strategie(payload);
    state.speech = {};
    if (location.hash !== '#/resultat') location.hash = '#/resultat';
    else { render(); if (payload.analyse_id) window.scrollTo(0, Math.min(keep, 200)); }
  } catch (e) {
    $('#app').innerHTML = `<section class="section"><div class="wrap wrap--narrow">${errorBox(e.message, { retry: Boolean(e.data?.relancer) })}</div></section>`;
    state.retry = () => switchStrategy(payload, label);
  }
}

const CADRE_CONTEXTE = { repas: 'repas', prive: 'prive', plusieurs: 'amis', reseaux: 'reseaux' };
const wizardPayload = (w) => {
  const p = nettoyerProfil(w.interlocuteur);
  return {
    affirmation: w.affirmation.trim(), volet: w.volet || 'autre', sous_theme: w.sousTheme || undefined,
    mode: w.mode || 'gagner', profil: profilSimple(p), contexte: CADRE_CONTEXTE[p.cadre] || (p.lien === 'public' ? 'public' : 'repas'),
    interlocuteur: p,
  };
};

// ---------------------------------------------------------------- événements
document.addEventListener('click', async (ev) => {
  const t = ev.target.closest('button, a');
  if (!t) return;
  const w = state.wizard;

  if (t.dataset.startMode) { w.mode = t.dataset.startMode; w.step = 2; persist(); return; }
  if (t.dataset.startVolet) {
    Object.assign(w, { volet: t.dataset.startVolet, sousTheme: t.dataset.startSub || null, step: w.mode ? 3 : 1 });
    persist();
    if (t.matches('button')) location.hash = '#/debat';
    return;
  }
  if (t.dataset.prefillText !== undefined) { w.affirmation = t.dataset.prefillText; w.step = w.mode ? 2 : 1; persist(); return; }
  if (t.hasAttribute('data-prefill-fiche') && state.currentFiche) {
    Object.assign(w, { affirmation: state.currentFiche.affirmation, volet: state.currentFiche.volet, sousTheme: state.currentFiche.sous_theme, step: w.mode ? 3 : 1 });
    persist();
    return;
  }
  if (t.dataset.tab) { selectFicheTab(t.dataset.tab); return; }
  if (t.dataset.tabOpen) {
    ev.preventDefault();
    selectFicheTab(t.dataset.tabOpen);
    $('.fiche-tabs')?.scrollIntoView({ behavior: reduceMotion() ? 'auto' : 'smooth', block: 'start' });
    $(`#tab-${t.dataset.tabOpen}`)?.focus({ preventScroll: true });
    return;
  }
  // questionnaire interlocuteur
  if (t.dataset.dim) {
    const ctx = t.dataset.ctx;
    const p = { ...nettoyerProfil(profilOf(ctx)) };
    delete p.inconnu;
    const d = INTERLOCUTEUR.find((x) => x.id === t.dataset.dim);
    if (d.multi) {
      const cur = Array.isArray(p[d.id]) ? p[d.id] : [];
      p[d.id] = cur.includes(t.dataset.val) ? cur.filter((x) => x !== t.dataset.val) : [...cur, t.dataset.val].slice(-d.multi);
    } else {
      p[d.id] = p[d.id] === t.dataset.val ? undefined : t.dataset.val;
    }
    setProfil(ctx, p);
    return;
  }
  if (t.dataset.inconnu) { setProfil(t.dataset.inconnu, { inconnu: true }); return; }
  if (t.dataset.useProfile) {
    const sp = store.profils().find((x) => x.id === t.dataset.useProfile);
    if (sp) { setProfil(t.dataset.ctx, sp.profil); toast(`Profil « ${sp.nom} » appliqué.`); }
    return;
  }
  if (t.dataset.saveProfile) {
    const ctx = t.dataset.saveProfile;
    const nom = ($(`#profile-name-${ctx}`)?.value || '').trim().slice(0, 40) || resumeProfil(profilOf(ctx)).slice(0, 40);
    const ok = store.enregistrerProfil({ nom, profil: nettoyerProfil(profilOf(ctx)) });
    toast(ok ? 'Profil enregistré sur cet appareil.' : 'Enregistrement impossible : le stockage local est refusé par ce navigateur.');
    setProfil(ctx, profilOf(ctx));
    return;
  }
  // argumentaire composé
  if (t.dataset.strat && state.compo) {
    state.compo.vue = t.dataset.strat;
    if (state.compo.conv && !state.compo.conv.terminee) {
      state.compo.conv.mode = state.compo.vue;
      const et = document.querySelector('.conv-etat .tag');
      if (et) et.textContent = state.compo.vue === 'gagner' ? 'Gagner le débat' : 'Convaincre avec empathie';
      sauverConv();
    }
    $$('[data-strat]').forEach((b) => { const on = b.dataset.strat === state.compo.vue; b.classList.toggle('is-on', on); b.setAttribute('aria-selected', String(on)); b.tabIndex = on ? 0 : -1; });
    $$('[id^="strat-panel-"]').forEach((el) => { el.hidden = el.id !== `strat-panel-${state.compo.vue}`; });
    return;
  }
  if (t.dataset.convRaccourci && state.compo) { envoyerConv($('#conv-msg')?.value || '', t.dataset.convRaccourci); return; }
  if (t.dataset.convOption && state.compo?.conv) {
    const [act, id] = t.dataset.convOption.split(':');
    if (act === 'basculer' && id) { basculerSujet(state.compo.conv, id); toast('Sujet suivant pris en compte. Le sujet initial reste dans l’historique.'); }
    else { revenirSujetInitial(state.compo.conv); toast('Retour au sujet initial.'); }
    sauverConv();
    refreshCompo();
    return;
  }
  if (t.dataset.convCopier && state.compo?.conv) {
    const tr = state.compo.conv.tours.find((x) => String(x.n) === t.dataset.convCopier);
    if (tr) copyText(tr.intervention.texte, 'Réponse copiée !');
    return;
  }
  if (t.dataset.deja !== undefined && state.compo) {
    const i = Number(t.dataset.deja);
    const u = state.compo.session.utilises;
    state.compo.session.utilises = u.includes(i) ? u.filter((x) => x !== i) : [...u, i];
    const cv = state.compo.conv;
    if (cv && !cv.terminee) {
      const fid = state.compo.fiche.id;
      if (u.includes(i)) cv.memoire.arguments = cv.memoire.arguments.filter((a) => !(a.fiche_id === fid && a.index === i && a.tour === 0));
      else if (!cv.memoire.arguments.some((a) => a.fiche_id === fid && a.index === i)) cv.memoire.arguments.push({ fiche_id: fid, index: i, texte: state.compo.fiche.faits[i].fait, tour: 0 });
      sauverConv();
    }
    state.compo.dejaOuvert = true;
    refreshCompo();
    return;
  }
  if (t.dataset.setMode) {
    store.setReglage('mode', t.dataset.setMode);
    state.status = t.dataset.setMode === 'connecte' ? await api.status() : null;
    updateModePill();
    render();
    toast(t.dataset.setMode === 'autonome' ? 'Mode autonome : tout fonctionne sans Internet.' : isLive() ? 'Mode connecté : recherche web active.' : 'Mode connecté : aucun serveur configuré pour ce site. Les fonctions locales restent disponibles.');
    return;
  }
  if (t.dataset.delArg) { store.supprimerArgumentaire(t.dataset.delArg); render(); return; }
  if (t.dataset.delProfile) { store.supprimerProfil(t.dataset.delProfile); render(); return; }
  if (t.dataset.clear) {
    store.effacer(t.dataset.clear);
    toast(t.dataset.clear === 'tout' ? 'Toutes tes données locales ont été effacées.' : 'Historique effacé.');
    render();
    return;
  }
  if (t.dataset.copyTab && state.currentFiche) {
    copyText(state.currentFiche.argumentaires?.[t.dataset.copyTab] || '', 'Texte copié !');
    return;
  }
  if (t.dataset.open) {
    ev.preventDefault();
    const el = document.getElementById(t.dataset.open);
    if (!el) return;
    el.closest('details')?.setAttribute('open', '');
    if (el.matches('details')) el.setAttribute('open', '');
    el.querySelector('details')?.setAttribute('open', '');
    el.scrollIntoView({ behavior: reduceMotion() ? 'auto' : 'smooth', block: 'start' });
    el.focus({ preventScroll: true });
    return;
  }

  // parcours
  if (t.dataset.pickMode) {
    w.mode = t.dataset.pickMode;
    $$('[data-pick-mode]').forEach((b) => { const on = b === t; b.classList.toggle('is-selected', on); b.setAttribute('aria-checked', String(on)); });
    w.step = 2; // un choix suffit : on passe directement au sujet
    persist();
    setTimeout(rerenderWizard, reduceMotion() ? 0 : 180);
    return;
  }
  if (t.dataset.pickVolet) {
    if (w.volet !== t.dataset.pickVolet) w.sousTheme = null;
    w.volet = t.dataset.pickVolet;
    persist();
    $('#wizard-body').innerHTML = wizardBody(w);
    $(`[data-pick-volet="${w.volet}"]`)?.focus();
    return;
  }
  if (t.dataset.pickSub) {
    w.sousTheme = w.sousTheme === t.dataset.pickSub ? null : t.dataset.pickSub;
    $$('[data-pick-sub]').forEach((b) => { const on = b.dataset.pickSub === w.sousTheme; b.classList.toggle('is-on', on); b.setAttribute('aria-pressed', String(on)); });
    persist();
    return;
  }
  if (t.dataset.exampleFill) {
    if (t.dataset.suggCible === 'express-text') {
      state.express.affirmation = t.dataset.exampleFill;
      $('#express-text').value = state.express.affirmation;
      $('#express-text').focus();
      persist();
      return;
    }
    w.affirmation = t.dataset.exampleFill;
    $('#affirmation').value = w.affirmation;
    $('#aff-count').textContent = `${w.affirmation.length} / ${LIMITS.claimMax}`;
    persist();
    return;
  }
  if (t.dataset.suggAutres) {
    const key = t.dataset.suggAutres;
    rafraichirSugg(key, key === 'express' ? 'express-text' : 'affirmation', { renouveler: true });
    document.querySelector(`#sugg-${key} .sugg-chip`)?.focus();
    return;
  }
  if (t.dataset.goto) { w.step = Number(t.dataset.goto); persist(); rerenderWizard(); return; }
  if (t.dataset.expressMode) {
    state.express.mode = t.dataset.expressMode;
    $$('[data-express-mode]').forEach((b) => { const on = b === t; b.classList.toggle('is-on', on); b.setAttribute('aria-checked', String(on)); });
    persist();
    rafraichirSugg('express', 'express-text');
    return;
  }

  // résultats
  if (t.dataset.switchMode && state.result?.dossier) {
    const r = state.result;
    if (r.strategie?.mode === t.dataset.switchMode) return;
    w.mode = t.dataset.switchMode;
    persist();
    const payload = r.origine === 'bibliotheque'
      ? { fiche_id: r.fiche_id || state.currentFiche?.id, mode: w.mode, profil: w.profil, contexte: w.contexte }
      : { analyse_id: r.analyse_id, mode: w.mode, profil: w.profil, contexte: w.contexte };
    switchStrategy(payload, MODES[w.mode].label);
    return;
  }
  if (t.dataset.ficheMode && state.currentFiche) {
    w.mode = t.dataset.ficheMode;
    persist();
    switchStrategy({ fiche_id: state.currentFiche.id, mode: w.mode, profil: w.profil, contexte: w.contexte }, MODES[w.mode].label);
    return;
  }
  if (t.dataset.speech) {
    const r = state.result;
    if (!r?.analyse_id) return;
    const out = $('#speech-out');
    $$('[data-speech]').forEach((b) => b.classList.toggle('is-on', b === t));
    out.innerHTML = '<p class="hint">Doc Source répète devant le miroir…</p>';
    try {
      const sp = await api.demonstration({ analyse_id: r.analyse_id, duree: Number(t.dataset.speech), mode: r.strategie.mode, profil: w.profil, contexte: w.contexte });
      out.innerHTML = `<h4>Version rédigée (${h(sp.mots)} mots)</h4><div class="speech"><p id="speech-text">${h(sp.redigee)}</p></div>
        ${sp.avertissement ? `<p class="num-warn">${h(sp.avertissement)}</p>` : ''}
        <button type="button" class="btn btn-secondary btn-small" data-action="copy-speech">Copier le texte</button>
        <h4>Version spontanée</h4><ul class="spontane">${sp.spontanee.map((x) => `<li>${h(x)}</li>`).join('')}</ul>`;
    } catch (e) {
      out.innerHTML = `<p class="form-error">${h(e.message)}</p>`;
    }
    return;
  }

  const action = t.dataset.action;
  if (!action) return;
  if (action === 'conv-terminer' && state.compo?.conv) {
    terminerConversation(state.compo.conv, { bibliotheque: kb.fiches });
    state.compo.convErreur = null;
    sauverConv();
    refreshCompo();
    $('#conv-bilan')?.scrollIntoView({ behavior: reduceMotion() ? 'auto' : 'smooth', block: 'start' });
    return;
  }
  if (action === 'conv-reprendre' && state.compo?.conv) {
    state.compo.conv.terminee = false;
    state.compo.conv.bilan = null;
    sauverConv();
    refreshCompo();
    return;
  }
  if (action === 'conv-nouvelle' && state.compo) {
    const c = state.compo;
    c.session = { utilises: [], objectionsVues: [], questionsPosees: [], retours: [] };
    c.conv = nouvelleConversation(c.fiche, { mode: c.vue, profil: c.profil, question: c.question });
    c.convErreur = null; c.convStatut = ''; c.convBrouillon = ''; c.convDoublon = null;
    sauverConv();
    refreshCompo();
    $('#conversation')?.scrollIntoView({ behavior: reduceMotion() ? 'auto' : 'smooth', block: 'start' });
    toast('Nouvelle conversation : contexte séparé, la précédente n’est pas mélangée.');
    return;
  }
  if (action === 'conv-reessayer' && state.compo?.convErreur) { const e = state.compo.convErreur; envoyerConv(e.texte, e.raccourci); return; }
  if (action === 'conv-local' && state.compo?.convErreur) { const e = state.compo.convErreur; state.compo.convErreur = null; envoyerConv(e.texte, e.raccourci, { local: true }); return; }
  if (action === 'conv-forcer' && state.compo?.convDoublon) { const d = state.compo.convDoublon; envoyerConv(d.texte, d.raccourci, { force: true }); return; }
  if (action === 'save-compo' && state.compo) {
    const c = state.compo;
    const ok = store.enregistrerArgumentaire({ fiche_id: c.fiche.id, affirmation: c.question || c.fiche.affirmation, profil: c.profil, resume_profil: resumeProfil(c.profil), vue: c.vue, replique: c.last?.gagner?.replique || '', retours: (c.conv?.tours || []).map((x) => x.analyse.type) });
    toast(ok ? 'Argumentaire enregistré sur cet appareil (Mes données).' : 'Enregistrement impossible : le stockage local est refusé par ce navigateur.');
    return;
  }
  if (action === 'share-compo' && state.compo) {
    const a = state.compo.last;
    const src = a.gagner.preuves.map((p) => p.source && `${p.source.organisme}, « ${p.source.titre} », ${p.source.date}. ${p.source.url}`).filter(Boolean);
    const text = [`« ${state.compo.fiche.affirmation} »`, '', a.gagner.replique, src.length ? `\nSources :\n${[...new Set(src)].join('\n')}` : '', '\nPréparé avec Gauchise tes parents.'].join('\n');
    if (navigator.share) { try { await navigator.share({ title: 'Gauchise tes parents', text }); return; } catch (e) { if (e?.name === 'AbortError') return; } }
    copyText(text, 'Réponse sourcée copiée : colle-la où tu veux !');
    return;
  }
  if ((action === 'web-compo' || action === 'web-search-local') && isLive()) {
    const c = state.compo;
    const base = state.request || wizardPayload(state.wizard);
    launchAnalyse({ ...base, affirmation: c?.question || base.affirmation, interlocuteur: c ? c.profil : base.interlocuteur, profil: profilSimple(c ? c.profil : base.interlocuteur) });
    return;
  }
  if (action === 'check-kb') {
    const msg = $('#kb-msg');
    msg.textContent = 'Vérification…';
    const r = await kb.checkUpdate();
    msg.textContent = {
      a_jour: 'La bibliothèque est à jour.',
      mise_a_jour: `Bibliothèque mise à jour : ${r.nb} fiches${r.empreinte_verifiee ? ' (intégrité vérifiée)' : ''}.`,
      hors_ligne: 'Pas de connexion : la bibliothèque actuelle reste disponible.',
      indisponible: 'Aucune version publiée trouvée sur ce site : la bibliothèque actuelle reste disponible.',
      integree: 'Version intégrée à cet aperçu : pas de mise à jour possible ici.',
      echec: `Mise à jour refusée : ${r.raison}.`,
    }[r.statut] || '';
    return;
  }
  if (action === 'copy-url') { copyText($('#share-url').value, 'Adresse copiée !'); return; }
  if (action === 'share-site') { try { await navigator.share({ title: 'Gauchise tes parents', text: 'Des arguments sourcés pour les repas de famille.', url: $('#share-url').value }); } catch { /* annulé */ } return; }
  if (action === 'prev') { w.step = Math.max(1, w.step - 1); persist(); rerenderWizard(); return; }
  if (action === 'retry') { state.retry?.(); return; }
  if (action === 'new') { state.wizard = { ...freshWizard(), mode: w.mode, step: w.mode ? 2 : 1, profil: w.profil, contexte: w.contexte }; persist(); return; }
  if (action === 'copy-speech') { copyText($('#speech-text')?.textContent || '', 'Texte copié !'); return; }

  const r = state.result && parseRoute().path === '/resultat' ? state.result : (state.currentFiche ? ficheToResult(state.currentFiche) : null);
  if (!r) return;
  if (action === 'copy-replique') { copyText($('#replique-text')?.textContent || '', 'Réplique copiée !'); return; }
  if (action === 'copy-refs') { copyText(referencesText(r.dossier), 'Références copiées !'); return; }
  if (action === 'share') {
    const text = shareText(r);
    if (navigator.share) {
      try { await navigator.share({ title: 'Gauchise tes parents', text }); return; } catch (e) { if (e?.name === 'AbortError') return; }
    }
    copyText(text, 'Résumé sourcé copié : colle-le où tu veux !');
    return;
  }
  if (action === 'fresh' && state.request) { launchAnalyse({ ...state.request, fraiche: true }); return; }
  if (action === 'rephrase' && r.analyse_id) {
    const btns = $$('[data-action="rephrase"]');
    btns.forEach((b) => { b.disabled = true; });
    const label = t.textContent;
    t.textContent = 'Reformulation…';
    try {
      const out = await api.reformuler({ analyse_id: r.analyse_id, variante: t.dataset.variante, mode: r.strategie.mode, profil: w.profil, contexte: w.contexte, replique: $('#replique-text').textContent });
      $('#replique-text').textContent = out.replique;
      toast('Nouvelle formulation prête !');
    } catch (e) {
      toast(e.message);
    } finally {
      btns.forEach((b) => { b.disabled = false; });
      t.textContent = label;
    }
  }
});

document.addEventListener('click', (ev) => {
  const b = ev.target.closest('[data-report-source]');
  if (!b) return;
  const id = b.dataset.reportSource;
  const slot = document.getElementById(`report-${id}`);
  if (slot.innerHTML) { slot.innerHTML = ''; return; }
  slot.innerHTML = `<form class="report-source-form" data-source="${h(id)}">
    <label class="field"><span class="field-label">Qu’est-ce qui est incorrect ?</span><textarea name="commentaire" rows="2" maxlength="1000" required></textarea></label>
    <button class="btn btn-secondary btn-small" type="submit">Envoyer le signalement</button><p class="form-msg" role="status"></p></form>`;
  slot.querySelector('textarea').focus();
});

document.addEventListener('toggle', (ev) => {
  const d = ev.target;
  if (d.matches?.('[data-more]')) state[`plus_${d.dataset.more}`] = d.open;
}, true);

document.addEventListener('change', (ev) => {
  if (ev.target.id === 'maj-auto') store.setReglage('majAuto', ev.target.checked);
});

document.addEventListener('submit', async (ev) => {
  const form = ev.target;
  ev.preventDefault();
  const w = state.wizard;
  if (form.id === 'conv-form' && state.compo) {
    envoyerConv($('#conv-msg').value, null);
    return;
  }
  if (form.id === 'veille-run') {
    const msg = form.querySelector('.form-msg');
    msg.textContent = 'Cycle de veille lancé… (cela peut prendre plusieurs minutes)';
    try {
      const r = await api.veilleRun($('#veille-token').value);
      msg.textContent = r.message || 'Cycle terminé.';
      $('#veille-box').innerHTML = veilleHtml(await api.veille());
    } catch (e) { msg.textContent = e.message; }
    return;
  }

  if (form.id === 'wizard-form') {
    const err = validateStep(w);
    if (err) { $('#wizard-error').textContent = err; return; }
    if (w.step < 3) { w.step += 1; persist(); rerenderWizard(); return; }
    if (isLive()) launchAnalyse(wizardPayload(w)); else launchLocal(wizardPayload(w));
    return;
  }
  if (form.id === 'express-form' || form.id === 'express-mini') {
    const e = state.express;
    if (form.id === 'express-mini') e.affirmation = $('#express-mini-text').value;
    if (e.affirmation.trim().length < 5) {
      if (form.id === 'express-mini') { persist(); location.hash = '#/express'; return; }
      $('#express-error').textContent = 'Écris l’affirmation (au moins quelques mots).';
      return;
    }
    persist();
    const pl = { affirmation: e.affirmation.trim(), volet: e.volet, mode: e.mode, profil: profilSimple(w.interlocuteur), contexte: w.contexte, express: true, interlocuteur: nettoyerProfil(w.interlocuteur) };
    if (isLive()) launchAnalyse(pl); else launchLocal(pl);
    return;
  }
  if (form.id === 'library-search') {
    const p = new URLSearchParams();
    const q = $('#lib-q').value.trim();
    const v = $('#lib-volet').value;
    const rb = $('#lib-rubrique').value;
    const fb = $('#lib-fiab').value;
    if (q) p.set('q', q);
    if (v) p.set('volet', v);
    if (rb) p.set('rubrique', rb);
    if (fb) p.set('fiabilite', fb);
    const next = `#/bibliotheque${p.toString() ? `?${p}` : ''}`;
    if (location.hash === next) render(); else location.hash = next;
    return;
  }

  // retours
  const msg = form.querySelector('.form-msg');
  const submit = form.querySelector('button[type="submit"]');
  const r = parseRoute().path === '/resultat' ? state.result : (state.currentFiche ? ficheToResult(state.currentFiche) : null);
  let payload;
  if (form.id === 'feedback-form') {
    const note = form.querySelector('input[name="note"]:checked')?.value;
    if (!note) { msg.textContent = 'Choisis une des trois réponses.'; return; }
    payload = {
      type: 'avis', note, commentaire: form.commentaire.value,
      verdict: r?.dossier?.verdict, volet: r?.volet, mode_debat: r?.strategie?.mode,
      fiche: r?.origine === 'bibliotheque' ? r.fiche_id || state.currentFiche?.id : undefined,
      mode: r?.origine === 'bibliotheque' ? 'bibliotheque' : 'live',
      joindre_affirmation: Boolean(form.joindre?.checked), affirmation: r?.affirmation,
    };
  } else if (form.classList.contains('report-source-form')) {
    const src = r?.dossier?.sources.find((s) => s.id === form.dataset.source);
    payload = { type: 'source_incorrecte', commentaire: form.commentaire.value, url: src?.url, verdict: r?.dossier?.verdict, fiche: r?.origine === 'bibliotheque' ? r.fiche_id : undefined };
  } else if (form.id === 'report-form') {
    if (!form.commentaire.value.trim()) { msg.textContent = 'Décris le problème en quelques mots.'; return; }
    payload = { type: 'erreur_fiche', commentaire: form.commentaire.value, url: form.url.value || undefined };
  } else {
    return;
  }
  submit.disabled = true;
  try {
    const out = await api.feedback(payload);
    msg.textContent = out.message;
    form.querySelectorAll('input, textarea, button').forEach((el) => { el.disabled = true; });
  } catch (e) {
    msg.textContent = e.message;
    submit.disabled = false;
  }
});

// Onglets de fiche : navigation au clavier (flèches, Début, Fin).
document.addEventListener('keydown', (ev) => {
  const t = ev.target.closest?.('.fiche-tab');
  if (!t) return;
  const i = TAB_IDS.indexOf(t.dataset.tab);
  const next = { ArrowRight: i + 1, ArrowLeft: i - 1, Home: 0, End: TAB_IDS.length - 1 }[ev.key];
  if (next === undefined) return;
  ev.preventDefault();
  selectFicheTab(TAB_IDS[(next + TAB_IDS.length) % TAB_IDS.length], { focus: true });
});

// ---------------------------------------------------------------- démarrage
async function init() {
  $('[data-logo]').innerHTML = LOGO_SVG.replace('<svg ', '<svg aria-hidden="true" focusable="false" ');
  $('#footer-support').innerHTML = supportCard('main', '-footer');
  // Hors-ligne : le service worker garde l'interface et la base (indisponible en fichier local ou en aperçu).
  if ('serviceWorker' in navigator && /^https?:$/.test(location.protocol) && !api.isStatic) {
    navigator.serviceWorker.register('sw.js').catch(() => { /* navigateur sans service worker : l'application marche en ligne */ });
  }
  await kb.load().catch(() => { /* la page « Mode » explique comment charger la base */ });
  // Le serveur n'est interrogé qu'en mode connecté : en mode autonome, aucune requête réseau n'est nécessaire.
  state.status = appMode() === 'connecte' ? await api.status() : null;
  updateModePill();
  window.addEventListener('hashchange', render);
  await render();
  if (store.reglages().majAuto && navigator.onLine !== false) {
    kb.checkUpdate().then((r) => { if (r.statut === 'mise_a_jour') toast(`Bibliothèque mise à jour : ${r.nb} fiches.`); }).catch(() => {});
  }
}
init();
