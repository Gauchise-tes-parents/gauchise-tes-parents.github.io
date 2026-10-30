# Tests de compréhension — moteur d'analyse argumentative (v8)

Rapport produit par `npm run rapport:comprehension` le 2026-10-30 : chaque phrase est réellement analysée ; rien n'est recopié à la main.

## Résultats

- **180 phrases** testées, dont 32 du lot de validation (écrites après les réglages).
- **Nouveau moteur : 180/180 réussies** (argument principal, fiche, arguments secondaires, fiches à exclure, émotions et procédés attendus).
- Ancienne correspondance par mots (v7), sur la bibliothèque v7 : 87/180 phrases avec la bonne fiche (ou l'absence de fiche quand aucune ne répond).
- Ancienne correspondance par mots, sur la bibliothèque actuelle (avec les fiches emploi ajoutées en v8) : 109/180.

Critère « ancien moteur » : la première fiche proposée est l'une des fiches attendues ; quand aucune fiche ne répond, il est compté juste seulement s'il ne propose rien. L'ancien moteur ne repérait ni arguments secondaires, ni émotions, ni procédés : ces critères ne lui sont pas appliqués.

| Catégorie | Phrases | Réussies |
|---|---:|---:|
| obligatoire | 16 | 16 |
| familier | 11 | 11 |
| simple | 51 | 51 |
| fautes | 3 | 3 |
| causalite | 9 | 9 |
| insinuation | 8 | 8 |
| emotionnel | 18 | 18 |
| multi | 14 | 14 |
| generalisation | 11 | 11 |
| provocation | 4 | 4 |
| chiffre | 5 | 5 |
| amalgame | 3 | 3 |
| question | 2 | 2 |
| peur | 2 | 2 |
| histoire | 5 | 5 |
| rebond | 2 | 2 |
| changement | 3 | 3 |
| preuve | 3 | 3 |
| autorite | 1 | 1 |
| anecdote | 2 | 2 |
| faux_dilemme | 1 | 1 |
| hors_sujet | 4 | 4 |
| nuance | 1 | 1 |
| nostalgie | 1 | 1 |

## Cartographie

- 38 concepts, 428 mots-clés, expressions, synonymes et fautes fréquentes ;
- 37 arguments reliés aux fiches qui y répondent (dont 6 sans fiche, signalés comme lacunes) ;
- 9 émotions, 12 procédés argumentatifs.

## Démonstration : « Plus il y a d’immigrés, moins il y a de travail pour les Français. »

**Avant (v7)** : la correspondance par mots proposait `immigres-aides` (forte, score 7), `france-plus-sure-moins-immigres` (partielle, score 6), `criminels-etrangers-proteges-justice` (partielle, score 5). Les mots « immigrés » et « Français » suffisaient à faire remonter la fiche sur les aides sociales, qui ne parle pas d'emploi.

**Après (v8)** :
1. Concepts repérés : Immigration (« immigres ») ; Emploi et marché du travail (« travail »).
2. Lien de cause affirmé : Immigration → Emploi et marché du travail (« plus… moins »).
3. Argument : **Immigration et concurrence sur le marché du travail** — sous-entendu : Le nombre d’emplois serait fixe : chaque emploi occupé par un immigré serait retiré à un Français.
4. Fiche retenue : `immigration-emploi` (« Les immigrés prennent le travail des Français. »).
5. Fiches écartées :
   - `immigres-aides` : elle traite de : prestations sociales, coût et finances publiques, pas de : emploi et marché du travail.
   - `rsa-smic` : elle traite de : salaires, prestations sociales, pas de : immigration.
   - `rsa-profiteurs` : elle traite de : prestations sociales, pas de : immigration, emploi et marché du travail.
   - `chomeurs-travailler` : elle traite de : prestations sociales, effort et valeur travail, pas de : immigration.
   - `impots-assistanat` : elle traite de : prestations sociales, fiscalité, pas de : immigration, emploi et marché du travail.
6. Procédé possible : Corrélation présentée comme une cause ; question : « Comment sait-on que c’est la cause, et pas autre chose qui arrive en même temps ? »
7. Phrase marquante (mode « gagner ») : « Le travail n’est pas un gâteau fixe : si chaque immigré « prenait » un emploi, il n’y aurait jamais eu de création d’emplois en France. »

## Erreurs corrigées par rapport à la v7 (93)

| Phrase | Avant (v7) | Après (v8) |
|---|---|---|
| Les immigrés prennent le travail des Français. | immigres-aides | Immigration et concurrence sur le marché du travail → immigration-emploi |
| On n’a plus de travail mais on continue à faire venir des étrangers. | immigres-aides | Immigration et concurrence sur le marché du travail → immigration-emploi |
| On ne peut plus se loger à cause de l’immigration. | statistiques-prouvent-insecurite-immigration | Immigration et logement → lacune reconnue |
| Les Français passent après tout le monde. | criminels-etrangers-proteges-justice | Sentiment que les Français passent après → immigres-aides |
| On ne peut plus rien dire sur l’islam. | gauche-laicite-debats | Islam et liberté d’expression → lacune reconnue |
| Les patrons préfèrent les immigrés parce qu’ils les paient moins. | france-plus-sure-moins-immigres | Immigration et salaires → immigration-salaires |
| Il y a du chômage, mais les entreprises disent qu’elles ne trouvent personne. | aucune fiche | Chômage et difficultés de recrutement → chomage-penurie-recrutement |
| Les étrangers ont droit à tout alors que les Français n’ont rien. | perte-automatique-droit-sejour | Immigration et prestations sociales → immigres-aides |
| On travaille toute sa vie et on n’arrive même plus à payer ses factures. | front-populaire-1936 | Pouvoir d’achat et revenus du travail → dividendes-salaires |
| La France était mieux avant. | judeo-bolchevisme-histoire | Nostalgie du passé → lacune reconnue |
| Plus il y a d’immigrés, moins il y a de travail pour les Français. | immigres-aides | Immigration et concurrence sur le marché du travail → immigration-emploi |
| Ils viennent piquer nos boulots. | aucune fiche | Immigration et concurrence sur le marché du travail → immigration-emploi |
| Les migrants volent les emplois des gens d’ici. | aucune fiche | Immigration et concurrence sur le marché du travail → immigration-emploi |
| A cause des immigres y a plus de taf pour nous | delinquance-principalement-immigration | Immigration et concurrence sur le marché du travail → immigration-emploi |
| Chaque étranger qui arrive, c’est un chômeur français de plus. | criminels-etrangers-proteges-justice | Immigration et concurrence sur le marché du travail → immigration-emploi |
| L’immigration augmente le chômage. | statistiques-prouvent-insecurite-immigration | Immigration et concurrence sur le marché du travail → immigration-emploi |
| Pourquoi faire venir des étrangers alors qu’il y a des millions de chômeurs ? | etranger-crime-plus-sa-place | Immigration et concurrence sur le marché du travail → immigration-emploi |
| Les immigrés font baisser les salaires. | expulser-reduit-criminalite | Immigration et salaires → immigration-salaires |
| Avec tous ces sans-papiers qui bossent au noir, les salaires stagnent. | aucune fiche | Immigration et salaires → immigration-salaires |
| Les patrons font venir de la main-d’œuvre étrangère pour casser les salaires. | resistance-communistes-etrangers | Immigration et salaires → immigration-salaires |
| Les entreprises embauchent des étrangers parce qu’ils coûtent moins cher. | france-plus-sure-moins-immigres | Immigration et salaires → immigration-salaires ; Immigration et concurrence sur le marché du travail → immigration-emploi |
| Les entreprises ne trouvent personne, donc il faut des immigrés. | perte-automatique-droit-sejour | Chômage et difficultés de recrutement → chomage-penurie-recrutement |
| Il y a des métiers en tension mais personne ne veut les faire. | aucune fiche | Chômage et difficultés de recrutement → chomage-penurie-recrutement |
| Les postes vacants, c’est parce que les chômeurs ne veulent pas bosser. | aucune fiche | Chômage et difficultés de recrutement → chomage-penurie-recrutement ; Les Français ne voudraient plus travailler → chomeurs-travailler |
| Les immigrés travaillent pour rien et nous on se retrouve au chômage. | chomeurs-travailler | Immigration et salaires → immigration-emploi |
| Il faut réserver les emplois aux Français. | souverainete-industrielle-alimentaire-energetique | Sentiment que les Français passent après → immigration-emploi |
| Les étrangers vivent des allocs. | agriculteurs-revenus | Immigration et prestations sociales → immigres-aides |
| La CAF donne tout aux étrangers. | criminels-etrangers-proteges-justice | Immigration et prestations sociales → immigres-aides |
| L’immigration nous coûte une fortune. | delinquance-principalement-immigration | Coût de l’immigration pour les finances publiques → immigres-aides |
| On paie des impôts pour les immigrés. | delinquance-principalement-immigration | Coût de l’immigration pour les finances publiques → immigres-aides |
| Les immigres coute plus qu’ils rapportent | delinquance-principalement-immigration | Coût de l’immigration pour les finances publiques → immigres-aides |
| Un étranger qui arrive a droit à la CMU et aux APL tout de suite. | perte-automatique-droit-sejour | Immigration et prestations sociales → immigres-aides |
| On se sent étrangers dans notre propre pays, les autres passent avant nous. | electricite-nucleaire-renouvelables | Identité et sentiment de dépossession → immigration-chiffres-definitions ; Sentiment que les Français passent après → immigres-aides |
| C’est toujours les mêmes qui profitent pendant que les Français trinquent. | dividendes-salaires | Sentiment que les Français passent après → immigres-aides |
| Les étrangers, c’est eux qui font les agressions. | expulser-tous-etrangers-condamnes | Immigration et délinquance → delinquance-principalement-immigration |
| Les étrangers sortent de prison et on les laisse rester en France. | etranger-crime-plus-sa-place | Étrangers, immigrés et population carcérale → etrangers-prisons ; Exécution des mesures d’éloignement → expulser-tous-etrangers-condamnes |
| On ne peut plus sortir le soir tranquille. | aucune fiche | Insécurité et justice → delinquance-partout |
| Les immigrés prennent le travail des Français et en plus ils viennent toucher le RSA. | immigres-aides | Immigration et concurrence sur le marché du travail → immigration-emploi ; Immigration et prestations sociales → immigres-aides |
| Ils prennent nos emplois, nos logements et nos aides. | pauvrete-france | Immigration et concurrence sur le marché du travail → immigration-emploi ; Immigration et prestations sociales → immigres-aides ; Immigration et logement → lacune reconnue |
| Les immigrés font baisser les salaires et remplissent les prisons. | immigres-prisons-surrepresentation | Immigration et salaires → immigration-salaires ; Étrangers, immigrés et population carcérale → immigres-prisons-surrepresentation |
| Les riches ne paient pas d’impôts et les pauvres paient pour tout. | aucune fiche | Fiscalité, riches et entreprises → dividendes-salaires ; Impôts → impots-assistanat ; Pauvreté → pauvrete-france |
| On ne peut plus se loger, on ne trouve plus de travail et on voit des aides distribuées partout. Pendant ce temps, les immigrés arrivent encore. | immigres-aides | Immigration et logement → lacune reconnue ; Immigration et concurrence sur le marché du travail → immigration-emploi ; Immigration et prestations sociales → immigres-aides |
| Les HLM c’est que pour les étrangers. | criminels-etrangers-proteges-justice | Immigration et logement → lacune reconnue |
| Il y a de plus en plus d’immigrés en France. | france-plus-sure-moins-immigres | Immigration et démographie → immigration-chiffres-definitions |
| On perd notre identité. | electricite-nucleaire-renouvelables | Identité et sentiment de dépossession → patriotisme-nationalisme |
| Les gauchistes n’aiment pas leur pays. | programme-cnr-1944 | La gauche et la patrie → gauche-nation-debats |
| La gauche a honte du drapeau. | gauche-assistes-travailleurs | La gauche et la patrie → gauche-nation-debats |
| Il faut rendre la France aux Français. | criminels-etrangers-proteges-justice | Sentiment que les Français passent après → immigres-aides |
| Avant on était fiers d’être Français. | commune-paris-1871 | La gauche et la patrie → patriotisme-nationalisme |
| C’était mieux de mon temps. | commune-paris-1871 | Nostalgie du passé → lacune reconnue |
| Le voile est contraire à la laïcité. | lfi-communautarisme | Islam et musulmans → laicite-loi-1905 ; Laïcité → gauche-laicite-debats |
| On n’a plus le droit de critiquer l’islam sans être traité de raciste. | gauche-laicite-debats | Islam et liberté d’expression → lacune reconnue |
| On ne peut plus rien dire en France. | etranger-crime-plus-sa-place | Liberté d’expression → lacune reconnue |
| Avec la bien-pensance, on ne peut plus rien dire. | securite-sociale-1945 | Liberté d’expression → lacune reconnue |
| Les Insoumis détestent la police. | melenchon-dangereux-democratie | Critiques visant Jean-Luc Mélenchon → lfi-contre-police |
| Si Mélenchon passe, la France est ruinée. | melenchon-change-avis | Critiques visant Jean-Luc Mélenchon → melenchon-ruiner-france |
| Les gens préfèrent rester au RSA plutôt que de bosser. | gauche-assistes-travailleurs | Assistanat et aides sociales → rsa-profiteurs |
| Le RSA, c’est mieux payé que le SMIC. | gauche-assistes-travailleurs | Assistanat et aides sociales → rsa-smic |
| Si on taxe les riches, ils vont tous partir. | aucune fiche | Fiscalité, riches et entreprises → melenchon-ruiner-france ; Impôts → impots-assistanat |
| Les fins de mois sont de plus en plus dures. | aucune fiche | Pouvoir d’achat et revenus du travail → dividendes-salaires |
| L’Europe nous impose tout. | melenchon-change-avis | Europe et souveraineté → souverainete-populaire |
| Les médias sont tous de gauche. | gauche-nation-debats | Défiance envers les médias → medias-concentration |
| Les politiques sont tous pourris. | musulmans-amalgames | Défiance envers les élus → lacune reconnue |
| Tous corrompus, droite comme gauche. | islamo-gauchisme-origine-usages | Défiance envers les élus → lacune reconnue |
| Et l’immigration alors, ça coûte une fortune. | delinquance-principalement-immigration | Coût de l’immigration pour les finances publiques → immigres-aides |
| Prouve-moi que les immigrés ne prennent pas le travail des Français. | immigres-aides | Immigration et concurrence sur le marché du travail → immigration-emploi |
| Soit on ferme les frontières, soit la France disparaît. | pauvrete-france | Identité et sentiment de dépossession → immigration-chiffres-definitions |
| J’en ai marre, on bosse comme des chiens et on n’a rien. | aucune fiche | Pouvoir d’achat et revenus du travail → dividendes-salaires |
| Personne ne nous écoute, les politiques s’en fichent de nous. | musulmans-amalgames |  |
| Ça me rend fou de voir qu’on aide tout le monde sauf nous. | aucune fiche | Sentiment que les Français passent après → immigres-aides |
| Les impôts locaux ont augmenté dans ma commune. | programme-irrealisable | Impôts → impots-assistanat |
| Le foot c’était mieux avant. | commune-paris-1871 | Nostalgie du passé → lacune reconnue |
| Les immigrés italiens des années 50 se sont bien intégrés. | france-plus-sure-moins-immigres | Argument sur : immigration → lacune reconnue |
| Les clandestins prennent les boulots dans le bâtiment. | aucune fiche | Immigration et concurrence sur le marché du travail → immigration-emploi |
| Les réfugiés ont tout gratuit : logement, santé, argent. | impots-assistanat | Immigration et prestations sociales → immigres-aides ; Immigration et logement → lacune reconnue |
| Ces gens-là viennent juste pour les allocations. | aucune fiche | Immigration et prestations sociales → immigres-aides |
| Le travail au noir des sans-papiers tire tout le monde vers le bas. | rsa-profiteurs | Immigration et salaires → immigration-salaires ; Immigration et concurrence sur le marché du travail → immigration-emploi |
| Ça sert à quoi de former des chômeurs si on fait venir des étrangers ? | aucune fiche | Immigration et concurrence sur le marché du travail → immigration-emploi |
| Les immigrés ne veulent pas s’intégrer. | delinquance-principalement-immigration | Argument sur : immigration → lacune reconnue |
| Les délinquants étrangers ne sont jamais expulsés. | expulser-reduit-criminalite | Exécution des mesures d’éloignement → expulser-tous-etrangers-condamnes |
| L’insécurité a explosé depuis qu’il y a des migrants dans la ville. | aucune fiche | Immigration et délinquance → delinquance-principalement-immigration |
| Les Français d’abord ! | criminels-etrangers-proteges-justice | Sentiment que les Français passent après → immigres-aides |
| Les musulmans veulent imposer la charia. | lfi-communautarisme | Islam et musulmans → musulmans-amalgames |
| Mélenchon soutient les islamistes. | lfi-antisemite | Accusation d’islamo-gauchisme → islamo-gauchisme-origine-usages ; Critiques visant Jean-Luc Mélenchon → melenchon-crie |
| Les riches créent les emplois, il faut les laisser tranquilles. | aucune fiche | Fiscalité, riches et entreprises → dividendes-salaires |
| Tous les élus se servent dans la caisse. | electricite-nucleaire-renouvelables |  |
| Avant, au moins, il y avait du respect. | france-plus-sure-moins-immigres | Nostalgie du passé → lacune reconnue |
| Bruxelles décide de tout à notre place. | aucune fiche | Europe et souveraineté → souverainete-populaire |
| Le nucléaire, c’est l’avenir, les écolos sont des idiots. | aucune fiche | Écologie → electricite-nucleaire-renouvelables |
| Pétain a sauvé la France. | chomeurs-travailler | Histoire de l’extrême droite → judeo-bolchevisme-histoire |
| J’ai l’impression que plus personne ne nous écoute. | justice-laxiste-prison |  |
| Et alors ? Les immigrés font quand même baisser les salaires. | expulser-reduit-criminalite | Immigration et salaires → immigration-salaires |
| Prouve-moi que l’immigration ne coûte rien. | statistiques-prouvent-insecurite-immigration | Coût de l’immigration pour les finances publiques → immigres-aides |

## Détail des 180 phrases

| Phrase | Catégorie | Arguments repérés | Concepts | Fiches retenues | Fiches écartées | Ancienne fiche (v7) | Résultat |
|---|---|---|---|---|---|---|---|
| Les immigrés prennent le travail des Français. | obligatoire | Immigration et concurrence sur le marché du travail | Immigration, Emploi et marché du travail | immigration-emploi | immigres-aides, rsa-smic, rsa-profiteurs, chomeurs-travailler, impots-assistanat | immigres-aides | réussi |
| Les immigrés touchent plus d’aides que nous. | obligatoire | Immigration et prestations sociales | Immigration, Prestations sociales | immigres-aides | immigration-emploi, rsa-smic | immigres-aides | réussi |
| On n’a plus de travail mais on continue à faire venir des étrangers. | obligatoire | Immigration et concurrence sur le marché du travail | Immigration, Emploi et marché du travail | immigration-emploi | immigres-aides, rsa-smic, rsa-profiteurs, chomeurs-travailler, impots-assistanat | immigres-aides | réussi |
| Les étrangers remplissent les prisons et on les laisse ressortir. | obligatoire | Étrangers, immigrés et population carcérale | Immigration, Prisons | etrangers-prisons | justice-laxiste-prison | etrangers-prisons | réussi |
| Il faut renvoyer tous les criminels chez eux. | obligatoire | Expulsion des étrangers condamnés | Délinquance et insécurité, Expulsion et éloignement | renvoyer-tous-deja-condamnes | — | renvoyer-tous-deja-condamnes | réussi |
| On ne peut plus se loger à cause de l’immigration. | obligatoire | Immigration et logement | Immigration, Logement | lacune reconnue | immigres-aides, statistiques-prouvent-insecurite-immigration | statistiques-prouvent-insecurite-immigration | réussi |
| Les Français passent après tout le monde. | obligatoire | Sentiment que les Français passent après | Priorité nationale | immigres-aides | criminels-etrangers-proteges-justice | criminels-etrangers-proteges-justice | réussi |
| On ne peut plus rien dire sur l’islam. | obligatoire | Islam et liberté d’expression | Islam et religion, Liberté d’expression | lacune reconnue | islamo-gauchisme-origine-usages, gauche-laicite-debats | gauche-laicite-debats | réussi |
| Mélenchon crie tout le temps, il est dangereux. | obligatoire | Critiques visant Jean-Luc Mélenchon ; Critiques visant Jean-Luc Mélenchon | Mélenchon et LFI, La gauche, Disqualification d’une personnalité | melenchon-crie ; melenchon-dangereux-democratie | — | melenchon-crie | réussi |
| La gauche déteste la France. | obligatoire | La gauche et la patrie | Patriotisme et nation, La gauche | gauche-nation-debats | — | gauche-nation-debats | réussi |
| Les patrons préfèrent les immigrés parce qu’ils les paient moins. | obligatoire | Immigration et salaires | Immigration, Salaires, Riches, entreprises et patronat | immigration-salaires | immigres-aides, rsa-smic, chomeurs-travailler | france-plus-sure-moins-immigres | réussi |
| Il y a du chômage, mais les entreprises disent qu’elles ne trouvent personne. | obligatoire | Chômage et difficultés de recrutement | Emploi et marché du travail, Pénurie et difficultés de recrutement, Riches, entreprises et patronat | chomage-penurie-recrutement | chomeurs-travailler, rsa-smic | aucune | réussi |
| Les étrangers ont droit à tout alors que les Français n’ont rien. | obligatoire | Immigration et prestations sociales | Immigration, Prestations sociales, Priorité nationale | immigres-aides | immigration-emploi, rsa-smic, perte-automatique-droit-sejour | perte-automatique-droit-sejour | réussi |
| On travaille toute sa vie et on n’arrive même plus à payer ses factures. | obligatoire | Pouvoir d’achat et revenus du travail | Pouvoir d’achat, Effort et valeur travail | dividendes-salaires | front-populaire-1936 | front-populaire-1936 | réussi |
| La France était mieux avant. | obligatoire | Nostalgie du passé | Nostalgie | lacune reconnue | judeo-bolchevisme-histoire | judeo-bolchevisme-histoire | réussi |
| Plus il y a d’immigrés, moins il y a de travail pour les Français. | obligatoire | Immigration et concurrence sur le marché du travail | Immigration, Emploi et marché du travail | immigration-emploi | immigres-aides, rsa-smic, rsa-profiteurs, chomeurs-travailler, impots-assistanat | immigres-aides | réussi |
| Ils viennent piquer nos boulots. | familier | Immigration et concurrence sur le marché du travail | Immigration, Emploi et marché du travail | immigration-emploi | immigres-aides, rsa-smic, rsa-profiteurs, chomeurs-travailler, impots-assistanat | aucune | réussi |
| Les migrants volent les emplois des gens d’ici. | simple | Immigration et concurrence sur le marché du travail | Immigration, Emploi et marché du travail | immigration-emploi | immigres-aides, rsa-smic, rsa-profiteurs, chomeurs-travailler, impots-assistanat | aucune | réussi |
| A cause des immigres y a plus de taf pour nous | fautes | Immigration et concurrence sur le marché du travail | Immigration, Emploi et marché du travail | immigration-emploi | immigres-aides, rsa-smic, rsa-profiteurs, chomeurs-travailler, impots-assistanat, delinquance-principalement-immigration | delinquance-principalement-immigration | réussi |
| Chaque étranger qui arrive, c’est un chômeur français de plus. | causalite | Immigration et concurrence sur le marché du travail | Immigration, Emploi et marché du travail | immigration-emploi | immigres-aides, rsa-smic, rsa-profiteurs, chomeurs-travailler, impots-assistanat | criminels-etrangers-proteges-justice | réussi |
| L’immigration augmente le chômage. | causalite | Immigration et concurrence sur le marché du travail | Immigration, Emploi et marché du travail | immigration-emploi | immigres-aides, rsa-smic, rsa-profiteurs, chomeurs-travailler, impots-assistanat, statistiques-prouvent-insecurite-immigration | statistiques-prouvent-insecurite-immigration | réussi |
| Pourquoi faire venir des étrangers alors qu’il y a des millions de chômeurs ? | insinuation | Immigration et concurrence sur le marché du travail | Immigration, Emploi et marché du travail | immigration-emploi | immigres-aides, rsa-smic, rsa-profiteurs, chomeurs-travailler, impots-assistanat | etranger-crime-plus-sa-place | réussi |
| Les immigrés font baisser les salaires. | simple | Immigration et salaires | Immigration, Salaires | immigration-salaires | immigres-aides, rsa-smic, chomeurs-travailler | expulser-reduit-criminalite | réussi |
| Avec tous ces sans-papiers qui bossent au noir, les salaires stagnent. | causalite | Immigration et salaires | Immigration, Origine supposée, Salaires | immigration-salaires | immigres-aides, rsa-smic, chomeurs-travailler | aucune | réussi |
| Les patrons font venir de la main-d’œuvre étrangère pour casser les salaires. | simple | Immigration et salaires | Immigration, Salaires, Riches, entreprises et patronat | immigration-salaires | immigres-aides, rsa-smic, chomeurs-travailler | resistance-communistes-etrangers | réussi |
| Les entreprises embauchent des étrangers parce qu’ils coûtent moins cher. | insinuation | Immigration et salaires ; Immigration et concurrence sur le marché du travail | Immigration, Emploi et marché du travail, Salaires, Riches, entreprises et patronat, Coût et finances publiques | immigration-salaires ; immigration-emploi | immigres-aides, rsa-smic, chomeurs-travailler | france-plus-sure-moins-immigres | réussi |
| Les entreprises ne trouvent personne, donc il faut des immigrés. | simple | Chômage et difficultés de recrutement | Immigration, Pénurie et difficultés de recrutement, Riches, entreprises et patronat | chomage-penurie-recrutement | chomeurs-travailler, rsa-smic | perte-automatique-droit-sejour | réussi |
| Il y a des métiers en tension mais personne ne veut les faire. | simple | Chômage et difficultés de recrutement | Emploi et marché du travail, Pénurie et difficultés de recrutement | chomage-penurie-recrutement | chomeurs-travailler, rsa-smic | aucune | réussi |
| Les postes vacants, c’est parce que les chômeurs ne veulent pas bosser. | causalite | Chômage et difficultés de recrutement ; Les Français ne voudraient plus travailler | Emploi et marché du travail, Pénurie et difficultés de recrutement, Effort et valeur travail | chomage-penurie-recrutement ; chomeurs-travailler | rsa-smic | aucune | réussi |
| Les immigrés travaillent pour rien et nous on se retrouve au chômage. | emotionnel | Immigration et salaires | Immigration, Emploi et marché du travail, Salaires | immigration-emploi | immigres-aides, rsa-smic, chomeurs-travailler | chomeurs-travailler | réussi |
| Il faut réserver les emplois aux Français. | simple | Sentiment que les Français passent après | Emploi et marché du travail, Priorité nationale | immigration-emploi | — | souverainete-industrielle-alimentaire-energetique | réussi |
| Ils arrivent et touchent le RSA direct. | familier | Immigration et prestations sociales | Immigration, Prestations sociales | immigres-aides | immigration-emploi, rsa-smic | immigres-aides | réussi |
| Les étrangers vivent des allocs. | familier | Immigration et prestations sociales | Immigration, Prestations sociales | immigres-aides | immigration-emploi, rsa-smic, agriculteurs-revenus | agriculteurs-revenus | réussi |
| Les migrants ont des logements gratuits et des aides que les Français n’ont pas. | multi | Immigration et prestations sociales ; Immigration et logement | Immigration, Prestations sociales, Logement | immigres-aides ; lacune reconnue | immigration-emploi, rsa-smic | immigres-aides | réussi |
| La CAF donne tout aux étrangers. | generalisation | Immigration et prestations sociales | Immigration, Prestations sociales | immigres-aides | immigration-emploi, rsa-smic, criminels-etrangers-proteges-justice | criminels-etrangers-proteges-justice | réussi |
| L’immigration nous coûte une fortune. | simple | Coût de l’immigration pour les finances publiques | Immigration, Coût et finances publiques | immigres-aides | impots-assistanat, rsa-profiteurs, delinquance-principalement-immigration | delinquance-principalement-immigration | réussi |
| On paie des impôts pour les immigrés. | insinuation | Coût de l’immigration pour les finances publiques | Immigration, Fiscalité, Coût et finances publiques | immigres-aides | impots-assistanat, rsa-profiteurs, delinquance-principalement-immigration | delinquance-principalement-immigration | réussi |
| Les immigres coute plus qu’ils rapportent | fautes | Coût de l’immigration pour les finances publiques | Immigration, Coût et finances publiques | immigres-aides | impots-assistanat, rsa-profiteurs, delinquance-principalement-immigration | delinquance-principalement-immigration | réussi |
| Un étranger qui arrive a droit à la CMU et aux APL tout de suite. | simple | Immigration et prestations sociales | Immigration, Prestations sociales | immigres-aides | immigration-emploi, rsa-smic, perte-automatique-droit-sejour | perte-automatique-droit-sejour | réussi |
| Priorité aux Français pour les aides sociales ! | provocation | Sentiment que les Français passent après | Prestations sociales, Priorité nationale | immigres-aides | — | immigres-aides | réussi |
| On se sent étrangers dans notre propre pays, les autres passent avant nous. | emotionnel | Identité et sentiment de dépossession ; Sentiment que les Français passent après | Immigration, Identité et appartenance, Priorité nationale | immigration-chiffres-definitions ; immigres-aides | electricite-nucleaire-renouvelables | electricite-nucleaire-renouvelables | réussi |
| C’est toujours les mêmes qui profitent pendant que les Français trinquent. | insinuation | Sentiment que les Français passent après | Prestations sociales, Priorité nationale | immigres-aides | dividendes-salaires | dividendes-salaires | réussi |
| Les étrangers remplissent les prisons. | simple | Étrangers, immigrés et population carcérale | Immigration, Prisons | etrangers-prisons | justice-laxiste-prison | etrangers-prisons | réussi |
| Les immigrés remplissent les prisons. | simple | Étrangers, immigrés et population carcérale | Immigration, Prisons | immigres-prisons-surrepresentation | justice-laxiste-prison | immigres-prisons-surrepresentation | réussi |
| Un quart des détenus sont étrangers, ça prouve tout. | chiffre | Étrangers, immigrés et population carcérale | Immigration, Prisons | etrangers-prisons | justice-laxiste-prison | etrangers-prisons | réussi |
| La délinquance, c’est surtout l’immigration. | simple | Immigration et délinquance | Immigration, Délinquance et insécurité | delinquance-principalement-immigration | delinquance-partout | delinquance-principalement-immigration | réussi |
| Avec moins d’immigrés, la France serait plus sûre. | causalite | Immigration et délinquance | Immigration, Délinquance et insécurité | france-plus-sure-moins-immigres | delinquance-partout | france-plus-sure-moins-immigres | réussi |
| Les chiffres montrent bien que l’immigration fait exploser l’insécurité. | chiffre | Immigration et délinquance | Immigration, Délinquance et insécurité, Chiffres et statistiques | statistiques-prouvent-insecurite-immigration | delinquance-partout | statistiques-prouvent-insecurite-immigration | réussi |
| Tous les délinquants sont des immigrés. | generalisation | Immigration et délinquance | Immigration, Délinquance et insécurité | delinquance-principalement-immigration | delinquance-partout | delinquance-principalement-immigration | réussi |
| Les étrangers, c’est eux qui font les agressions. | amalgame | Immigration et délinquance | Immigration, Délinquance et insécurité | delinquance-principalement-immigration | delinquance-partout, expulser-tous-etrangers-condamnes | expulser-tous-etrangers-condamnes | réussi |
| Il faut expulser tous les étrangers condamnés. | simple | Expulsion des étrangers condamnés ; Justice jugée laxiste | Immigration, Expulsion et éloignement, Justice pénale | expulser-tous-etrangers-condamnes ; justice-laxiste-prison | — | expulser-tous-etrangers-condamnes | réussi |
| Un étranger qui commet un crime n’a plus rien à faire chez nous. | simple | Expulsion des étrangers condamnés | Immigration, Délinquance et insécurité, Expulsion et éloignement, Identité et appartenance | etranger-crime-plus-sa-place | — | etranger-crime-plus-sa-place | réussi |
| Si on expulsait les délinquants étrangers, il n’y aurait plus de criminalité. | causalite | Expulsion des étrangers condamnés ; Immigration et délinquance | Immigration, Délinquance et insécurité, Expulsion et éloignement | expulser-reduit-criminalite ; delinquance-principalement-immigration | — | expulser-reduit-criminalite | réussi |
| Un étranger condamné devrait perdre automatiquement son titre de séjour. | simple | Expulsion des étrangers condamnés ; Justice jugée laxiste | Immigration, Expulsion et éloignement, Justice pénale | perte-automatique-droit-sejour ; justice-laxiste-prison | — | perte-automatique-droit-sejour | réussi |
| Les juges protègent les criminels étrangers. | simple | Justice et étrangers ; Immigration et délinquance | Immigration, Délinquance et insécurité, Justice pénale | criminels-etrangers-proteges-justice ; delinquance-principalement-immigration | — | criminels-etrangers-proteges-justice | réussi |
| Les OQTF ne sont jamais appliquées. | simple | Exécution des mesures d’éloignement | Expulsion et éloignement | expulser-tous-etrangers-condamnes | — | expulser-tous-etrangers-condamnes | réussi |
| Les étrangers sortent de prison et on les laisse rester en France. | multi | Étrangers, immigrés et population carcérale ; Exécution des mesures d’éloignement | Immigration, Prisons, Expulsion et éloignement | etrangers-prisons ; expulser-tous-etrangers-condamnes | justice-laxiste-prison, etranger-crime-plus-sa-place | etranger-crime-plus-sa-place | réussi |
| Les étrangers remplissent les prisons, et quand ils sortent on les laisse rester en France. | multi | Étrangers, immigrés et population carcérale ; Exécution des mesures d’éloignement | Immigration, Prisons, Expulsion et éloignement | etrangers-prisons ; expulser-tous-etrangers-condamnes | justice-laxiste-prison | etrangers-prisons | réussi |
| La justice est laxiste, les délinquants ressortent tout de suite. | simple | Justice jugée laxiste | Délinquance et insécurité, Prisons, Justice pénale | justice-laxiste-prison | — | justice-laxiste-prison | réussi |
| Il y a de la délinquance partout maintenant. | simple | Insécurité et justice | Délinquance et insécurité | delinquance-partout | — | delinquance-partout | réussi |
| On ne peut plus sortir le soir tranquille. | emotionnel | Insécurité et justice | Délinquance et insécurité | delinquance-partout | — | aucune | réussi |
| Les immigrés prennent le travail des Français et en plus ils viennent toucher le RSA. | multi | Immigration et concurrence sur le marché du travail ; Immigration et prestations sociales | Immigration, Emploi et marché du travail, Prestations sociales | immigration-emploi ; immigres-aides | rsa-smic, rsa-profiteurs, chomeurs-travailler, impots-assistanat | immigres-aides | réussi |
| Ils prennent nos emplois, nos logements et nos aides. | multi | Immigration et concurrence sur le marché du travail ; Immigration et prestations sociales ; Immigration et logement | Immigration, Emploi et marché du travail, Prestations sociales, Logement | immigration-emploi ; immigres-aides ; lacune reconnue | rsa-smic, rsa-profiteurs, chomeurs-travailler, impots-assistanat | pauvrete-france | réussi |
| Les immigrés font baisser les salaires et remplissent les prisons. | multi | Immigration et salaires ; Étrangers, immigrés et population carcérale | Immigration, Salaires, Prisons | immigration-salaires ; immigres-prisons-surrepresentation | immigres-aides, rsa-smic, chomeurs-travailler | immigres-prisons-surrepresentation | réussi |
| Les étrangers touchent les aides et en plus ils sont tous délinquants. | multi | Immigration et prestations sociales ; Immigration et délinquance | Immigration, Prestations sociales, Délinquance et insécurité | immigres-aides ; delinquance-principalement-immigration | immigration-emploi, rsa-smic | immigres-aides | réussi |
| Il y a trop d’immigrés, ça fait monter le chômage et l’insécurité. | multi | Immigration et concurrence sur le marché du travail ; Immigration et délinquance ; Immigration et démographie | Immigration, Emploi et marché du travail, Délinquance et insécurité, Démographie | immigration-emploi ; delinquance-principalement-immigration ; immigration-chiffres-definitions | immigres-aides, rsa-smic, rsa-profiteurs, chomeurs-travailler, impots-assistanat | delinquance-principalement-immigration | réussi |
| Mélenchon veut ouvrir les frontières et en plus il est antisémite. | multi | Critiques visant Jean-Luc Mélenchon | Immigration, Mélenchon et LFI, La gauche, Antisémitisme | lfi-antisemite | — | lfi-antisemite | réussi |
| Les riches ne paient pas d’impôts et les pauvres paient pour tout. | multi | Fiscalité, riches et entreprises ; Impôts ; Pauvreté | Fiscalité, Riches, entreprises et patronat, Pauvreté et précarité | dividendes-salaires ; impots-assistanat ; pauvrete-france | — | aucune | réussi |
| Les chômeurs profitent du RSA et les immigrés aussi. | multi | Assistanat et aides sociales | Immigration, Emploi et marché du travail, Prestations sociales | rsa-profiteurs | immigres-aides | immigres-aides | réussi |
| On ne peut plus se loger, on ne trouve plus de travail et on voit des aides distribuées partout. Pendant ce temps, les immigrés arrivent encore. | emotionnel | Immigration et logement ; Immigration et concurrence sur le marché du travail ; Immigration et prestations sociales | Immigration, Emploi et marché du travail, Prestations sociales, Logement | lacune reconnue ; immigration-emploi ; immigres-aides | statistiques-prouvent-insecurite-immigration | immigres-aides | réussi |
| La gauche est islamo-gauchiste et déteste la France. | multi | Accusation d’islamo-gauchisme ; La gauche et la patrie | Patriotisme et nation, Islam et religion, La gauche | islamo-gauchisme-origine-usages ; gauche-nation-debats | — | islamo-gauchisme-origine-usages | réussi |
| Les logements sociaux sont tous donnés aux immigrés. | generalisation | Immigration et logement | Immigration, Logement | lacune reconnue | immigres-aides, statistiques-prouvent-insecurite-immigration | aucune | réussi |
| Les HLM c’est que pour les étrangers. | familier | Immigration et logement | Immigration, Logement | lacune reconnue | immigres-aides, statistiques-prouvent-insecurite-immigration, criminels-etrangers-proteges-justice | criminels-etrangers-proteges-justice | réussi |
| Les loyers explosent à cause des migrants. | causalite | Immigration et logement | Immigration, Logement | lacune reconnue | immigres-aides, statistiques-prouvent-insecurite-immigration | aucune | réussi |
| Impossible de trouver un appart, les loyers sont trop chers. | emotionnel | Difficulté à se loger | Logement | lacune reconnue | — | aucune | réussi |
| Mes enfants n’arrivent pas à se loger. | emotionnel | Difficulté à se loger | Logement | lacune reconnue | — | aucune | réussi |
| On est en train d’être remplacés. | insinuation | Identité et sentiment de dépossession | Identité et appartenance | immigration-chiffres-definitions | — | immigration-chiffres-definitions | réussi |
| Les immigrés, c’est déjà un tiers de la population. | chiffre | Immigration et démographie | Immigration, Démographie | immigration-chiffres-definitions | — | immigration-chiffres-definitions | réussi |
| Il y a de plus en plus d’immigrés en France. | simple | Immigration et démographie | Immigration, Démographie | immigration-chiffres-definitions | france-plus-sure-moins-immigres | france-plus-sure-moins-immigres | réussi |
| On perd notre identité. | emotionnel | Identité et sentiment de dépossession | Identité et appartenance | patriotisme-nationalisme | electricite-nucleaire-renouvelables | electricite-nucleaire-renouvelables | réussi |
| Les gauchistes n’aiment pas leur pays. | familier | La gauche et la patrie | Patriotisme et nation, La gauche | gauche-nation-debats | programme-cnr-1944 | programme-cnr-1944 | réussi |
| Être patriote, c’est être de droite. | simple | La gauche et la patrie | Patriotisme et nation | patriotisme-nationalisme | — | patriotisme-nationalisme | réussi |
| La gauche a honte du drapeau. | insinuation | La gauche et la patrie | Patriotisme et nation, La gauche | gauche-nation-debats | gauche-assistes-travailleurs | gauche-assistes-travailleurs | réussi |
| Il faut rendre la France aux Français. | provocation | Sentiment que les Français passent après | Priorité nationale | immigres-aides | criminels-etrangers-proteges-justice | criminels-etrangers-proteges-justice | réussi |
| Avant on était fiers d’être Français. | emotionnel | La gauche et la patrie | Patriotisme et nation | patriotisme-nationalisme | commune-paris-1871 | commune-paris-1871 | réussi |
| C’était mieux de mon temps. | simple | Nostalgie du passé | Nostalgie | lacune reconnue | commune-paris-1871 | commune-paris-1871 | réussi |
| Les musulmans sont tous des islamistes. | amalgame | Islam et musulmans | Islam et religion | musulmans-amalgames | — | musulmans-amalgames | réussi |
| Immigrés, musulmans, islamistes, c’est pareil. | amalgame | Islam et musulmans | Immigration, Islam et religion | musulmans-amalgames | — | musulmans-amalgames | réussi |
| Le voile est contraire à la laïcité. | simple | Islam et musulmans ; Laïcité | Islam et religion, Laïcité | laicite-loi-1905 ; gauche-laicite-debats | lfi-communautarisme | lfi-communautarisme | réussi |
| La gauche a abandonné la laïcité. | simple | Laïcité | Laïcité, La gauche | gauche-laicite-debats | — | gauche-laicite-debats | réussi |
| La laïcité interdit les signes religieux partout. | simple | Laïcité | Laïcité | laicite-loi-1905 | — | laicite-loi-1905 | réussi |
| On n’a plus le droit de critiquer l’islam sans être traité de raciste. | emotionnel | Islam et liberté d’expression | Islam et religion, Liberté d’expression | lacune reconnue | islamo-gauchisme-origine-usages, gauche-laicite-debats | gauche-laicite-debats | réussi |
| On ne peut plus rien dire en France. | simple | Liberté d’expression | Liberté d’expression | lacune reconnue | etranger-crime-plus-sa-place | etranger-crime-plus-sa-place | réussi |
| Avec la bien-pensance, on ne peut plus rien dire. | familier | Liberté d’expression | Liberté d’expression | lacune reconnue | securite-sociale-1945 | securite-sociale-1945 | réussi |
| Les islamo-gauchistes sont partout à l’université. | simple | Accusation d’islamo-gauchisme | Islam et religion, La gauche | islamo-gauchisme-origine-usages | — | islamo-gauchisme-origine-usages | réussi |
| L’islamo-gauchisme, c’est comme le judéo-bolchevisme ? | question | Accusation d’islamo-gauchisme | Islam et religion, La gauche, Histoire de l’extrême droite | islamo-gauchisme-judeo-bolchevisme-comparaison | — | islamo-gauchisme-judeo-bolchevisme-comparaison | réussi |
| Mélenchon est un dictateur en puissance. | simple | Critiques visant Jean-Luc Mélenchon | Mélenchon et LFI, La gauche, Disqualification d’une personnalité | melenchon-autoritaire | — | melenchon-autoritaire | réussi |
| Mélenchon est agressif avec tout le monde. | simple | Critiques visant Jean-Luc Mélenchon | Délinquance et insécurité, Mélenchon et LFI, La gauche, Disqualification d’une personnalité | melenchon-agressif | — | melenchon-agressif | réussi |
| Melenchon il gueule tout le temps | fautes | Critiques visant Jean-Luc Mélenchon | Mélenchon et LFI, La gauche, Disqualification d’une personnalité | melenchon-crie | — | melenchon-crie | réussi |
| LFI est antisémite. | simple | Critiques visant Jean-Luc Mélenchon | Mélenchon et LFI, La gauche, Antisémitisme | lfi-antisemite | — | lfi-antisemite | réussi |
| Les Insoumis détestent la police. | simple | Critiques visant Jean-Luc Mélenchon | Mélenchon et LFI, La gauche | lfi-contre-police | melenchon-dangereux-democratie | melenchon-dangereux-democratie | réussi |
| LFI fait du communautarisme. | simple | Critiques visant Jean-Luc Mélenchon | Mélenchon et LFI, La gauche | lfi-communautarisme | — | lfi-communautarisme | réussi |
| Mélenchon change d’avis comme de chemise. | familier | Critiques visant Jean-Luc Mélenchon | Mélenchon et LFI, La gauche | melenchon-change-avis | — | melenchon-change-avis | réussi |
| Le programme de LFI est irréalisable. | simple | Critiques visant Jean-Luc Mélenchon | Mélenchon et LFI, La gauche | programme-irrealisable | — | programme-irrealisable | réussi |
| Si Mélenchon passe, la France est ruinée. | peur | Critiques visant Jean-Luc Mélenchon | Mélenchon et LFI, La gauche | melenchon-ruiner-france | melenchon-change-avis | melenchon-change-avis | réussi |
| Mélenchon est dangereux pour la démocratie. | simple | Critiques visant Jean-Luc Mélenchon | Mélenchon et LFI, La gauche, Disqualification d’une personnalité | melenchon-dangereux-democratie | — | melenchon-dangereux-democratie | réussi |
| La gauche est dangereuse. | simple | La gauche jugée dangereuse | La gauche, Disqualification d’une personnalité | melenchon-dangereux-democratie | — | melenchon-dangereux-democratie | réussi |
| La gauche défend les assistés et pas les travailleurs. | simple | Assistanat et aides sociales | Prestations sociales, La gauche | gauche-assistes-travailleurs | — | gauche-assistes-travailleurs | réussi |
| Les chômeurs ne veulent pas travailler. | simple | Les Français ne voudraient plus travailler | Emploi et marché du travail, Effort et valeur travail | chomeurs-travailler | — | chomeurs-travailler | réussi |
| Les gens préfèrent rester au RSA plutôt que de bosser. | familier | Assistanat et aides sociales | Emploi et marché du travail, Prestations sociales | rsa-profiteurs | gauche-assistes-travailleurs | gauche-assistes-travailleurs | réussi |
| Le RSA, c’est mieux payé que le SMIC. | chiffre | Assistanat et aides sociales | Salaires, Prestations sociales | rsa-smic | gauche-assistes-travailleurs | gauche-assistes-travailleurs | réussi |
| Les profiteurs du RSA nous coûtent cher. | simple | Assistanat et aides sociales | Prestations sociales, Coût et finances publiques | rsa-profiteurs | — | rsa-profiteurs | réussi |
| On paie trop d’impôts pour les assistés. | simple | Impôts | Prestations sociales, Fiscalité, Démographie, Coût et finances publiques | impots-assistanat | — | impots-assistanat | réussi |
| Si on taxe les riches, ils vont tous partir. | peur | Fiscalité, riches et entreprises ; Impôts | Fiscalité, Riches, entreprises et patronat | melenchon-ruiner-france ; impots-assistanat | — | aucune | réussi |
| Les actionnaires se gavent pendant que les salaires stagnent. | simple | Fiscalité, riches et entreprises | Salaires, Riches, entreprises et patronat | dividendes-salaires | — | dividendes-salaires | réussi |
| Le pouvoir d’achat s’effondre. | simple | Pouvoir d’achat et revenus du travail | Pouvoir d’achat | dividendes-salaires | — | dividendes-salaires | réussi |
| Les fins de mois sont de plus en plus dures. | emotionnel | Pouvoir d’achat et revenus du travail | Pouvoir d’achat | dividendes-salaires | — | aucune | réussi |
| Il y a de plus en plus de pauvres en France. | simple | Pauvreté | Pauvreté et précarité | pauvrete-france | — | pauvrete-france | réussi |
| Les agriculteurs crèvent de faim. | simple | Écologie | Écologie | agriculteurs-revenus | — | agriculteurs-revenus | réussi |
| Les éoliennes, ça ne sert à rien, il faut du nucléaire. | simple | Écologie | Écologie | electricite-nucleaire-renouvelables | — | electricite-nucleaire-renouvelables | réussi |
| L’Europe nous impose tout. | simple | Europe et souveraineté | Europe et souveraineté | souverainete-populaire | melenchon-change-avis | melenchon-change-avis | réussi |
| Les médias sont tous de gauche. | generalisation | Défiance envers les médias | Médias, La gauche | medias-concentration | gauche-nation-debats | gauche-nation-debats | réussi |
| Les journalistes nous mentent. | simple | Défiance envers les médias | Médias | medias-concentration | — | medias-concentration | réussi |
| Les politiques sont tous pourris. | generalisation | Défiance envers les élus | Défiance envers les élus | lacune reconnue | musulmans-amalgames | musulmans-amalgames | réussi |
| Tous corrompus, droite comme gauche. | familier | Défiance envers les élus | La gauche, Défiance envers les élus | lacune reconnue | islamo-gauchisme-origine-usages | islamo-gauchisme-origine-usages | réussi |
| Le Front populaire n’a rien apporté. | histoire | Correspondance avec une fiche | — | front-populaire-1936 | — | front-populaire-1936 | réussi |
| La Sécurité sociale, c’est de Gaulle qui l’a créée. | histoire | Correspondance avec une fiche | — | securite-sociale-1945 | — | securite-sociale-1945 | réussi |
| La Commune de Paris, c’était des voyous. | histoire | Correspondance avec une fiche | — | commune-paris-1871 | — | commune-paris-1871 | réussi |
| La Résistance, c’était la droite, pas les communistes. | histoire | Correspondance avec une fiche | La gauche | resistance-communistes-etrangers | — | resistance-communistes-etrangers | réussi |
| Peu importe les statistiques, il faut tous les renvoyer chez eux. | rebond | Expulsion des étrangers condamnés | Expulsion et éloignement, Chiffres et statistiques | expulser-tous-etrangers-condamnes | — | expulser-tous-etrangers-condamnes | réussi |
| Et l’immigration alors, ça coûte une fortune. | changement | Coût de l’immigration pour les finances publiques | Immigration, Coût et finances publiques | immigres-aides | impots-assistanat, rsa-profiteurs, delinquance-principalement-immigration | delinquance-principalement-immigration | réussi |
| De toute façon les chômeurs ne veulent pas travailler. | changement | Les Français ne voudraient plus travailler | Emploi et marché du travail, Effort et valeur travail | chomeurs-travailler | — | chomeurs-travailler | réussi |
| Et la délinquance augmente partout. | changement | Insécurité et justice | Délinquance et insécurité | delinquance-partout | — | delinquance-partout | réussi |
| Prouve-moi que les immigrés ne prennent pas le travail des Français. | preuve | Immigration et concurrence sur le marché du travail | Immigration, Emploi et marché du travail | immigration-emploi | immigres-aides, rsa-smic, rsa-profiteurs, chomeurs-travailler, impots-assistanat | immigres-aides | réussi |
| T’as des chiffres sur les étrangers en prison ? | preuve | Étrangers, immigrés et population carcérale | Immigration, Prisons, Chiffres et statistiques | etrangers-prisons | justice-laxiste-prison | etrangers-prisons | réussi |
| Tout le monde sait que les immigrés touchent plus d’aides. | autorite | Immigration et prestations sociales | Immigration, Prestations sociales | immigres-aides | immigration-emploi, rsa-smic | immigres-aides | réussi |
| Mon voisin est arabe et il touche toutes les aides. | anecdote | Immigration et prestations sociales | Origine supposée, Prestations sociales | immigres-aides | immigration-emploi, rsa-smic | immigres-aides | réussi |
| Soit on ferme les frontières, soit la France disparaît. | faux_dilemme | Identité et sentiment de dépossession | Immigration, Identité et appartenance | immigration-chiffres-definitions | pauvrete-france | pauvrete-france | réussi |
| J’en ai marre, on bosse comme des chiens et on n’a rien. | emotionnel | Pouvoir d’achat et revenus du travail | Pouvoir d’achat | dividendes-salaires | — | aucune | réussi |
| Personne ne nous écoute, les politiques s’en fichent de nous. | emotionnel | — | — | aucune | — | musulmans-amalgames | réussi |
| J’ai peur pour l’avenir de mes enfants. | emotionnel | — | — | aucune | — | aucune | réussi |
| On est abandonnés dans nos campagnes, plus de médecin, plus de poste. | emotionnel | Argument sur : emploi et marché du travail | Emploi et marché du travail | lacune reconnue | — | aucune | réussi |
| Ça me rend fou de voir qu’on aide tout le monde sauf nous. | emotionnel | Sentiment que les Français passent après | Prestations sociales, Priorité nationale, Disqualification d’une personnalité | immigres-aides | — | aucune | réussi |
| Il fait beau aujourd’hui. | hors_sujet | — | — | aucune | — | aucune | réussi |
| Bof, je sais pas trop. | hors_sujet | — | — | aucune | — | aucune | réussi |
| Les impôts locaux ont augmenté dans ma commune. | hors_sujet | Impôts | Fiscalité | impots-assistanat | programme-irrealisable | programme-irrealisable | réussi |
| Le foot c’était mieux avant. | hors_sujet | Nostalgie du passé | Nostalgie | lacune reconnue | commune-paris-1871 | commune-paris-1871 | réussi |
| Les immigrés italiens des années 50 se sont bien intégrés. | nuance | Argument sur : immigration | Immigration | lacune reconnue | — | france-plus-sure-moins-immigres | réussi |
| Les clandestins prennent les boulots dans le bâtiment. | simple (validation) | Immigration et concurrence sur le marché du travail | Immigration, Emploi et marché du travail | immigration-emploi | immigres-aides, rsa-smic, rsa-profiteurs, chomeurs-travailler, impots-assistanat | aucune | réussi |
| Les réfugiés ont tout gratuit : logement, santé, argent. | generalisation (validation) | Immigration et prestations sociales ; Immigration et logement | Immigration, Prestations sociales, Logement | immigres-aides ; lacune reconnue | immigration-emploi, rsa-smic, impots-assistanat | impots-assistanat | réussi |
| Ces gens-là viennent juste pour les allocations. | insinuation (validation) | Immigration et prestations sociales | Immigration, Prestations sociales | immigres-aides | immigration-emploi, rsa-smic | aucune | réussi |
| Le travail au noir des sans-papiers tire tout le monde vers le bas. | causalite (validation) | Immigration et salaires ; Immigration et concurrence sur le marché du travail | Immigration, Origine supposée, Emploi et marché du travail, Salaires | immigration-salaires ; immigration-emploi | immigres-aides, rsa-smic, chomeurs-travailler | rsa-profiteurs | réussi |
| Ça sert à quoi de former des chômeurs si on fait venir des étrangers ? | question (validation) | Immigration et concurrence sur le marché du travail | Immigration, Emploi et marché du travail | immigration-emploi | immigres-aides, rsa-smic, rsa-profiteurs, chomeurs-travailler, impots-assistanat | aucune | réussi |
| Les immigrés ne veulent pas s’intégrer. | generalisation (validation) | Argument sur : immigration | Immigration | lacune reconnue | — | delinquance-principalement-immigration | réussi |
| Dans les prisons, il n’y a que des étrangers. | generalisation (validation) | Étrangers, immigrés et population carcérale | Immigration, Prisons | etrangers-prisons | justice-laxiste-prison | etrangers-prisons | réussi |
| Les délinquants étrangers ne sont jamais expulsés. | simple (validation) | Exécution des mesures d’éloignement | Immigration, Délinquance et insécurité, Expulsion et éloignement | expulser-tous-etrangers-condamnes | expulser-reduit-criminalite | expulser-reduit-criminalite | réussi |
| Les juges sont trop laxistes avec les étrangers. | simple (validation) | Justice et étrangers | Immigration, Justice pénale | criminels-etrangers-proteges-justice | — | criminels-etrangers-proteges-justice | réussi |
| L’insécurité a explosé depuis qu’il y a des migrants dans la ville. | causalite (validation) | Immigration et délinquance | Immigration, Délinquance et insécurité | delinquance-principalement-immigration | delinquance-partout | aucune | réussi |
| Il faut virer tous ceux qui ont un casier. | familier (validation) | Expulsion des étrangers condamnés | Expulsion et éloignement | expulser-tous-etrangers-condamnes | renvoyer-tous-deja-condamnes | renvoyer-tous-deja-condamnes | réussi |
| Les loyers sont hors de prix et on fait passer les migrants en priorité pour les HLM. | multi (validation) | Difficulté à se loger ; Immigration et logement | Immigration, Logement | lacune reconnue ; lacune reconnue | — | aucune | réussi |
| Les Français d’abord ! | provocation (validation) | Sentiment que les Français passent après | Priorité nationale | immigres-aides | criminels-etrangers-proteges-justice | criminels-etrangers-proteges-justice | réussi |
| Les musulmans veulent imposer la charia. | generalisation (validation) | Islam et musulmans | Islam et religion | musulmans-amalgames | lfi-communautarisme | lfi-communautarisme | réussi |
| On ne peut même plus faire une blague sans se faire censurer. | emotionnel (validation) | Liberté d’expression | Liberté d’expression | lacune reconnue | — | aucune | réussi |
| Mélenchon soutient les islamistes. | insinuation (validation) | Accusation d’islamo-gauchisme ; Critiques visant Jean-Luc Mélenchon | Islam et religion, Mélenchon et LFI, La gauche | islamo-gauchisme-origine-usages ; melenchon-crie | lfi-antisemite | lfi-antisemite | réussi |
| Les insoumis, ce sont des extrémistes. | simple (validation) | Critiques visant Jean-Luc Mélenchon | Mélenchon et LFI, La gauche, Disqualification d’une personnalité | melenchon-dangereux-democratie | — | melenchon-dangereux-democratie | réussi |
| Les gauchos veulent ruiner le pays avec leurs taxes. | familier (validation) | Impôts | Fiscalité, La gauche | melenchon-ruiner-france | — | melenchon-ruiner-france | réussi |
| Les riches créent les emplois, il faut les laisser tranquilles. | simple (validation) | Fiscalité, riches et entreprises | Emploi et marché du travail, Riches, entreprises et patronat | dividendes-salaires | immigration-emploi | aucune | réussi |
| Les chômeurs sont des fainéants. | generalisation (validation) | Les Français ne voudraient plus travailler | Emploi et marché du travail, Effort et valeur travail | chomeurs-travailler | — | chomeurs-travailler | réussi |
| Avec le RSA, on gagne autant qu’en travaillant. | chiffre (validation) | Assistanat et aides sociales | Prestations sociales | rsa-smic | — | rsa-smic | réussi |
| L’essence et les courses, tout augmente sauf les salaires. | emotionnel (validation) | Pouvoir d’achat et revenus du travail | Salaires, Pouvoir d’achat | dividendes-salaires | — | dividendes-salaires | réussi |
| Les médias nous cachent la vérité sur l’immigration. | multi (validation) | Défiance envers les médias | Immigration, Médias | medias-concentration | — | aucune | réussi |
| Tous les élus se servent dans la caisse. | generalisation (validation) | — | — | aucune | — | electricite-nucleaire-renouvelables | réussi |
| Avant, au moins, il y avait du respect. | nostalgie (validation) | Nostalgie du passé | Nostalgie | lacune reconnue | france-plus-sure-moins-immigres | france-plus-sure-moins-immigres | réussi |
| Bruxelles décide de tout à notre place. | simple (validation) | Europe et souveraineté | Europe et souveraineté | souverainete-populaire | — | aucune | réussi |
| Le nucléaire, c’est l’avenir, les écolos sont des idiots. | provocation (validation) | Écologie | La gauche, Écologie | electricite-nucleaire-renouvelables | — | aucune | réussi |
| Pétain a sauvé la France. | histoire (validation) | Histoire de l’extrême droite | Histoire de l’extrême droite | judeo-bolchevisme-histoire | chomeurs-travailler | chomeurs-travailler | réussi |
| Je connais une famille d’immigrés qui vit des aides depuis vingt ans. | anecdote (validation) | Immigration et prestations sociales | Immigration, Prestations sociales | immigres-aides | immigration-emploi, rsa-smic | immigres-aides | réussi |
| J’ai l’impression que plus personne ne nous écoute. | emotionnel (validation) | — | — | aucune | — | justice-laxiste-prison | réussi |
| Et alors ? Les immigrés font quand même baisser les salaires. | rebond (validation) | Immigration et salaires | Immigration, Salaires | immigration-salaires | immigres-aides, rsa-smic, chomeurs-travailler | expulser-reduit-criminalite | réussi |
| Prouve-moi que l’immigration ne coûte rien. | preuve (validation) | Coût de l’immigration pour les finances publiques | Immigration, Coût et finances publiques | immigres-aides | impots-assistanat, rsa-profiteurs, statistiques-prouvent-insecurite-immigration | statistiques-prouvent-insecurite-immigration | réussi |
