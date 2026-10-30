// Moteur d'analyse argumentative (mode autonome, règles explicites, sans modèle d'IA).
//
// Couches : 1. normalisation → 2. concepts et mots-clés → 3. découpage en arguments (une phrase peut en
// contenir plusieurs) → 4. relations de cause affirmées → 5. émotions → 6. procédés argumentatifs →
// 7. sélection documentaire STRICTE (une fiche doit couvrir l'argument ; sinon on reconnaît la lacune)
// → 8. formulation marquante et question → 9. éléments à vérifier.
//
// Garde-fous : aucune donnée n'est créée ; les fiches voisines sont écartées avec leur raison ;
// les émotions et procédés sont des lectures possibles, pas des diagnostics.
// NB : noms préfixés an… / AN_ (l'aperçu concatène les modules).
import { CA_CONCEPTS, CA_ARGUMENTS, CA_EMOTIONS, CA_PROCEDES, CA_PHRASES } from './cartographie.js';
import { kbNormalize, kbScore, kbMatch } from './kbsearch.js';
import { atteintesDignite } from './ligne-editoriale.js';

const anNorm = (t) => ` ${kbNormalize(t).replace(/[^a-z0-9%!? ]+/g, ' ').replace(/\s+/g, ' ').trim()} `;
const anRe = (motifs, flags = 'g') => new RegExp(`(?:^|\\s)(${motifs.join('|')})(?=\\s|$|[!?])`, flags);
const AN_CONCEPT_RE = Object.fromEntries(Object.entries(CA_CONCEPTS).map(([id, c]) => [id, anRe(c.motifs)]));
const AN_EMO_RE = Object.fromEntries(Object.entries(CA_EMOTIONS).map(([id, c]) => [id, new RegExp(c.motifs.join('|'))]));
const AN_PROC_RE = Object.fromEntries(Object.entries(CA_PROCEDES).filter(([, c]) => c.motifs.length).map(([id, c]) => [id, new RegExp(c.motifs.join('|'))]));
const anHash = (s) => { let x = 0; for (const ch of s) x = (x * 31 + ch.charCodeAt(0)) >>> 0; return x; };

/** Concepts présents dans un texte normalisé, avec les mots qui les ont déclenchés. */
export const AN_SUJETS_PORTEURS = ['immigration', 'melenchon_lfi', 'gauche'];
export function anConcepts(norm) {
  const out = [];
  for (const [id, re] of Object.entries(AN_CONCEPT_RE)) {
    re.lastIndex = 0;
    const mots = [...norm.matchAll(re)].map((m) => m[1]);
    if (mots.length) out.push({ id, label: CA_CONCEPTS[id].label, central: CA_CONCEPTS[id].central, mots: [...new Set(mots)] });
  }
  return out;
}

/** Concepts d'une fiche (métadonnées enregistrées, sinon calculées sur son affirmation et ses mots-clés). */
const anCache = new Map();
export function conceptsFiche(f) {
  if (Array.isArray(f.concepts) && f.concepts.length) return f.concepts;
  if (!anCache.has(f.id)) anCache.set(f.id, anConcepts(anNorm(`${f.affirmation} ${(f.mots_cles || []).join(' ')} ${f.sous_theme || ''}`)).map((c) => c.id));
  return anCache.get(f.id);
}

// Découpage : connecteurs qui introduisent souvent un second argument.
const AN_SEP = /\s*(?:;|\.\s+|!\s+|\?\s+|,?\s+et en plus\s+|,?\s+en plus(?:,)?\s+|,?\s+et puis\s+|,?\s+mais\s+|,?\s+pendant ce temps,?\s+|,?\s+alors que\s+|,?\s+et quand\s+|,?\s+et(?=\s+(?:on|ils|elles|il|en plus|quand|les|leurs?)\b)\s+|,\s+(?=(?:on|ils?|elles?|et|les)\b))\s*/i;
export function anSegments(texte) {
  return String(texte || '').split(AN_SEP).map((s) => s.trim()).filter((s) => s.split(/\s+/).length >= 2);
}

