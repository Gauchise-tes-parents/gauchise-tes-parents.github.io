# Moteur de personnalisation — fonctionnement et table de décision

_Document généré par `node scripts/doc-moteur.js` à partir du code (`public/js/composer.js`, `public/js/profile.js`) et des fiches scientifiques. Les effets « mesurés » sont recalculés à chaque génération sur les 40 fiches thématiques._

## 1. Principe

Le mode autonome n’utilise **aucun modèle d’IA** : c’est un moteur de règles déterministe (même contexte → même réponse). Il procède en trois temps :

1. **Nettoyage du profil** (`nettoyerProfil`) : seules les options prévues sont gardées ; « je ne connais pas cette personne » annule toutes les autres hypothèses ; trois valeurs au plus.
2. **Plan explicite** (`planifier`) : à partir de la fiche, du mode, du profil, des arguments déjà avancés, des objections et questions déjà traitées et des fiches récemment utilisées, le moteur choisit : l’approche (factuelle, historique ou institutionnelle, valeurs et conséquences), le point d’entrée, les preuves et leur ordre, le niveau de détail, la source mise en avant, l’objection à anticiper, les questions, le ton, la conclusion, l’ordre des blocs et la prochaine étape. Chaque choix est justifié (« Pourquoi cette stratégie » dans l’interface).
3. **Rendu** (`blocs`) : les blocs sont assemblés dans l’ordre du plan. Les seuls textes ajoutés par le moteur sont des formules de liaison sans contenu factuel ; les faits, chiffres, sources et réponses courtes sont repris **tels quels** depuis la fiche.

**Résolution des conflits entre options.** Les poids d’approche s’additionnent ; pour le point d’entrée, le ton et la conclusion, chaque mode a une liste de priorité (par exemple en « gagner un débat » : correction > fait > cadre > concession… ; en « convaincre » : reformulation > question > vécu…). Le nombre maximal de preuves est le plus petit demandé ; « méfiance » peut ajouter une source concordante d’un autre organisme (jusqu’à trois preuves). Le mode infléchit l’approche (+0,75 vers factuelle en « gagner », vers valeurs en « convaincre ») sans écraser le profil.

**Ce qui ne change jamais selon le profil** : le texte des faits, les chiffres, les sources et leurs dates, la réponse courte, les limites de la fiche, les avertissements d’ancienneté et de débat.

## 2. Table de décision

Pour chaque option : l’information qu’elle apporte, les éléments du plan qu’elle influence, la consigne affichée (avec son fondement), les cas où elle ne doit rien changer, l’effet mesuré (nombre de fiches dont la réponse change quand on ajoute cette seule option) et le test automatisé qui la vérifie.

### Mode

- **Gagner un débat** — Objectif de l’échange : convaincre le public présent, même si l’interlocuteur reste campé. Influence : entree, detail, ordre, conclusion, ton, stratégie ouverte par défaut. Sans effet sur : Les faits et les sources restent identiques dans les deux modes. Test : « le mode change le contenu, pas les faits ».
- **Convaincre** — Objectif : faire avancer la personne elle-même, sans la braquer. Influence : entree, questions, ordre, conclusion, ton, stratégie ouverte par défaut. Sans effet sur : Les faits et les sources restent identiques dans les deux modes. Test : « le mode change le contenu, pas les faits ».
- **Volet (thème)** — Thème de la question. Influence : choix de la fiche (départage des correspondances). Quand l’affirmation correspond fortement à une fiche, le volet ne la remplace pas.

### Rapport au débat (question essentielle)

| Option | Information apportée | Éléments influencés | Consigne affichée (fondement) | Ne change pas | Effet mesuré | Test |
|---|---|---|---|---|---|---|
| Calme | Échange posé. | niveau de détail | Un échange posé permet de présenter plusieurs éléments et d’entrer dans le détail. (bonne pratique ; sci-deliberation) | Ne change ni l’approche ni les preuves. | 40 / 40 fiches | effet non nul (test de couverture) |
| Compétitif | Aime la confrontation. | niveau de détail, ton, point d’entrée, conclusion, nombre de preuves, approche | Réponse courte, ferme et structurée : une idée centrale et une preuve vérifiable. Ne multiplie pas les arguments ; demande une preuve précise pour toute affirmation contestable. (bonne pratique ; sci-persuasion-modeste) | N’autorise aucun raccourci factuel. | 40 / 40 fiches | attente « une seule preuve, ton ferme » |
| Provocateur | Cherche à faire réagir. | niveau de détail, ton, point d’entrée, conclusion, recentrage | Pas d’escalade : identifie la seule affirmation qui mérite une réponse, refuse les détournements et prévois une phrase courte pour les personnes qui écoutent. (bonne pratique ; sci-polarisation-groupe) | Ne change pas les faits. | 40 / 40 fiches | attente « recentrage, réponse courte » |
| Susceptible | Se braque vite. | point d’entrée, ton, ordre (questions avant contre-argument), nombre de preuves | Reformule et pose une question ouverte AVANT tout contre-argument ; évite ce qui peut la faire passer pour mal informée ; laisse-lui le droit de ne pas changer d’avis tout de suite. (recherche ; sci-reactance) | Les faits ne sont pas atténués. | 40 / 40 fiches | attente « questions avant contre-argument (deux modes) » |
| Évite le conflit | Évite le conflit. | point d’entrée, ton, ordre | Reformule et pose une question ouverte AVANT tout contre-argument ; évite ce qui peut la faire passer pour mal informée ; laisse-lui le droit de ne pas changer d’avis tout de suite. (recherche ; sci-reactance) | Les faits ne sont pas atténués. | 40 / 40 fiches | attente « questions avant contre-argument » |
| Hésitant | Hésite. | conclusion (plusieurs pistes), incertitudes, ton, ordre (demander ce qui fait hésiter) | Propose plusieurs pistes et reconnais les incertitudes plutôt que de forcer une conclusion. (bonne pratique ; sci-autonomie) | Ne fabrique pas d’incertitude là où les faits sont établis. | 40 / 40 fiches | attente « conclusion « plusieurs pistes » » |

### Ce qui le convainc (question essentielle)

