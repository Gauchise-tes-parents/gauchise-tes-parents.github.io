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