function anArgumentsSegment(norm, concepts, contexte, phraseIds = new Set()) {
  const ids = new Set([...concepts.map((c) => c.id), ...contexte]);
  const propres = new Set(concepts.map((c) => c.id));
  const cand = [];
  for (const a of CA_ARGUMENTS) {
    if (!a.tous.every((c) => ids.has(c))) continue;
    // au moins un concept propre au segment (le contexte seul ne suffit que si le segment dit quelque chose)
    if (!a.tous.some((c) => propres.has(c)) && !(contexte.length && propres.size)) continue;
    if ((a.aucun || []).some((c) => ids.has(c))) continue;
    if ((a.aucunPhrase || []).some((c) => ids.has(c) || phraseIds.has(c))) continue;
    const signaux = (a.signaux || []).filter((s) => new RegExp(s).test(norm)).length;
    if (a.requiertSignal && !signaux) continue;
    if ((a.requiertSignalAvec || []).some((c) => ids.has(c)) && !signaux) continue;
    cand.push({ a, score: a.tous.length * 10 + signaux * 3 - CA_ARGUMENTS.indexOf(a) * 0.01 });
  }
  cand.sort((x, y) => y.score - x.score);
  // on écarte un argument dont les concepts sont inclus dans ceux d'un argument plus spécifique déjà retenu
  const retenus = [];
  for (const c of cand) {
    const t = new Set(c.a.tous);
    const couvert = retenus.some((r) => c.a.tous.every((x) => r.a.tous.includes(x)) && (r.a.tous.length > c.a.tous.length || [...t].every((x) => r.a.tous.includes(x))));
    if (!couvert) retenus.push(c);
  }
  return retenus.map((r) => r.a);
}

function anChoisirFiche(arg, segNorm, segTexte, lib, phraseNorm = segNorm) {
  const dispo = arg.fiches.map((id) => lib.find((f) => f.id === id)).filter(Boolean);
  if (!dispo.length) return null;
  // départage par formulation : d'abord dans la proposition, puis dans toute la phrase
  if (arg.choisir) for (const n of [segNorm, phraseNorm]) for (const [id, re] of Object.entries(arg.choisir)) if (new RegExp(re).test(n)) { const f = dispo.find((x) => x.id === id); if (f) return { f }; }
  // sinon : la plus proche du texte parmi les fiches de l'argument (ordre éditorial à égalité)
  // sinon : la plus proche du texte si la ressemblance est nette, à défaut la première dans l'ordre éditorial
  const best = dispo.map((f, i) => ({ f, s: kbScore(f, segTexte).score - i * 0.5 })).sort((a, b) => b.s - a.s)[0];
  if (best.s >= (arg.choisir ? 6 : 3)) return { f: best.f };
  return { f: dispo[0], indecis: Boolean(arg.choisir && dispo.length > 2) };
}

function anRaisonExclusion(f, arg, lib) {
  const cf = conceptsFiche(f);
  const manque = arg.tous.filter((c) => !cf.includes(c)).map((c) => CA_CONCEPTS[c].label.toLowerCase());
  const traite = cf.filter((c) => CA_CONCEPTS[c]?.central && !arg.tous.includes(c)).map((c) => CA_CONCEPTS[c].label.toLowerCase());
  return manque.length
    ? `elle traite ${traite.length ? `de : ${traite.slice(0, 2).join(', ')}` : 'd’un autre sujet'}, pas de : ${manque.join(', ')}`
    : 'elle ne répond qu’à un aspect secondaire de la question';
}

function anCausalites(norm, concepts) {
  const out = [];
  const lab = (ids) => ids.map((c) => CA_CONCEPTS[c].label).join(', ');
  const centraux = (t) => anConcepts(t).filter((c) => c.central).map((c) => c.id);
  let m = norm.match(/^(.*)\sa cause (?:de |d |des |du )(.*)$/);
  if (m) { const effet = centraux(` ${m[1]} `); const cause = centraux(` ${m[2]} `); if (cause.length) out.push({ cause: lab(cause), effet: lab(effet.filter((c) => !cause.includes(c))) || 'la situation décrite', forme: '« à cause de »' }); }
  m = norm.match(/plus (?:il y a )?(.{3,60}?)\s(?:moins|plus) (?:il y a )?(.{3,60})/);
  if (m) { const cause = centraux(` ${m[1]} `); const effet = centraux(` ${m[2]} `); if (cause.length && effet.length) out.push({ cause: lab(cause), effet: lab(effet), forme: '« plus… moins »' }); }
  m = norm.match(/^(.*)\s(?:cree(?:nt)?|provoque(?:nt)?|diminue(?:nt)?|augmente(?:nt)?|fait baisser|font baisser|detruit|detruisent)\s(.*)$/);
  if (m && !out.length) { const cause = centraux(` ${m[1]} `); const effet = centraux(` ${m[2]} `); if (cause.length && effet.length) out.push({ cause: lab(cause), effet: lab(effet), forme: 'verbe de cause' }); }
  if (!out.length && /\s(arrivent encore|pendant ce temps|et en plus)\s/.test(norm)) {
    const ids = concepts.filter((c) => c.central).map((c) => c.id);
    if (ids.includes('immigration') && ids.length > 1) out.push({ cause: 'Immigration', effet: lab(ids.filter((c) => c !== 'immigration')), forme: 'juxtaposition (lien suggéré, pas affirmé)', implicite: true });
  }
  return out;
}

