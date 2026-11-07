# Journal des fiches quotidiennes (phase alpha)

Chaque passage de la tâche quotidienne ajoute ici : la date, le nombre de questions testées, les fiches créées
(identifiants), les questions écartées et pourquoi (déjà couvertes, sources introuvables ou invérifiables).
Aucune fiche n'est créée sans au moins deux sources réellement ouvertes et lues.


## 7 novembre 2026 — passage de 00 h 28 (UTC)

**Questions testées : 25** (fichier passé dans `node scripts/verifier-couverture.mjs`). Une première liste de 30 phrases a été testée : 4 étaient réellement couvertes et ont été écartées comme quasi-doublons (OQTF non exécutées → `expulser-tous-etrangers-condamnes` ; RSA dès l'arrivée et « l'immigration coûte plus qu'elle ne rapporte » → `immigres-aides` ; droit du sol → `nationalite-trop-facile`). Les autres phrases de cette liste (dette et dépenses sociales, normes européennes et agriculteurs, éoliennes et oiseaux, sécurité sociale des étrangers) ont été remplacées pour varier les thèmes.

Sur les 25 questions retenues, 7 étaient signalées « LACUNE » et **18 étaient « couvertes » par une fiche voisine hors sujet** (ex. Pétain → fiche sur l'antisémitisme aujourd'hui ; juges de gauche → justice laxiste ; liens RN-Russie → concentration des médias ; colonisation → financement des services publics ; AME → aides aux immigrés, qui ne parle pas de l'AME). Elles ont été traitées comme des lacunes réelles, conformément à la règle v12 (jamais une fiche voisine présentée comme réponse).

1. L'aide médicale d'État soigne gratuitement les clandestins et coûte une fortune.
2. La France paie beaucoup plus à l'Union européenne qu'elle ne reçoit.
3. Le réchauffement climatique n'est pas causé par l'homme, le climat a toujours changé.
4. Les éoliennes polluent plus qu'elles ne rapportent.
5. Les voitures électriques polluent plus que les voitures thermiques.
6. Il y a trop de fonctionnaires en France.
7. Les étrangers touchent le minimum vieillesse sans avoir jamais cotisé.
8. La France est le pays le plus taxé du monde.
9. Pétain a protégé les Juifs français.
10. Le Front national n'a jamais eu de lien avec d'anciens collaborateurs.
11. Les juges sont tous de gauche.
12. Les liens du RN avec la Russie, c'est de la propagande.
13. La colonisation a apporté des routes, des écoles et des hôpitaux.
14. Le niveau scolaire s'effondre.
15. Les mineurs étrangers isolés sont pour la plupart des majeurs qui mentent sur leur âge.
16. Baisser la TVA sur l'énergie, comme le propose le RN, c'est bon pour le pouvoir d'achat.
17. Privatiser l'audiovisuel public, comme le veut le RN, fera économiser de l'argent.
18. La France insoumise veut régulariser tous les sans-papiers.
19. Légaliser le cannabis ferait exploser la consommation.
20. Les chômeurs indemnisés gagnent plus qu'en travaillant.
21. Les prisons françaises sont des hôtels.
22. La préférence nationale, il suffit d'une loi pour l'appliquer.
23. Les entreprises françaises paient les impôts les plus élevés d'Europe.
24. La Seine-Saint-Denis vit des aides de l'État.
25. L'IVG est devenue un moyen de contraception.

**Fiches créées : 25** (générateur `scripts/fiches/quotidien_20261107_0028.py`, toutes avec `publics` et une « lecture de gauche ») — chaque fiche repose sur au moins deux sources ouvertes et lues le 7 novembre 2026 :

| Fiche | Verdict | Sources principales |
|---|---|---|
| `ame-cout-sans-papiers` | trompeur | Sénat (rapport PLF 2026 et rapport Delahaye 2025) ; mission Évin-Stefanini (LCP, 2023) |
| `minimum-vieillesse-etrangers` | trompeur | DREES (minima sociaux 2025) ; réponse ministérielle à l'Assemblée (2026) |
| `mineurs-isoles-age` | trompeur | Conseil constitutionnel (2018-768 QPC) ; Académie de médecine (2007) ; Défenseur des droits (2022) ; Localtis (Sénat, 2021) |
| `preference-nationale-constitution` | contredit | Conseil constitutionnel (93-325 DC) ; Club des juristes (décision d'avril 2024) ; Public Sénat (2021) |
| `lfi-regulariser-sans-papiers` | trompeur | Programme du NFP (2024) ; amendement LFI CL737 (Assemblée, 2023) ; DGEF via Public Sénat (2026) |
| `france-contributeur-net-ue` | trompeur | Sénat (PLF 2025) ; Toute l'Europe (2026) ; CEPII (2018) |
| `impots-entreprises-europe` | trompeur | Toute l'Europe (2021, 2023) ; Institut Montaigne (impôts de production) ; commission d'enquête du Sénat sur les aides (Public Sénat, 2025) |
| `france-pays-plus-taxe` | plutôt exact | OCDE (recettes publiques 2025) ; Eurostat via Toute l'Europe (2026) ; DREES (2025) ; OCDE santé (2025) |
| `trop-de-fonctionnaires` | opinion | Insee (2026) ; OCDE (2025) ; France Stratégie (2017) |
| `rn-tva-energie` | trompeur | Bercy via Public Sénat (2024) ; Institut Montaigne (2024) ; Insee Analyses n° 78 (2022) |
| `rechauffement-origine-humaine` | contredit | GIEC AR6 (2021) ; Météo-France ; ministère de la Transition écologique (2026) |
| `eoliennes-polluent` | contredit | Réponse ministérielle (ACV pour l'ADEME, 2021) ; DREAL Auvergne-Rhône-Alpes (2023) |
| `voiture-electrique-pollue` | contredit | ADEME (2022) ; ICCT (2021) ; Carbone 4 (2022) |
| `cannabis-legalisation-consommation` | trompeur | OFDT (2024) ; mission de l'Assemblée (2021) ; CAE (2019) ; Statistique Canada (2021) |
| `ivg-contraception` | contredit | DREES (2025) ; HAS (2013) ; réponse ministérielle (2011) |
| `petain-juifs-francais` | contredit | Laurent Joly (CNRS, conférence 2022 et compte rendu APHG) ; Mémorial de la Shoah ; Jacques Semelin (Public Sénat, 2023) ; discours de 1995 |
| `fn-fondateurs-collaboration` | contredit | Nicolas Lebourg (2014) ; RTBF (2021) ; Fondation Jean-Jaurès (présentation d'ouvrage) |
| `colonisation-routes-ecoles` | trompeur | Kamel Kateb (INED, 2004) ; réponse ministérielle sur la loi de 2005 (2006) ; Assemblée (loi de 1946) |
| `rn-russie-liens` | contredit | Rapport de la commission d'enquête sur les ingérences (Assemblée, 2023) ; LCP (2023) ; AFP (2023) |
| `juges-de-gauche` | contredit | Ministère de la Justice (élections 2026) ; Public Sénat (2023, 2025) ; Actu-Juridique (2019) |
| `niveau-scolaire-effondre` | plutôt exact | OCDE (PISA 2022) ; DEPP (TIMSS 2023) ; Public Sénat (2023) |
| `indemnisation-chomage-salaire` | trompeur | Unédic (2021, 2025, 2026) ; France Travail (taux de remplacement) |
| `prisons-hotels` | contredit | Ministère de la Justice (1er octobre 2026) ; Sénat (rapport CGLPL, 2026) ; LCP (CGLPL, 2024) |
| `seine-saint-denis-aides` | trompeur | Rapport Cornut-Gentille et Kokouendo (Assemblée, 2018) ; Insee (2024) ; Caf 93 (2025) |
| `privatiser-audiovisuel-public` | trompeur | Institut Montaigne (2022, 2024) ; Puremédias (2024) ; Sénat (2024) ; Assemblée / UER (2024) |

**Reconnaissance des questions** : 16 concepts et 23 arguments ajoutés dans `public/js/cartographie.js` (avec formules pour les deux modes) ; les 25 questions mènent désormais à leur fiche. Le classement des sources reconnaît désormais l'ADEME, le GIEC, Météo-France, l'OFDT, la HAS et Statistique Canada comme organismes publics (`public/js/ligne-editoriale.js`).

**Fiches existantes adaptées aux deux publics (10)** : `cartes-vitale-en-trop`, `smic-detruit-emplois`, `heritage-taxation`, `fraude-sociale-fiscale`, `francais-travaillent-pas-assez`, `retraite-64-ans`, `emploi-apres-50-ans`, `syndicats-bloquent`, `nationalite-trop-facile`, `grand-remplacement` (champ `publics` ajouté dans `scripts/fiches/refonte_v12.py`, à partir du seul contenu sourcé de chaque fiche).

**Questions écartées** : aucune pour sources invérifiables. Points non sourcés laissés hors des fiches et signalés dans leurs limites : temps de retour énergétique et effet de l'éolien sur les oiseaux, données de l'Uruguay sur le cannabis, part de l'AME dans les dépenses d'assurance maladie, position du RN sur l'audiovisuel public en 2026, prix de location d'une télévision en prison.

**Tests** : `npm test` 471/471 ; e2e 38/38. Un mot-clé trop large de la fiche sur l'indemnisation chômage captait « les chômeurs ne veulent pas travailler » : mots-clés resserrés et identifiant renommé (`indemnisation-chomage-salaire`) ; la phrase « Les éoliennes, ça ne sert à rien, il faut du nucléaire » reste dirigée vers la fiche sur le mix électrique.

## 7 novembre 2026 — passage de 06 h 13 (UTC)

**Questions testées : 25** (fichier passé dans `node scripts/verifier-couverture.mjs`). Une première liste de 31 phrases a été testée ; 6 ont été écartées comme déjà couvertes ou quasi-doublons d'une fiche existante (jours fériés → `francais-travaillent-pas-assez` ; âge de départ comparé à l'Europe → voisin de `retraite-64-ans` ; dette et dépenses sociales → `services-publics-moyens` ; natalité des immigrées → voisin de `grand-remplacement` ; arrêts maladie et « impôts des ultra-riches », remplacées pour varier les thèmes). Sur les 25 retenues, 11 étaient « LACUNE » et **14 étaient « couvertes » par une fiche voisine hors sujet** (ex. pacte européen sur l'asile → souveraineté populaire ; aide à l'Algérie → RSA et SMIC ; antifas → délinquance ; éducation sexuelle → services publics ; taxe Zucman → « Mélenchon veut ruiner la France » ; feux de forêt → mix électrique ; glyphosate → programme de Mélenchon) : elles ont été traitées comme de vraies lacunes (règle v12).

1. Le pacte de Marrakech de l'ONU oblige la France à accepter une immigration massive.
2. Le pacte européen sur la migration et l'asile va imposer des milliers de migrants à la France.
3. L'accord franco-algérien de 1968 donne des privilèges aux Algériens.
4. La France verse des milliards d'aide au développement à l'Algérie.
5. La France envoie des centaines de milliards à l'Ukraine pendant que les Français se serrent la ceinture.
6. Le gouvernement ukrainien est dirigé par des nazis.
7. Les antifas sont plus violents et plus dangereux que l'ultradroite.
8. Il y a des actes antichrétiens tous les jours et on brûle nos églises dans l'indifférence.
9. L'éducation à la sexualité à l'école apprend la théorie du genre aux enfants.
10. La taxe Zucman ferait fuir les riches et tuerait les start-up.
11. Le RN veut supprimer l'impôt sur le revenu pour les moins de 30 ans, c'est une bonne mesure pour la jeunesse.
12. Le RN promet la retraite à 60 ans pour tout le monde.
13. Les feux de forêt sont causés par des pyromanes, pas par le réchauffement climatique.
14. Les zones à faibles émissions punissent les pauvres qui ne peuvent pas changer de voiture.
15. Les vaccins à ARN messager ont fait plus de morts que le covid.
16. Le Nouveau Front populaire n'a pas gagné les législatives de 2024, il n'avait aucune légitimité pour gouverner.
17. Le RN défend les travailleurs et vote pour la hausse des salaires.
18. L'Europe nous interdit de vendre des voitures thermiques en 2035.
19. Le glyphosate n'est pas dangereux, les écolos font peur pour rien.
20. Les mosquées en France sont financées par l'étranger.
21. Les déboutés du droit d'asile restent presque tous en France.
22. Les logements sociaux sont attribués en priorité aux immigrés.
23. Les médecins étrangers sont moins compétents que les médecins français.
24. L'accord avec le Mercosur va tuer nos agriculteurs et le RN est le seul à s'y opposer.
25. La France est le pays d'Europe qui accueille le plus de demandeurs d'asile.

**Fiches créées : 25** (générateur `scripts/fiches/quotidien_20261107_0613.py`, toutes avec `publics` et une « lecture de gauche ») — chaque fiche repose sur au moins deux sources ouvertes et lues le 7 novembre 2026 :

| Fiche | Verdict | Sources principales |
|---|---|---|
| `pacte-marrakech-onu` | contredit | Texte du pacte (ONU, 2018) ; réponse du ministère des Affaires étrangères (AN, 2019) ; Club des juristes (2018) ; Public Sénat (2018) |
| `pacte-europeen-migration-asile` | trompeur | Conseil de l'UE (2023) ; décision d'exécution 2025/2642 (réserve 2026) ; Euronews (juin 2026, deux articles) |
| `accord-franco-algerien-1968` | plutôt exact | LCP (rapport Rodwell-Lefèvre, 2025) ; Public Sénat (2023) ; université de Montpellier (2023) |
| `aide-developpement-algerie` | contredit | Réponse du ministère des Affaires étrangères (AN, 2025) ; Focus 2030 d'après l'OCDE (2026) |
| `aide-ukraine-montant` | contredit | Public Sénat (audition du ministre des Armées, 2024) ; ministère des Armées (2024) ; Institut de Kiel via Statista et Public Sénat (2025) ; Commission européenne (2026) |
| `ukraine-gouvernement-nazis` | contredit | FactCheck.org (2022) ; ADL (2022) ; EUvsDisinfo (SEAE) |
| `ultragauche-ultradroite-violence` | contredit | Réponse du ministère de l'Intérieur (AN, 2024) ; Public Sénat (2023, 2026) ; document du rapporteur de la PPL 877 (AN, 2023) ; rapport d'enquête n° 1824 (AN, 2023) |
| `actes-antichretiens-eglises` | trompeur | Bilan des actes antireligieux 2025 (ministère de l'Intérieur) ; réponse ministérielle (AN, 2026) ; Le Monde (2019) ; Le Parisien (2020) |
| `education-sexualite-genre` | trompeur | Bulletin officiel (février 2025) ; L'Étudiant (2025) ; Public Sénat (2024) ; réponse ministérielle (AN, 2025) |
| `taxe-zucman-exil` | trompeur | Conseil d'analyse économique (2025) ; Sénat (2025) ; Public Sénat (2025) ; LCP (2025, deux articles) |
| `rn-impot-moins-30-ans` | opinion | Institut Montaigne (2022) ; Public Sénat (2024) ; LCP (2026) ; MoneyVox (2022) |
| `rn-retraite-60-ans` | contredit | Public Sénat (2022, 2024, 2026) ; LCP (2024) ; Institut Montaigne (2024) |
| `feux-foret-pyromanes` | trompeur | Ministère de la Transition écologique (2026, page et dossier de presse) ; Météo-France (2026) ; GIEC AR6 |
| `zfe-menages-modestes` | plutôt exact | SDES (2025) ; Santé publique France (2021) ; Observatoire des inégalités d'après la DREES (2024) ; LCP (décision 2026-903 DC) ; réponse ministérielle (AN, 2022) |
| `vaccins-arn-mortalite` | contredit | EPI-PHARE (2025) ; ANSM (2021-2022) ; Santé publique France (2023) ; AlloDocteurs/AFP (2022) ; OMS Europe (2024) |
| `nfp-legislatives-2024` | opinion | Datan (2024) ; Constitution, art. 8 (Légifrance) ; Public Sénat (2024) ; LCP (2024, deux articles) |
| `rn-salaires-votes` | trompeur | Scrutins publics n° 38, 42 et 44 du 20 juillet 2022 (via Datan) ; LCP (2023) |
| `voitures-thermiques-2035` | trompeur | Parlement européen, Observatoire législatif (2023) ; Commission européenne (2026) ; Journal de l'Automobile (4 novembre 2026) ; LCP (2025) |
| `glyphosate-danger` | trompeur | CIRC (2015) ; Inserm (2021) ; EFSA (2023) ; Commission européenne (2023) |
| `mosquees-financement-etranger` | trompeur | Sénat (mission d'information, 2016) ; Localtis (2016) ; Service-public.fr (2025) ; Middle East Eye (2024) |
| `deboutes-asile-restent` | plutôt exact | Sénat (rapport n° 874, juillet 2026) ; Cour des comptes (2024) ; Acteurs publics (2015) |
| `logements-sociaux-immigres` | contredit | Ministère du Logement (2024) ; Insee (2023) ; Économie et Statistique (2014) ; LCP (2026) |
| `medecins-diplome-etranger` | trompeur | Réponse du ministère de la Santé (Sénat, 2026) ; Académie nationale de médecine (2026) ; Santé mentale d'après l'Ordre (2025) ; BMJ / Harvard (2017) |
| `mercosur-agriculteurs` | trompeur | LCP (vote du 26 novembre 2024) ; Club des juristes (2026) ; Commission européenne (2026) ; Public Sénat (2024) ; Institut Jacques Delors (2026) |
| `france-premier-pays-asile` | contredit | Agence de l'UE pour l'asile (2026, deux pages) ; Eurostat (mars 2026) ; Sénat (juillet 2026) |

**Reconnaissance des questions** : 23 concepts et 27 arguments ajoutés dans `public/js/cartographie.js` ; l'argument « la gauche jugée dangereuse » exclut désormais les phrases sur le glyphosate et les vaccins. Les 25 questions mènent à leur fiche, ainsi que 16 variantes testées (« Zelensky est un nazi », « Les HLM c'est que pour les immigrés », « Le RN a voté contre le smic »…), sans déplacer les phrases voisines (voiture électrique, retraite à 64 ans, éoliennes, Mélenchon). Deux phrases du corpus de compréhension qui attendaient « aucune fiche » sur l'attribution des HLM (`tests/comprehension/phrases.js`) attendent désormais la nouvelle fiche ; les phrases générales sur les loyers et la crise du logement restent sans fiche, comme avant.

**Fiches existantes adaptées aux deux publics (10)** : `devenir-proprietaire`, `louer-sans-cdi`, `pauvres-efforts`, `gauche-immigres-travailleurs` (dans `scripts/fiches/refonte_v12.py`) ; `aider-tout-le-monde`, `services-publics-moyens`, `gauche-augmenter-impots`, `riches-creent-emplois` (dans `scripts/fiches/reponses_directes.py`) ; `etrangers-prisons`, `delinquance-principalement-immigration` (dans `scripts/fiches/immigration_prisons.py`, dont l'assistant de génération transmet désormais le champ `publics`). Textes écrits à partir du seul contenu sourcé de chaque fiche. 70 fiches sur 152 ont désormais un champ `publics`.

**Tests** : `npm test` 471/471 ; e2e 38/38.

**Questions écartées** : aucune pour sources invérifiables. Points non vérifiés laissés hors des fiches et signalés dans leurs limites : part française exacte des aides européennes à l'Ukraine et chiffres de Kiel pour 2025-2026 (site de l'institut inaccessible) ; résultats officiels du ministère de l'Intérieur pour les législatives de 2024 (décompte de Datan) ; votes RN sur le Smic après 2022 ; montant des aides à la conversion en 2026 ; bilan des déclarations de financements étrangers des cultes depuis 2021 ; nombre exact de déboutés encore présents en France (données de l'administration jugées incohérentes par le Sénat). Le seuil de déclaration des financements étrangers retenu est celui de Service-public.fr (15 300 €), et non les 10 000 € parfois cités. Les sources d'opinion ou peu fiables trouvées pendant la recherche (Revue Conflits, Hérodote, ObservAlgérie, Boursorama, Le Petit Journal) n'ont pas été utilisées.
