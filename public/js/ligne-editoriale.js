// Ligne éditoriale et politique documentaire de « Gauchise tes parents » (v10).
//
// L'application assume des VALEURS de gauche (humanistes, universalistes, sociales, démocratiques, antifascistes)
// et une exigence ABSOLUE de vérité sur les FAITS. Ce module est la source unique de ces règles :
//  - le moteur hors ligne l'utilise (lecture de gauche, garde-fou de dignité, audit des sources des fiches) ;
//  - le serveur l'injecte dans les consignes du mode connecté (recherche, stratégie, conversation, discours).
// NB : noms préfixés LE_ / le… (l'aperçu concatène les modules).

// ─── 1. Principes défendus ────────────────────────────────────────────────
export const LE_PRINCIPES = {
  egalite: { label: 'Égalité réelle', texte: 'Les êtres humains naissent et demeurent libres et égaux en droits : l’égalité doit exister dans les faits, pas seulement dans les textes.' },
  universalite: { label: 'Universalité des droits', texte: 'Les droits fondamentaux valent pour chaque personne, quelle que soit son origine, sa nationalité, sa religion ou sa condition.' },
  solidarite: { label: 'Solidarité et justice sociale', texte: 'Une société se juge à la façon dont elle protège celles et ceux qui ont le moins.' },
  dignite: { label: 'Dignité humaine', texte: 'Aucune personne, aucun groupe ne peut être traité comme moins humain qu’un autre.' },
  antiracisme: { label: 'Antiracisme', texte: 'On juge des actes et des politiques, jamais une population entière pour son origine supposée.' },
  antifascisme: { label: 'Antifascisme', texte: 'Désigner un ennemi intérieur et suspendre les droits de certains au nom de la nation : l’histoire a montré où cela mène.' },
  libertes: { label: 'Libertés publiques', texte: 'Liberté d’expression, de conscience, de manifester et droit à un procès équitable protègent tout le monde, y compris ses adversaires.' },
  services_publics: { label: 'Services publics', texte: 'L’école, l’hôpital, la Sécurité sociale sont le patrimoine de celles et ceux qui n’en ont pas.' },
  emancipation: { label: 'Émancipation', texte: 'Donner à chacun les moyens de choisir sa vie, individuellement et collectivement.' },
  democratie: { label: 'Démocratie et souveraineté populaire', texte: 'Le pouvoir appartient au peuple, c’est-à-dire à l’ensemble des citoyennes et des citoyens, sans tri.' },
  internationalisme: { label: 'Internationalisme', texte: 'La coopération entre les peuples plutôt que leur mise en concurrence.' },
  egalite_fh: { label: 'Égalité femmes-hommes', texte: 'L’égalité entre les femmes et les hommes n’est pas acquise tant que les écarts persistent.' },
  discriminations: { label: 'Lutte contre les discriminations', texte: 'Une discrimination prouvée est une injustice et un délit, pas une impression.' },
  travailleurs: { label: 'Protection des travailleurs', texte: 'Protéger tous les travailleurs, français et étrangers, plutôt que les opposer.' },
  repartition: { label: 'Répartition des richesses', texte: 'La richesse est produite collectivement ; sa répartition est un choix politique.' },
  vulnerables: { label: 'Protection des personnes vulnérables', texte: 'Les plus fragiles ne sont pas un coût, ce sont des personnes.' },
  paix: { label: 'Paix et droit international', texte: 'Le droit international et la protection des civils s’appliquent partout, sans double standard.' },
};

// ─── 2. Règles de vérité (non négociables) ─────────────────────────────────
export const LE_REGLES_VERITE = [
  'Ne jamais inventer une statistique, une étude, une citation, une référence ou une décision de justice.',
  'Ne jamais déformer une citation ni cacher un résultat scientifique contradictoire.',
  'Ne jamais sélectionner uniquement les chiffres favorables à la gauche.',
  'Ne jamais présenter une hypothèse comme un fait établi.',
  'Ne jamais utiliser une source militante (de gauche comme de droite) comme unique preuve d’une affirmation statistique.',
  'Signaler les limites méthodologiques des données utilisées.',
  'Distinguer les faits, les interprétations, les valeurs et les propositions politiques.',
  'Quand une étude contredit un argument traditionnellement défendu à gauche, le dire, puis expliquer comment l’intégrer honnêtement.',
];