function anProcedes(norm, concepts, args) {
  const ids = concepts.map((c) => c.id);
  const out = [];
  for (const [id, re] of Object.entries(AN_PROC_RE)) {
    if (!re.test(norm)) continue;
    if (id === 'causalite' && concepts.filter((c) => c.central).length < 2) continue;
    if (id === 'generalisation' && /\s(certains|quelques|une partie|des fois|parfois|beaucoup d|la plupart)\s/.test(norm)) continue;
    out.push(id);
  }
  if (/\simm?igr/.test(norm) && /\setran[gj]/.test(norm)) out.push('amalgame');
  else if (ids.includes('immigration') && (ids.includes('delinquance') || ids.includes('prison')) && out.includes('generalisation')) out.push('amalgame');
  else if (ids.includes('islam') && /\sislamis|terror/.test(norm) && /\smusulman|islam\s/.test(norm)) out.push('amalgame');
  if (ids.includes('origine') && (ids.includes('prestations') || ids.includes('delinquance') || ids.includes('emploi'))) out.push('amalgame');
  if (ids.includes('melenchon_lfi') && ids.includes('dangerosite')) out.push('personnalisation');
  if (ids.includes('penurie') && /\schom/.test(norm)) out.push('contradiction');
  return [...new Set(out)].map((id) => ({ id, ...CA_PROCEDES[id] }));
}

/**
 * Analyse complète d'une phrase. options : { bibliotheque, mode ('gagner'|'convaincre') }.
 * Renvoie une structure lisible par l'interface et par les tests.
 */