| Option | Information apportée | Éléments influencés | Consigne affichée (fondement) | Ne change pas | Effet mesuré | Test |
|---|---|---|---|---|---|---|
| Chiffres et statistiques | Sensible aux données. | approche, choix des preuves, niveau de détail, méthode | Des données sourcées, comparables, avec ordres de grandeur, période, périmètre et limites. Pas d’avalanche de statistiques. (bonne pratique ; sci-raisonnement-motive) | Si la fiche n’a pas de chiffre, le moteur le signale au lieu d’en inventer. | 40 / 40 fiches | attente « preuve chiffrée en tête ou absence signalée » |
| Exemples concrets | Sensible aux exemples concrets. | approche, point d’entrée, choix des preuves | Pars d’un exemple concret ou de son vécu, reconnais qu’il est réel pour elle, puis mets-le en perspective avec des données plus générales. (recherche ; sci-persuasion-modeste) | Aucun exemple n’est inventé : seuls les faits de la fiche sont utilisés. | 40 / 40 fiches | effet non nul (test de couverture) |
| Témoignages | Sensible aux récits. | approche, point d’entrée, choix des preuves | Pars d’un exemple concret ou de son vécu, reconnais qu’il est réel pour elle, puis mets-le en perspective avec des données plus générales. (recherche ; sci-persuasion-modeste) | Aucun témoignage n’est inventé. | 40 / 40 fiches | effet non nul (test de couverture) |
| Raisonnement logique | Sensible au raisonnement. | approche, conclusion | Des données sourcées, comparables, avec ordres de grandeur, période, périmètre et limites. Pas d’avalanche de statistiques. (bonne pratique ; sci-raisonnement-motive) | — | 40 / 40 fiches | effet non nul (test de couverture) |
| Expérience personnelle | Raisonne par son vécu. | approche, point d’entrée, questions | Pars d’un exemple concret ou de son vécu, reconnais qu’il est réel pour elle, puis mets-le en perspective avec des données plus générales. (recherche ; sci-persuasion-modeste) | — | 40 / 40 fiches | attente « entrée par le vécu » |

### Rapport aux institutions et aux sources (question essentielle)

| Option | Information apportée | Éléments influencés | Consigne affichée (fondement) | Ne change pas | Effet mesuré | Test |
|---|---|---|---|---|---|---|
| Fait confiance aux institutions | Fait confiance aux institutions. | source mise en avant, approche | Appuie-toi d’abord sur la source officielle (organisme, date, document). (bonne pratique ; sci-desinformation-confiance) | — | 15 / 40 fiches | effet non nul (test de couverture) |
| Se méfie des institutions | Se méfie des institutions. | méthode, sources concordantes, objection anticipée, questions | Montre d’où viennent les données, comment elles sont calculées et leurs limites ; ajoute une source indépendante concordante quand il y en a une. Ne réponds pas « les experts l’ont dit », mais n’écarte pas pour autant les données publiques. (recherche ; sci-desinformation-confiance) | Les données publiques restent utilisées : le moteur montre leur méthode, il ne les écarte pas. | 40 / 40 fiches | attente « méthode affichée pour chaque preuve » |
| Préfère les sources indépendantes | Préfère les sources indépendantes. | source mise en avant, méthode | Montre d’où viennent les données, comment elles sont calculées et leurs limites ; ajoute une source indépendante concordante quand il y en a une. Ne réponds pas « les experts l’ont dit », mais n’écarte pas pour autant les données publiques. (recherche ; sci-desinformation-confiance) | Les médias et institutions ne sont pas exclus automatiquement. | 40 / 40 fiches | attente « méthode affichée » |

### Rapport au changement (facultative)

| Option | Information apportée | Éléments influencés | Consigne affichée (fondement) | Ne change pas | Effet mesuré | Test |
|---|---|---|---|---|---|---|
| Prudent | Prudent | approche, conclusion | Insiste sur ce qui est établi et sur les risques ; présente des pas progressifs plutôt qu’un bouleversement. (bonne pratique ; sci-dissonance) | Aucun fait, chiffre ni source n’est modifié. | 40 / 40 fiches | effet non nul (test de couverture) |
| Pragmatique | Pragmatique | choix des preuves, approche | Parle de résultats mesurables et de conséquences concrètes, plus que de principes. (bonne pratique ; sci-valeurs-morales) | Aucun fait, chiffre ni source n’est modifié. | 14 / 40 fiches | effet non nul (test de couverture) |
| Réformiste | Réformiste | approche (exemples institutionnels) | Mets en avant les améliorations possibles et les exemples institutionnels qui ont fonctionné. (bonne pratique ; sci-valeurs-morales) | Aucun fait, chiffre ni source n’est modifié. | 18 / 40 fiches | effet non nul (test de couverture) |
| Favorable aux ruptures | Favorable aux ruptures | niveau de détail, approche | Elle accepte l’idée de changements profonds : montre l’ampleur du problème et les choix structurels, sans exagérer les faits. (bonne pratique ; sci-valeurs-morales) | Aucun fait, chiffre ni source n’est modifié. | 40 / 40 fiches | effet non nul (test de couverture) |

### Valeurs prioritaires (3 au plus) (facultative)