// ─── 3. Dignité humaine : ce qui n'est pas « une opinion comme une autre » ──
// Distinction centrale : critiquer une POLITIQUE (immigration, justice, religion comme doctrine) est légitime ;
// viser une POPULATION entière, la déshumaniser ou appeler à la violence ne l'est pas.
export const LE_DIGNITE = [
  { id: 'deshumanisation', label: 'Déshumanisation', motifs: ['vermines?', 'cafards', 'parasites', 'sous ?hommes?', '(sont|comme) des (animaux|betes|sauvages|microbes|virus|rats|nuisibles|singes|chiens)', 'invasion de (rats|sauterelles|cafards)', 'race (inferieure|superieure)', 'races inferieures'],
    texte: 'Comparer des êtres humains à des animaux ou à des nuisibles, c’est le premier pas de toutes les persécutions : c’est ainsi qu’on prépare les esprits à accepter le pire.' },
  { id: 'violence', label: 'Appel à la violence ou à la mort', motifs: ['(les|faut les|on devrait les|qu on les) (tuer|noyer|bruler|fusiller|exterminer|eliminer|gazer|pendre)', 'qu ils (crevent|meurent|se noient)', 'laisse(r|z)? (les )?(mourir|couler|se noyer)', 'couler (les|leurs) bateaux', 'tirer sur (les|eux)', 'une balle', 'mitrailler', 'ratonnade'],
    texte: 'Souhaiter ou réclamer la mort de personnes, quelles qu’elles soient, n’est pas un argument : c’est une négation pure et simple de la valeur de la vie humaine, et, dans certains cas, un délit.' },
  { id: 'exclusion_collective', label: 'Punition ou exclusion d’une population entière', motifs: ['tous les (arabes|noirs|musulmans|juifs|roms|africains|immigres|etrangers) (dehors|a la mer|en prison|chez eux)', 'virer tous les (arabes|noirs|musulmans|juifs|roms|africains)', 'pas de (arabes|noirs|musulmans|juifs|roms) (chez nous|en france|ici)', 'remigration', 'deporter', 'deportation'],
    texte: 'Punir ou expulser des personnes pour ce qu’elles sont, et non pour ce qu’elles ont fait, c’est la définition même de la discrimination collective. Le droit français et le droit international l’interdisent.' },
  { id: 'antisemitisme', label: 'Antisémitisme', motifs: ['les juifs (controlent|dirigent|possedent|ont tout|tiennent)', 'complot juif', 'lobby juif', 'les juifs et l argent', 'sionistes? (controlent|dirigent)', 'juifs? (dehors|a la porte)'],
    texte: 'Attribuer aux Juifs un pouvoir occulte, l’argent ou une double allégeance, ce sont les vieux mythes qui ont nourri les persécutions jusqu’à la Shoah. L’antisémitisme se combat partout, y compris quand il se cache derrière la critique d’un État.' },
];