export function analyserPhrase(texte, { bibliotheque = [], mode = 'gagner', contexte: contexteExterne = [] } = {}) {
  const lib = bibliotheque.filter((f) => f.type !== 'science');
  const norm = anNorm(texte);
  const concepts = anConcepts(norm);
  const segs = anSegments(texte);
  const unites = segs.length > 1 ? segs : [String(texte || '')];
  // contexte de phrase : l'immigration évoquée dans une partie vaut pour les pronoms des autres parties
  // (sujets « porteurs » : immigration, Mélenchon/LFI, la gauche)
  const AN_SUJETS = ['immigration', 'melenchon_lfi', 'gauche'];
  const contexte = concepts.filter((c) => AN_SUJETS.includes(c.id)).map((c) => c.id);
  // une origine supposée (« arabe », « africain »…) est souvent employée pour parler d'immigration : on le note, sans l'affirmer
  const origineSeule = concepts.some((c) => c.id === 'origine') && !contexte.includes('immigration');
  if (origineSeule) contexte.push('immigration');
  // « …Pendant ce temps, les immigrés arrivent encore » : le lien est suggéré pour toute la phrase
  const juxtapose = contexte.includes('immigration') && /\s(arrivent encore|pendant ce temps|on continue a faire venir|continuent d arriver|on fait venir)\s/.test(norm);
  const phraseIds = new Set(concepts.map((c) => c.id));
  const args = [];
  const ajouter = (a, n, u) => {
    const ch = anChoisirFiche(a, n, u, lib, norm);
    const fiche = ch?.f || null;
    if (args.some((x) => x.id === a.id && (x.fiche?.id || null) === (fiche?.id || null))) return;
    if (fiche && args.some((x) => x.fiche?.id === fiche.id)) return;
    {
      args.push({
        id: a.id, label: a.label, famille: a.famille, segment: u,
        concepts: a.tous.map((c) => CA_CONCEPTS[c].label),
        fiche: fiche ? { id: fiche.id, affirmation: fiche.affirmation, court: fiche.argumentaires?.court || '', volet: fiche.volet } : null,
        pertinence: fiche ? (a.partielle || ch.indecis ? 'partielle' : 'directe') : 'aucune',
        lacune: !fiche,
        implicite: a.implicite || '', verifier: a.verifier || '',
        _arg: a,
      });
    }
  };
  for (const u of unites) {
    const n = anNorm(u);
    const cs = anConcepts(n);
    const pronom = /\s(ils?|eux|elles?|leur|leurs|lui)\s/.test(n) || /\s(les|leur|l)\s+\w+(ent|ont)\s/.test(n);
    const ctx = [...(juxtapose || unites.length === 1 || pronom ? contexte : []), ...(pronom ? contexteExterne.filter((c) => !contexte.includes(c)) : [])];
    for (const a of anArgumentsSegment(n, cs, ctx, phraseIds)) ajouter(a, n, u);
  }
  // concepts répartis sur plusieurs propositions (« On n’a plus de travail mais on fait venir des étrangers »)
  if (unites.length > 1) {
    const parSeg = unites.map((u) => new Set(anConcepts(anNorm(u)).map((c) => c.id)));
    for (const a of anArgumentsSegment(norm, concepts, origineSeule ? ['immigration'] : [], phraseIds)) {
      if (args.some((x) => x.id === a.id)) continue;
      const etale = a.tous.length >= 2 && !parSeg.some((cs) => a.tous.every((c) => cs.has(c)));
      if (!args.length || juxtapose || etale) {
        // l'argument qui relie les propositions remplace ceux qui n'en couvraient qu'une partie
        for (let i = args.length - 1; i >= 0; i--) if (args[i]._arg && args[i]._arg.tous.length < a.tous.length && args[i]._arg.tous.every((c) => a.tous.includes(c))) args.splice(i, 1);
        const avant = args.length;
        ajouter(a, norm, texte);
        if (etale && args.length > avant) args.unshift(args.pop());
      }
    }
  }
  // repli : aucun argument cartographié → correspondance textuelle, mais seulement si la fiche couvre les concepts centraux
  if (!args.length && norm.trim().length > 6) {
    const centraux = concepts.filter((c) => c.central).map((c) => c.id);
    const m = kbMatch(lib, texte)[0];
    const couvre = m && centraux.every((c) => conceptsFiche(m.fiche).includes(c));
    if (m && m.force === 'forte' && (couvre || !centraux.length)) {
      args.push({ id: 'texte', label: 'Correspondance avec une fiche', famille: m.fiche.volet, segment: texte, concepts: centraux.map((c) => CA_CONCEPTS[c].label), fiche: { id: m.fiche.id, affirmation: m.fiche.affirmation, court: m.fiche.argumentaires?.court || '', volet: m.fiche.volet }, pertinence: 'directe', lacune: false, implicite: '', verifier: '' });
    } else if (centraux.length) {
      args.push({ id: 'non_cartographie', label: `Argument sur : ${centraux.map((c) => CA_CONCEPTS[c].label.toLowerCase()).join(', ')}`, famille: '', segment: texte, concepts: centraux.map((c) => CA_CONCEPTS[c].label), fiche: null, pertinence: 'aucune', lacune: true, implicite: '', verifier: 'Les données disponibles sur ce point précis.' });
    }
  }
  // fiches voisines écartées (ce qu'une simple ressemblance de mots aurait choisi)
  const ecartees = [];
  const retenues = new Set(args.map((a) => a.fiche?.id).filter(Boolean));
  const voisine = kbMatch(lib, texte)[0];
  const principal = args[0] || null;
  if (principal?._arg) {
    const ex = new Set([...(principal._arg.exclues || []), ...(voisine && !retenues.has(voisine.fiche.id) ? [voisine.fiche.id] : [])]);
    for (const id of ex) {
      const f = lib.find((x) => x.id === id);
      if (!f || retenues.has(id)) continue;
      ecartees.push({ id, affirmation: f.affirmation, raison: anRaisonExclusion(f, principal._arg, lib) });
    }
  }
  const emotions = Object.entries(AN_EMO_RE).filter(([, re]) => re.test(norm)).map(([id]) => ({ id, label: CA_EMOTIONS[id].label, reponse: CA_EMOTIONS[id].reponse }));
  const causalites = anCausalites(norm, concepts);
  const procedes = anProcedes(norm, concepts, args);
  const phraseGenerique = !CA_PHRASES[principal?.id];
  const banque = CA_PHRASES[principal?.id] || CA_PHRASES.generique;
  const choix = banque[mode] || banque.gagner;
  const phrase = choix[anHash(norm) % choix.length];
  const ficheP = principal?.fiche ? lib.find((f) => f.id === principal.fiche.id) : null;
  const question = procedes[0]?.question || ficheP?.questions?.[0] || (CA_PHRASES.generique.convaincre[0]);
  const aVerifier = [...new Set([...args.map((a) => a.verifier), ...procedes.map((p) => p.verifier)].filter(Boolean))];
  for (const a of args) delete a._arg;
  return {
    texte: String(texte || ''), mode,
    concepts: concepts.map(({ id, label, mots, central }) => ({ id, label, mots, central })),
    arguments: args, principal: args[0] || null, secondaires: args.slice(1),
    causalites, implicites: [...new Set(args.map((a) => a.implicite).filter(Boolean))], aVerifier,
    emotions, procedes: procedes.map(({ id, label, explication, verifier, question: q }) => ({ id, label, explication, verifier, question: q })),
    ecartees, phrase, phraseGenerique, question,
    dignite: atteintesDignite(texte),
    lacune: !args.length || Boolean(args[0]?.lacune),
  };
}