| Option | Information apportée | Éléments influencés | Consigne affichée (fondement) | Ne change pas | Effet mesuré | Test |
|---|---|---|---|---|---|---|
| Justice sociale | Justice sociale | approche, angle de valeur, choix des preuves | Pars des situations vécues et des inégalités ; relie les chiffres à des conséquences concrètes, en présentant les arbitrages et les limites. (recherche ; sci-valeurs-morales) | Aucun fait, chiffre ni source n’est modifié. | 40 / 40 fiches | attente « angle justice » |
| Sécurité | Sécurité | approche, angle de valeur, point d’entrée, choix des preuves | Pars de sa préoccupation pour la sécurité ; examine les résultats mesurables des politiques. Ne caricature pas sa volonté de sécurité. (recherche ; sci-menace-biologie) | Aucun fait, chiffre ni source n’est modifié. | 40 / 40 fiches | attente « angle sécurité » |
| Liberté | Liberté | angle de valeur, choix des preuves | Présente le fait sous l’angle du travail récompensé, de la responsabilité ou de la liberté de choix, sans changer les faits. (recherche ; sci-valeurs-morales) | Aucun fait, chiffre ni source n’est modifié. | 40 / 40 fiches | effet non nul (test de couverture) |
| Ordre | Ordre | approche, angle de valeur, point d’entrée | Pars de sa préoccupation pour la sécurité ; examine les résultats mesurables des politiques. Ne caricature pas sa volonté de sécurité. (recherche ; sci-menace-biologie) | Aucun fait, chiffre ni source n’est modifié. | 40 / 40 fiches | attente « angle sécurité » |
| Solidarité | Solidarité | approche, angle de valeur, choix des preuves | Pars des situations vécues et des inégalités ; relie les chiffres à des conséquences concrètes, en présentant les arbitrages et les limites. (recherche ; sci-valeurs-morales) | Aucun fait, chiffre ni source n’est modifié. | 40 / 40 fiches | effet non nul (test de couverture) |
| Mérite | Mérite | angle de valeur, choix des preuves | Présente le fait sous l’angle du travail récompensé, de la responsabilité ou de la liberté de choix, sans changer les faits. (recherche ; sci-valeurs-morales) | Aucun fait, chiffre ni source n’est modifié. | 40 / 40 fiches | effet non nul (test de couverture) |
| Égalité | Égalité | approche, angle de valeur, choix des preuves | Pars des situations vécues et des inégalités ; relie les chiffres à des conséquences concrètes, en présentant les arbitrages et les limites. (recherche ; sci-valeurs-morales) | Aucun fait, chiffre ni source n’est modifié. | 40 / 40 fiches | effet non nul (test de couverture) |
| Tradition | Tradition | approche, angle de valeur | Appuie-toi sur l’histoire commune et la fierté collective (conquêtes sociales, institutions) pour présenter les faits. (recherche ; sci-valeurs-morales) | Aucun fait, chiffre ni source n’est modifié. | 40 / 40 fiches | attente « angle nation » |
| Souveraineté | Souveraineté | approche, angle de valeur | Appuie-toi sur l’histoire commune et la fierté collective (conquêtes sociales, institutions) pour présenter les faits. (recherche ; sci-valeurs-morales) | Aucun fait, chiffre ni source n’est modifié. | 40 / 40 fiches | attente « angle nation » |
| Protection du groupe | Protection du groupe | approche, angle de valeur | Appuie-toi sur l’histoire commune et la fierté collective (conquêtes sociales, institutions) pour présenter les faits. (recherche ; sci-valeurs-morales) | Aucun fait, chiffre ni source n’est modifié. | 40 / 40 fiches | effet non nul (test de couverture) |

### Ce qu’il sait du sujet (facultative)

| Option | Information apportée | Éléments influencés | Consigne affichée (fondement) | Ne change pas | Effet mesuré | Test |
|---|---|---|---|---|---|---|
| Peu de choses | Connaît peu le sujet. | niveau de détail, ton, choix des preuves, questions | Reste simple et concret : un fait clair, des mots courants, pas de jargon ni de sigles. (bonne pratique ; sci-autonomie) | — | 40 / 40 fiches | attente « ton pédagogique ou nuancé » |
| Un peu | Connaît un peu le sujet. | — | — | Valeur par défaut : aucun changement volontaire. | neutre par conception | effet non nul (test de couverture) |
| Beaucoup | Connaît bien le sujet. | niveau de détail, méthode, objection anticipée | Va au détail : méthode, période, périmètre, limites ; anticipe l’objection la plus sérieuse. (bonne pratique ; sci-raisonnement-motive) | — | 40 / 40 fiches | attente « détail et méthode » |

### Rapport à la politique (facultative)

| Option | Information apportée | Éléments influencés | Consigne affichée (fondement) | Ne change pas | Effet mesuré | Test |
|---|---|---|---|---|---|---|
| Très engagé | Très engagé | point d’entrée (reconnaître ce qui est fondé), ton | Ne l’humilie pas et ne présente pas son camp comme mauvais par nature ; reconnais d’abord ce qui est fondé dans sa position ; propose des faits à examiner sans exiger de capitulation. (recherche ; sci-identite-sociale) | Aucun fait, chiffre ni source n’est modifié. | 27 / 40 fiches | effet non nul (test de couverture) |
| Partisan | Partisan | point d’entrée, ton | Ne l’humilie pas et ne présente pas son camp comme mauvais par nature ; reconnais d’abord ce qui est fondé dans sa position ; propose des faits à examiner sans exiger de capitulation. (recherche ; sci-identite-sociale) | Aucun fait, chiffre ni source n’est modifié. | 40 / 40 fiches | attente « reconnaître d’abord un point fondé » |
| Désabusé | Désabusé | ton, choix des preuves | Évite les étiquettes de partis ; pars du quotidien et de ce qui peut changer concrètement. (bonne pratique ; sci-autonomie) | Aucun fait, chiffre ni source n’est modifié. | 40 / 40 fiches | effet non nul (test de couverture) |
| Peu informé | Peu informé | niveau de détail, ton, choix des preuves | Reste simple et concret : un fait clair, des mots courants, pas de jargon ni de sigles. (bonne pratique ; sci-autonomie) | Aucun fait, chiffre ni source n’est modifié. | 40 / 40 fiches | effet non nul (test de couverture) |
| Ouvert à la discussion | Ouvert à la discussion | niveau de détail, comparaison des approches mise en avant | Tu peux proposer plusieurs angles et entrer dans le détail. (bonne pratique ; sci-deliberation) | Aucun fait, chiffre ni source n’est modifié. | 40 / 40 fiches | effet non nul (test de couverture) |

### Ton lien avec lui ou elle (facultative)

| Option | Information apportée | Éléments influencés | Consigne affichée (fondement) | Ne change pas | Effet mesuré | Test |
|---|---|---|---|---|---|---|
| Parent | Parent | ton, conclusion, phrase sur le lien | Rappelle que le désaccord ne change rien au lien ; reconnais l’histoire familiale avant d’exposer ton point de vue. (recherche ; sci-famille-socialisation) | Aucun fait, chiffre ni source n’est modifié. | 40 / 40 fiches | attente « conclusion sur le lien » |
| Ami | Ami | ton | La franchise est possible : dis clairement ton désaccord, en gardant le respect. (bonne pratique ; sci-autonomie) | Aucun fait, chiffre ni source n’est modifié. | 40 / 40 fiches | effet non nul (test de couverture) |
| Collègue | Collègue | niveau de détail, ton | Reste bref et factuel ; évite que le désaccord déborde sur le travail. (bonne pratique ; sci-deliberation) | Aucun fait, chiffre ni source n’est modifié. | 40 / 40 fiches | effet non nul (test de couverture) |
| Conjoint | Conjoint | ton, conclusion, phrase sur le lien | Rappelle que le désaccord ne change rien au lien ; reconnais l’histoire familiale avant d’exposer ton point de vue. (recherche ; sci-famille-socialisation) | Aucun fait, chiffre ni source n’est modifié. | 40 / 40 fiches | attente « conclusion sur le lien » |
| Connaissance | Connaissance | ton | Pas de lien à préserver à tout prix : reste factuel et courtois, sans chercher à convaincre à tout prix. (bonne pratique ; sci-persuasion-modeste) | Aucun fait, chiffre ni source n’est modifié. | 40 / 40 fiches | effet non nul (test de couverture) |
| Débat public | Débat public | conclusion, ton, phrase pour le public | Le vrai public, ce sont aussi les autres : une phrase claire et vérifiable, sans attaque personnelle ; n’exige pas d’aveu en public. (recherche ; sci-polarisation-groupe) | Aucun fait, chiffre ni source n’est modifié. | 40 / 40 fiches | attente « conclusion adressée au public » |

