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

## 7 novembre 2026 — passage de 12 h (UTC)

**Questions testées : 25** (fichier passé dans `node scripts/verifier-couverture.mjs`). Une première liste de 30 phrases a été testée, puis 2 phrases de remplacement (32 au total) ; 7 ont été écartées : 4 déjà couvertes par une fiche qui y répond réellement (Cour européenne des droits de l'homme et expulsions → `criminels-etrangers-proteges-justice` ; exécution des OQTF → `expulser-tous-etrangers-condamnes` ; VIe République de Mélenchon → `melenchon-dangereux-democratie` ; Mélenchon et le Venezuela → voisin de `melenchon-autoritaire`), 2 trop difficiles à traiter de façon factuelle ou trop marginales (« le RN n'a jamais gouverné, il faut leur laisser une chance » ; viande cultivée en laboratoire), et 1 reformulée (impôts locaux et hébergement des migrants). Sur les 25 retenues, 12 étaient « LACUNE » et **13 étaient « couvertes » par une fiche voisine hors sujet** (ex. 80 % des lois → souveraineté populaire ; condamnation de Marine Le Pen → justice laxiste ; LFI et l'euro → « Mélenchon crie » ; cantines → amalgames sur les musulmans ; dette → services publics ; écriture inclusive → services publics ; insectes → souveraineté populaire ; écologie « de bobos » → mix électrique) : elles ont été traitées comme de vraies lacunes (règle v12).

1. 80 % de nos lois sont décidées à Bruxelles.
2. Le RN a changé, ce n'est plus un parti d'extrême droite.
3. La condamnation de Marine Le Pen est un complot des juges pour l'empêcher de se présenter.
4. La France insoumise veut faire sortir la France de l'Union européenne et de l'euro.
5. Les cantines scolaires imposent le halal et suppriment le porc.
6. Le RN veut interdire le voile dans tout l'espace public.
7. Si la gauche ferme les centrales nucléaires, on va manquer d'électricité.
8. La France a la dette la plus élevée d'Europe, elle va faire faillite comme la Grèce.
9. Les ouvriers votent RN parce que la gauche les a abandonnés.
10. L'écriture inclusive est imposée aux enfants à l'école.
11. Les radars sont une pompe à fric pour l'État.
12. Même Georges Marchais voulait arrêter l'immigration.
13. Les émeutes de 2023 ont été commises par des étrangers.
14. Le passage à l'euro a fait exploser les prix.
15. On n'a pas le droit de compter les immigrés en France, l'État cache les chiffres.
16. Les enfants d'immigrés ne se sentent pas français.
17. L'Union européenne veut nous faire manger des insectes.
18. Les demandeurs d'asile touchent plus que nos retraités.
19. Les chiffres du chômage sont truqués, il y a en réalité six millions de chômeurs.
20. L'écologie, c'est un truc de bobos qui punit les classes populaires.
21. Les fonctionnaires sont mieux payés que les salariés du privé.
22. La France est le pays qui a le plus de jours de grève.
23. Il suffit de supprimer le droit du sol pour régler le problème de l'immigration.
24. Les communes paient avec nos impôts locaux l'hébergement des migrants.
25. Les migrants ont tous des smartphones, ce ne sont pas de vrais réfugiés.

**Fiches créées : 25** (générateur `scripts/fiches/quotidien_20261107_1200.py`, toutes avec `publics` et une « lecture de gauche ») — chaque fiche repose sur au moins deux sources ouvertes et lues le 7 novembre 2026 :

| Fiche | Verdict | Sources principales |
|---|---|---|
| `lois-bruxelles-80-pourcent` | contredit | Public Sénat (études Sciences Po Bordeaux et Notre Europe, 2017) ; Euronews (2024) |
| `rn-plus-extreme-droite` | trompeur | Conseil d'État n° 488378 (2024) ; Club des juristes (2024) ; Sciences Po (2022) ; LCP (2024) ; blog Landot (CE, février 2026) |
| `le-pen-condamnation-juges` | contredit | Toute l'Europe et LCP (arrêt d'appel du 7 juillet 2026) ; commentaire d'avocat (2026) ; LCP (QPC, 2025) |
| `lfi-sortie-ue-euro` | trompeur | Public Sénat (2018) ; Terra Nova (2024) ; LCP (programme NFP, 2024) ; Euronews (2024) |
| `cantines-halal-porc` | contredit | Conseil d'État (communiqué, 2020) ; AFP (2020) ; CNCDH ; Banque des Territoires (EGalim, 2019) |
| `rn-voile-espace-public` | plutôt exact | Public Sénat (2022, juillet et août 2026) ; CEDH, S.A.S. c. France (2014) |
| `sortie-nucleaire-penurie` | trompeur | RTE, Futurs énergétiques 2050 (2021) et réactualisation (2026) ; LCP (2021) ; Reporterre (programme Nupes, 2022) |
| `dette-france-grece` | trompeur | Eurostat (2025) et Euronews d'après Eurostat (octobre 2026) ; Insee (septembre 2026) ; Agence France Trésor (août 2026) ; Public Sénat / Cour des comptes (2025) ; La finance pour tous (2025) |
| `ouvriers-vote-rn` | trompeur | Ipsos Talan (législatives 2024, deux enquêtes) ; Fondation Jean-Jaurès (2024) |
| `ecriture-inclusive-ecole` | contredit | Conseil d'État (décembre 2024) ; Sénat (2023) ; Public Sénat (2023) |
| `radars-pompe-a-fric` | trompeur | Cour des comptes (avril 2025) ; Sénat (2024, 2017) ; réponse du ministère de l'Intérieur (AN, 2023) |
| `marchais-immigration-1981` | plutôt exact | Hommes & migrations (A. Hargreaves, 2016) ; Christian Science Monitor (1981) ; Tribune socialiste (1981) |
| `emeutes-2023-etrangers` | contredit | Rapport IGJ-IGA (2023) ; Public Sénat (2023, 2024) ; Insee (2026) |
| `euro-hausse-prix` | contredit | Insee (2002, 2017) ; Banque de France (2007) |
| `statistiques-immigres-cachees` | contredit | Insee (séries 1921-2025 ; portrait social 2025 ; page « statistiques ethniques ») ; Plein droit (2008) |
| `enfants-immigres-sentiment-francais` | contredit | Insee (TeO2, 2023 et 2024) ; dossier de presse de l'Ined (mai 2026, copie d'un tiers) |
| `insectes-union-europeenne` | trompeur | Règlement (UE) 2023/58 ; Commission européenne (2021) ; AFP (2023) ; ALVA Luxembourg (2025) |
| `demandeurs-asile-allocation-retraites` | contredit | Service-public.fr (ADA ; accès au travail, 2026) ; DREES (2025) ; Assurance retraite (Aspa, 2026) |
| `chomage-chiffres-truques` | trompeur | Insee (août 2026 ; appariement 2019) ; France Travail / Dares (octobre 2026 ; définitions 2019) |
| `ecologie-bobos-classes-populaires` | trompeur | Conseil d'analyse économique (2019) ; Insee (2024, 2026) ; Observatoire des inégalités d'après l'OFCE (2022) |
| `fonctionnaires-salaires-prive` | trompeur | Insee Première n° 2043, 2079, 2100, 2101, 2102 (2025-2026) |
| `france-championne-greves` | plutôt exact | Euronews d'après l'ETUI (2023) ; Paris Match Belgique d'après le WSI (2023) ; Éditions Tissot et TPE Actu d'après la Dares (2026) |
| `droit-du-sol-suppression` | trompeur | Code civil, art. 21-7 (Légifrance) ; Insee (2026) ; Banque des Territoires (2026) ; Public Sénat (2025) ; Institut Montaigne (2024) |
| `hebergement-migrants-impots-locaux` | trompeur | Assemblée nationale (PLF 2026) ; Sénat (juillet 2026 ; questions de 2022 et 2024) |
| `migrants-smartphones-refugies` | contredit | HCR (2016) ; Slate (2015) ; EUAA (rapport OFPRA 2025) ; Sénat (2026) ; Eurostat (2026) |

**Méthode** : la recherche documentaire a été répartie entre cinq agents de recherche (WebSearch puis lecture de chaque page avec WebFetch) ; seules les pages effectivement lues ont été retenues, et les passages reprennent les chiffres lus. L'outil de lecture résume les pages : les citations entre guillemets sont courtes et pourraient être revérifiées mot à mot.

**Reconnaissance des questions** : 10 concepts et 20 arguments ajoutés dans `public/js/cartographie.js` ; les 25 questions mènent à leur fiche, ainsi que des variantes testées (« Mélenchon veut le Frexit », « Marine Le Pen est innocente, c'est un procès politique », « On mange des insectes sans le savoir », « La taxe carbone, c'est encore les pauvres qui paient », « Les fonctionnaires sont des privilégiés »…), sans déplacer les phrases voisines (trop de fonctionnaires, services publics, juges de gauche, laïcité, nationalité, éoliennes, asile en Europe, HLM, ZFE). Trois ajustements après les tests : mots-clés resserrés pour les fiches sur les grèves, les statistiques et le chômage, argument « interdire le voile » qui laisse « la laïcité, c'est interdire le voile » à la fiche sur la loi de 1905, et affirmation de la fiche chômage légèrement reformulée pour ne pas capter « les chômeurs profitent du système ».

**Fiches existantes adaptées aux deux publics (10)** : `immigres-aides`, `rsa-smic`, `chomeurs-travailler`, `laicite-loi-1905`, `musulmans-amalgames`, `souverainete-populaire`, `justice-laxiste-prison`, `melenchon-ruiner-france`, `france-pays-immigration`, `pauvrete-france`. Ces fiches n'ayant pas de générateur actif, le champ `publics` est ajouté par un nouveau module `scripts/publics-complements.js`, appliqué de façon idempotente par `scripts/corrections-v10.js` (étape 4). Textes écrits à partir du seul contenu sourcé de chaque fiche. 105 fiches sur 177 ont désormais un champ `publics`.