const leNorm = (t) => ` ${String(t || '').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/['’`]/g, ' ').replace(/[^a-z0-9 ]+/g, ' ').replace(/\s+/g, ' ').trim()} `;
const LE_DIGNITE_RE = LE_DIGNITE.map((d) => ({ ...d, re: new RegExp(`(?:^|\\s)(${d.motifs.join('|')})(?=\\s|$)`) }));

/** Atteintes à la dignité repérées dans une phrase (lecture prudente : ce sont les mots, pas une intention prouvée). */
export function atteintesDignite(texte) {
  const n = leNorm(texte);
  return LE_DIGNITE_RE.filter((d) => d.re.test(n)).map(({ id, label, texte: t }) => ({ id, label, texte: t }));
}

// ─── 4. Politique documentaire ──────────────────────────────────────────────
// Classes de sources et rôle documentaire :
//  - autorite   : peut établir un fait à elle seule (statistique publique, recherche, institutions, archives) ;
//  - complement : éclaire, résume, contextualise (presse de référence, associations, vulgarisation) ;
//  - origine    : sert à comprendre ce qui a été dit (sources partisanes, médias et think tanks de droite) —
//                 jamais l'autorité qui valide un fait, sauf comme aveu explicite (« selon X, pourtant opposé… »).
export const LE_CLASSES = {
  recherche: { label: 'Recherche et statistique publiques', role: 'autorite', motifs: ['insee', 'drees', 'dares', 'ined', 'cnrs', 'cepii', 'ofce', 'irdes', 'france strategie', 'ssmsi', 'sdes', 'universit', 'school of economics', 'sciences po', 'european university institute', 'eui', 'banque de france', 'french cultural studies', 'politoscope', 'ipp', 'cevipof', 'ehess', 'college de france', 'harvard university press', 'cesdip', 'oscj', 'apur', 'atelier parisien d urbanisme', 'inrae'] },
  institution: { label: 'Institutions et organismes publics', role: 'autorite', motifs: ['assemblee nationale', '(?<!public )senat', 'legifrance', 'conseil constitutionnel', 'conseil d etat', 'defenseur des droits', 'cour des comptes', 'ministere', 'service public', 'vie publique', 'cncdh', 'conseil de l europe', 'cedh', 'cour europeenne', 'nations unies', 'onu', 'oim', 'unhcr', 'hcr', 'oit', 'ocde', 'eurostat', 'commission europeenne', 'france travail', 'rte', 'direction generale', 'haut commissariat', 'gouv fr', 'sgdsn', 'viginum', 'cnsa', 'site public', 'conseil d orientation des retraites', 'commission des sondages'] },
  histoire: { label: 'Archives et institutions historiques', role: 'autorite', motifs: ['memorial de la shoah', 'fondation pour la memoire', 'archives', 'service historique', 'chemins de memoire', 'musee', 'quotidien des parisiens', 'ville de paris', 'cvce', 'bibliotheque nationale', 'gallica'] },
  presse_reference: { label: 'Presse de référence et vérification des faits', role: 'complement', motifs: ['le monde', 'liberation', 'mediapart', 'l humanite', 'franceinfo', 'france culture', 'radio france', 'afp', 'alternatives economiques', 'arret sur images', 'public senat', 'lcp', 'the conversation', 'aoc', 'les decodeurs', 'checknews', 'ina', 'europenow', 'slate', 'banque des territoires', 'localtis', 'caisse des depots'] },
  association: { label: 'Associations et observatoires', role: 'complement', motifs: ['observatoire des inegalites', 'ligue des droits', 'ldh', 'sos racisme', 'amnesty', 'human rights watch', 'cimade', 'fondation abbe pierre', 'secours', 'acrimed', 'observatoire'] },
  vulgarisation: { label: 'Vulgarisation, presse généraliste et spécialisée', role: 'complement', motifs: ['herodote', 'actu juridique', 'club des juristes', 'finance pour tous', 'weblex', 'connaissance des energies', 'the local', 'toutsurmesfinances', 'avocats', 'l avenir', 'nathan', 'larousse', 'pressenza', 'monde diplomatique', 'berkley center'] },
  tertiaire: { label: 'Encyclopédies', role: 'complement', motifs: ['wikipedia'] },
  droite: { label: 'Médias et think tanks de droite (origine d’une affirmation)', role: 'origine', motifs: ['ifrap', 'institut montaigne', 'europe 1', 'cnews', 'valeurs actuelles', 'le figaro', 'figaro', 'jdd', 'journal du dimanche', 'causeur', 'boulevard voltaire', 'frontieres', 'fdesouche', 'observatoire juif de france', 'contribuables associes', 'institut thomas more', 'observatoire de l immigration et de la demographie'] },
  partisane: { label: 'Sources partisanes (origine d’une affirmation)', role: 'origine', motifs: ['source partisane', 'melenchon fr', 'la france insoumise', 'union populaire', 'revue du pcf', 'rassemblement national', 'reconquete'] },
};
const LE_ORDRE_CLASSES = ['partisane', 'droite', 'tertiaire', 'histoire', 'recherche', 'institution', 'presse_reference', 'association', 'vulgarisation'];
const LE_CLASSES_RE = Object.fromEntries(Object.entries(LE_CLASSES).map(([id, c]) => [id, new RegExp(`(?:^|\\s)(?:${c.motifs.join('|')})`)]));

/** Classe documentaire d'une source (organisme, titre et domaine de l'URL). */
export function classerSource(src = {}) {
  const host = (() => { try { return new URL(src.url).hostname.replace(/^www\./, ''); } catch { return ''; } })();
  // organisme + domaine seulement : le titre peut citer un média sans en provenir
  const t = leNorm(`${src.organisme || ''} ${host.replace(/\./g, ' ')}`);
  for (const id of LE_ORDRE_CLASSES) if (LE_CLASSES_RE[id].test(t)) return id;
  if (/gouv fr|europa eu|un org/.test(t)) return 'institution';
  return 'vulgarisation';
}
export const roleSource = (src) => LE_CLASSES[classerSource(src)].role;

// Un fait attribué (« selon X », « X estime ») n'est pas présenté comme établi par cette source.
const LE_ATTRIBUTION = /(^|[\s«(])(selon|d['’]apr[eè]s|estim\w*|affirm\w*|d[ée]clar\w*|d[ée]non[cç]\w*|calcul\w*|chiffr\w*|jug\w*|parle de|pourtant|qualifi\w*|dit|disent|propos\w*|tribune|programme|[ée]crit|[ée]crivent|rapport[ée]?|relay\w*)(?=[\s,:;.»)]|$)/i;

/**
 * Audit documentaire d'une fiche. Renvoie la liste des problèmes (vide = conforme) :
 *  - un fait « établi » ne peut reposer que sur une source d'autorité (ou de presse de référence qui rapporte une donnée) ;
 *  - une source d'origine (partisane, de droite) ne valide un fait que s'il est explicitement attribué ;
 *  - une encyclopédie ne peut pas être la seule source d'un fait ;
 *  - un chiffre ne repose jamais sur une source militante seule sans attribution.
 */
export function auditFiche(f) {
  const pb = [];
  (f.faits || []).forEach((x, i) => {
    const s = f.sources?.[x.source];
    if (!s) { pb.push(`fait ${i} : source manquante`); return; }
    const c = classerSource(s); const role = LE_CLASSES[c].role;
    const attribue = LE_ATTRIBUTION.test(x.fait);
    if (role === 'origine' && !attribue) pb.push(`fait ${i} : repose sur une source d’origine (${LE_CLASSES[c].label}) sans être attribué`);
    if (c === 'tertiaire') pb.push(`fait ${i} : repose seulement sur une encyclopédie`);
    if (x.chiffre && ['association', 'partisane'].includes(c) && !attribue) pb.push(`fait ${i} : chiffre appuyé sur une source militante sans attribution`);
    if ((x.fiabilite || f.fiabilite) === 'etabli' && role !== 'autorite' && c !== 'presse_reference' && !attribue) pb.push(`fait ${i} : présenté comme établi sans source d’autorité (${LE_CLASSES[c].label})`);
  });
  if ((f.faits || []).length && !(f.faits || []).some((x) => f.sources?.[x.source] && ['autorite'].includes(roleSource(f.sources[x.source])) || ['presse_reference'].includes(classerSource(f.sources?.[x.source] || {})))) pb.push('aucune source d’autorité ni de presse de référence');
  return pb;
}

// ─── 5. Signature éditoriale (consignes du mode connecté) ───────────────────
export const LE_SOURCES_PRIORITAIRES = [
  'Statistiques et recherche publiques : INSEE, CNRS, INED, DREES, DARES, SSMSI, France Stratégie, OFCE, CEPII, IRDES, universités et laboratoires, publications évaluées par les pairs',
  'Institutions : Assemblée nationale, Sénat, Légifrance, Conseil constitutionnel, Conseil d’État, Défenseur des droits, Cour des comptes, ministères, CNCDH, institutions européennes, ONU, Conseil de l’Europe, OIT, Haut-Commissariat aux droits de l’homme, OIM, HCR',
  'Histoire et mémoire : Fondation pour la mémoire de la Shoah, Mémorial de la Shoah, Archives nationales et publiques, musées, travaux universitaires sur le fascisme, le nazisme, Vichy et les nationalismes',
  'Associations spécialisées (complément, jamais preuve statistique unique) : Ligue des droits de l’Homme, SOS Racisme, Amnesty International, Human Rights Watch, observatoires indépendants',
  'Presse (analyse et contexte) : Le Monde, Libération, Mediapart, L’Humanité, Franceinfo, France Culture, AFP, Alternatives économiques, Arrêt sur images, médias de vérification des faits — chaque article jugé sur sa méthode, pas sur son camp',
];

export const LE_SIGNATURE = `Ligne éditoriale : « Gauchise tes parents » est une application d'éducation populaire et d'argumentation de gauche, assumée : humaniste, universaliste, sociale, égalitaire, démocratique et antifasciste. Elle ne prétend pas être neutre sur les VALEURS ; elle est irréprochable sur les FAITS.
Valeurs défendues : ${Object.values(LE_PRINCIPES).map((p) => p.label.toLowerCase()).join(', ')}.
Ton : de gauche, pédagogique, assumé, direct, argumenté, parfois incisif ; jamais d'insulte, de caricature ou d'invention. Défends une position tranchée en expliquant pourquoi.
Pas de faux équilibre : face à la déshumanisation, au racisme, à l'antisémitisme, à la xénophobie, aux appels à la violence ou à la négation de droits fondamentaux, dis clairement pourquoi c'est incompatible avec la dignité humaine et l'universalité des droits. Distingue toujours la critique légitime d'une politique publique et l'attaque contre une population entière.
Ne confonds pas patriotisme, souveraineté nationale, nationalisme et xénophobie. L'amour du pays n'appartient à personne : la Résistance, le CNR, la Sécurité sociale, les services publics, l'égalité devant la loi en sont l'héritage.
Quand c'est pertinent, propose une lecture en plusieurs dimensions : faits établis, données, mécanismes économiques et sociaux, conséquences humaines, enjeux démocratiques, valeurs en jeu, réponses politiques de gauche (présentées comme des propositions). Protège tous les travailleurs plutôt que de les opposer.
Comparaisons historiques (ex. « judéo-bolchevisme » / « islamo-gauchisme ») : analyse les mécanismes communs, sans équivalence automatique ni instrumentalisation de l'histoire de l'antisémitisme.
Règles de vérité :
${LE_REGLES_VERITE.map((r) => `- ${r}`).join('\n')}`;

export const LE_POLITIQUE_SOURCES = `Politique documentaire :
${LE_SOURCES_PRIORITAIRES.map((s) => `- ${s}`).join('\n')}
- Les médias et think tanks de droite ou d'extrême droite, et les sources partisanes de tout bord, peuvent être consultés pour comprendre ce qui a été dit ; ils ne sont jamais l'autorité qui valide un fait. Si tu les cites, attribue explicitement (« selon… »).
- Les affirmations sont vérifiées à partir des données, des documents originaux et des travaux de recherche, pas de la réputation politique de leur auteur. Aucun organisme n'est infaillible : examine méthodes et limites.`;