### Contexte (facultative)

| Option | Information apportée | Éléments influencés | Consigne affichée (fondement) | Ne change pas | Effet mesuré | Test |
|---|---|---|---|---|---|---|
| Discussion privée | Discussion privée | niveau de détail (on peut approfondir sans public) | Sans public, la personne peut changer d’avis sans perdre la face : tu peux approfondir. (recherche ; sci-dissonance) | Aucun fait, chiffre ni source n’est modifié. | 40 / 40 fiches | effet non nul (test de couverture) |
| Repas de famille | Repas de famille | niveau de détail, point d’entrée, proposition de pause | Relation personnelle et risque de conflit : une question vaut souvent mieux qu’un long argumentaire ; propose de reprendre plus tard si ça monte. (bonne pratique ; sci-communication-non-violente) | Aucun fait, chiffre ni source n’est modifié. | 40 / 40 fiches | attente « proposition de pause » |
| Conversation à plusieurs | Conversation à plusieurs | phrase pour le public, règles de discussion | Le vrai public, ce sont aussi les autres : une phrase claire et vérifiable, sans attaque personnelle ; n’exige pas d’aveu en public. (recherche ; sci-polarisation-groupe) | Aucun fait, chiffre ni source n’est modifié. | 40 / 40 fiches | attente « conclusion adressée au public » |
| Réseaux sociaux | Réseaux sociaux | phrase pour le public, niveau de détail | Le vrai public, ce sont aussi les autres : une phrase claire et vérifiable, sans attaque personnelle ; n’exige pas d’aveu en public. (recherche ; sci-polarisation-groupe) | Aucun fait, chiffre ni source n’est modifié. | 40 / 40 fiches | attente « conclusion adressée au public » |

### Ton objectif (facultative)

| Option | Information apportée | Éléments influencés | Consigne affichée (fondement) | Ne change pas | Effet mesuré | Test |
|---|---|---|---|---|---|---|
| Faire réfléchir | Faire réfléchir | conclusion | Termine par une question plutôt que par une conclusion. (recherche ; sci-entretien-motivationnel) | Aucun fait, chiffre ni source n’est modifié. | 40 / 40 fiches | effet non nul (test de couverture) |
| Répondre à une attaque | Répondre à une attaque | niveau de détail, point d’entrée, phrase pour le public | Réponse courte, vérifiable, sans digression ; vise aussi ceux qui écoutent. (bonne pratique ; sci-polarisation-groupe) | Aucun fait, chiffre ni source n’est modifié. | 40 / 40 fiches | attente « phrase pour le public » |
| Corriger une information | Corriger une information | approche, point d’entrée (correction expliquée) | Donne le bon chiffre, sa source et pourquoi l’autre est faux ; propose une explication de remplacement. (recherche ; sci-backfire) | Aucun fait, chiffre ni source n’est modifié. | 40 / 40 fiches | attente « entrée par la correction » |
| Trouver un terrain d’entente | Trouver un terrain d’entente | point d’entrée, conclusion | Commence par ce sur quoi vous êtes d’accord ; cherche une valeur commune. (recherche ; sci-valeurs-morales) | Aucun fait, chiffre ni source n’est modifié. | 40 / 40 fiches | effet non nul (test de couverture) |
| Faire évoluer une opinion | Faire évoluer une opinion | conclusion, approche | Vise un petit pas, pas une conversion ; échange des expériences plutôt qu’empiler des arguments. (recherche ; sci-persuasion-modeste) | Aucun fait, chiffre ni source n’est modifié. | 40 / 40 fiches | effet non nul (test de couverture) |

Le test « chaque option du questionnaire modifie le plan sur au moins une fiche, ou est documentée comme neutre » (`tests/unit/personnalisation.test.js`) échoue si une option devient décorative.

## 3. Exemples imposés

### « La personne se méfie des médias et des institutions »

Fiche « Les impôts ne servent qu'à payer l'assistanat. », mode « gagner un débat », profil de départ neutre-calme. Effet de l’ajout de « se méfie des institutions » :

| Élément du plan | Sans l’information | Avec l’information |
|---|---|---|
| preuves (index des faits) | 0, 1 | 0 (avec méthode), 1 (avec méthode), 3 (avec méthode) |
| sources concordantes | — | Insee, DREES |
| prochaine étape prévue | concede | truquees, concede |

Le moteur **ne remplace pas** les données publiques par d’autres : il affiche période, périmètre et organisme pour chaque preuve, ajoute une source d’un autre organisme quand la fiche en contient une, pose la question « Quelle source te paraîtrait fiable ? » et prépare la réponse au retour « elle dit que les chiffres sont truqués ».

### « Repas de famille »

Fiche « La délinquance augmente partout. », mode « convaincre », profil de départ neutre-calme. Effet de l’ajout de « repas de famille » :

| Élément du plan | Sans l’information | Avec l’information |
|---|---|---|
| proposition de pause | non | oui |
| ordre des blocs | entree → question → preuves → reconnaitre → empathie → conclusion | entree → question → preuves → reconnaitre → empathie → conclusion → pause |

Même ajout en mode « gagner un débat » :

| Élément du plan | Sans l’information | Avec l’information |
|---|---|---|
| point d’entrée | fait | question |
| proposition de pause | non | oui |

Et avec, en plus, « c’est un parent » (mode « convaincre ») :

| Élément du plan | Sans l’information | Avec l’information |
|---|---|---|
| ton | bienveillant | chaleureux |
| conclusion | question | lien |
| phrase sur le lien | non | oui |

## 4. Échanges successifs

Après chaque réponse, l’utilisateur peut indiquer ce qui s’est passé (boutons ou texte libre interprété localement par mots-clés). Le moteur garde en mémoire, pour la durée de la discussion seulement, les faits déjà présentés, les objections déjà traitées et les questions déjà posées : rien n’est répété. Les hypothèses du profil peuvent être corrigées à tout moment.