**Questions écartées** : aucune pour sources invérifiables. Points non vérifiés laissés hors des fiches et signalés dans leurs limites : texte de l'arrêt d'appel Le Pen et date de la décision de cassation ; programme actuel de LFI (2026-2027) ; texte original de la lettre de Georges Marchais (L'Humanité, janvier 1981) et suite de l'histoire du PCF ; nationalité des mineurs interpellés en 2023 ; montant 2026 du minimum vieillesse ; volume des radiations de France Travail ; émissions de CO2 par niveau de vie postérieures à 2011 ; effet des restrictions du droit du sol à Mayotte ; publications primaires de la Dares (pages protégées par un CAPTCHA) et de l'ETUI ; comparaison avec la crise grecque de 2010. Sources trouvées mais non utilisées : un blog militant (texte de la lettre de Marchais, daté de façon erronée), un témoignage militant sur Vitry, et un site d'extrême droite (écarté d'office).

## 7 novembre 2026 — passage de 20 h 15 (UTC)

**Questions testées : 27** (fichier passé dans `node scripts/verifier-couverture.mjs`), pour 26 fiches créées : une phrase de plus que l'objectif a été gardée, car sa recherche était complète. 1 phrase a été écartée comme quasi-doublon (« Les journalistes sont tous de gauche » → `medias-concentration`, qui y répond déjà). Sur les 26 retenues, 11 étaient « LACUNE » et **15 étaient « couvertes » par une fiche voisine hors sujet**. Exemples : peine de mort → délinquance ; syndicats et subventions → RSA ; SDF et migrants → expulsions ; migrants climatiques → grand remplacement ; députés → RSA ; 35 heures → temps de travail ; violences policières → délinquance. Elles ont été traitées comme de vraies lacunes (règle v12).

1. En France, on n'a plus le droit de se défendre chez soi, c'est la victime qui finit en prison.
2. Il faut rétablir la peine de mort, ça dissuaderait les criminels.
3. Les peines planchers font baisser la récidive.
4. Les refus d'obtempérer explosent à cause du laxisme.
5. Les violences policières n'existent pas.
6. Le RN veut nationaliser les autoroutes pour baisser les péages.
7. La proportionnelle rendrait la France ingouvernable.
8. Le RN a toujours défendu le droit à l'avortement.
9. Le RN veut sortir la France de l'OTAN.
10. Le RN est le premier parti de France, il représente la majorité des Français.
11. Les jeunes votent massivement pour le RN.
12. Les députés touchent 15 000 euros par mois.
13. Les syndicats vivent des subventions de l'État.
14. Les crèches de Noël sont interdites dans les mairies.
15. La fermeture de C8 est une censure politique.
16. Une retraite par capitalisation rapporterait plus que la répartition.
17. Le prix de l'essence, ce sont surtout des taxes.
18. Les 35 heures ont ruiné la France.
19. On paie l'électricité plus cher à cause du marché européen.
20. Dans les banlieues, les jeunes ne veulent pas travailler.
21. On loge les migrants à l'hôtel pendant que les SDF français dorment dehors.
22. Des centaines de millions de migrants climatiques vont envahir l'Europe.
23. La Chine pollue bien plus que nous, nos efforts pour le climat ne servent à rien.
24. La France compte le plus de musulmans d'Europe, ils seront bientôt majoritaires.
25. Le massacre du 17 octobre 1961 est une invention de la gauche.
26. Les retraités ont un meilleur niveau de vie que les actifs.

**Fiches créées : 26.** Elles sont produites par le générateur `scripts/fiches/quotidien_20261107_2015.py`. Toutes ont un champ `publics` et une « lecture de gauche ». Chaque fiche repose sur au moins deux sources ouvertes et lues le 7 novembre 2026 :

| Fiche | Verdict | Sources principales |
|---|---|---|
| `legitime-defense-domicile` | contredit | Assemblée nationale : PPL n° 557 reproduisant les articles 122-5 et 122-6 du code pénal (2022), réponse ministérielle (2016), document d'étape PPL n° 691 (2026) ; Club des juristes (2026) |
| `peine-de-mort-dissuasion` | contredit | National Research Council (2012) ; Death Penalty Information Center (2025) ; ministère de la Justice (archives 2007) ; Institut Montaigne / Ipsos BVA, *Fractures françaises* (2025) |
| `peines-planchers-recidive` | trompeur | IPP, note n° 105 (2024) ; Infostat Justice n° 118 (2012) ; Assemblée nationale, commission des lois (2025) |
| `refus-obtemperer-hausse` | trompeur | Gendarmerie d'après le SSMSI (2024) ; rapport d'information AN n° 2692 (2024) ; LCP (2024) ; Public Sénat (2023) |
| `violences-policieres-existent` | contredit | Rapport annuel IGPN 2024 ; réponse du ministère de l'Intérieur (AN, 2025) ; Défenseur des droits (2025) ; Club des juristes sur l'arrêt CEDH Fraisse (2025) |
| `rn-nationaliser-autoroutes` | plutôt exact | Institut Montaigne (2022) ; Sénat (rapports 2020 et 2024) ; Assemblée nationale (questions au gouvernement 2023, PPL LFI 2025) |
| `proportionnelle-ingouvernable` | trompeur | info.gouv.fr ; Larousse (1987) ; La Vie des idées (2025) ; Le Grand Continent (2025) ; LCP (2025) |
| `rn-ivg-toujours-defendu` | contredit | LCP (janvier et mars 2024) ; Public Sénat (deux articles de décembre 2016) |
| `rn-sortie-otan` | trompeur | Institut Montaigne (2022) ; Public Sénat (2022) ; Europe 1 / AFP (2024) ; AFP via Les Nouvelles Calédoniennes (2024) ; Élysée (2009) |
| `rn-premier-parti-majorite` | trompeur | Public Sénat (2024) ; Maire-info (2024) ; LCP (2024) |
| `jeunes-vote-rn` | trompeur | Ipsos (européennes 2024) ; Ipsos Talan (législatives 2024) ; Fondation Jean-Jaurès (2024) |
| `deputes-salaire-15000` | contredit | Assemblée nationale, fiche n° 7 (janvier 2026) ; IPP, note n° 91 (2023) ; Public Sénat (2022) |
| `syndicats-subventions` | trompeur | Cour des comptes (2024) ; Journal du Net (octobre 2026) ; CFDT ; Assemblée nationale (question écrite, 2011) |
| `creches-noel-mairies` | trompeur | Conseil d'État (2016, 2018) ; Banque des Territoires (2016) |
| `c8-fermeture-censure` | trompeur | Public Sénat (2025) ; arrêt du Conseil d'État du 19 février 2025 (via le blog Landot) ; Conseil d'État (CNews, 2024) ; Puremédias (2025) |
| `retraite-capitalisation-rendement` | trompeur | COR (dossier de décembre 2025, contributions d'A. Lavigne et de l'OCDE) ; Diario Financiero d'après l'OCDE (2009) |
| `essence-prix-taxes` | plutôt exact | Réponse ministérielle (AN, 2025) ; Connaissance des Énergies d'après la DGEC, l'UFIP et la Commission (2026) ; Banque de France (2021) |
| `trente-cinq-heures-ruine` | contredit | Rapport AN n° 2436 (2014) ; Ires (2014) ; Institut Montaigne (2014) ; Insee (2026) |
| `electricite-prix-marche-europeen` | trompeur | Sénat (2023) ; SDES (2023 et 2026) ; CRE (2026) |
| `banlieues-jeunes-travailler` | contredit | Observatoire des inégalités d'après l'ONPV (2025) ; Banque des Territoires d'après l'ONPV (2026) ; Insee, *Économie et Statistique* n° 541 (2023) |
| `migrants-hotel-sdf` | trompeur | Conseil d'État (2012, art. L. 345-2-2 CASF) ; Insee-Ined (2013) ; Public Sénat (2026) ; Unicef-FAS (2025) ; Sénat (2024) |
| `migrants-climatiques-europe` | contredit | Banque mondiale, Groundswell (2021) ; IDMC (2026) ; HCR (2025) ; Euronews (2025) |
| `chine-pollue-efforts-inutiles` | trompeur | Global Carbon Project (2025, 2026) ; SDES (2026) ; Carbon Brief (2024) ; Our World in Data (2025) |
| `musulmans-majoritaires-france` | contredit | Pew Research Center (2017) ; Insee (TeO2 et fécondité, 2023) ; Maldita.es (2019) |
| `massacre-17-octobre-1961` | contredit | Élysée (2021) ; LCP (2024) ; La Vie des idées (2008) ; J.-P. Brunet, *The Historical Journal* (2008) ; Assemblée nationale (1997) |
| `retraites-niveau-vie-actifs` | trompeur | COR (rapport annuel 2026) ; DREES (2025) |

**Méthode.** La recherche documentaire a été répartie entre cinq agents de recherche. Chacun cherchait avec WebSearch puis lisait chaque page avec WebFetch. Seules les pages effectivement lues ont été retenues comme sources. Les chiffres viennent des passages lus.

Les pages qui n'ont pas pu être ouvertes n'ont pas été citées : Légifrance, Dares, plusieurs pages de Vie publique, DREES sans-domicile, Ined, rapport complet de Pew, OCDE, Rexecode, note du SSMSI. L'outil de lecture résume les pages : les citations entre guillemets sont courtes et pourraient être revérifiées mot à mot.

Lors de la relecture, plusieurs affirmations non sourcées ont été retirées des fiches :
- le maintien de CNews sur la TNT ;
- le couvre-feu de 1961 ;
- les attentats du FLN ;
- la part chinoise des renouvelables ;
- la concentration du patrimoine par génération ;
- le dispositif d'accueil des demandeurs d'asile.

Les noms de deux victimes ont aussi été remplacés par une description, sauf dans l'intitulé d'un arrêt de la CEDH.

**Reconnaissance des questions.**
- `public/js/cartographie.js` reçoit 23 concepts et 29 arguments. Les 26 questions mènent à leur fiche.
- Des variantes testées y mènent aussi : « Si un cambrioleur entre chez moi, c'est moi qui irai en prison », « Remettons la peine de mort pour les terroristes », « Les jeunes des cités ne veulent pas bosser », « À la pompe, on paie que des taxes », « Hanouna a été censuré par l'Arcom », « Dans 20 ans les musulmans seront majoritaires », « Les boomers vivent mieux que nous »…
- Ces ajouts ne déplacent aucune des 92 phrases de contrôle : les 75 questions des passages précédents et 17 phrases voisines (comparaison avant/après).
- « Les crèches pour enfants manquent de places » reste correctement une lacune.
- Un ajustement a été fait après les tests : le motif « par répartition » a été retiré du concept capitalisation. « D'où vient la retraite par répartition ? » doit en effet rester sans fiche (test v12).

**Fiches existantes adaptées aux deux publics (10).** Le champ `publics` a été ajouté, à partir du seul contenu sourcé de chaque fiche, via `scripts/publics-complements.js`, appliqué par `scripts/corrections-v10.js`. Fiches concernées : `medias-concentration`, `delinquance-partout`, `homicides-record`, `lfi-contre-police`, `discriminations-embauche`, `electricite-nucleaire-renouvelables`, `rsa-profiteurs`, `impots-assistanat`, `expulser-tous-etrangers-condamnes`, `dividendes-salaires`.

**Questions écartées.** Aucune pour sources invérifiables.

**Points non vérifiés, laissés hors des fiches et signalés dans leurs limites :**
- présence de la nationalisation des autoroutes et de la sortie du commandement intégré de l'OTAN dans les programmes RN de 2027 ;
- vote des sénateurs et eurodéputés RN sur l'IVG ;
- score exact du RN aux européennes 2024 (31,37 % ou 31,47 % selon les sources) ;
- statistiques nationales sur la légitime défense ;
- condamnations pénales de policiers ;
- chiffre 2025 des refus d'obtempérer (seulement via un média) ;
- abrogation des peines planchers en 2014 ;
- émissions par habitant de la Chine ;
- affirmation « la France compte le plus de musulmans d'Europe » ;
- rapport Mandelkern ;
- dispositif d'hébergement des demandeurs d'asile.

## 8 novembre 2026 — premier passage (00 h, UTC)

**Questions testées : 25** (fichier passé dans `node scripts/verifier-couverture.mjs`). Une première liste de 29 phrases a été testée. Quatre ont été écartées : « l'immigration coûte des dizaines de milliards » (déjà traitée par `immigres-aides`), et trois phrases gardées en réserve faute de place (patrons du CAC 40, arrêts maladie des fonctionnaires, Taubira et la traite) ; elles pourront servir à un prochain passage.

Sur les 25 questions retenues, 9 étaient signalées « LACUNE » et **16 étaient « couvertes » par une fiche voisine hors sujet**. Exemples : Rocard → `aider-tout-le-monde`, qui ne parle pas de la citation ; LFI pro-Poutine → `melenchon-crie` ; uniforme → `services-publics-moyens` ; racisme anti-blanc → `discriminations-embauche` ; Suède → `delinquance-principalement-immigration`. Elles ont été traitées comme des lacunes réelles (règle v12).

1. La France ne peut pas accueillir toute la misère du monde, comme disait Michel Rocard.
2. Des milliers de retraités centenaires fantômes à l'étranger touchent encore leur pension.
3. Le Brexit a été un succès pour le Royaume-Uni.
4. Orbán a réussi à relancer la natalité en Hongrie.
5. Giorgia Meloni a stoppé l'immigration en Italie.
6. La Suède a sombré dans la violence à cause de l'immigration.
7. La gauche veut donner le droit de vote aux étrangers.
8. Le racisme anti-blanc est devenu le racisme le plus répandu en France.
9. Les francocides se multiplient : on tue des Français parce qu'ils sont français.
10. Les mineurs délinquants sont de plus en plus jeunes, il faut supprimer l'excuse de minorité.
11. La limitation à 80 km/h n'a servi à rien.
12. La gauche dénonce le 49.3 mais c'est elle qui l'a le plus utilisé.
13. Les travailleurs détachés font du dumping social.
14. Le SMIC français est l'un des plus élevés d'Europe.
15. On a déversé des milliards dans les banlieues pour rien.
16. Les profs ne travaillent que 18 heures par semaine.
17. Les cheminots partent à la retraite à 50 ans.
18. Les abayas et les atteintes à la laïcité envahissent l'école.
19. En France, on fait changer de sexe des enfants.
20. L'uniforme à l'école réglerait les problèmes de discipline.
21. Interdire les néonicotinoïdes tue nos agriculteurs.
22. Les mégabassines sont indispensables pour l'agriculture.
23. LFI est pro-Poutine.
24. Le RN veut interdire certains postes aux binationaux.
25. LFI veut une VIe République.

**Fiches créées : 25.** Elles sont produites par le générateur `scripts/fiches/quotidien_20261108_0000.py`. Toutes ont un champ `publics` et une « lecture de gauche ». Chaque fiche repose sur au moins deux sources ouvertes et lues le 8 novembre 2026 :

| Fiche | Verdict | Sources principales |
|---|---|---|
| `rocard-misere-du-monde` | trompeur | INA (2023) ; 3millions7, CFJ (2015) ; La Cimade (2016, témoignage) |
| `retraites-centenaires-algerie` | trompeur | Les Surligneurs (2024) ; CNAV, étude 2020-039 (2021) ; réponse ministérielle AN (2012) ; résumé du rapport de la Cour des comptes par le CCME (2025) |
| `brexit-succes` | contredit | Office for Budget Responsibility (2020 et 2026) ; YouGov (2026) ; ONS (2025) |
| `hongrie-natalite-orban` | contredit | KSH, office statistique hongrois (2026) ; AFP via La Libre Belgique (2025) ; AEI (2025) |
| `meloni-immigration-italie` | contredit | Ministère italien de l'Intérieur (2025) ; Istat (2025) ; Le Grand Continent (2026) ; Euronews (2025) |
| `suede-violence-immigration` | trompeur | Police suédoise (janvier et juillet 2026) ; Brå (rapports 2021:8, 2021:9, 2026:10) |
| `droit-vote-etrangers` | plutôt exact | Sénat, texte adopté n° 21 (2011) ; AN, rapport n° 2428 (2026) ; LCP (février 2026, deux articles) |
| `racisme-anti-blanc` | contredit | Insee-Ined, Insee Première n° 1911 (TeO2, 2022-2023) ; Ined, TeO 2008 ; CNCDH (2026) |
| `francocide-terme` | invérifiable | AFP via The Local (2023) ; Université de Liège (2024) ; Localtis d'après le SSMSI (2024) |
| `excuse-de-minorite` | trompeur | Sénat, rapport n° 885 (2022) ; Public Sénat et LCP sur la décision du Conseil constitutionnel (2025) ; Infostat Justice n° 205 (2025) |
| `limitation-80-kmh` | contredit | ONISR-Cerema (2020) ; Cerema, rapport final (2020) ; ONISR, synthèse du retour à 90 km/h (2022) |
| `article-49-3-gauche` | plutôt exact | Public Sénat (2020) ; Assemblée nationale, fiche n° 64 ; Université de Lille (2023) ; programme du NFP (2024) |
| `travailleurs-detaches-dumping` | trompeur | Dares Résultats n° 1 (2024) ; Parlement européen (2026) ; Sénat, rapport n° 599 (2017) |
| `smic-europe-classement` | plutôt exact | Eurostat (janvier et juillet 2026) ; Insee Références (2026) |
| `banlieues-milliards-politique-ville` | trompeur | Cour des comptes (2020 et 2026) ; AN, rapport n° 1014 sur la Seine-Saint-Denis (2018) |
| `profs-18-heures` | trompeur | Décret n° 2014-940 (Légifrance) ; IH2EF d'après la DEPP (2022) ; Weka d'après la DEPP (2025) |
| `cheminots-retraite-50-ans` | trompeur | COR, fiche CPRPF (2024) ; Public Sénat (2023 et 2024) ; DREES (2025) |
| `abaya-laicite-ecole` | trompeur | Conseil d'État (2024) ; Public Sénat (2024) ; Courthouse News (2023) |
| `mineurs-transition-genre` | trompeur | Sénat, rapport n° 622 (2024) ; Public Sénat (2024) ; Haute Autorité de santé (2025) |
| `uniforme-ecole-discipline` | trompeur | Localtis sur le rapport de la DEPP (2026) ; AFP (2026) ; Ohio State University (2021) ; University of Houston (vers 2010) |
| `neonicotinoides-agriculteurs` | trompeur | LCP (2025) ; Public Sénat (2025) ; Anses (2018) ; INRAE (2025) |
| `megabassines-agriculture` | trompeur | Académie d'agriculture (2024) ; Localtis (2023) ; AFP via Terre-net (2025) |
| `lfi-pro-poutine` | trompeur | Compte rendu AN du 1er mars 2022 ; communiqué de la délégation LFI au Parlement européen (2022, cité pour décrire son vote) ; LCP (2024) ; Public Sénat (2025) |
| `rn-binationaux-postes` | confirmé | Public Sénat (2024) ; LCP (2024) ; Ined-Insee, TeO (2009) |
| `lfi-sixieme-republique` | confirmé | L'Avenir en commun (2022) et contrat de législature du NFP (2024), cités pour décrire le programme ; Public Sénat (2019) |

**Méthode.** La recherche documentaire a été répartie entre cinq agents de recherche. Chacun cherchait avec WebSearch puis lisait chaque page avec WebFetch. Seules les pages effectivement lues ont été retenues. Les chiffres viennent des passages lus.

Pages qui n'ont pas pu être ouvertes, donc non citées : franceinfo (robots.txt, notamment sur le « francocide »), Libération CheckNews (centenaires), Vie publique (JavaScript), pages de la DEPP et du ministère de l'Éducation, pages de l'Ined sur TeO2, InfoMigrants et France 24. L'outil de lecture résume les pages : les citations entre guillemets sont courtes et pourraient être revérifiées mot à mot.

Lors de la relecture, plusieurs affirmations non sourcées ont été retirées des fiches :
- l'utilisation du 49.3 pour la réforme des retraites de 2023 et pour la loi Travail ;
- la « division par deux » de la peine au titre de l'excuse de minorité ;
- la circonstance aggravante du code pénal (fiches « francocide » et racisme) ;
- l'accord des parents pour les traitements de mineurs trans ;
- la baisse de fécondité dans toute l'Europe depuis 2021 ;
- le nombre de quartiers prioritaires ;
- le rôle des syndicats dans la dénonciation de la fraude au détachement ;
- un jugement validant d'autres mégabassines ;
- une estimation de fraude aux pensions tirée d'une question écrite d'un député RN, source écartée.

**Reconnaissance des questions.**
- `public/js/cartographie.js` reçoit 14 concepts et 14 arguments, placés en tête de la liste des arguments parce que leurs concepts sont très spécifiques. Les 25 questions mènent à leur fiche.
- Variantes testées qui y mènent aussi : « Rocard disait qu'on ne peut pas accueillir toute la misère du monde », « Les centenaires algériens touchent nos retraites », « La justice des mineurs est trop laxiste », « Les profs sont tout le temps en vacances », « Remettons l'uniforme à l'école », « Mélenchon est copain avec Poutine », « Avec les bassines on vole l'eau des paysans ».
- Comparaison avant/après sur 344 phrases de contrôle (affirmations de la bibliothèque, questions des passages précédents, phrases des tests) : seules les 14 questions visées changent de fiche.
- Ajustements après les tests : « On peut pas accueillir toute la misère du monde », sans Rocard, doit rester sur `aider-tout-le-monde` (le concept Rocard ne repose plus que sur le nom). Les mots-clés trop généraux de la fiche abaya (« signes religieux », « voile à l'école ») ont été retirés pour laisser « La laïcité interdit les signes religieux dans la rue » à `laicite-loi-1905`. Les mots-clés « RIC » ont été retirés de la fiche VIe République : « Il faut un référendum d'initiative citoyenne » reste une lacune plutôt que d'être envoyé vers le programme de LFI. Les deux fiches LFI ne sont pas classées dans la rubrique « Mélenchon et LFI », réservée aux fiches en cinq parties.
- `public/js/ligne-editoriale.js` : les organismes statistiques publics étrangers (ONS, OBR, Istat, KSH, Brå, police suédoise) et le Parlement européen sont désormais reconnus comme sources d'autorité.

**Fiches existantes adaptées aux deux publics (10).** Le champ `publics` a été ajouté, à partir du seul contenu sourcé de chaque fiche, via `scripts/publics-complements.js`, appliqué par `scripts/corrections-v10.js`. Fiches concernées : `aah-suffisante`, `egalite-salariale`, `encadrement-loyers`, `immigration-emploi`, `immigration-salaires`, `chomage-penurie-recrutement`, `morts-au-travail`, `agriculteurs-revenus`, `abstention-inegale`, `sondages-mille-personnes`.

**Questions écartées.** Aucune pour sources invérifiables. La fiche « francocide » a le dossier le plus mince : deux sources lues sur l'origine du mot, aucune statistique officielle sur un mobile « anti-français », d'où le verdict « invérifiable ».

**Points non vérifiés, laissés hors des fiches et signalés dans leurs limites :**
- rapport 2025 de la Cour des comptes sur les pensions versées à l'étranger (lu seulement à travers un résumé) ;
- arrivées en Italie en 2022 et causes de la baisse de 2024 ;
- rapport de la DEPP sur l'uniforme et note DEPP 2025 sur le temps de travail des enseignants (lus à travers la presse spécialisée) ;
- texte de la décision du Conseil constitutionnel de juin 2025 sur la justice des mineurs ;
- nombre actuel de binationaux (chiffre lu : 2009) ;
- chiffres nationaux sur les bloqueurs de puberté et les hormones chez les mineurs ;
- usages du 49.3 en 2025 et décompte nominatif d'Élisabeth Borne ;
- part des agriculteurs bénéficiaires des réserves de substitution.

## 8 novembre 2026 — passage de 06 h 13 (UTC)

**Questions testées : 25** (fichier passé dans `node scripts/verifier-couverture.mjs`). Une première liste de 30 phrases a été testée. Cinq ont été écartées :
- trois déjà couvertes par une fiche qui y répond réellement : exécution des OQTF (`expulser-tous-etrangers-condamnes`), Cour européenne des droits de l'homme et expulsions (`etranger-crime-plus-sa-place`), violences sexuelles et étrangers (voisin de `delinquance-principalement-immigration`, qui donne la part des étrangers par type d'infraction) ;
- deux quasi-doublons : natalité des immigrées (`grand-remplacement`) et dépenses sociales (`services-publics-moyens`).

Cinq phrases difficiles à sourcer ont été remplacées avant la recherche : fausses accusations de viol, élections truquées, « zones de non-droit », terroristes « tous immigrés », écologistes et viande.

Sur les 25 retenues, 11 étaient « LACUNE » et **14 étaient « couvertes » par une fiche voisine hors sujet**. Exemples : école privée → services publics ; pollution de l'air → mix électrique ; ISF → impôts et assistanat ; mères voilées → loi de 1905 ; Conseil constitutionnel → « juges de gauche ». Elles ont été traitées comme de vraies lacunes (règle v12).

Les 25 questions :
1. Le regroupement familial fait venir des centaines de milliers d'immigrés chaque année.
2. Le RN veut supprimer le regroupement familial.
3. Les étudiants étrangers, c'est une immigration déguisée.
4. Schengen empêche la France de contrôler ses frontières.
5. La France donne des milliards d'aide au développement à l'Afrique pour rien.
6. Les Français abusent des arrêts maladie.
7. Le RSA conditionné à 15 heures d'activité, ça remet les gens au travail.
8. Les jeunes ne veulent plus travailler.
9. Le pouvoir d'achat des Français ne cesse de baisser.
10. À l'hôpital, il y a plus d'administratifs que de soignants.
11. Les entreprises ne touchent presque pas d'aides publiques, c'est l'assistanat des pauvres qui coûte.
12. La suppression de l'ISF a relancé l'investissement.
13. En France, on ne peut pas licencier.
14. Le RN veut taxer les super-riches.
15. Le blocage des prix proposé par la gauche provoquerait des pénuries.
16. La gauche veut forcer les médecins à s'installer à la campagne.
17. L'école privée est meilleure que l'école publique.
18. Les mères voilées n'ont pas le droit d'accompagner les sorties scolaires.
19. Le Conseil constitutionnel empêche la volonté du peuple, c'est le gouvernement des juges.
20. Le narcotrafic explose en France.
21. Le RN est le meilleur rempart contre l'antisémitisme.
22. Pendant la guerre d'Algérie, la torture était l'exception.
23. L'esclavage, la France n'a pas à s'en excuser, ce sont des Africains qui vendaient les esclaves.
24. Les sanctions contre la Russie nous font plus de mal qu'à elle.
25. La pollution de l'air, ça ne tue pas tant que ça.

**Fiches créées : 25.** Elles sont produites par le générateur `scripts/fiches/quotidien_20261108_0613.py`. Toutes ont un champ `publics` et une « lecture de gauche ». Chaque fiche repose sur au moins deux sources ouvertes et lues le 8 novembre 2026 :

| Fiche | Verdict | Sources principales |
|---|---|---|
| `regroupement-familial-chiffres` | contredit | Ined, Population & Sociétés n° 643 (2026) ; F. Héran, ICM/CNRS (2023) ; Public Sénat (2023 et 2026) |
| `rn-regroupement-familial` | plutôt exact | LCP (2022 et 2024) ; AN, proposition de loi constitutionnelle n° 2120 du RN (2024, citée pour décrire sa position) ; décision 93-325 DC (traduction de l'Université du Texas) ; directive 2003/86/CE (EUR-Lex) |
| `etudiants-etrangers-immigration` | trompeur | OCDE, Perspectives des migrations internationales (2022) ; Campus France (2022 et 2025) ; ministère de l'Enseignement supérieur (2019) ; Public Sénat (2026) |
| `schengen-controles-frontieres` | contredit | Conseil d'État, décision n° 499702 (2025) ; Commission européenne (notifications) ; Parlement européen (2024) ; Mission opérationnelle transfrontalière (2026) ; Public Sénat sur la Cour des comptes (2024) |
| `aide-developpement-afrique` | trompeur | OCDE, CAD (2026) ; Sénat, avis n° 141 (2025) ; Focus 2030 (2024) ; AFD (2026) |
| `arrets-maladie-abus` | trompeur | Cour des comptes, RALFSS (2024) ; DREES (2025) ; Public Sénat (2025) ; Legisocial d'après l'Assurance maladie (2025) |
| `rsa-15-heures-activite` | trompeur | Dares-IPP, rapport n° 68 (2026) ; Localtis (2024 et 2025) ; CNCDH, déclaration D-2024-7 |
| `jeunes-ne-veulent-plus-travailler` | contredit | Insee Première n° 2096 (2026) ; Localtis (2024) ; Trésor-Éco n° 376 (2025) ; Institut Montaigne (2025, cité avec attribution) |
| `pouvoir-achat-baisse` | trompeur | Insee (séries 1960-2025, France portrait social 2025, Insee Première n° 2105 et n° 2079) ; Banque de France (2025) |
| `licenciement-impossible-france` | contredit | Insee Références (2025) ; Sénat, rapport n° 488 (2026) ; OCDE (2020) ; IRES (2014) ; Lefebvre Dalloz (2022 et 2026) |
| `aides-publiques-entreprises` | contredit | Sénat, rapport n° 808 (2025) ; Public Sénat (2025, deux articles) ; DREES, minima sociaux (2025) |
| `suppression-isf-investissement` | contredit | France Stratégie, rapport final du comité d'évaluation (2023) ; Public Sénat (2021) ; Localtis sur le rapport du Sénat (2019) |
| `rn-taxe-zucman` | trompeur | Public Sénat (2025) ; LCP (2025, deux articles) ; scrutin n° 3300 via Datan ; Legifiscal (2025) |
| `blocage-prix-penuries` | trompeur | Programme du NFP (2024, cité pour décrire son contenu) ; Le Club des juristes (2024) ; Insee Analyses n° 75 (2022) ; Banque de France (2024) ; Institut Montaigne (2024, argument contraire attribué) |
| `regulation-installation-medecins` | trompeur | LCP (2025, deux articles) ; Public Sénat (2025) ; Localtis (2026) ; DREES, Études et Résultats n° 1144 (2020) et n° 1267 (2023) |
| `ecole-privee-meilleure` | trompeur | Cour des comptes, rapport sur l'enseignement privé sous contrat (2023) ; Localtis (2023 et 2025, d'après la DEPP) |
| `meres-voilees-sorties-scolaires` | contredit | AN, réponse ministérielle à la question n° 57422 (2015) ; Les Surligneurs (2025) ; Public Sénat (2019 et 2021) |
| `conseil-constitutionnel-gouvernement-juges` | trompeur | LCP (2024) ; Actu-Juridique (2024) ; Assemblée nationale, fiche n° 55 ; Sénat, révisions de la Constitution ; Public Sénat (2024) |
| `narcotrafic-explosion` | plutôt exact | Sénat, rapport n° 588 (2024) et loi du 13 juin 2025 ; AFP d'après le ministère de l'Intérieur (2025 et 2026) ; AFP d'après l'OFDT (2025) |
| `hopital-administratifs-soignants` | contredit | DREES, Les établissements de santé, fiches 05 et 06 (2026) ; Acteurs publics (2025, deux articles) |
| `rn-rempart-antisemitisme` | trompeur | Nonna Mayer, Droits & Libertés n° 214 (2026, d'après le baromètre CNCDH) ; CNCDH, communiqué (2026) ; Public Sénat (2018) ; AFP via JusticeInfo (2025) |
| `torture-guerre-algerie` | contredit | Élysée, déclaration sur Maurice Audin (2018) et reconnaissance de l'assassinat d'Ali Boumendjel (2021) ; Raphaëlle Branche, CICR (2007) |
| `esclavage-traite-responsabilite` | trompeur | BnF (2021) ; Sénat, rapport n° 262 (2000) ; AN, réponse ministérielle à la question n° 13957 (2026) ; Myriam Cottias, CNRS (2021) ; Académie des sciences d'outre-mer |
| `sanctions-russie-effets` | trompeur | Direction générale du Trésor (2026) ; Commission européenne (2024 et 2025) ; Eurostat (2022) ; Banque de France (2023) |
| `pollution-air-deces` | contredit | Santé publique France (2021) ; Agence européenne pour l'environnement (2025) ; OMS (2024) ; SDES (2025) |

**Méthode.** La recherche documentaire a été répartie entre cinq agents de recherche. Chacun cherchait avec WebSearch puis lisait chaque page avec WebFetch. Seules les pages effectivement lues ont été retenues. Les chiffres viennent des passages lus. Les sources de droite (Institut Montaigne) ou partisanes (programme du NFP, proposition de loi du RN) ne servent qu'à décrire une position ou un argument contraire, toujours avec attribution.

Pages qui n'ont pas pu être ouvertes, donc non citées :
- Vie publique et Légifrance (JavaScript ou autorisation expirée) ;
- pages du ministère de l'Intérieur (statistiques des titres de séjour) et du Conseil constitutionnel (décisions 93-325 DC et 2023-863 DC) ;
- ameli.fr (bilan de la fraude 2025) et PDF de la Dares (CAPTCHA) ;
- jeu de données de l'OCDE sur la protection de l'emploi.

L'outil de lecture résume les pages : les citations entre guillemets sont courtes et pourraient être revérifiées mot à mot.

Lors de la relecture, plusieurs affirmations non sourcées ont été retirées des fiches :
- une régulation existante de l'installation d'autres professions de santé ;
- un effet de l'exclusion des mères voilées sur le nombre d'accompagnateurs ;
- un niveau de morts liés au trafic en 2024 « supérieur à 2021-2022 » (lu seulement dans Euronews, non retenu) ;
- le mode de nomination des membres du Conseil constitutionnel ;
- une formule prêtant au RN l'intention de « viser les musulmans ».

Chiffres signalés comme douteux par la recherche et non repris :
- « 12 millions de francs » pour l'indemnité de 1849, contradictoire avec les 126 millions avancés par l'historienne Myriam Cottias ;
- 538 400 ruptures conventionnelles en 2024, incohérent avec l'Insee, le Sénat et l'Unédic ;
- 723 M€ de fraudes détectées en 2025, lu seulement dans des titres de résultats de recherche.

**Reconnaissance des questions.**
- `public/js/cartographie.js` reçoit 14 concepts et 14 arguments, placés en tête de la liste des arguments : aide à l'Afrique, RSA et heures d'activité, jeunes et travail, baisse du pouvoir d'achat, administratifs à l'hôpital, aides aux entreprises, ISF, RN et taxation des riches, blocage des prix, école privée, mères voilées, Conseil constitutionnel, RN et antisémitisme, pollution de l'air. Les 25 questions mènent à leur fiche.
- Pour départager, trois arguments existants excluent désormais les nouveaux concepts :
  - `juges_rouges` et `juges_gauche` excluent `conseil_constit` ;
  - `services_publics_moyens` exclut, au niveau de la phrase, `hopital_admin` et `ecole_privee`.
- Variantes testées qui y mènent aussi : « Les jeunes d'aujourd'hui sont des feignants », « On vit moins bien qu'avant », « Il faut rétablir l'ISF », « Bardella veut taxer les milliardaires », « Bloquer les prix, c'est soviétique », « Une maman voilée ne devrait pas accompagner les sorties scolaires », « Le Conseil constitutionnel a censuré la loi immigration », « Les particules fines ne tuent personne », « On donne des milliards à l'Afrique », « Les patrons touchent des aides publiques énormes », « Le RN protège les juifs », « L'hôpital croule sous la bureaucratie ».
- Comparaison avant/après sur 271 phrases de contrôle (affirmations de la bibliothèque et questions des passages précédents) : seules les 14 questions visées changent de fiche. « Les juges sont tous de gauche » reste sur `juges-de-gauche`.
- Ajustement après les tests : « Le pouvoir d'achat s'effondre », phrase du test de compréhension, doit rester sur `dividendes-salaires` / `pauvrete-france`. Les motifs « effondrement » et « chute » ont donc été retirés du concept de baisse du pouvoir d'achat.

**Fiches existantes adaptées aux deux publics (10).** Le champ `publics` a été ajouté, à partir du seul contenu sourcé de chaque fiche, via `scripts/publics-complements.js`, appliqué par `scripts/corrections-v10.js`. Fiches concernées : `commune-paris-1871`, `front-populaire-1936`, `criminels-etrangers-proteges-justice`, `etranger-crime-plus-sa-place`, `expulser-reduit-criminalite`, `france-plus-sure-moins-immigres`, `immigration-chiffres-definitions`, `immigres-prisons-surrepresentation`, `ingerences-etrangeres`, `passoires-thermiques`.

**Questions écartées pour sources invérifiables : aucune.** Les dossiers les plus minces sont :
- `hopital-administratifs-soignants` : DREES et presse spécialisée seulement, sans rapport de la Cour des comptes ni vérification de presse ;
- `conseil-constitutionnel-gouvernement-juges` : la décision elle-même n'a pas pu être ouverte.

**Points non vérifiés, laissés hors des fiches et signalés dans leurs limites :**
- total de l'immigration familiale en 2025 ;
- note actuelle de la France à l'indicateur de protection de l'emploi de l'OCDE (la valeur citée date de 2013) ;
- effet propre des quinze heures d'activité et des sanctions sur le RSA ;
- sort de l'« impôt sur la fortune improductive » dans la loi de finances 2026 ;
- texte de la loi Taubira sur Légifrance ;
- effet propre des sanctions sur l'économie russe ;
- part des décisions de non-conformité dans l'ensemble des décisions du Conseil constitutionnel.

## 8 novembre 2026 — passage de 12 h 13 (UTC)

**Questions testées : 25** (fichier passé dans `node scripts/verifier-couverture.mjs`). Une première liste de 47 phrases a été testée. Les 25 retenues étaient toutes « LACUNE » et n'avaient pas de quasi-doublon dans `data/library` (vérifié par grep sur les affirmations et les mots-clés).

Phrases écartées avant la recherche :
- déjà couvertes : antifas et ultragauche (`ultragauche-ultradroite-violence`), OQTF (`expulser-tous-etrangers-condamnes`), juifs qui quittent la France (`antisemitisme-aujourdhui`) ;
- quasi-doublon : « juger les mineurs de 16 ans comme des adultes » (`excuse-de-minorite`).

Phrases « couvertes » par une fiche voisine hors sujet, non traitées ce passage (pistes pour les suivants) :
- « le nazisme, c'était de gauche » (→ `gauche-nation-debats`) ;
- « LFI refuse de dire que le Hamas est terroriste » (→ `melenchon-crie`) ;
- « le RN veut sortir de la CEDH » (→ `souverainete-populaire`) ;
- « les profs font de la propagande de gauche » (→ `medias-concentration`) ;
- « les fonctionnaires sont plus souvent absents » et « ne peuvent jamais être licenciés » (→ `services-publics-moyens`) ;
- « la viande halal finance le terrorisme » et « les Frères musulmans infiltrent les associations » (→ `musulmans-amalgames`) ;
- « les polygames touchent des allocations pour toutes leurs épouses » (→ `rsa-smic`) ;
- « Mayotte est submergée par l'immigration » (→ `grand-remplacement`).

Questions testées :
1. Le communisme a fait 100 millions de morts, la gauche n'a pas de leçons à donner.
2. Les guerres de Vendée, c'était un génocide commis par la Révolution.
3. La sociologie, c'est la culture de l'excuse.
4. On ne peut plus rien dire en France, la liberté d'expression est morte.
5. Les élus sont tous pourris, tous corrompus.
6. Le Japon refuse l'immigration et s'en sort très bien.
7. La Pologne n'a pas d'immigration et elle est prospère.
8. Milei a sauvé l'Argentine avec sa tronçonneuse.
9. La France a perdu toute influence en Afrique.
10. La gauche veut l'indépendance de la Nouvelle-Calédonie.
11. Les migrants qui arrivent sont presque tous des jeunes hommes.
12. Les étrangers en situation irrégulière votent aux élections.
13. Les immigrés ne font aucun effort pour apprendre le français.
14. Il y a des zones de non-droit où la police ne peut plus entrer.
15. Les jeunes de banlieue brûlent des voitures à chaque Nouvel An.
16. Les écolos veulent interdire la viande.
17. Le bio, c'est une arnaque.
18. Les loups massacrent les troupeaux et les écolos s'en fichent.
19. L'hiver démographique va tuer la France.
20. Il faut rétablir le service militaire obligatoire.
21. Les Restos du cœur nourrissent surtout des migrants.
22. La GPA va être légalisée, la gauche veut marchandiser les enfants.
23. Les villes gérées par le RN sont les mieux gérées de France.
24. Le RN veut couper les subventions aux associations.
25. La France est le pays où l'on a le plus de jours de congés.

**Fiches créées : 25.** Elles sont produites par le générateur `scripts/fiches/quotidien_20261108_1213.py`. Toutes ont un champ `publics` et une « lecture de gauche ». Chaque fiche repose sur au moins trois sources ouvertes et lues le 8 novembre 2026 :

| Fiche | Verdict | Sources principales |
|---|---|---|
| `communisme-100-millions-morts` | trompeur | La Vie des idées (Collège de France), recensions de N. Werth (2009) et de Yang Jisheng (2013) ; Times Higher Education (1998) ; tribunal khmer rouge via Lepetitjournal (2018) ; Fondation Jean-Jaurès (2010) ; Larousse (1980) |
| `vendee-genocide` | trompeur | Jean-Clément Martin, APHG (2018) ; propositions de loi de l'Assemblée nationale (2012, 2013, 2018) ; Slate (2013) |
| `sociologie-culture-excuse` | trompeur | European Journal of Social Theory (2021) ; La Vie des idées (2016) ; Observatoire des inégalités (B. Lahire, 2016) ; HAL (2016) ; Politis (2016) |
| `liberte-expression-plus-rien-dire` | contredit | Public Sénat (2020, 2023) ; CEDH, arrêt Handyside ; RSF (2026, deux pages) ; CB News (2026) ; Ifop pour la Fondation Jean-Jaurès (2025) ; Ifop pour Sud Radio et CNews (2017, cité comme fait défavorable) |
| `elus-tous-corrompus` | contredit | Observatoire SMACL via Maire-info (2026) ; Public Sénat sur la HATVP (2026) ; Transparency International (2026) ; Localtis sur le CEVIPOF (2025) et l'AFA (2024) |
| `japon-sans-immigration` | contredit | Jiji Press via Nippon.com (2026, trois articles) et Adnkronos (2025) ; AFP (2026) ; FMI, article IV (2026) |
| `pologne-sans-immigration` | contredit | Notes from Poland d'après l'Office des étrangers, le GUS et Eurostat (2025-2026) ; Polskie Radio (2026) ; École SGH de Varsovie (2024) |
| `milei-argentine-bilan` | trompeur | FMI, deuxième revue (2026) ; Chequeado d'après l'INDEC (2025, 2026) ; El Economista d'après l'INDEC (2026, deux articles) |
| `france-influence-afrique` | trompeur | Assemblée nationale, rapport n° 2683 (2026) ; Sénat, rapport sur la sécurité africaine (2025) ; AFP (2025) |
| `nouvelle-caledonie-gauche-independance` | trompeur | Sénat, rapport n° 409 (2026) ; Assemblée nationale, rapport n° 1980 (2025) et scrutin n° 6022 (2026) ; Matignon (2020) ; LCP (2026) ; Université Laval (accords de Matignon) |
| `migrants-jeunes-hommes` | trompeur | Agence de l'UE pour l'asile (2025) ; Ofpra, rapport 2024 ; Insee Première n° 2051 (2025) ; Insee, Femmes et hommes (2022) ; HCR (2024) |
| `etrangers-irreguliers-votent` | contredit | Assemblée nationale, rapport sur la PPLC n° 149 (2026) ; Service-public.fr (deux fiches) ; Insee, Répertoire électoral unique ; Landot & associés sur le TA de Guyane (2026) |
| `immigres-apprendre-francais` | contredit | Insee d'après TeO2 Ined-Insee (2023) ; ministère de l'Intérieur, ELIPA 2 ; Sénat, rapport Ciuntu (2024) ; Service-public.fr (2026) |
| `zones-de-non-droit` | trompeur | F. Jobard, CNRS, revue Criminologie (2005) ; Localtis sur la Cour des comptes (2023), les opérations « place nette » (2024) et le SSMSI (2024) ; Assemblée nationale, rapport n° 2692 (2024) |
| `voitures-brulees-nouvel-an` | trompeur | Ministère de l'Intérieur via l'AFP (2026), Caradisiac (2024) et macommune.info (2023) ; Public Sénat (2017, 2024) ; ONDRP (2012) ; Sénat, rapport sur les émeutes (2024) |
| `ecolos-interdire-viande` | trompeur | Ministère de la Transition écologique (2023) ; Localtis (2021) ; Agreste (2026) ; Santé publique France (2024) ; Public Sénat sur le HCC (2024) et sur Lyon (2021) |
| `bio-arnaque` | contredit | Cour des comptes, synthèse (2022) ; Inra et Inserm, NutriNet-Santé (2018) ; EFSA (2016, 2025) ; Agence BIO (2025) |
| `loups-troupeaux` | trompeur | OFB et préfet coordonnateur (2025) ; AN, réponse ministérielle à la question n° 10988 (2026) ; Réussir et Pleinchamp (presse agricole, 2024-2025) ; Localtis (2022) |
| `hiver-demographique` | trompeur | Insee Première n° 2087 (2026) et n° 1881 (2021) ; Public Sénat sur l'Ined (2026) ; Eurostat via Euronews et The Brussels Times (2026) |
| `service-militaire-obligatoire` | opinion | Cour des comptes sur le SNU (2024) ; Localtis (2024) ; ministère des Armées (2025) ; Public Sénat (2025) ; LCP (2026) ; Acteurs publics (2007) ; Ipsos (2025) |
| `restos-coeur-migrants` | trompeur | Restos du cœur, étude 2023-2024 et synthèse 2025 ; Insee Première n° 1907 (2022) ; Localtis avec l'AFP (2023) |
| `gpa-gauche-legalisation` | contredit | Code civil via l'académie de Versailles ; Sénat, question écrite n° 26667 (2022) ; Le Club des juristes (2019) ; Le Quotidien du médecin sur le CCNE (2018) ; gouvernement (2014) ; Aleteia avec l'AFP (2026) |
| `villes-rn-gestion` | trompeur | Public Sénat avec l'AFP (2020) ; CRC PACA sur Fréjus via Presse Agence (2025) ; Acta Politica (2023) ; La Grande Conversation (E. Négrier, CNRS, et A. Gibellini, 2026) |
| `rn-subventions-associations` | plutôt exact | La Libre Belgique d'après France Info (2014) ; Carenews (2024) ; Acta Politica (2023) ; Public Sénat (2020, 2026) |
| `france-record-conges` | contredit | Eurofound (2023) ; Euronews (2025) ; Public Sénat d'après l'OCDE (2025) ; Insee Références (2025) ; Service-public.fr (2026) |

**Méthode.** La recherche documentaire a été répartie entre cinq agents de recherche. Chacun cherchait avec WebSearch puis lisait chaque page avec WebFetch. Seules les pages effectivement lues ont été retenues. Les chiffres viennent des passages lus. Deux pages de Wikipédia lues par un agent ont été écartées des sources : les faits qui en dépendaient (répartition par pays des « 100 millions », estimations de Lebrun et Hussenet sur la Vendée) n'ont pas été repris. Les sources partisanes ou militantes ne servent qu'à décrire une position ou un fait défavorable, avec attribution :
- propositions de loi de députés de droite et d'extrême droite sur la Vendée ;
- sondage Ifop pour Sud Radio et CNews ;
- Fondation Jean-Jaurès, proche du PS.

Pages qui n'ont pas pu être ouvertes, donc non citées :
- Vie publique (JavaScript requis), dont le rapport complet de la Cour des comptes sur le bio et la page HATVP ;
- plusieurs pages du ministère de l'Intérieur et de la préfecture Auvergne-Rhône-Alpes ;
- notes pays de l'OCDE sur la Pologne et page Eurostat sur les titres de séjour (navigation seule) ;
- articles du Monde et de Libération sur la GPA, fact-check de TF1 Info sur les Restos du cœur ;
- HAL Lorraine, deux pages de Cambridge, Maire-info sur la Nouvelle-Calédonie.

L'outil de lecture résume les pages : les citations entre guillemets sont courtes et pourraient être revérifiées mot à mot.

**Reconnaissance des questions.**
- Après génération, 22 des 25 questions menaient déjà à leur fiche par les mots-clés.
- `public/js/cartographie.js` reçoit deux concepts (`vendee`, `bio`) et deux arguments placés en tête (Vendée, agriculture biologique).
- Les arguments existants `liberte_expression` et `corruption`, qui annonçaient jusque-là une lacune, renvoient désormais à `liberte-expression-plus-rien-dire` et `elus-tous-corrompus`. Le corpus de compréhension (`tests/comprehension/phrases.js`) attend donc ces fiches pour cinq phrases qui étaient des lacunes documentées : « On ne peut plus rien dire en France », « Avec la bien-pensance… », « Les politiques sont tous pourris », « Tous corrompus, droite comme gauche », « On ne peut même plus faire une blague… ».
- Le concept `bio` corrige un faux « suspect » du test de cohérence : « Pourquoi le bio reste-t-il si cher ? » mène à `bio-arnaque`, qui traite du prix et du soutien public.
- Un mot-clé trop large (« bilan des maires RN ») envoyait « Les émissions importées comptent-elles dans le bilan de la France ? » vers `villes-rn-gestion` ; il a été retiré.
- Comparaison avant/après sur 308 phrases de contrôle (affirmations de la bibliothèque, questions des passages précédents, candidates de ce passage) : seules les 25 questions visées changent de fiche.
- Variantes vérifiées : « Tous des corrompus ces politiciens », « La liberté d'expression n'existe plus », « On est dans la pensée unique », « La Vendée a été massacrée par les révolutionnaires ». « La fermeture de C8, c'est de la censure » reste sur `c8-fermeture-censure`.

**Autres ajustements.**
- La politique documentaire signalait `communisme-100-millions-morts` et `milei-argentine-bilan` comme dépourvues de source d'autorité. L'organisme de La Vie des idées mentionne désormais le Collège de France, son éditeur. `public/js/ligne-editoriale.js` reconnaît le « Fonds monétaire international » comme institution, au même titre que l'OCDE.
- Un fait historique sourcé (Lionel Jospin, 1999, d'après l'European Journal of Social Theory) a été ajouté à `sociologie-culture-excuse` pour que le compositeur propose au moins deux approches.

**Fiches existantes adaptées aux deux publics (10).** Le champ `publics` a été ajouté, à partir du seul contenu sourcé de chaque fiche, via `scripts/publics-complements.js`, appliqué par `scripts/corrections-v10.js`. Fiches concernées : `antisemitisme-aujourdhui`, `gauche-assistes-travailleurs`, `gauche-au-pouvoir-bilan`, `migrants-mediterranee`, `perte-automatique-droit-sejour`, `programme-cnr-1944`, `programme-irrealisable`, `referendum-democratie-directe`, `renvoyer-tous-deja-condamnes`, `securite-sociale-1945`.

**Questions écartées pour sources invérifiables : aucune.** Les dossiers les plus minces :
- `voitures-brulees-nouvel-an` : chiffres du réveillon lus à travers des sites qui reprennent le ministre ou l'AFP (La Gazette France, Caradisiac, macommune.info) ; aucun profil des interpellés publié ;
- `villes-rn-gestion` : rapports des chambres régionales des comptes lus à travers des comptes rendus ;
- `pologne-sans-immigration` : plusieurs chiffres viennent d'un même média, Notes from Poland, qui cite les sources officielles ;
- `gpa-gauche-legalisation` : la position de 2026 n'a été lue que dans Aleteia (dépêche AFP).

**Points non vérifiés, laissés hors des fiches et signalés dans leurs limites :**
- positions programmatiques des partis de gauche sur la GPA, la Nouvelle-Calédonie et la viande ;
- positions des partis sur le service militaire obligatoire, et coût d'un service obligatoire (seul le SNU est chiffré) ;
- issue du procès du maire de Fréjus prévu en septembre 2026 ;
- profil des auteurs des incendies du réveillon ;
- nouvelles projections démographiques de l'Insee intégrant la fécondité de 2025 ;
- écart de prix entre bio et conventionnel ;
- coût social détaillé des coupes de Javier Milei.

## 8 novembre 2026 — passage de 20 h 14 (UTC)

**Questions testées : 28 candidates, 25 retenues.** Les phrases ont été rassemblées à partir de ce que documentent les vérificateurs (AFP, PolitiFact, FactCheck.org, Euronews, Public Sénat) et des débats publics récents. Elles sont reformulées de façon générale. `node scripts/verifier-couverture.mjs` a donné :
- 12 « LACUNE » ;
- 16 « COUVERTE ». Trois étaient réellement traitées par une fiche existante et ont été écartées : les OQTF non exécutées et le refus de l'Algérie de reprendre ses ressortissants, couverts par `expulser-tous-etrangers-condamnes` et `renvoyer-tous-deja-condamnes` ; les écologistes qui voudraient revenir « à la bougie », jugé trop vague pour être sourcé. Les 13 autres étaient orientées vers une fiche hors sujet (par exemple Notre-Dame vers `medias-concentration`, gratuité des transports vers `rsa-smic`, taxe foncière vers `impots-assistanat`). Elles ont été traitées comme des lacunes.

Questions retenues :
1. La semaine de 32 heures proposée par la gauche ruinerait l'économie.
2. Le trou de la Sécu prouve que notre modèle social est intenable.
3. La dette publique vient des dépenses sociales excessives.
4. La réforme de l'assurance chômage remet les gens au travail.
5. La taxe foncière explose à cause des maires dépensiers.
6. La remigration proposée par l'extrême droite est réalisable.
7. L'Allemagne a raté l'intégration du million de réfugiés de 2015.
8. Le Danemark, gouverné par la gauche, a fermé ses frontières : il faut faire pareil.
9. Il faut une immigration choisie avec des quotas, comme au Canada.
10. Les féminicides sont surtout commis par des étrangers.
11. Le RN a renoncé à sortir de l'euro, il est devenu un parti sérieux.
12. Les sénateurs ont des privilèges exorbitants.
13. Paris est ruinée par la gestion de la gauche, sa dette a explosé.
14. Les agressions d'élus locaux explosent.
15. Le RN défend mieux les homosexuels que la gauche.
16. Les traînées blanches des avions répandent des produits chimiques.
17. L'incendie de Notre-Dame était un attentat qu'on nous cache.
18. Le passe sanitaire, c'était une dictature.
19. Le mariage pour tous a détruit la famille.
20. La viande halal finance l'islamisme.
21. La gratuité des transports publics, c'est irréaliste.
22. Les droits de douane de Trump protègent les ouvriers américains.
23. L'aide à l'Ukraine est détournée par la corruption.
24. Les profs se font agresser tous les jours, l'école est devenue violente.
25. Les gens du voyage ne paient pas d'impôts et ont tous les droits.

**Fiches créées : 25**, par le générateur `scripts/fiches/quotidien_20261108_2014.py`. Toutes ont un champ `publics` et une « lecture de gauche ». Chacune repose sur quatre à huit sources ouvertes et lues le 8 novembre 2026 :

| Fiche | Verdict | Sources principales |
|---|---|---|
| `semaine-32-heures` | trompeur | Programme du NFP (2024) ; Insee, Économie et Statistique (2005) ; Assemblée nationale, rapport n° 2436 (2014) ; Institut Montaigne (2022, attribué) ; CORDIS, Commission européenne (2023) |
| `trou-secu-intenable` | trompeur | Cour des comptes via Santé Mentale et Public Sénat (2026) ; DSS via Acteurs publics (2026) ; Sénat, PLFSS 2027 ; Insee Première n° 2106 (2026) ; LCP sur le rapport Ferracci-Guedj (2023) |
| `dette-depenses-sociales` | trompeur | Insee Première n° 2106 (2026) ; Sénat, intervention de P. Moscovici (2022) et rapport Husson (2024) ; Localtis sur la Cour des comptes (2024) ; F. Ecalle pour l'Institut Montaigne (2021) |
| `reforme-assurance-chomage-emploi` | plutôt exact | Comité d'évaluation de la Dares (2025) ; Unédic (2025, deux études) ; AFP via Weka (2025) |
| `taxe-fonciere-maires` | trompeur | Localtis d'après la DGFiP et l'OFGL (2023, 2024, 2024) ; Maire-info d'après la DGCL (2026) ; Cour des comptes via Localtis (2024) |
| `remigration-realisable` | trompeur | Public Sénat et Europe 1 (2022, citations attribuées) ; dpa via Berliner Zeitung (2024) ; Conseil constitutionnel (2015) ; Conseil de l'Europe (arrêt Hirsi Jamaa) ; Sénat, avis PLF 2026 ; AFP (2026) ; Insee (2025) |
| `allemagne-refugies-2015` | contredit | IAB (2024, 2025) ; ZDF (2025) ; gouvernement fédéral allemand (2023) |
| `danemark-gauche-frontieres` | trompeur | Commission européenne, contrôles Schengen notifiés ; Fondation Robert Schuman (2026) ; RTÉ (2026) ; Copenhagen Post d'après le Service danois de l'immigration (2025) ; Amnesty (2021) ; The Local (2025) ; blue News (2026) |
| `immigration-choisie-canada` | trompeur | Ministère canadien de l'Immigration (2024, 2025-2026) ; Statistique Canada (2026) ; Public Sénat (2019, 2024, 2026) |
| `feminicides-etrangers` | contredit | Ministère de l'Intérieur, études nationales sur les morts violentes au sein du couple 2023 et 2024 ; Public Sénat (2025) ; Insee (2025) |
| `rn-sortie-euro-abandon` | trompeur | Public Sénat (2017, 2019 ×2, 2022) ; LCP (2022) ; Institut Montaigne (2024, attribué) |
| `senateurs-privileges` | trompeur | Sénat, Bureau du 12 juillet 2023 ; Assemblée nationale, fiche 7 (2026) ; Public Sénat (2023 ×2, 2024) |
| `paris-dette-gestion` | trompeur | Ville de Paris, compte administratif 2025 ; Institut Montaigne (2020, 2026, attribué) ; Club des juristes (2022) ; AN, question écrite n° 1311 (2023) |
| `agressions-elus-locaux` | plutôt exact | Ministère de l'Intérieur, rapport du CALAE (2025) ; Assemblée nationale (2024) ; Maire-info (2026) ; Public Sénat (2026) ; Localtis (2024) |
| `rn-homosexuels-droits` | contredit | LCP (2022, 2023, 2024) ; Public Sénat (2019) ; Le Quotidien du Médecin (2019) ; Datan (2021) ; PinkNews (2017, attribué) ; Observatoire des inégalités (2025) |
| `chemtrails-trainees-avions` | contredit | UC Irvine et IOP Publishing (2016) ; AN, réponses ministérielles (2013, 2014) ; Boursorama (2024) ; Euronews (2024) |
| `notre-dame-incendie-attentat` | contredit | AFP via L'Avenir et La Libre (2019) ; Tendance Ouest (2019) ; Public Sénat (2022) ; Blick (2024) ; FactCheck.org (2019) |
| `passe-sanitaire-dictature` | trompeur | Conseil constitutionnel (2021, 2022) ; Conseil d'État (2021) ; CNIL (2021) ; Maire-info sur la Défenseure des droits (2021) ; VIDAL (2022) |
| `mariage-pour-tous-famille` | contredit | Insee (Focus n° 381, séries mariages-Pacs, TEF 2019, bilan démographique 2025) ; LCP (2023) ; Slate/The Conversation |
| `halal-finance-islamisme` | trompeur | Sénat, mission sur l'islam (2016) ; Localtis (2016) ; La Vie des idées (2013) ; Public Sénat (2018) ; AN, question n° 3977 (2012) ; InDaily (2015) |
| `gratuite-transports-irrealiste` | trompeur | Sénat (2019) ; Public Sénat (2019) ; Cour des comptes via Localtis et l'AFP (2025) ; Localtis sur Montpellier (2024) |
| `trump-droits-douane-ouvriers` | trompeur | Réserve fédérale (2019) ; Peterson Institute (2018) ; université de Chicago (2019) ; Institut de Kiel (2026) ; CBO (2025) ; EPI d'après le BLS (2026) |
| `ukraine-aide-corruption` | trompeur | GAO (2024) ; PolitiFact (2024) ; Voice of America (2025) ; Kyiv Independent (2024) ; Euronews (2025) ; Transparency International Ukraine (2026) |
| `profs-agresses-ecole-violente` | trompeur | DEPP, notes n° 25.28 et 25.47 (2025) et n° 25 (2014) ; Localtis (2025) ; Acteurs publics (2026) |
| `gens-du-voyage-impots` | contredit | Défenseur des droits (2024 et fiche ancienne) ; AN, réponses ministérielles (2004, 2010) ; Localtis (2017) |

**Méthode.** La recherche a été répartie entre cinq agents documentalistes, plus un sixième pour deux sources officielles complémentaires (Commission européenne, GAO). Chacun cherchait avec WebSearch puis lisait chaque page avec WebFetch. Seules les pages effectivement lues ont été retenues, et les chiffres viennent des passages lus.

Les sources orientées ne servent qu'avec attribution explicite :
- Institut Montaigne, Europe 1, PinkNews et Fondation Robert Schuman ;
- Amnesty International, Economic Policy Institute et Peterson Institute ;
- Voice of America et Kyiv Independent.

L'outil de lecture résume les pages : les citations entre guillemets sont courtes et pourraient être revérifiées mot à mot.

Pages non ouvertes, donc non citées :
- Vie publique, quand la page exige JavaScript ;
- page de la Dares sur les 35 heures (vérification anti-robot) ;
- pages officielles de la DEPP sur education.gouv.fr (lues sur des copies de l'académie de Nice) ;
- page du ministère de l'Intérieur sur l'éloignement et sur l'étude des morts violentes au sein du couple (lue sur Vie publique) ;
- rapport Mazeaud (2008) ;
- rapport de la chambre régionale des comptes d'Île-de-France sur Paris (2025) ;
- OFCE sur les crises et la dette.

**Reconnaissance des questions.**
- Après génération, 12 des 25 questions (les 12 lacunes initiales) menaient déjà à leur fiche par les mots-clés.
- `public/js/cartographie.js` reçoit 14 concepts : `remigration`, `paris_dette`, `gratuite_transports`, `danemark`, `notre_dame`, `halal`, `gens_voyage`, `trou_secu`, `dette_social`, `ukraine_corruption`, `profs_agresses`, `chemtrails`, `taxe_fonciere`, `elus_agresses`. Il reçoit aussi 15 arguments placés en tête, dont deux pour le Danemark : l'un exige le concept « immigration » pour l'emporter sur `gauche_immigres`, l'autre suffit pour « le modèle danois ».
- L'argument « halal » exclut le concept `cantine`, pour que « Les cantines imposent le halal » reste sur `cantines-halal-porc`.
- Comparaison avant/après sur 311 phrases de contrôle (affirmations de la bibliothèque, questions des passages précédents) ; le corpus de compréhension est vérifié par `npm test` : seules les questions visées changent de fiche.
- Variantes vérifiées : « Hidalgo a ruiné Paris », « Les bus gratuits, c'est n'importe quoi », « Zelensky s'achète des yachts avec notre argent », « Les maires se font agresser de plus en plus », « Les profs se font frapper dans les collèges », « Les gitans ne paient pas d'impôts », « La Sécu est en faillite », « Les chemtrails nous empoisonnent », « Ma taxe foncière a doublé ».
- « La France envoie des milliards à l'Ukraine… » reste sur `aide-ukraine-montant`. « Le halal… finance les mosquées » mène à `mosquees-financement-etranger`.

**Politique documentaire.** `public/js/ligne-editoriale.js` reconnaît désormais trois institutions publiques :
- le Government Accountability Office (organe de contrôle du Congrès américain) ;
- le « gouvernement fédéral allemand » ;
- l'IAB, comme institut de recherche de l'Agence fédérale allemande pour l'emploi.

**Fiches existantes adaptées aux deux publics (10).** Le champ `publics` a été ajouté via `scripts/publics-complements.js`, à partir du seul contenu sourcé de chaque fiche : `gauche-laicite-debats`, `gauche-nation-debats`, `islamo-gauchisme-origine-usages`, `lfi-antisemite`, `lfi-communautarisme`, `melenchon-agressif`, `melenchon-autoritaire`, `melenchon-change-avis`, `patriotisme-nationalisme`, `statistiques-prouvent-insecurite-immigration`.

**Questions écartées pour sources invérifiables : aucune.** Les dossiers les plus minces :
- `danemark-gauche-frontieres` : chiffres de l'asile lus à travers un média local qui cite le Service de l'immigration ;
- `ukraine-aide-corruption` : aucun fact-check français lisible ; sources surtout anglophones ;
- `halal-finance-islamisme` : sources de 2012 à 2016 ;
- `gens-du-voyage-impots` : réponses fiscales de 2004 et 2010.

**Points non vérifiés, laissés hors des fiches et signalés dans leurs limites :**
- vote des députés FN sur le mariage pour tous en 2013, et vote définitif de la PMA en 2021 groupe par groupe ;
- maintien de la taxe sur les résidences mobiles créée en 2010 ;
- rapport de la chambre régionale des comptes sur Paris ;
- part des allègements de cotisations non compensés par l'État ;
- état de l'enquête sur Notre-Dame après novembre 2024 ;
- effets de la réforme de l'assurance chômage de 2023 sur l'emploi.


## 11 novembre 2026 — passage de 12 h 17 (UTC)

**Questions testées : 37 candidates, 25 retenues.** Les phrases ont été choisies parmi les thèmes documentés par les vérificateurs de presse, les rapports publics et les débats récents. Elles sont reformulées de façon générale. `node scripts/verifier-couverture.mjs` a donné, sur les 33 premières :
- 9 « LACUNE » ;
- 24 « COUVERTE ».

Questions écartées parce qu'une fiche y répondait déjà vraiment :
- la majorité des viols commis par des étrangers (`delinquance-principalement-immigration`) ;
- les journalistes tous de gauche (`medias-concentration`) ;
- les Juifs qui quittent la France (`antisemitisme-aujourdhui`) ;
- le coût de l'immigration et les étrangers au RSA (`immigres-aides`) ;
- les OQTF jamais exécutées (`expulser-tous-etrangers-condamnes`) ;
- « LFI soutient le Hamas », traitée dans `lfi-antisemite` : quasi-doublon ;
- le RN, parti du pouvoir d'achat : trop vague pour une fiche (la question des votes du RN sur les salaires est traitée dans `rn-salaires-votes`) ;
- le compteur Linky (lacune, mais hors du champ politique visé).

Une question de réserve a été testée en plus (« le bac est donné à tout le monde », lacune). Trois autres candidates de réserve n'ont pas servi : fraude électorale par procuration (couverte par `etrangers-irreguliers-votent`), armée française, Roms.

Les 16 questions retenues parmi les « COUVERTE » menaient à une fiche hors sujet : par exemple les Frères musulmans vers `musulmans-amalgames`, Mayotte vers `grand-remplacement`, les eurodéputés RN et la Russie vers `souverainete-populaire`, les vaccins des enfants vers `vaccins-arn-mortalite`, les pénuries de médicaments vers `chomage-penurie-recrutement`.

Questions retenues :
1. Les migrants ramènent des maladies comme la tuberculose et la gale.
2. Mayotte est submergée par l'immigration comorienne.
3. Il faut envoyer les demandeurs d'asile au Rwanda comme le Royaume-Uni.
4. Trump a réglé le problème de l'immigration en expulsant massivement.
5. L'Afrique va déverser sa démographie sur l'Europe.
6. Les Frères musulmans infiltrent la France.
7. Les sportives voilées n'ont rien à faire en compétition.
8. La CAF verse des allocations aux familles polygames.
9. Les élèves étrangers font baisser le niveau des classes.
10. Le bac est donné à tout le monde aujourd'hui.
11. Les 10 % les plus riches paient déjà presque tout l'impôt sur le revenu.
12. Supprimer les agences de l'État permettrait d'économiser des milliards.
13. Les intermittents du spectacle sont des assistés payés par nos impôts.
14. Le RN veut remplacer l'IFI par un impôt sur la fortune financière.
15. La retraite à 60 ans promise par LFI est impossible à financer.
16. C'est l'OTAN qui a provoqué la guerre en Ukraine.
17. La Russie de Poutine défend les valeurs chrétiennes de l'Europe.
18. Les eurodéputés RN ne travaillent pas au Parlement européen.
19. Les jeunes préfèrent un régime autoritaire à la démocratie.
20. Le wokisme a pris le contrôle des universités.
21. Les onze vaccins obligatoires des enfants sont dangereux.
22. Les pénuries de médicaments sont la faute de l'Europe.
23. Les Chinois rachètent nos terres agricoles.
24. Les inondations sont la faute des écologistes qui interdisent de curer les rivières.
25. Les squatteurs sont mieux protégés que les propriétaires.

**Fiches créées : 25**, par le générateur `scripts/fiches/quotidien_20261111_1217.py`. Toutes ont un champ `publics` et une « lecture de gauche ». Chacune repose sur quatre à sept sources ouvertes et lues le 11 novembre 2026 :

| Fiche | Verdict | Sources principales |
|---|---|---|
| `migrants-maladies-contagieuses` | trompeur | Santé publique France (2026) ; Santé publique France (2020) ; OMS (2019) ; TB Online (2018) ; Santé publique France (2012) ; Pourquoi Docteur (2017) |
| `mayotte-immigration-comores` | plutôt exact | Insee (2019) ; Insee (2020) ; Banque des Territoires (2026) ; Sénat (2026) ; Sénat (2021) |
| `asile-externalisation-rwanda` | trompeur | National Audit Office (2024) ; 11KBW (2023) ; ITV News (2024) ; Migration Observatory (2024) ; AFP (2025) ; Dawn (2026) |
| `trump-expulsions-immigration` | trompeur | Migration Policy Institute (2025) ; Associated Press (2026) ; PolitiFact (2026) ; Pew Research Center (2025) ; CBS News (2026) |
| `afrique-demographie-migrations` | contredit | INED (2024) ; INED (2018) ; La Vie des idées (2018) ; The Star (2024) ; Union africaine (2025) |
| `freres-musulmans-entrisme` | trompeur | Rapport remis au gouvernement (2025) ; Public Sénat (2025) ; AFP (2025) ; Politis (2025) |
| `voile-sport-competition` | opinion | Conseil d'État (2023) ; Amnesty International (2023) ; Public Sénat (2025) ; Public Sénat (2025) ; Sénat (2026) ; Human Rights Watch (2024) |
| `polygamie-allocations-caf` | trompeur | Assemblée nationale (2010) ; Assemblée nationale (2005) ; Caisse nationale des allocations familiales (1997) ; Sénat (2024) ; Commission nationale consultative des droits de l’homme (2024) ; Assemblée nationale (2014) |
| `eleves-allophones-niveau` | trompeur | DEPP (2025) ; OCDE (2023) ; Cnesco (2015) ; A. Ohinata et J.C. van Ours (2011) ; P. Jensen et A. Würtz Rasmussen (2011) |
| `bac-donne-a-tous` | trompeur | DEPP (2026) ; DEPP (2026) ; DEPP (2025) ; Onisep (2025) ; AFP (2021) ; DEPP (2025) |
| `riches-paient-impot-revenu` | trompeur | Le Journal de l'Économie (2025) ; Observatoire des inégalités (2025) ; Institut des politiques publiques (2023) ; Insee (2023) |
| `agences-etat-suppression` | trompeur | Sénat (2025) ; Sénat (2025) ; Public Sénat (2025) ; FIPECO (2025) ; Banque des Territoires (2025) |
| `intermittents-spectacle-assistes` | trompeur | Unédic (2026) ; Unédic (2026) ; Unédic (2022) ; France Travail (2025) ; Ministère de la Culture (2025) |
| `rn-impot-fortune-financiere` | confirmé | Institut Montaigne (2022) ; Politis (2024) ; Public Sénat (2025) ; LCP (2025) ; LCP (2025) ; Mayer Brown (2026) |
| `lfi-retraite-60-ans` | trompeur | Programme du Nouveau Front populaire (2024) ; LCP (2024) ; Institut Montaigne (2024) ; FIPECO (2024) ; Conseil d'orientation des retraites (2026) |
| `otan-provoque-guerre-ukraine` | trompeur | OTAN (2008) ; Brookings Institution (2022) ; Al Jazeera (2022) ; Le Grand Continent (2022) ; Sciences Po (2022) ; Service européen pour l'action extérieure (2022) ; Le Rubicon (2023) |
| `russie-valeurs-chretiennes` | trompeur | Pew Research Center (2017) ; Associated Press (2022) ; Aleteia (2022) ; Novaya Gazeta Europe (2022) ; FIDH (2024) |
| `rn-eurodeputes-travail` | plutôt exact | Le Parisien (2025) ; France 24 (2024) ; Institut Jacques Delors (2025) ; Public Sénat (2024) ; EU Matrix (2024) |
| `jeunes-democratie-autoritarisme` | trompeur | Ipsos bva (2025) ; Institut Montaigne (2022) ; Public Sénat (2026) ; Fondation Jean-Jaurès (2023) ; Cevipof (2025) |
| `wokisme-universite` | trompeur | Sénat (2026) ; Public Sénat (2021) ; Public Sénat (2019) ; Observatoire du décolonialisme (2021) |
| `vaccins-obligatoires-enfants` | contredit | Santé publique France (2019) ; ANSM (2021) ; ANSM (2019) ; Santé publique France (2025) ; Santé publique France (2025) |
| `penurie-medicaments-europe` | trompeur | DREES (2025) ; Sénat (2023) ; Conseil de l'Union européenne (2026) ; Commission européenne (2025) |
| `terres-agricoles-chinois` | trompeur | Assemblée nationale (2016) ; Réussir (2019) ; Localtis – Banque des Territoires (2023) ; Assemblée nationale (2025) ; Assemblée nationale (2025) |
| `inondations-curage-ecologistes` | contredit | IGEDD et CGAAER (2024) ; Localtis – Banque des Territoires (2024) ; Assemblée nationale (2024) ; Météo-France (2025) |
| `squatteurs-proprietaires` | contredit | Localtis – Banque des Territoires (2023) ; Maire-info (2024) ; Centre de recherche de l’École des officiers de la gendarmer (2023) ; Ministère de la Justice (2023) ; Fondation pour le logement des défavorisés (2025) |

**Méthode.** La recherche a été répartie entre cinq agents documentalistes, chacun chargé de cinq questions. Chacun cherchait avec WebSearch puis lisait chaque page avec WebFetch. Seules les pages effectivement lues ont été retenues, et les chiffres viennent des passages lus. Relecture finale de toutes les fiches : vérification que les affirmations sensibles des résumés et des réponses aux publics figurent bien dans un passage de source (attribution de la phrase sur la charia au rapport et non au ministre, restrictions de l'avortement en Russie d'après la FIDH, profil social des répondants autoritaires d'après l'enquête de 2022).

Les sources orientées ne servent qu'avec attribution explicite :
- Institut Montaigne, Fondation Jean-Jaurès, Observatoire du décolonialisme ;
- Politis, Amnesty International, Human Rights Watch, FIDH ;
- Migration Policy Institute, Brookings, Le Rubicon, cabinet Mayer Brown.

L'outil de lecture résume les pages : les citations entre guillemets sont courtes et pourraient être revérifiées mot à mot. Dans les deux sources sur la gale, les passages reprennent le sens de la page sans être recopiés mot à mot.

Pages non ouvertes, donc non citées :
- Vie publique (JavaScript requis) ;
- bilans DREES des 3e et 4e années de l'obligation vaccinale (vérification anti-robot) ;
- version française du Population et Sociétés n° 558 de l'INED (version anglaise lue) ;
- communiqué du CIO sur les athlètes voilées (cité d'après Human Rights Watch) ;
- article du Ceseda sur Légifrance ;
- bulletin DGFiP Statistiques n° 32 ;
- déclaration de 2008 sur elysee.fr ;
- PDF complet du rapport du Sénat n° 943 sur l'université (trois extraits lus) ;
- Reporterre, Quotidien du pharmacien, Maire-info sur les mesures du ministre du Logement.

**Reconnaissance des questions.**
- Après génération, 9 des 25 questions menaient déjà à leur fiche par les mots-clés.
- `public/js/cartographie.js` reçoit 19 concepts : `mayotte`, `trump_expulsions`, `afrique_demo`, `freres_musulmans`, `voile_sport`, `polygamie`, `riches_ir`, `agences_etat`, `intermittents`, `rn_fortune_fin`, `retraite_60`, `russie_chretiens`, `rn_eurodeputes`, `wokisme_univ`, `vaccins_enfants`, `medicaments`, `squat`, `bac`, `inondations`. Il reçoit aussi 19 arguments placés en tête.
- L'argument « Mayotte » exclut le concept `nationalite`, pour que « Supprimer le droit du sol à Mayotte… » reste sur `droit-du-sol-suppression`. L'argument LFI exige les concepts `retraite_60` et `melenchon_lfi` : « Le RN promet la retraite à 60 ans » reste sur `rn-retraite-60-ans`.
- Comparaison avant/après sur 576 phrases de contrôle (affirmations de la bibliothèque, questions citées dans ce journal) : seules les questions visées changent de fiche, plus trois questions citées dans un passage précédent comme mal orientées (Frères musulmans, polygames, Mayotte), qui mènent désormais à leur fiche.
- Variantes vérifiées : « À Mayotte il y a plus de Comoriens que de Mahorais », « Trump expulse des millions de clandestins », « Avec la natalité africaine, l'Europe va être submergée », « Le hijab n'a pas sa place dans le football », « Il y a des centaines d'agences de l'État qui ne servent à rien », « Mélenchon promet la retraite à 60 ans, c'est du délire », « Poutine est le dernier défenseur des chrétiens », « Bardella n'a jamais siégé au Parlement européen », « Les facs sont tenues par les wokistes », « Le vaccin contre la rougeole donne l'autisme », « On ne trouve plus d'amoxicilline à cause de Bruxelles », « Les crues sont dues au fait qu'on ne peut plus curer les fossés », « Un squatteur ne peut pas être expulsé de chez vous ».
- « Le vaccin covid a tué des milliers de gens » reste sur `vaccins-arn-mortalite`. « L'islamo-gauchisme gangrène l'université » reste sur `islamo-gauchisme-origine-usages`. « Le RN veut taxer les super riches avec la taxe Zucman » reste sur `rn-taxe-zucman`.

**Politique documentaire.** `public/js/ligne-editoriale.js` reconnaît désormais :
- comme institutions publiques : Santé publique France, l'ANSM, l'OMS et l'ECDC ;
- comme centres de recherche : le Pew Research Center et le Migration Policy Institute ;
- comme presse de référence : Associated Press, PolitiFact et CBS News.

**Fiches existantes adaptées aux deux publics (6).** Le champ `publics` a été ajouté via `scripts/publics-complements.js`, à partir du seul contenu sourcé de chaque fiche : `islamo-gauchisme-judeo-bolchevisme-comparaison`, `judeo-bolchevisme-histoire`, `melenchon-crie`, `melenchon-dangereux-democratie`, `resistance-communistes-etrangers`, `souverainete-industrielle-alimentaire-energetique`. Seules restent sans ce champ les 16 fiches « Science du dialogue » (`sci-…`), dont les affirmations sont des idées reçues sur la manière de discuter, pas des arguments d'extrême droite : leur ajouter des réponses à un électeur convaincu n'aurait pas de sens. C'est pourquoi 6 fiches seulement ont été adaptées, et non 10.

**Questions écartées pour sources invérifiables : aucune.** Les dossiers les plus minces :
- `rn-eurodeputes-travail` : repose surtout sur les données de Jordan Bardella, pas sur un classement complet des élus RN ; deux articles lus sur des copies tierces ;
- `polygamie-allocations-caf` : estimation ancienne (CNCDH, vers 2006) et règles CNAF de 1997 ;
- `terres-agricoles-chinois` : aucune part nationale des acheteurs étrangers trouvée ;
- `wokisme-universite` : quatre sources, dont une orientée et attribuée.

**Points non vérifiés, laissés hors des fiches et signalés dans leurs limites :**
- nombre de squats et d'évacuations administratives (aucune statistique officielle récente) ;
- taux d'avortement et de divorce en Russie (Rosstat) ;
- part des tuberculoses contractées avant ou après l'arrivée en France ;
- nombre d'étrangers en situation irrégulière à Mayotte ;
- chiffrage des recettes prévues par le NFP pour les retraites ;
- économies réellement réalisées sur les agences de l'État en 2026 ;
- état, après janvier 2026, de la proposition de loi sur les signes religieux dans le sport ;
- lien entre l'acheteur de l'Indre (HongYang) et le groupe Reward.

**Vérifications.** `npm test` : 471 tests, 471 réussis (après deux corrections : un fait de `lfi-retraite-60-ans` est désormais attribué explicitement à l'Institut Montaigne ; l'affirmation de `bac-donne-a-tous` ne contient plus « aujourd'hui », qui attirait la phrase hors sujet « Il fait beau aujourd'hui », et un concept `bac` a été ajouté). Tests de bout en bout : 38 sur 38.

## 11 novembre 2026 — passage de 20 h 13 (UTC)

**Questions testées : 35 candidates, 25 retenues.** Les phrases ont été choisies parmi les thèmes documentés par les vérificateurs de presse (AFP Factuel, Libération, PolitiFact, Full Fact, CORRECTIV), Conspiracy Watch, les rapports publics et les débats récents. Elles sont reformulées de façon générale. `node scripts/verifier-couverture.mjs` a donné, sur les 35 candidates, 5 « LACUNE » et 30 « COUVERTE ». Chaque phrase « COUVERTE » a été comparée à l'affirmation de la fiche trouvée.

Questions écartées parce qu'une fiche y répondait déjà vraiment :
- les OQTF jamais exécutées (`deboutes-asile-restent`, `expulser-tous-etrangers-condamnes`) ;
- les mineurs délinquants de plus en plus jeunes (`excuse-de-minorite`) ;
- la gauche qui aurait abandonné les ouvriers (`ouvriers-vote-rn`) ;
- l'appel d'air des régularisations (`lfi-regulariser-sans-papiers`, `migrants-mediterranee`) ;
- LFI et le Hamas (`lfi-antisemite`) ;
- les étrangers au RSA dès leur arrivée (`immigres-aides`, qui détaille la condition de cinq ans de séjour) ;
- les impôts de production (`impots-entreprises-europe`) ;
- LFI et la sortie de l'OTAN (`lfi-pro-poutine`, et `rn-sortie-otan` pour le RN).

Questions de réserve non retenues : la chasse que les écologistes voudraient interdire, le « plan Kalergi » (proche de `grand-remplacement`).

Les 20 questions retenues parmi les « COUVERTE » menaient à une fiche hors sujet. Exemples :
- les transports des sans-papiers et les réfugiés ukrainiens vers `immigres-aides` ;
- la CEDH vers `etranger-crime-plus-sa-place` ;
- les attaques au couteau, la déchéance de nationalité, les prénoms des agresseurs vers `delinquance-partout` ;
- les églises et la charia vers `musulmans-amalgames` ;
- Mitterrand et Jaurès vers `patriotisme-nationalisme` ;
- Soros et l'euro numérique vers `souverainete-populaire` ;
- l'arabe à l'école vers `musulmans-majoritaires-france`.

Questions retenues :
1. Les sans-papiers voyagent quasiment gratuitement dans les transports en Île-de-France.
2. Les réfugiés ukrainiens touchent plus d'aides que les Français.
3. On verse des allocations familiales pour des enfants restés au pays.
4. La Cour européenne des droits de l'homme empêche la France d'expulser.
5. Il faut déchoir de leur nationalité les binationaux délinquants.
6. Il y a des attaques au couteau tous les jours, c'est l'ensauvagement.
7. Il faut supprimer les allocations familiales aux parents de délinquants.
8. Les médias cachent les prénoms des agresseurs.
9. Partout en France, des églises sont transformées en mosquées.
10. Les musulmans placent la charia au-dessus des lois de la République.
11. Les communistes étaient alliés des nazis avec le pacte germano-soviétique.
12. Le nazisme était un mouvement de gauche, c'est écrit dans son nom : national-socialisme.
13. Mitterrand a fait monter le Front national pour diviser la droite.
14. Jaurès voterait aujourd'hui pour le Rassemblement national.
15. Mélenchon veut la créolisation de la France.
16. La dépense publique représente 57 % du PIB, c'est un record mondial.
17. La France va bientôt être mise sous tutelle du FMI.
18. Les fonctionnaires ne peuvent jamais être licenciés.
19. Avec le zéro artificialisation nette, on ne pourra plus construire de maisons individuelles.
20. Enseigner l'arabe à l'école, c'est favoriser l'islamisation.
21. L'Union européenne veut supprimer l'argent liquide avec l'euro numérique.
22. Avec le DSA, Bruxelles censure les réseaux sociaux.
23. Avec l'IVG dans la Constitution, on pourra avorter jusqu'à la naissance.
24. Le Great Reset de Davos veut nous déposséder de tout.
25. George Soros finance l'immigration en Europe.

**Fiches créées (25)** dans `scripts/fiches/quotidien_20261111_2013.py`, chacune avec le champ `publics` et une entrée dans `scripts/lectures-gauche.js` :

| Fiche | Verdict | Sources principales |
|---|---|---|
| `sans-papiers-transports-idf` | contredit | Île-de-France Mobilités (2026, deux pages) ; Conseil d'État (2019, lu via Landot & associés) ; Public Sénat (2018, deux articles) ; Banque des Territoires (2024) ; Le Courrier de l'Atlas (2019) |
| `refugies-ukrainiens-aides` | contredit | DREES (2025) ; Service-public.fr (2026) ; La finance pour tous (2026) ; Cnaf (2026) ; Cour des comptes (2023, via Maire-info) ; Assemblée nationale (2022) |
| `allocations-familiales-enfants-pays` | trompeur | Service-public.fr (2026) ; Assemblée nationale (2023) ; Cour de cassation (2011, via le CCME) ; Cleiss (2025-2026) ; Caf (2026) |
| `cedh-empeche-expulser` | trompeur | CEDH (statistiques des mesures provisoires 2023-2026, fiche pays France 2026) ; Public Sénat (2023, 2026) ; Le Club des juristes (2019, 2023) |
| `decheance-nationalite-binationaux` | opinion | Assemblée nationale (2023) ; Conseil constitutionnel (2015) ; Conseil d'État (2016) ; Présidence de la République (2016) ; Acteurs publics (2016) ; Public Sénat (2024) |
| `attaques-couteau-ensauvagement` | trompeur | Assemblée nationale (2020) ; Sénat (2022) ; ONDRP (2020) ; CESDIP ; Europe 1 (2020) ; La Libre Belgique (2020) ; The Connexion (2026) |
| `allocations-familiales-parents-delinquants` | opinion | Banque des Territoires (2011, 2013) ; Public Sénat (2023) ; LCP (2023) ; Assemblée nationale (2023, rapport n° 1698) |
| `prenoms-agresseurs-caches` | trompeur | Légifrance (code de la justice pénale des mineurs) ; Service-Public.fr (2021) ; RTBF (2018) ; France 24 (2026) ; Euronews (2026) ; Ined (2019) ; Puremédias (2016) |
| `eglises-transformees-mosquees` | trompeur | Europe 1 (2015) ; BuzzFeed News France (2016) ; The Irish Times (2015) ; Banque des Territoires (2016, 2024) ; Assemblée nationale (2019) |
| `musulmans-charia-sondage` | trompeur | Ifop (2025) ; The Conversation (2025, entretien avec des chercheurs du CNRS et de l'Ined) ; Mediapart (2025) ; Institut Montaigne (2016) ; Politis (2016) |
| `pacte-germano-sovietique-communistes` | trompeur | Encyclopédie multimédia de la Shoah, USHMM (2022) ; Universalis (G.-H. Soutou, J.-M. Guillon) ; Larousse ; Fondation Jean-Jaurès (2019) ; Fondation de la Résistance (2023) |
| `nazisme-gauche-socialisme` | contredit | Full Fact (2019) ; USHMM (2021, 2024, 2025) ; Encyclopaedia Britannica ; G. Bel, Economic History Review (2010) |
| `mitterrand-fn-proportionnelle` | trompeur | Vie publique ; Universalis ; Larousse (1987) ; Hérodote.net (2026) ; LCP-INA ; Fondation Jean-Jaurès (2018) |
| `jaures-recuperation-rn` | trompeur | Fondation Jean-Jaurès (2011, 2016, 2024) ; CNRS Le journal (2014) ; Assemblée nationale ; Politis (2009) |
| `creolisation-melenchon` | trompeur | Reporterre (2021) ; Slate (2021) ; Puremédias (2025) ; Acta fabula (2025) ; AFP (2026) ; Fondation Jean-Jaurès (2018) |
| `depense-publique-57-pib` | plutôt exact | Insee (2026) ; Eurostat (2026) ; Banque de France (2025) ; FIPECO (2022) ; Acteurs publics d'après l'OCDE (2017) |
| `fmi-tutelle-france` | trompeur | Reuters (2025) ; Banque de France (2025) ; IRIS (2025) ; FMI (2026) ; Cour des comptes (2026, via Public Sénat) ; Agence France Trésor (2026) ; Insee (2026) |
| `fonctionnaires-licenciement` | contredit | Service-Public.fr (2026) ; DGAFP (2024) ; collectivites-locales.gouv.fr (2025) ; Acteurs publics (2025) ; Insee et DGAFP (2026) ; AP-HP (2019) |
| `zan-maisons-individuelles` | contredit | Banque des Territoires (2021, 2025, 2026, données du Cerema) ; Public Sénat (2023, 2026) ; Maire-info (2025) ; Weka (2026) ; L'info durable (2024) |
| `arabe-ecole-islamisation` | contredit | Assemblée nationale (2019, 2022) ; Institut Montaigne (2018) ; Public Sénat (2018) ; Libération (2017, 2020) ; Banque des Territoires (2020) |
| `euro-numerique-especes` | contredit | Commission européenne (2023) ; Eunews (2025) ; Parlement européen (2026, deux communiqués) ; AFP (2025) ; CNIL (2023) |
| `dsa-censure-bruxelles` | trompeur | Règlement (UE) 2022/2065 ; Commission européenne (2025, 2026) ; Observatoire européen de l'audiovisuel (2025) ; Le Club des juristes (2025) ; Euronews (2025) |
| `ivg-constitution-naissance` | contredit | Journal officiel (2024, via Landot & associés) ; LCP (2024) ; Le Club des juristes (2024) ; Le Quotidien du médecin (2022) ; DREES (2025, 2026 via VIDAL) ; Agence de la biomédecine (2025) |
| `great-reset-davos` | contredit | PolitiFact (2023) ; CORRECTIV (2023) ; Conspiracy Watch (2021) ; Associated Press (2023) ; Fondation Rosa-Luxemburg (2021) ; Public Sénat / Oxfam (2026) |
| `soros-immigration` | trompeur | Open Society Foundations (2018) ; Bloomberg Opinion (2018) ; AFP (2017) ; CJUE (2021) ; J. Richardson et R. Wodak (2022) ; ADL (2018) |

**Méthode.** Cinq agents documentalistes ont fait la recherche, chacun sur cinq questions. Chacun cherchait avec WebSearch puis lisait chaque page avec WebFetch. Seules les pages effectivement lues sont citées, et les chiffres viennent des passages lus. Chaque fiche contient au moins un fait défavorable ou une limite honnête, par exemple :
- l'ancienne réduction de 75 % accordée aux bénéficiaires de l'AME et son coût en 2015 ;
- les exceptions européennes et bilatérales aux allocations pour des enfants vivant à l'étranger ;
- les condamnations de la France pour des renvois vers la Russie ;
- les cas réels d'églises devenues mosquées (Graulhet, Lille, Nantes) ;
- les chiffres Ifop défavorables ;
- l'attitude du PCF en 1939-1941 ;
- la phrase de Jaurès sur la main-d'œuvre étrangère ;
- la France parmi les pays qui dépensent le plus ;
- la hausse de la charge de la dette ;
- le très petit nombre de licenciements pour insuffisance ;
- le poids de l'habitat dans l'artificialisation ;
- les anciens cours ELCO jugés « vecteur de séparatisme » ;
- les vraies questions de vie privée de l'euro numérique ;
- les critiques du DSA ;
- les IMG tardives ;
- le financement réel d'ONG d'aide aux migrants par l'OSF.

Les sources orientées ne servent qu'avec attribution explicite :
- Institut Montaigne, IRIS, Fondation Jean-Jaurès, Fondation Rosa-Luxemburg ;
- Politis, Mediapart, ADL, Oxfam ;
- Europe 1 (un fait reformulé en « Selon Europe 1 » pour respecter la politique documentaire).

**Ajustements.**
- Deux valeurs de fiabilité proposées par les agents, « debattu » et « probable », ont été ramenées aux valeurs reconnues par l'application (« debat », « interpretation »).
- Les affirmations de deux fiches ont été reformulées sans le mot « délinquants », qui faisait passer ces fiches avant `delinquance-partout` dans la recherche par mot-clé : `decheance-nationalite-binationaux` (« … les binationaux qui commettent des crimes ») et `allocations-familiales-parents-delinquants` (« … aux parents des mineurs qui commettent des délits »). Les questions d'origine mènent toujours à ces fiches.

Pages non ouvertes, donc non citées :
- Vie publique (JavaScript requis ou erreur serveur, plusieurs pages) ;
- Légifrance pour le code civil et le code de la sécurité sociale (erreur), EUR-Lex ;
- pages Interstats du ministère de l'Intérieur ;
- info.gouv.fr ;
- la page de la représentation de la Commission « Non, le DSA ne vise pas à censurer » ;
- pages TeO2 de l'Ined ;
- La Gazette des communes, The Conversation sur le ZAN ;
- Le Temps, Slate (plusieurs articles), un article HAL (protection anti-robots).

**Reconnaissance des questions.**
- Après génération, 6 des 25 questions menaient déjà à leur fiche.
- `public/js/cartographie.js` reçoit 25 concepts : `transports_idf`, `ukrainiens_aides`, `af_etranger`, `cedh`, `decheance`, `couteau`, `af_delinquants`, `prenoms`, `eglises_mosquees`, `charia_lois`, `pacte_gs`, `nazisme_gauche`, `mitterrand_fn`, `jaures`, `creolisation`, `depense_publique`, `fmi`, `fonct_licenciement`, `zan`, `arabe_ecole`, `euro_numerique`, `dsa`, `ivg_naissance`, `great_reset`, `soros`.
- Il reçoit aussi 32 arguments placés en tête : un par fiche, et des variantes à deux ou trois concepts (immigration, prestations, AME, islam, gauche) pour l'emporter sur les arguments généraux `immigres-aides`, `ame`, `musulmans_nombre` et `gauche_bilan`.
- Comparaison avant/après sur 493 phrases de contrôle (affirmations de la bibliothèque, questions citées dans ce journal) : seules les questions visées changent de fiche. S'y ajoutent trois phrases témoins qui passent en « LACUNE », ce qui est correct : « Il fait beau aujourd'hui », « aujourd'hui » et « ne peuvent jamais être licenciés ».
- 24 variantes familières vérifiées, dont :
  - « Les bénéficiaires de l'AME ont le Navigo presque gratuit » ;
  - « La CAF paie les allocs pour des gosses qui vivent au bled » ;
  - « 120 agressions au couteau par jour en France ! » ;
  - « Hitler était socialiste » ;
  - « C'est Mitterrand qui a créé Le Pen avec la proportionnelle » ;
  - « Le ZAN va empêcher nos enfants d'avoir une maison » ;
  - « Bientôt le cash sera interdit par Bruxelles » ;
  - « Maintenant on peut avorter à 9 mois » ;
  - « Davos veut qu'on ne possède rien » ;
  - « Soros paie les ONG qui font venir les migrants ».
- Une variante reste mal orientée : « Staline et Hitler étaient alliés, les communistes ont collaboré » mène à `programme-irrealisable`. Ses deux moitiés, testées séparément, mènent bien à `pacte-germano-sovietique-communistes`.

**Fiches existantes adaptées aux deux publics : aucune.** Toutes les fiches ont déjà le champ `publics`, sauf les 16 fiches « Science du dialogue » (`sci-…`). Comme indiqué au passage précédent, ces fiches portent sur la manière de discuter, pas sur des arguments d'extrême droite.

**Questions écartées pour sources invérifiables : aucune.** Les dossiers les plus minces :
- `attaques-couteau-ensauvagement` : aucune statistique nationale récente sur les armes blanches n'a pu être lue (pages du ministère bloquées) ; le chiffre des « 120 par jour » vient d'une estimation de l'ONDRP pour 2015-2017 ;
- `musulmans-charia-sondage` : le chiffre de 2016 (29 %) n'est connu que par Politis ; Mediapart a été lu dans une republication ;
- `mitterrand-fn-proportionnelle` : l'invitation de Le Pen à L'Heure de vérité « à la demande » de Mitterrand ne repose que sur Hérodote.net, signalée comme probable ;
- `zan-maisons-individuelles` : l'état de la loi « Trace » après avril 2026 n'a pas pu être confirmé ;
- `fmi-tutelle-france` : la déclaration de l'économiste en chef du FMI n'est connue qu'à travers la tribune de l'IRIS.

**Points non vérifiés, laissés hors des fiches et signalés dans leurs limites :**
- nombre actuel de bénéficiaires de la réduction AME et son coût ;
- accès des déplacés ukrainiens à la prime d'activité (sources contradictoires) ;
- montant total des allocations versées pour des enfants vivant à l'étranger ;
- déchéances de nationalité après 2022 et motif exact de la censure de 2024 ;
- part des homicides commis à l'arme blanche ;
- nombre de révocations de fonctionnaires ;
- nombre d'élèves apprenant l'arabe après 2020 ;
- plafond de détention de l'euro numérique (négociations en cours) ;
- lettre de Mitterrand à Le Pen en 1982 ;
- citations de Jaurès utilisées par le RN.

## 11 novembre 2026 — jauge de soutien Tipeee (demande du propriétaire)

- Ajout d'une jauge discrète sous l'en-tête, à droite. Sur ordinateur, elle affiche « Merci ! Vous nous soutenez à hauteur de 45 € / mois · objectif 1 000 € », avec une petite barre qui se remplit et le montant qui défile au chargement. Sur mobile, elle affiche « 45 € / 1 000 € ». L'ensemble est un lien « Nous soutenir » vers Tipeee, qui s'ouvre dans un nouvel onglet. L'animation est désactivée si l'utilisateur a demandé à réduire les animations.
- Les chiffres sont dans `public/js/soutien.js`. Ils sont relevés sur l'API publique de Tipeee (`parameters.tipperAmount` = 45, campagne « par mois » ; `parameters.tipperNumber` = 11) et mis à jour à chaque passage quotidien. Le site ne contacte jamais Tipeee : la politique « zéro site tiers » est inchangée.
- Tests : nouveau `tests/unit/soutien.test.js`. Le test de bout en bout des liens Tipeee compte désormais trois liens sur l'accueil (accueil, jauge, pied de page) et vérifie la jauge.