| Retour | Réponse proposée (exemple sur « Les impôts ne servent qu'à payer l'assistanat. », retours enchaînés dans cet ordre) | Conseil | Fondement |
|---|---|---|---|
| La personne a écouté | **Elle écoute : un élément de plus, pas dix** — Les dépenses publiques totales atteignaient 1 672 Md€ en 2024, soit 57 % du PIB. | Présente un seul nouvel élément, puis demande ce qu’elle en pense. | sci-persuasion-modeste |
| Elle s’est braquée | **Elle s’est braquée : on ralentit** — Je comprends qu'on ait envie de savoir où va son argent ; c'est normal quand on paie beaucoup. Mais quand on regarde, la plus grande part va aux retraites, à la santé et à l'école. Le RSA, c'est moins que les intérêts de la dette. | Arrête d’ajouter des arguments. Reformule son inquiétude, rappelle qu’elle reste libre de son avis, propose de reprendre plus tard. | sci-reactance |
| Elle a demandé une source ou une preuve | **Elle demande une source : montre-la, avec la méthode** — La protection sociale représente 693 Md€ (41 % du total) ; les retraites en sont le principal moteur de hausse (+23 Md€ en un an). | Donne le lien, la date et le périmètre (c’est une source officielle ou primaire). Dis aussi ce que le chiffre ne montre pas : Les données Insee 2024 sont provisoires et seront révisées. | sci-desinformation-confiance |
| Elle dit que les chiffres sont truqués | **Elle doute des chiffres : explique leur fabrication** — Prends un chiffre et montre comment il est fabriqué : qui le produit (Insee, 5 février 2026), sur quelle période et quel périmètre. Le détail est juste en dessous. | Montre que plusieurs organismes vont dans le même sens (Insee, DREES), et dis honnêtement les limites. Ne réponds pas « les experts l’ont dit ». | sci-desinformation-confiance |
| D’accord sur le constat, pas sur les causes | **D’accord sur le constat, pas sur les causes** — On est d’accord sur le constat, c’est déjà beaucoup. Sur les causes, voilà ce qu’on sait : Les dépenses publiques regroupent celles de l'État, des collectivités et de la Sécurité sociale. Elles sont financées par les impôts, les cotisations sociales et l'emprunt. | Sépare le constat (acquis) des causes (à discuter) ; demande quelle cause lui paraît la plus importante et pourquoi. | sci-entretien-motivationnel |
| D’accord sur le problème, pas sur la solution | **D’accord sur le problème, pas sur la solution** — On est d’accord qu’il y a un problème. On peut ne pas être d’accord sur la solution, c’est normal : regardons les options et leurs limites. | Discute des solutions comme d’un choix de valeurs, en reconnaissant leurs limites (par exemple : Les données Insee 2024 sont provisoires et seront révisées.). | sci-valeurs-morales |
| Elle hésite | **Elle hésite : propose des pistes, pas une conclusion** — Il y a plusieurs façons de regarder la question : les chiffres, l’histoire, les conséquences concrètes. Prends le temps. | Reconnais ce qu’on ne sait pas (Les données Insee 2024 sont provisoires et seront révisées.) et laisse-la choisir l’angle qui lui parle. | sci-autonomie |
| Elle a changé de sujet | **Elle a changé de sujet** — On parlait de ce point précis. Je veux bien parler de l’autre sujet, mais d’abord : est-ce qu’on est d’accord sur ce premier fait ? | Recentre une fois, calmement. Si elle insiste, accepte de changer de sujet. | sci-deliberation |
| Elle a reconnu un point | **Elle a reconnu un point : consolide sans triompher** — C’est déjà un vrai point commun entre nous. Le reste, on peut y réfléchir chacun de notre côté. | Salue l’ouverture, ne demande pas davantage tout de suite : un petit pas qui dure vaut mieux qu’une victoire forcée. | sci-dissonance |
| La discussion est terminée | **La discussion est terminée** — Merci d’en avoir parlé. On n’est pas forcément d’accord, mais je suis content qu’on ait pu en discuter. Je t’envoie la source si tu veux. | Termine sur le lien, pas sur le désaccord. Tu peux enregistrer cet argumentaire pour la prochaine fois. | sci-autonomie |

Chaque proposition rappelle qu’elle repose uniquement sur ce que l’utilisateur a observé et qu’elle est approximative.

## 5. Référentiel scientifique

Chaque consigne renvoie à une fiche scientifique de la bibliothèque (rubrique « Science du dialogue »). Aucune de ces notions n’est une loi universelle : les effets mesurés sont généralement modestes et dépendent du contexte. Les consignes marquées « bonne pratique » ne reposent pas directement sur une étude ; elles sont présentées comme telles.

### Pour convaincre, il faut lui dire quoi penser.

- **Référence principale** : Ryan, R. M., & Deci, E. L. (2000). Self-determination theory and the facilitation of intrinsic motivation, social development, and well-being. American Psychologist, 55(1), 68-78. — [lien](https://pubmed.ncbi.nlm.nih.gov/11392867/)
- **Auteurs, année** : Ryan, R. M. ; Deci, E. L., 2000
- **Résumé** : La théorie de l'autodétermination (Ryan et Deci, 2000) identifie trois besoins psychologiques : compétence, autonomie et appartenance. Les contextes qui les respectent favorisent la motivation et l'adhésion ; ceux qui les frustrent l'affaiblissent. Dans une discussion, laisser l'autre construire sa propre conclusion respecte son autonomie.
- **Conditions d’application** : Contextes d'éducation, de travail, de santé, de sport.
- **Limites** : Théorie de la motivation : l'application au débat politique est une extrapolation.
- **Niveau de confiance** : moyenne
- **Consignes qui s’y réfèrent** : Elle hésite ; Elle connaît peu le sujet ; Elle est désabusée ; C’est un ami

### Corriger une fausse information, ça ne fait que la renforcer.

- **Référence principale** : Wood, T., & Porter, E. The Elusive Backfire Effect: Mass Attitudes' Steadfast Factual Adherence. Political Behavior (2019). — [lien](https://papers.ssrn.com/abstract=2819073)
- **Auteurs, année** : Wood, T. ; Porter, E., 2019
- **Résumé** : L'« effet boomerang » (backfire) de la correction est beaucoup plus rare qu'on ne l'a cru. Sur 52 sujets testés auprès de plus de 10 100 personnes, Wood et Porter n'en trouvent aucun. Coppock (2023) conclut aussi que la plupart des gens bougent un peu dans le sens de l'information et que le retour de flamme est rare. Mais une correction n'efface pas totalement la fausse information.
- **Conditions d’application** : Corrections factuelles écrites, échantillons en ligne, États-Unis.
- **Limites** : Effets à court terme ; accepter un fait ne change pas forcément l'opinion.
- **Niveau de confiance** : élevée
- **Autres sources de la fiche** : [University of Chicago Press](https://press.uchicago.edu/ucp/books/book/chicago/P/bo181475008.html), [Skeptical Science (reprise de Tech Policy Press)](https://skepticalscience.com/news.php?n=5295)
- **Consignes qui s’y réfèrent** : Objectif : corriger une information

### Parler calmement de ses émotions, c'est de la naïveté : ça ne change rien.

- **Référence principale** : Pereira, J. S., & Durgante, H. B. (2025). Interventions in Nonviolent Communication to Promote Empathy: Integrative Review. Revista Brasileira em Promoção da Saúde, 38, 1-14. — [lien](https://ojs.unifor.br/RBPS/article/view/16464)
- **Auteurs, année** : Pereira, J. S. ; Durgante, H. B., 2025
- **Résumé** : La communication non violente (observer sans juger, exprimer un ressenti et un besoin, formuler une demande) est très diffusée. Une revue intégrative de 15 études (Pereira et Durgante, 2025) l'associe à davantage d'empathie et à moins de colère et de stress, mais ces études sont majoritairement non randomisées et présentent des faiblesses méthodologiques : l'effet sur des désaccords politiques n'est pas démontré.
- **Conditions d’application** : Interventions en santé, éducation, organisations.
- **Limites** : Études majoritairement non randomisées ; aucune sur la politique.
- **Niveau de confiance** : faible
- **Consignes qui s’y réfèrent** : Repas de famille

### Les gens ordinaires sont incapables de débattre calmement de politique.

- **Référence principale** : Deliberative opinion poll (article encyclopédique) — [lien](https://en.wikipedia.org/wiki/Deliberative_opinion_poll)
- **Auteurs, année** : Fishkin, J. S. (méthode) ; synthèse encyclopédique, 2019
- **Résumé** : Les sondages délibératifs (James Fishkin, 1988) réunissent un échantillon aléatoire de citoyens, informés par des documents équilibrés et réunis en petits groupes animés. Les participants deviennent plus informés et une partie change d'avis ; lors d'« America in One Room » (2019, 526 Américains), les opinions se sont rapprochées du centre pendant au moins un an. Les conditions (animation, équilibre des informations) comptent beaucoup.
- **Conditions d’application** : Délibération encadrée avec échantillon aléatoire et documents équilibrés.
- **Limites** : Conditions exigeantes, rarement réunies spontanément ; source secondaire.
- **Niveau de confiance** : moyenne
- **Consignes qui s’y réfèrent** : Elle discute calmement ; Elle est ouverte à la discussion ; C’est un collègue

### Il suffit de dire « c'est faux » pour qu'une fausse info disparaisse.

- **Référence principale** : Ecker, U. K. H., Lewandowsky, S., Cook, J., et al. (2022). The psychological drivers of misinformation belief and its resistance to correction. Nature Reviews Psychology, 1(1), 13-29. — [lien](https://research-repository.uwa.edu.au/en/publications/the-psychological-drivers-of-misinformation-belief-and-its-resist/)
- **Auteurs, année** : Ecker, U. K. H. et al., 2022
- **Résumé** : La revue d'Ecker et al. (2022) montre qu'une fausse information continue souvent d'influencer le raisonnement après sa correction. Ses ressorts sont cognitifs, sociaux et affectifs : raccourcis mentaux, émotions, menaces identitaires, crédibilité de la source, défiance envers les experts. Les interventions efficaces combinent prévention (« prebunking ») et correction expliquée.
- **Conditions d’application** : Fausses informations et corrections, contextes variés.
- **Limites** : Revue lue en résumé ; recommandations générales, pas de prédiction individuelle.
- **Niveau de confiance** : élevée
- **Autres sources de la fiche** : [Skeptical Science (reprise de Tech Policy Press)](https://skepticalscience.com/news.php?n=5295)
- **Consignes qui s’y réfèrent** : Elle se méfie des institutions ou préfère les sources indépendantes ; Elle fait confiance aux institutions

### Si je lui prouve qu'il a tort, il l'admettra.

- **Référence principale** : Harmon-Jones, E., & Harmon-Jones, C. (2007). Cognitive dissonance theory after 50 years of development. Zeitschrift für Sozialpsychologie, 38(1), 7-16. — [lien](https://researchers.westernsydney.edu.au/en/publications/cognitive-dissonance-theory-after-50-years-of-development/)
- **Auteurs, année** : Harmon-Jones, E. ; Harmon-Jones, C., 2007
- **Résumé** : La dissonance cognitive est l'inconfort ressenti face à une incohérence entre ses croyances, ses actes ou une information nouvelle. La théorie, révisée depuis 50 ans, prédit que les gens cherchent à réduire cet inconfort, ce qui peut passer par le changement d'avis, mais aussi par le rejet de l'information ou la minimisation. Offrir une porte de sortie honorable facilite le premier chemin.
- **Conditions d’application** : Incohérences entre croyances et actes ; expériences de laboratoire.
- **Limites** : Revue lue en résumé ; rôle de l'affirmation de soi présenté comme hypothèse.
- **Niveau de confiance** : moyenne
- **Consignes qui s’y réfèrent** : Elle est prudente face au changement ; Discussion en tête-à-tête

### Pour aider quelqu'un à changer, il faut le confronter à ses contradictions.

- **Référence principale** : Lundahl, B., Burke, B. L., Tollefson, D. R., Kunz, C., & Browell, C. (2010). A Metaanalysis of Motivational Interviewing: Twenty Five Years of Empirical Studies. Research on Social Work Practice, 20(2), 137-160. — [lien](https://digitalcommons.usu.edu/sswa_facpubs/199)
- **Auteurs, année** : Lundahl, B. et al. ; Itzchakov, G. et al., 2010
- **Résumé** : L'entretien motivationnel, méthode issue de la clinique, repose sur l'écoute, la reformulation et l'évocation des propres raisons de la personne plutôt que sur la confrontation. Une méta-analyse de 119 études (Lundahl et al., 2010) trouve un effet faible mais significatif et durable par rapport à l'absence d'intervention. L'écoute de qualité réduit aussi l'anxiété sociale de l'interlocuteur (Itzchakov et al., 2018).
- **Conditions d’application** : Changements de comportement en santé ; expériences sur l'écoute.
- **Limites** : Transposition aux opinions politiques non démontrée.
- **Niveau de confiance** : moyenne
- **Autres sources de la fiche** : [Université de Haïfa (répertoire de recherche)](https://cris.haifa.ac.il/en/publications/the-listener-sets-the-tone-high-quality-listening-increases-attit/)
- **Consignes qui s’y réfèrent** : Profil neutre : commencer par comprendre ; Objectif : faire réfléchir

### Ce qu'on pense en politique, ça ne vient pas de sa famille.

- **Référence principale** : Jennings, M. K., Stoker, L., & Bowers, J. (2009). Politics across generations: Family transmission reexamined. The Journal of Politics, 71, 782-799. — [lien](https://synapsesocial.com/papers/W1988686891)
- **Auteurs, année** : Jennings, M. K. ; Stoker, L. ; Bowers, J., 2009
- **Résumé** : Les orientations politiques se transmettent en partie dans la famille. L'étude longitudinale de Jennings, Stoker et Bowers (2009) sur trois générations américaines montre une transmission plus forte quand la famille est très politisée et que les parents envoient des signaux stables, et plus forte pour les sujets concrets et chargés d'émotion. Les acquis précoces pèsent sur le parcours politique adulte.
- **Conditions d’application** : Familles américaines suivies sur trois générations.
- **Limites** : Transposition en France non vérifiée ; déterminisme exclu.
- **Niveau de confiance** : élevée
- **Autres sources de la fiche** : [Département de science politique, Université de Californie à Santa Barbara](https://polsci.ucsb.edu/node/203)
- **Consignes qui s’y réfèrent** : C’est un proche

### Les opinions politiques, c'est un choix purement individuel et rationnel.

- **Référence principale** : Jetten, J. (2025). Social Identity. Open Encyclopedia of Cognitive Science. — [lien](https://oecs.mit.edu/pub/qlm9zp9e/download/pdf)
- **Auteurs, année** : Jetten, J. (synthèse) ; Tajfel, H. ; Turner, J., 2025
- **Résumé** : Nos opinions s'inscrivent aussi dans nos appartenances. Les expériences de Tajfel montrent qu'une catégorisation arbitraire suffit à créer du favoritisme envers son groupe. La théorie de l'identité sociale explique pourquoi un désaccord politique peut être vécu comme une menace contre le groupe auquel on appartient. Le contexte compte : la compétition accentue les biais, la coopération les réduit.
- **Conditions d’application** : Appartenances de groupe, contextes compétitifs ou coopératifs.
- **Limites** : Expériences de laboratoire ; hypothèse de l'estime de soi abandonnée.
- **Niveau de confiance** : élevée
- **Autres sources de la fiche** : [Behavioural Public Policy (Cambridge University Press)](https://www.cambridge.org/core/journals/behavioural-public-policy/article/abs/motivated-numeracy-and-enlightened-selfgovernment/EC9F2410D5562EF10B7A5E2539063806)
- **Consignes qui s’y réfèrent** : Elle est très attachée à son camp

### Les gens de droite ont peur de tout, c'est biologique.

- **Référence principale** : Bakker, B. N., Schumacher, G., Gothreau, C., & Arceneaux, K. (2020). Conservatives and liberals have similar physiological responses to threats. Nature Human Behaviour. — [lien](https://uva.nl/en/content/news/press-releases/2020/02/replication-study-contradicts-claim-that-conservatives-have-stronger-physiological-responses-to-threats-than-liberals.html)
- **Auteurs, année** : Bakker, B. N. et al., 2020
- **Résumé** : Une étude de 2008 (46 participants) avait rapporté des réactions physiologiques plus fortes aux images menaçantes chez les conservateurs. Une réplication plus large publiée en 2020 dans Nature Human Behaviour ne trouve aucune relation entre orientation politique et réaction physiologique. L'explication « biologique » des opinions politiques ne tient pas sur cette base.
- **Conditions d’application** : Mesures physiologiques face à des images menaçantes.
- **Limites** : Ne dit rien de l'ensemble des travaux sur menace et opinions.
- **Niveau de confiance** : moyenne
- **Consignes qui s’y réfèrent** : Elle tient à l’ordre et à la sécurité

### Convaincre, c'est forcément manipuler.

- **Référence principale** : Noggle, R. The Ethics of Manipulation. Stanford Encyclopedia of Philosophy. — [lien](https://plato.stanford.edu/Entries/ethics-manipulation/)
- **Auteurs, année** : Noggle, R., 2018
- **Résumé** : La philosophie distingue la persuasion rationnelle (donner de bonnes raisons), la coercition (forcer ou menacer) et la manipulation, qui se situe entre les deux. Selon les approches recensées par la Stanford Encyclopedia of Philosophy, la manipulation contourne la raison, trompe ou exerce une pression non coercitive. Informer, débattre et persuader honnêtement ne sont pas manipuler.
- **Conditions d’application** : Philosophie morale : distinction persuasion, manipulation, coercition.
- **Limites** : Aucune définition de la manipulation ne fait consensus.
- **Niveau de confiance** : élevée
- **Consignes qui s’y réfèrent** : Règle de base

### Avec un bon argument, il changera d'avis d'un coup.

- **Référence principale** : Kalla, J. L., & Broockman, D. E. (2020). Reducing exclusionary attitudes through interpersonal conversation: Evidence from three field experiments. American Political Science Review, 114(2), 410-425. — [lien](https://isps.yale.edu/research/publications/isps20-01)
- **Auteurs, année** : Kalla, J. L. ; Broockman, D. E., 2020
- **Résumé** : Les effets de la persuasion politique mesurés dans les expériences sont réels mais modestes. Les conversations les plus efficaces observées par Kalla et Broockman (2020) réduisent les attitudes d'exclusion d'environ 0,08 écart-type, durablement, et uniquement quand elles incluent un échange de récits personnels ; les arguments seuls n'ont eu aucun effet. Changer d'avis est un processus lent.
- **Conditions d’application** : Conversations en face à face, porte-à-porte, États-Unis.
- **Limites** : Effets faibles (d de 0,04 à 0,08) ; sujets précis (immigration, personnes transgenres).
- **Niveau de confiance** : élevée
- **Autres sources de la fiche** : [University of Chicago Press](https://press.uchicago.edu/ucp/books/book/chicago/P/bo181475008.html)
- **Consignes qui s’y réfèrent** : Elle aime la confrontation ; Elle raisonne par l’expérience ou l’exemple ; C’est une simple connaissance ; Objectif : faire évoluer une opinion

### Discuter entre gens du même avis, ça permet de réfléchir plus calmement.

- **Référence principale** : Strandberg, K., Himmelroos, S., & Grönlund, K. (2019). Do discussions in like-minded groups necessarily lead to more extreme opinions? Deliberative democracy and group polarization. International Political Science Review, 40(1), 41-57. — [lien](https://research.abo.fi/en/publications/do-discussions-in-like-minded-groups-necessarily-lead-to-more-ext/)
- **Auteurs, année** : Strandberg, K. ; Himmelroos, S. ; Grönlund, K., 2019
- **Résumé** : Discuter uniquement entre personnes du même avis peut rendre les opinions plus extrêmes (polarisation de groupe). Une expérience finlandaise (Strandberg, Himmelroos et Grönlund, 2019) montre que la discussion libre entre personnes du même avis polarise, alors que des groupes qui suivent des règles délibératives (écoute, arguments justifiés, respect) évitent cette polarisation.
- **Conditions d’application** : Discussions de groupes homogènes, Finlande, en face à face et en ligne.
- **Limites** : Une seule expérience ; résumé consulté.
- **Niveau de confiance** : moyenne
- **Consignes qui s’y réfèrent** : Elle cherche surtout à provoquer ; D’autres personnes écoutent ; Objectif : répondre à une attaque

### Ce sont les gens d'en face qui sont biaisés, pas nous.

- **Référence principale** : Ditto, P. H., et al. (2019). At least bias is bipartisan: A meta-analytic comparison of partisan bias in liberals and conservatives. Perspectives on Psychological Science. — [lien](https://www.psychologicalscience.org/publications/observer/obsonline/bias-is-blind-partisan-prejudice-across-the-political-spectrum.html)
- **Auteurs, année** : Ditto, P. H. et al. ; Kahan, D. M. et al., 2019
- **Résumé** : Le raisonnement motivé consiste à juger une information plus favorablement quand elle soutient ce que l'on pense déjà. Une méta-analyse de 51 expériences (Ditto et al.) trouve des biais partisans de degré voisin chez les progressistes et les conservateurs, résultat contesté par d'autres chercheurs. Une expérience de Kahan et al. (2017) montre que les plus à l'aise avec les chiffres peuvent être les plus polarisés sur un sujet politisé.
- **Conditions d’application** : Évaluation d'informations politisées, surtout aux États-Unis.
- **Limites** : Égalité des biais entre camps contestée (Baron et Jost, 2019).
- **Niveau de confiance** : moyenne
- **Autres sources de la fiche** : [Behavioural Public Policy (Cambridge University Press)](https://www.cambridge.org/core/journals/behavioural-public-policy/article/abs/motivated-numeracy-and-enlightened-selfgovernment/EC9F2410D5562EF10B7A5E2539063806)
- **Consignes qui s’y réfèrent** : Elle aime les chiffres ou la logique ; Elle connaît bien le sujet

### Si j'insiste assez, il finira par céder.

- **Référence principale** : Rains, S. A. (2013). The nature of psychological reactance revisited: A meta-analytic review. Human Communication Research, 39(1), 47-73. — [lien](https://academic.oup.com/hcr/article-abstract/39/1/47/4093682)
- **Auteurs, année** : Rains, S. A., 2013
- **Résumé** : La réactance psychologique désigne la résistance qui apparaît quand une personne sent sa liberté de penser ou d'agir menacée. Une méta-analyse de 20 études (Rains, 2013) la décrit comme un mélange de colère et de contre-arguments. Insister, ordonner ou culpabiliser tend donc à renforcer la résistance plutôt qu'à la vaincre.
- **Conditions d’application** : Messages persuasifs perçus comme contraignants, surtout en santé publique ; mesures à court terme.
- **Limites** : Méta-analyse de 20 études ; peu d'études en face à face sur la politique.
- **Niveau de confiance** : élevée
- **Consignes qui s’y réfèrent** : Elle se braque facilement

### Les arguments qui me convainquent convaincront tout le monde.

- **Référence principale** : Framing persuasive messages : présentation de Feinberg & Willer (2015), Personality and Social Psychology Bulletin — [lien](https://news.stanford.edu/stories/2015/10/framing-persuasive-messages-101215)
- **Auteurs, année** : Feinberg, M. ; Willer, R., 2015
- **Résumé** : Les gens n'accordent pas tous la même importance aux mêmes valeurs morales. Feinberg et Willer (2015) montrent que les arguments reformulés dans les valeurs de l'interlocuteur sont plus persuasifs, alors que spontanément chacun argumente avec ses propres valeurs. La théorie des fondements moraux qui sous-tend ces travaux a été révisée (égalité et proportionnalité distinguées) et reste discutée.
- **Conditions d’application** : Messages écrits adressés au camp opposé, États-Unis.
- **Limites** : Tendances moyennes ; théorie révisée (MFQ-2) ; risque de paraître opportuniste.
- **Niveau de confiance** : moyenne
- **Autres sources de la fiche** : [PsyPost](https://www.psypost.org/decoding-morality-across-cultures-insights-from-a-mega-study-of-moral-foundations-theory/)
- **Consignes qui s’y réfèrent** : Elle est pragmatique ; Elle est réformiste ; Elle est favorable aux ruptures ; Elle tient à la justice sociale ; Elle tient au mérite ou à la liberté ; Elle tient à la nation, à la tradition ou à son groupe ; Objectif : trouver un terrain d’entente

## 6. Données personnelles

- Les réponses au questionnaire servent au calcul puis restent dans la page ; **aucun profil n’est enregistré automatiquement**. L’enregistrement d’un profil (sous un surnom libre, sans nom réel requis) est une action explicite, limitée à 12 profils, sur cet appareil uniquement (localStorage).
- La discussion en cours (faits déjà utilisés, retours) et la liste des fiches récemment consultées sont gardées en sessionStorage et disparaissent à la fermeture de l’onglet.
- La page « Mes données » liste tout ce qui est stocké et permet de supprimer chaque élément ou tout effacer.
- En mode autonome, rien n’est envoyé sur le réseau. En mode connecté, le profil nettoyé (options prédéfinies seulement, jamais de texte libre identifiant) est transmis au serveur pour la requête en cours et n’est pas conservé.

## 7. Limites

- Le moteur adapte la **présentation** de faits vérifiés ; il ne peut pas être plus riche que la fiche (une fiche de trois faits limite la variété possible).
- L’interprétation du texte libre des retours repose sur des mots-clés : elle peut se tromper, et l’utilisateur peut toujours choisir le bon bouton.
- Les profils sont des hypothèses de l’utilisateur sur une personne, jamais un diagnostic ; les règles décrivent des tendances moyennes observées dans la recherche, qui peuvent ne pas s’appliquer à une personne donnée.
- Aucune efficacité persuasive n’a été mesurée sur de vraies personnes.
