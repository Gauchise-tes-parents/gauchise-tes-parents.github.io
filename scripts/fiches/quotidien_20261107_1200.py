"""Fiches quotidiennes du 7 novembre 2026, passage de 12 h (UTC) — phase alpha.

25 questions qui circulent (extrême droite, clichés sur la gauche, programmes) et qui n'avaient pas de fiche
qui leur réponde vraiment. Toutes les sources ont été ouvertes et lues le 7 novembre 2026 (consultee=True) ;
les chiffres viennent uniquement des passages cités. Données anciennes signalées dans les limites.
Chaque fiche contient les réponses selon le public (« publics » : électeur d'extrême droite convaincu / indécis).
Usage : python3 scripts/fiches/quotidien_20261107_1200.py  (puis node scripts/corrections-v10.js et node scripts/enrichir-fiches.js)
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from reponses_directes import src, fait, fiche as _fiche, OUT

TODAY = '2026-11-07'

def fiche(**k):
    d = _fiche(**k)
    d['derniere_verification'] = TODAY
    return d

# ── Sources : Europe et institutions ───────────────────────────────────────
PS_80 = ('ps_80', src("Check Point : 80 % de nos lois sont-elles imposées par l'Union européenne ?", "Public Sénat (Thomas Mignon)", "14 mars 2017 (mis à jour le 27 avril 2017)",
  "https://www.publicsenat.fr/actualites/politique/check-point-80-de-nos-lois-sont-elles-imposees-par-l-union-europeenne-57198",
  "Selon Yves Bertoncini (Notre Europe, 2009), au 1er juillet 2008, 9 685 actes européens étaient en vigueur, soit 28,1 % des 34 476 normes applicables en France. Selon Brouard, Costa et Kerrouche (Sciences Po Bordeaux, 2012), la part des lois « européanisées » passe de moins de 3 % en 1986 à 13,3 % en 2006, avec 39 % dans le secteur scientifique, technologique et spatial et environ 24 % en agriculture ; « dans 80% des cas, les lois françaises sont adoptées en marge de toute contrainte européenne directe ». Le chiffre de 80 % vient d'une prévision de Jacques Delors (1988).",
  "Fact-check d'un média parlementaire reprenant deux études universitaires.", 'media'))
EN_80 = ('en_80', src("Fact-check: Does the EU decide 80% of our laws?", "Euronews (Sophia Khatsenkova)", "22 mars 2024",
  "https://www.euronews.com/my-europe/2024/03/22/fact-check-does-the-eu-decide-80-of-our-laws",
  "Une étude française de 2009 situe l'influence de l'UE « more like 20-25% » ; la part dépasse 50 % dans l'agriculture, l'environnement et l'économie, et elle est bien plus faible pour l'emploi, la sécurité intérieure ou la santé. Jacques Delors avait annoncé que d'ici 2000, « 80% of economic legislation will be of Community origin ».",
  "Fact-check d'un média européen.", 'media'))
CE_RN = ('ce_rn', src("Décision n° 488378 (association Rassemblement national)", "Conseil d'État", "11 mars 2024",
  "https://conseil-etat.fr/fr/arianeweb/CE/decision/2024-03-11/488378",
  "Le Conseil d'État rejette la requête du RN contre la circulaire du ministre de l'Intérieur qui classe la nuance RN dans le bloc « extrême droite » : il ne relève pas d'erreur manifeste d'appréciation et juge que « la circulaire attaquée ne méconnaît pas le principe de sincérité du scrutin ». « La requête de l'association Rassemblement national est rejetée. »",
  "Décision de la plus haute juridiction administrative."))
CDJ_RN = ('cdj_rn', src("Le Conseil d'Etat a-t-il qualifié le RN « d'extrême-droite » ?", "Le Club des juristes (Arnaud Gossement, université Paris I)", "28 juin 2024",
  "https://www.leclubdesjuristes.com/justice/le-conseil-detat-a-t-il-qualifie-le-rn-dextreme-droite-6426/",
  "« le Conseil d'Etat n'a pas affirmé que le RN est d'extrême-droite » : son contrôle était limité à l'erreur manifeste d'appréciation de la circulaire, et il n'a pas qualifié de manière générale la sensibilité politique des partis.",
  "Analyse juridique universitaire.", 'etude'))
SCPO_RN = ('scpo_rn', src("Présidentielle : les démocraties à l'épreuve de l'extrême droite en France et en Europe", "Sciences Po (Nonna Mayer, Florence Haegel)", "22 avril 2022",
  "https://www.sciencespo.fr/fr/actualites/actualit%C3%A9s/presidentielle-les-democraties-a-l-epreuve-de-l-extreme-droite-en-france-et-en-europe/7275",
  "Pour la politiste Nonna Mayer, Marine Le Pen a « véritablement “ripoliné” le parti », mais « rien n'a vraiment changé » sur le fond : la priorité nationale reste au cœur du programme. Florence Haegel rappelle : « C'est un parti qui est tout à fait légal ».",
  "Analyse de chercheuses en science politique (2022).", 'etude'))
LCP_RN_IMMI = ('lcp_rn_immi', src("Législatives 2024 : le programme du Rassemblement national en matière d'immigration à l'épreuve de la Constitution", "LCP (Raphaël Marchal)", "28 juin 2024",
  "https://lcp.fr/actualites/legislatives-2024-le-programme-du-rassemblement-national-en-matiere-d-immigration-a-l",
  "Le RN veut « mettre en place la priorité nationale » (si nécessaire par référendum constitutionnel) et réserver les allocations familiales aux Français. Laurent Fabius, président du Conseil constitutionnel, a déclaré que la « préférence nationale, appliquée de façon systématique, est contraire à la Constitution ».",
  "Média parlementaire.", 'media'))
LANDOT = ('landot', src("Nuançage politique et tâtonnements juridiques (mise à jour au 3 mars 2026)", "Blog Landot & associés (Éric Landot, avocat)", "3 mars 2026",
  "https://blog.landot-avocats.net/2026/03/03/nuancage-politique-et-tatonnements-juridiques-video-et-article-mise-a-jour-au-3-mars-2026-apres-la-non-censure-du-classement-du-rn-certes-mais-aussi-de-lfi-et-de-ludr-dans-les-extrem/amp/",
  "Par une décision du 27 février 2026 (n° 512694), le Conseil d'État a jugé que le classement de LFI à « l'extrême gauche » dans la circulaire des municipales n'était pas manifestement erroné, et a validé le classement de l'UDR à « l'extrême droite ».",
  "Commentaire d'avocat spécialiste du droit public.", 'secondaire'))
LCP_LEPEN = ('lcp_lepen', src("Marine Le Pen condamnée dans l'affaire des assistants parlementaires, reste éligible pour 2027", "LCP", "7 juillet 2026",
  "https://lcp.fr/actualites/marine-le-pen-condamnee-dans-l-affaire-des-assistants-parlementaires-reste-eligible-pour",
  "En appel, Marine Le Pen est condamnée à « trois ans de prison dont deux avec sursis », 100 000 € d'amende et « une peine d'inéligibilité de 45 mois, dont 30 avec sursis » ; les 15 mois fermes ont déjà été exécutés. Elle reste éligible pour 2027. Elle a toujours contesté les accusations en dénonçant une décision politique.",
  "Média parlementaire.", 'media'))
TE_LEPEN = ('te_lepen', src("Procès de Marine Le Pen : tout savoir sur l'affaire des assistants du RN au Parlement européen", "Toute l'Europe", "Mis à jour le 7 juillet 2026",
  "https://www.touteleurope.eu/institutions/qu-est-ce-que-l-affaire-des-assistants-du-rn-au-parlement-europeen/",
  "Jugement du 31 mars 2025 : quatre ans de prison dont deux ferme, cinq ans d'inéligibilité avec exécution provisoire ; montant détourné d'« environ 2,9 millions d'euros » selon le tribunal. Procès en appel du 13 janvier au 12 février 2026, arrêt le 7 juillet 2026 ; le RN, personne morale, est condamné à 2 M€ d'amende dont 1 M€ avec sursis ; Marine Le Pen forme un pourvoi en cassation.",
  "Site d'information européenne.", 'media'))
SIMONNET = ('simonnet', src("L'arrêt Marine Le Pen/assistants parlementaires du 7 juillet 2026 expliqué par un avocat", "Valentin Simonnet, avocat au barreau de Paris", "8 juillet 2026",
  "https://www.simonnetavocat.fr/larret-marine-le-pen-assistants-parlementaires-du-7-juillet-2026-explique-par-un-avocat/",
  "La cour d'appel confirme la culpabilité des 12 appelants ; les 28 contrats ont été examinés un par un, avec des relaxes partielles ; le préjudice financier du Parlement européen est fixé à 1 943 696,31 € ; l'absence d'enrichissement personnel est prise en compte pour la peine. L'arrêt n'est pas assorti d'exécution provisoire et le pourvoi en cassation est suspensif.",
  "Commentaire juridique d'un avocat.", 'secondaire'))
LCP_QPC = ('lcp_qpc', src("Inéligibilité : qu'a décidé le Conseil constitutionnel sur la QPC avant la décision de la justice concernant Marine Le Pen ?", "LCP (Anne-Charlotte Dusseaulx)", "28 mars 2025",
  "https://lcp.fr/index%2Ephp/actualites/ineligibilite-qu-a-decide-le-conseil-constitutionnel-sur-la-qpc-avant-la-decision-de-la",
  "Saisi d'une QPC posée pour un élu de Mayotte, le Conseil constitutionnel déclare conformes à la Constitution les articles du code électoral en cause, avec une réserve : le juge doit « apprécier le caractère proportionné de l'atteinte » que l'exécution provisoire porte notamment à « la préservation de la liberté de l'électeur ».",
  "Média parlementaire.", 'media'))
PS_LFI_UE = ('ps_lfi_ue', src("LFI : un des fondateurs critique l'« hégémonie » de Mélenchon et sa « posture électoraliste » sur l'Europe", "Public Sénat", "24 août 2018",
  "https://www.publicsenat.fr/actualites/politique/lfi-un-des-fondateurs-critique-l-hegemonie-de-melenchon-et-sa-posture",
  "En 2017, le « plan A » de LFI prévoyait de « désobéir » aux traités européens et le « plan B » une sortie de l'euro, voire de l'UE, en cas d'échec de la renégociation. Selon un cofondateur du mouvement, « Le plan B est donc devenu caduc », LFI se disant désormais favorable à l'euro.",
  "Média parlementaire (2018).", 'media'))
TN_LFI = ('tn_lfi', src("Protestataire ou euro-critique ? La stratégie européenne de La France insoumise", "La Grande Conversation (Terra Nova, Louis Andrieu)", "15 mai 2024",
  "https://www.lagrandeconversation.com/app/uploads/2024/05/protestataire-ou-euro-critique-la-strategie-europeenne-de-la-france-insoumise-la-grande-conversation.pdf",
  "En 2022, « cette menace de sortie se transforma en stratégie de désobéissance » (veto, contribution au budget européen conditionnée). En 2024, LFI défend une refonte des traités par la procédure de l'article 48 du traité sur l'UE et vote contre le nouveau cadre budgétaire européen.",
  "Analyse d'un think tank (centre gauche).", 'etude'))
LCP_NFP = ('lcp_nfp', src("Accord à gauche : retraites, salaires, fiscalité, international… Que contient le « programme de gouvernement » du Nouveau Front populaire ?", "LCP (Soizic Bonvarlet)", "14 juin 2024 (mis à jour le 19 juin 2024)",
  "https://lcp.fr/actualites/accord-a-gauche-retraites-salaires-fiscalite-international-que-contient-le-programme-de",
  "Sur l'Europe, le programme prévoit de « refuser le pacte de stabilité budgétaire » ; il ne prévoit pas de sortie de l'Union. Bruno Le Maire y voit « l'assurance […] de la sortie de l'Union européenne », une appréciation de sa part et non un engagement du programme.",
  "Média parlementaire.", 'media'))
EN_NFP_UE = ('en_nfp_ue', src("Les programmes du RN et du NFP sont-ils compatibles avec les règles de l'UE ?", "Euronews", "1er juillet 2024",
  "https://fr.euronews.com/2024/07/01/les-programmes-du-rn-et-du-nfp-sont-ils-compatibles-avec-les-regles-de-lue",
  "« Le programme du NFP pourrait créer des tensions à Bruxelles sur les questions budgétaires. » Selon l'analyste Éric Maurice, les partis du NFP ne remettent pas frontalement en cause l'engagement européen de la France ; le NFP propose la fin des traités de libre-échange et une réforme de la PAC.",
  "Média européen.", 'media'))
# ── Sources : laïcité ─────────────────────────────────────────────────────
CE_CANTINE = ('ce_cantine', src("Menus de substitution dans les cantines scolaires (commune de Chalon-sur-Saône) — communiqué", "Conseil d'État", "11 décembre 2020",
  "https://conseil-etat.fr/Media/actualites/documents/2020/12-decembre/cp-menus-de-substitution",
  "« il n'est ni obligatoire ni interdit pour les collectivités territoriales de proposer aux élèves des repas différenciés » ; elles doivent veiller à ce que « tous les enfants puissent accéder à ce service public ». La délibération de 2015 supprimant les menus de substitution est annulée parce qu'elle n'était fondée que sur les principes de laïcité et de neutralité.",
  "Communiqué de la plus haute juridiction administrative."))
AFP_CANTINE = ('afp_cantine', src("Proposer des menus sans porc à la cantine ne contrevient pas à la laïcité, juge le Conseil d'État (dépêche AFP)", "AFP (revue de presse de l'académie de Normandie)", "11 décembre 2020",
  "https://media.ac-normandie.fr/-/communication/revue-presse/2020/12/14/AFP_nat_ok_20201211_Proposer%20des%20menus%20sans%20porc%20%e0%20la%20cantine%20ne%20contrevient%20pas%20%e0%20la%20la%efcit%e9,%20juge%20le%20Conseil%20d'%c9tat.PDF",
  "À Chalon-sur-Saône, des menus de substitution existaient depuis 1984 ; le maire (LR) les a supprimés en 2015 et déclare : « Je ne rétablirai pas les menus de substitution dans les cantines scolaires de Chalon ». Les juges ne lui imposent pas de les rétablir.",
  "Dépêche d'agence de presse.", 'media'))
CNCDH_CANTINE = ('cncdh_cantine', src("Génération Laïcité — La laïcité en pratique pour les collégiens (questions-réponses)", "Commission nationale consultative des droits de l'homme (CNCDH)", "2017 (fichier mis en ligne en octobre 2023)",
  "https://www.cncdh.fr/sites/default/files/2023-10/Questionsr%C3%A9ponses%20g%C3%A9n%C3%A9ration%20laicit%C3%A9%20V2.pdf",
  "La cantine est un « service public administratif facultatif » ; « la cantine n'est pas obligée de fournir un repas de substitution lorsqu'il y a de la viande de porc au menu » ; selon une circulaire de 2011, les menus confessionnels ne constituent « ni un droit pour les usagers ni une obligation pour les collectivités ».",
  "Autorité administrative indépendante.", 'secondaire'))
BDT_VEGE = ('bdt_vege', src("Lancement du repas végétarien hebdomadaire dans les cantines scolaires", "Banque des Territoires (Localtis)", "31 octobre 2019",
  "https://www.banquedesterritoires.fr/lancement-du-repas-vegetarien-hebdomadaire-par-semaine-dans-les-cantines-scolaires",
  "Les cantines scolaires doivent servir « un repas végétarien hebdomadaire », « conformément à ce qui est prévu par la loi Egalim » (expérimentation lancée à l'automne 2019).",
  "Média des collectivités (Caisse des dépôts).", 'secondaire'))
PS_VOILE26 = ('ps_voile26', src("Sanctionner le port du voile par une amende : le RN maintient sa proposition polémique et inconstitutionnelle", "Public Sénat (Simon Barbarit)", "31 août 2026",
  "https://www.publicsenat.fr/actualites/politique/sanctionner-le-port-du-voile-par-une-amende-le-rn-maintient-sa-proposition-polemique-et-inconstitutionnelle",
  "Le député RN Jean-Philippe Tanguy confirme vouloir « sanctionner le port du voile » par « une amende », mesure qui figurera au programme de 2027. Pour le juriste Mathieu Carpentier (université Toulouse Capitole), « Interdire le voile n'a aucun lien avec la politique sociale de la nation », ce qui exclut le référendum de l'article 11 ; pour Nicolas Hervieu (Sciences Po), une telle interdiction violerait les articles 9 et 14 de la Convention européenne des droits de l'homme.",
  "Média parlementaire.", 'media'))
PS_VOILE_REF = ('ps_voile_ref', src("Interdiction du voile : en envisageant la piste d'un référendum, Marine Le Pen met la pression sur le Conseil constitutionnel", "Public Sénat (Simon Barbarit)", "16 juillet 2026",
  "https://www.publicsenat.fr/actualites/politique/interdiction-du-voile-en-envisageant-la-piste-dun-referendum-marine-le-pen-met-la-pression-sur-le-conseil-constitutionnel",
  "La proposition de loi RN de 2021 « visant à combattre les idéologies islamistes » visait, dans l'espace public, les signes ou tenues constituant une affirmation ostentatoire de cette idéologie. Après la dissolution de 2024, Jordan Bardella avait retiré la mesure du programme, proposant de commencer par les « bâtiments publics », la rue restant « un objectif à terme ». Depuis 1962, le Conseil constitutionnel ne contrôle pas les lois adoptées par référendum.",
  "Média parlementaire.", 'media'))
PS_VOILE22 = ('ps_voile22', src("Interdiction du voile : la proposition de Marine Le Pen est-elle applicable ?", "Public Sénat (Simon Barbarit)", "19 avril 2022",
  "https://www.publicsenat.fr/actualites/politique/interdiction-du-voile-la-proposition-de-marine-le-pen-est-elle-applicable-203096",
  "Pour le constitutionnaliste Jean-Philippe Derosier, « dans l'espace public, l'interdiction du voile serait disproportionnée ». En 2016, le Conseil d'État a jugé les arrêtés anti-burkini constitutifs d'« une atteinte grave et manifestement illégale aux libertés fondamentales ».",
  "Média parlementaire (2022).", 'media'))
CEDH_SAS = ('cedh_sas', src("Arrêt de Grande Chambre S.A.S. c. France (requête n° 43835/11) — communiqué du greffier CEDH 191 (2014)", "Cour européenne des droits de l'homme", "1er juillet 2014",
  "https://ccme.org.ma/wp-content/uploads/2014/07/CEDH.pdf",
  "Pas de violation des articles 8 et 9 : la préservation des conditions du « vivre ensemble » est un objectif légitime. La loi de 2010 « n'est pas explicitement fondée sur la connotation religieuse des vêtements mais sur le seul fait qu'ils dissimulent le visage » et « n'affecte pas la liberté de porter dans l'espace public des habits ou éléments vestimentaires » qui ne dissimulent pas le visage.",
  "Communiqué officiel de la Cour (copie hébergée par un organisme public marocain)."))
CE_INCLUSIVE = ('ce_inclusive', src("L'interdiction de recourir à certains éléments de l'écriture inclusive, notamment le point médian, pour l'enseignement est légale (décision n° 474812-487671)", "Conseil d'État", "20 décembre 2024",
  "https://conseil-etat.fr/actualites/l-interdiction-de-recourir-a-certains-elements-de-l-ecriture-inclusive-notamment-le-point-median-pour-l-enseignement-est-legale",
  "La circulaire du 5 mai 2021 « proscrit l'usage et l'enseignement de certaines règles relevant de l'écriture inclusive, et notamment le point médian » ; elle demande aux enseignants de féminiser systématiquement les noms de fonctions. Le Conseil d'État retient l'objectif de faciliter l'apprentissage de la lecture et rejette le recours.",
  "Décision de la plus haute juridiction administrative."))
SENAT_INCLUSIVE = ('senat_inclusive', src("L'essentiel — Proposition de loi visant à interdire l'usage de l'écriture inclusive", "Sénat", "25 octobre 2023 (mis à jour le 30 octobre 2023)",
  "https://www.senat.fr/lessentiel/ppl21-404.pdf",
  "La circulaire du Premier ministre du 21 novembre 2017 ne vise que les actes publiés au Journal officiel ; la circulaire de 2021 proscrit l'écriture inclusive dans les pratiques d'enseignement. Le Sénat relève une progression de cet usage à l'université et veut étendre l'interdiction aux cours, examens, thèses et mémoires.",
  "Document du Sénat."))
PS_INCLUSIVE = ('ps_inclusive', src("Le Sénat adopte à une large majorité une proposition de loi pour interdire l'écriture inclusive", "Public Sénat", "31 octobre 2023",
  "https://www.publicsenat.fr/actualites/parlementaire/le-senat-adopte-a-une-large-majorite-une-proposition-de-loi-pour-interdire-lecriture-inclusive",
  "Texte adopté le 30 octobre 2023 par 221 voix contre 82 ; la double flexion (« les Françaises et les Français ») n'est pas interdite ; son adoption à l'Assemblée est jugée « loin d'être sûre ».",
  "Média parlementaire.", 'media'))
# ── Sources : énergie, dette, économie ─────────────────────────────────────
RTE_FE = ('rte_fe', src("Futurs énergétiques 2050 — Résumé exécutif", "RTE (fichier hébergé par Vie publique)", "25 octobre 2021",
  "https://vie-publique.fr/files/rapports/fichiers_joints/282232-resume-executif.pdf",
  "Le scénario M0 (« Sortie du nucléaire en 2050 ») suppose environ 208 GW de solaire, 74 GW d'éolien terrestre et 62 GW d'éolien en mer. Son coût peut s'approcher de celui des scénarios avec nouveaux réacteurs sous plusieurs conditions (éolien flottant, financement favorable, système hydrogène compétitif), mais il reste le plus coûteux ; « Se passer de nouveaux réacteurs nucléaires implique des rythmes de développement des énergies renouvelables » plus rapides que ceux des pays européens les plus dynamiques. La France dépendrait de ses voisins pour sa sécurité d'approvisionnement environ 5 % du temps, contre 1 % aujourd'hui.",
  "Gestionnaire public du réseau de transport d'électricité (données de 2021)."))
LCP_RTE = ('lcp_rte', src("Pour le patron de RTE « Construire de nouveaux réacteurs nucléaires est pertinent du point de vue économique »", "LCP (Ariel Guez)", "27 octobre 2021",
  "https://lcp.fr/actualites/pour-le-patron-de-rte-construire-de-nouveaux-reacteurs-nucleaires-est-pertinent-du-point",
  "Le président de RTE indique que tous les scénarios garantissent la sécurité d'approvisionnement ; en coûts complets, les scénarios avec nouveau nucléaire reviendraient environ 10 Md€ par an moins cher en 2050 ; il faut au minimum multiplier le solaire par 7 et l'éolien terrestre par 2,5 ; « La France consommera plus d'électricité en 2050 ».",
  "Média parlementaire (audition de 2021).", 'media'))
RTE_2026 = ('rte_2026', src("Réactualisation des Futurs énergétiques 2050 — synthèse de la consultation publique", "RTE", "3 avril 2026",
  "https://assets.rte-france.com/prod/public/2026-04/RTE-Reactualisation-FE-2050-consultation-publique-2026-synthese.pdf",
  "Les hypothèses retenues tendent à rehausser les trajectoires de consommation d'électricité ; les rythmes récents du photovoltaïque conduisent à lever certains doutes sur la capacité de l'industrie ; le document envisage une prolongation au-delà de 60 ans pour l'essentiel du parc nucléaire ; le scénario sans nouveau nucléaire est maintenu dans l'exercice.",
  "Document du gestionnaire du réseau (2026)."))
REPORTERRE_NUPES = ('reporterre_nupes', src("Climat, nucléaire, justice sociale… le programme de l'union de la gauche et des écologistes dévoilé", "Reporterre", "19 mai 2022",
  "https://reporterre.net/Climat-nucleaire-justice-sociale-le-programme-de-l-union-de-la-gauche-et-des-ecologistes",
  "LFI et les écologistes veulent « planifier le passage à 100 % d'énergies renouvelables et la sortie du nucléaire » ; le PCF défend un mix associant renouvelables et nucléaire ; le PS veut optimiser la durée de vie des centrales ; le point reste non tranché et renvoyé au Parlement.",
  "Média spécialisé dans l'écologie.", 'media'))
EN_DETTE = ('en_dette', src("La dette publique de la zone euro atteint 88,8 % du PIB, l'Italie talonne la Grèce", "Euronews (d'après Eurostat)", "21 octobre 2026",
  "https://fr.euronews.com/2026/10/21/la-dette-publique-de-la-zone-euro-atteint-888-du-pib-litalie-talonne-la-grece",
  "Deuxième trimestre 2026 : Grèce 140,8 % du PIB (−11,2 points sur un an), Italie 139,9 %, France 119,1 % (+3,7 points), Belgique 110,2 %, Espagne 101,4 % ; zone euro 88,8 %. La dette grecque atteignait 177,8 % en 2022.",
  "Média européen reprenant le communiqué d'Eurostat.", 'media'))
EUROSTAT_DETTE = ('eurostat_dette', src("La dette publique à 88,0 % du PIB dans la zone euro (premier trimestre 2025)", "Eurostat", "21 juillet 2025",
  "https://ec.europa.eu/eurostat/fr/web/products-euro-indicators/w/2-21072025-ap",
  "Premier trimestre 2025 : Grèce 152,5 %, Italie 137,9 %, France 114,1 %, Belgique 106,8 %, Espagne 103,5 %, Portugal 96,4 %.",
  "Office statistique de l'Union européenne."))
INSEE_DETTE = ('insee_dette', src("À la fin du deuxième trimestre 2026, le ratio de dette publique s'établit à 119,0 % du PIB (Informations rapides n° 239)", "Insee", "29 septembre 2026",
  "https://www.insee.fr/fr/statistiques/9053525",
  "Dette publique au sens de Maastricht : 3 595,5 Md€, soit 119,0 % du PIB (+59,6 Md€ sur le trimestre) ; dette nette : 3 366,8 Md€ (111,4 % du PIB) ; titres négociables à long terme : 2 937,3 Md€, à court terme : 291,7 Md€.",
  "Statistique publique de référence."))
AFT_DETTE = ('aft_dette', src("Bulletin mensuel n° 435 (août 2026)", "Agence France Trésor", "Août 2026",
  "https://www.aft.gouv.fr/files/medias-aft/7_Publications/7.2_BM/435_Bulletin%20mensuel%20aout%202026.pdf",
  "Au 31 juillet 2026, dette négociable de l'État : 2 882 Md€ ; durée de vie moyenne : 8 ans et 163 jours ; part détenue par les non-résidents : 57,5 % (premier trimestre 2026, Banque de France).",
  "Agence publique chargée de la dette de l'État."))
PS_DETTE = ('ps_dette', src("En 2026, le coût des intérêts de la dette pourrait dépasser le budget de l'Éducation nationale, avertit Pierre Moscovici", "Public Sénat", "8 juillet 2025",
  "https://www.publicsenat.fr/actualites/economie/en-2026-le-cout-des-interets-de-la-dette-pourrait-depasser-le-budget-de-leducation-nationale-avertit-pierre-moscovici",
  "Selon la Cour des comptes, la charge de la dette atteint 60,2 Md€ en 2024 (+7,3 Md€) et pourrait dépasser 100 Md€ avant la fin de la décennie. Pierre Moscovici : « Réduire la dette n'est pas une option, c'est un impératif » ; « Nous risquons de nous trouver confrontés à un véritable effet boule de neige. »",
  "Média parlementaire rapportant la position du premier président de la Cour des comptes.", 'media'))
FPT_FITCH = ('fpt_fitch', src("Agences de notation : la dégradation de la note de la France par Fitch a-t-elle un impact ?", "La finance pour tous (Institut pour l'éducation financière du public)", "17 septembre 2025",
  "https://www.lafinancepourtous.com/2025/09/17/agences-de-notation-la-degradation-de-la-note-de-la-france-par-fitch-a-t-elle-un-impact/",
  "Fitch a abaissé la note de la France de AA- à A+ le 12 septembre 2025 ; le taux à 10 ans s'établit à 3,48 %, proche de celui de l'Italie ; « la France reste un émetteur de bonne qualité », mais son « coussin » de crédibilité s'est réduit.",
  "Association d'éducation financière reconnue d'intérêt général.", 'secondaire'))
INSEE_EURO17 = ('insee_euro17', src("Une inflation modérée depuis le passage à l'euro (Insee Focus n° 87)", "Insee (Marie Leclair, Vladimir Passeron)", "24 mai 2017",
  "https://www.insee.fr/fr/statistiques/2854085",
  "« un impact modéré du passage à l'euro, de l'ordre de + 0,1 % à + 0,2 % sur les prix » ; inflation de 1,4 % par an en moyenne de 2002 à 2016, contre 2,1 % de 1986 à 2001 ; effets d'arrondi plus marqués dans les cafés (+1,5 point) et sur le pain et la pâtisserie (+0,3 point) ; l'opinion des ménages sur l'évolution des prix s'est nettement écartée de l'indice après 2002.",
  "Statistique publique de référence."))
INSEE_EURO02 = ('insee_euro02', src("Un premier bilan de l'effet du passage à l'euro sur les prix (Note de conjoncture)", "Insee (Philippe Gallot)", "Juin 2002",
  "https://insee.fr/fr/statistiques/fichier/1406989/juin2002d1.pdf",
  "Effet d'environ +0,1 point sur l'inflation de janvier 2002, quasi nul en février et mars : l'effet « apparaît pour l'essentiel concentré sur le mois de janvier 2002 » ; les services augmentent de 0,5 % au premier trimestre (restauration, cafés, loisirs, réparation automobile), les cafés-restaurants représentant près de la moitié de l'effet de janvier.",
  "Statistique publique (2002)."))
BDF_EURO = ('bdf_euro', src("L'€uro est-il inflationniste ? (Documents & Débats n° 1)", "Banque de France", "29 janvier 2007",
  "https://www.citeco.fr/sites/default/files/images_spip/documents-et-debats-numero-1-l-euro-est-il-inflationniste.pdf",
  "Hausse des prix d'environ 0,2 % liée au passage à l'euro ; le café en salle augmente de 6 % entre août 2001 et avril 2002 ; l'inflation perçue en France atteint environ le double de l'indice de l'Insee ; de 1996 à 2006, 40 % des ménages ont connu une inflation supérieure à l'indice moyen.",
  "Banque centrale nationale (2007)."))
# ── Sources : politique, histoire ──────────────────────────────────────────
IPSOS_SOCIO = ('ipsos_socio', src("Sociologie des électorats — Législatives 2024 (premier tour)", "Ipsos Talan pour France Télévisions, Radio France et Public Sénat", "30 juin 2024",
  "https://www.ipsos.com/fr-fr/legislatives-2024/node/1025896",
  "Enquête des 27 et 28 juin 2024 auprès de 10 286 personnes. Vote des ouvriers : RN et alliés 57 % (+12 points par rapport à 2022), NFP 21 % ; employés : RN 44 % ; cadres : RN 22 % (11 % en 2022).",
  "Institut de sondage (estimation, marge d'erreur).", 'etude'))
IPSOS_PARTI = ('ipsos_parti', src("Une participation exceptionnelle, dans tous les électorats — Législatives 2024", "Ipsos Talan", "30 juin 2024",
  "https://www.ipsos.com/fr-fr/legislatives-2024/node/1025891",
  "Participation au premier tour : 66,7 % (47,5 % en 2022) ; ouvriers 54 %, employés 58 %, cadres 65 %, retraités 79 %.",
  "Institut de sondage (estimation).", 'etude'))
FJJ_RN = ('fjj_rn', src("Vote Rassemblement national : comment casser la dynamique ?", "Fondation Jean-Jaurès (Bassem Asseh, Adélaïde Zulfikarpasic ; enquête BVA Xsight)", "12 septembre 2024",
  "https://www.jean-jaures.org/publication/vote-rassemblement-national-comment-casser-la-dynamique/",
  "33 % des personnes interrogées estiment que « la gauche a déçu lorsqu'elle était au pouvoir » ; 28 % la jugent déconnectée des classes populaires, 28 % trouvent qu'elle ne parle pas assez de sécurité et 27 % pas assez d'immigration. Les auteurs décrivent une crainte du « grand déclassement » plutôt que du « grand remplacement ».",
  "Fondation proche du Parti socialiste, enquête par sondage.", 'etude'))
HARGREAVES = ('hargreaves', src("La percée du Front national (Hommes & migrations n° 1313)", "Alec G. Hargreaves (Florida State University), revue du Musée national de l'histoire de l'immigration", "2016",
  "https://core.ac.uk/download/223612776.pdf",
  "En décembre 1980, le maire communiste de Vitry, « soutenu par Georges Marchais et le Comité central du PCF », fait bloquer par un bulldozer l'installation de « trois cents travailleurs maliens » ; deux mois plus tard, à Montigny-lès-Cormeilles, un maire communiste dénonce une famille marocaine accusée de trafic de drogue. L'auteur y voit des calculs électoraux qui ont préparé la stigmatisation des immigrés dans l'ensemble de la classe politique.",
  "Article universitaire.", 'etude'))
CSM_1981 = ('csm_1981', src("French Communists' 'bull in a china shop' campaign may win votes", "The Christian Science Monitor (Sophie Fisher)", "16 mars 1981",
  "https://www.csmonitor.com/1981/0316/031649.html",
  "Avant Noël 1980, une cinquantaine de militants communistes menés par le maire enfoncent au bulldozer la porte d'un foyer destiné à des travailleurs maliens et coupent gaz, électricité et eau. À Montigny, l'accusation de trafic de drogue visant un habitant marocain, fondée sur une lettre anonyme, s'est révélée infondée. Le journal juge ce virage incohérent avec la ligne antérieure d'unité des travailleurs français et immigrés.",
  "Presse étrangère de l'époque.", 'media'))
TS_1981 = ('ts_1981', src("Vitry : la boucle est bouclée (Tribune socialiste n° 20)", "Paul Oriol, Tribune socialiste (PSU) — archives de l'Institut Tribune socialiste", "Février 1981",
  "https://www.institut-tribune-socialiste.fr/wp-content/uploads/1981/02/81-02-01-TSMens-ImmigresVitry.pdf",
  "Cite la déclaration de Georges Marchais du 10 janvier 1981 en soutien au maire de Vitry : « J'approuve son refus [...] de laisser s'accroître dans sa commune le nombre élevé de travailleurs immigrés », et la critique : « Cela ne justifie pas les moyens employés contre les travailleurs maliens ».",
  "Journal d'un parti de gauche de l'époque (source engagée, citée pour la citation et la réaction à gauche).", 'secondaire'))
IGA_EMEUTES = ('iga_emeutes', src("Analyse des profils et motivations des délinquants interpellés lors des violences urbaines du 27 juin au 7 juillet 2023 (rapport définitif)", "Inspection générale de la justice et Inspection générale de l'administration", "Août 2023",
  "https://www.vie-publique.fr/files/rapport/pdf/291024.pdf",
  "Selon le SSMSI, 79 % des mis en cause sont de nationalité française ; 75 % sont nés en France. Sur un échantillon de 395 condamnés, 78 % sont français ; âge moyen 23 ans pour les hommes ; 226 condamnés sur 395 (57 %) n'ont aucun antécédent judiciaire. Les mineurs représentent 28 % des mis en cause enregistrés par les parquets au 31 juillet 2023.",
  "Rapport d'inspections de l'État."))
PS_EMEUTES23 = ('ps_emeutes23', src("Violences urbaines de juin 2023 : moins de 8 % des condamnés font référence à la mort de Nahel pour justifier leur comportement", "Public Sénat (Romain David)", "26 octobre 2023",
  "https://www.publicsenat.fr/actualites/societe/violences-urbaines-de-juin-2023-moins-de-8-des-condamnes-font-reference-a-la-mort-de-nawel-pour-justifier-leur-comportement",
  "Audition des inspecteurs devant la commission des lois du Sénat : profil type d'un « homme de nationalité française », né en France dans 75 % des cas, d'environ 23 ans ; un peu moins d'un tiers des quelque 4 000 auteurs sont mineurs ; 57 % sans antécédent ; les inspecteurs parlent d'une « photographie à l'instant T ».",
  "Média parlementaire.", 'media'))
PS_EMEUTES24 = ('ps_emeutes24', src("Violences urbaines : quel est le profil des émeutiers ?", "Public Sénat (Simon Barbarit)", "11 avril 2024",
  "https://www.publicsenat.fr/actualites/parlementaire/violences-urbaines-quel-est-le-profil-des-emeutiers",
  "Selon le rapport de la commission d'enquête du Sénat, 71 % des émeutiers sont de nationalité française, 91 % sont des hommes, âge moyen 23 ans, près de 60 % sont primo-délinquants ; le rapport juge que « les données disponibles demeurent fort insuffisantes ».",
  "Média parlementaire.", 'media'))
INSEE_IMMI = ('insee_immi', src("Population immigrée et étrangère en France — données annuelles de 1921 à 2025", "Insee", "4 juin 2026",
  "https://www.insee.fr/fr/statistiques/2381757",
  "En 2025 (données provisoires) : 7 970 000 immigrés, soit 11,6 % de la population, et 6 297 000 étrangers, soit 9,1 %, sur 68 852 000 habitants. En 2014 : 6 028 000 immigrés (9,1 %) et 4 289 000 étrangers (6,5 %).",
  "Statistique publique de référence."))
INSEE_DESC = ('insee_desc', src("Immigrés et descendants d'immigrés (France, portrait social, édition 2025)", "Insee", "18 novembre 2025",
  "https://www.insee.fr/fr/statistiques/8612512",
  "En 2024 : 7,6 millions d'immigrés (11,2 % de la population) et 8,0 millions de descendants d'immigrés (12 % de la population vivant en logement ordinaire) ; 34 % des immigrés sont français. Un immigré est « une personne née étrangère à l'étranger et résidant en France ».",
  "Statistique publique de référence."))
INSEE_ETHN = ('insee_ethn', src("Statistiques ethniques", "Insee", "27 août 2020",
  "https://www.insee.fr/fr/information/2108548",
  "Cadre : RGPD, loi Informatique et libertés et décision du Conseil constitutionnel du 15 novembre 2007, qui juge contraire à la Constitution un référentiel ethno-racial. Sont proscrits les variables de race ou de religion dans les fichiers administratifs ; restent possibles les études sur la diversité, les discriminations et l'intégration à partir de données objectives (pays de naissance, nationalité antérieure, origine géographique) et du ressenti d'appartenance. Le recensement collecte le pays de naissance et la nationalité ; l'enquête Trajectoires et Origines (2009, puis 2019-2020) a été réalisée avec l'avis du Cnis et l'accord de la CNIL.",
  "Statistique publique de référence."))
PLEINDROIT_2007 = ('pleindroit_2007', src("À quoi sert encore le Conseil constitutionnel ? (Plein droit n° 76)", "Véronique Champeil-Desplats, professeure de droit public (Paris Nanterre)", "Mars 2008",
  "https://droit.cairn.info/article/PLD_076_0027/pdf?lang=fr",
  "La décision du 15 novembre 2007 censure l'article 63 de la loi sur l'immigration ; les traitements nécessaires aux études sur la diversité des origines, la discrimination et l'intégration « peuvent porter sur des données objectives » mais « ne sauraient [...] reposer sur l'origine ethnique ou la race ».",
  "Analyse juridique universitaire.", 'etude'))
INSEE_TEO_SENT = ('insee_teo_sent', src("Ressentis par rapport à la migration et sentiment d'intégration (Immigrés et descendants d'immigrés en France, édition 2023, fiche 6.6)", "Insee (enquête Trajectoires et Origines 2, Ined-Insee, 2019-2020)", "30 mars 2023",
  "https://www.insee.fr/fr/statistiques/fichier/6793304/IMMFRA23-F41.pdf",
  "France métropolitaine, 18-59 ans : « Je me sens chez moi en France » : d'accord pour 95 % des descendants d'immigrés (76 % tout à fait d'accord), 92 % des immigrés et 93 % des personnes sans ascendance migratoire. « On me voit comme un Français » : 20 % des descendants ne sont pas d'accord, 29 à 30 % pour les origines maghrébines et 35 à 39 % pour l'Afrique sahélienne, guinéenne ou centrale, contre 3 % pour l'UE à 27.",
  "Statistique publique de référence (données 2019-2020)."))
INSEE_TEO_DISCRI = ('insee_teo_discri', src("Le sentiment de discrimination persiste à la deuxième génération (France, portrait social, édition 2024)", "Insee et Ined (Odile Rouhban, Pierre Tanneau, Patrick Simon)", "21 novembre 2024",
  "https://www.insee.fr/fr/statistiques/8242403",
  "Traitements inégalitaires ou discriminations déclarés sur cinq ans : 24 % des immigrés et 25 % des descendants d'immigrés ; 34 % des descendants d'origine non européenne (35 % pour le Maghreb, 40 % pour les autres pays d'Afrique) ; 29 % des descendants d'origine non européenne déclarent un « déni de la qualité de Français », contre 8 % des descendants d'origine européenne.",
  "Statistique publique de référence (données 2019-2020)."))
INED_TEO = ('ined_teo', src("Trajectoires et Origines 2 : diversité des populations et inégalités sociales en France — dossier de presse", "Ined (dir. Cris Beauchemin, Mathieu Ichou, Patrick Simon), copie hébergée par la Fondation Lilian Thuram", "19 mai 2026",
  "https://www.thuram.org/wp-content/uploads/2026/06/Trajectoires-et-origines-2.DP_.pdf",
  "Enquête auprès de plus de 27 000 personnes de 18 à 59 ans. Se sentent français : 71 % des immigrés, 94 % des descendants de deux parents immigrés, 98 % des descendants d'un couple mixte et 97 % de la population sans ascendance migratoire.",
  "Dossier de presse de l'institut public de recherche (copie d'un tiers, contenu de l'Ined).", 'secondaire'))
# ── Sources : sécurité routière ────────────────────────────────────────────
CC_RADARS = ('cc_radars', src("Analyse de l'exécution budgétaire 2024 — compte d'affectation spéciale « Contrôle de la circulation et du stationnement routiers »", "Cour des comptes", "Avril 2025",
  "https://www.ccomptes.fr/sites/default/files/2025-04/NEB-2024-Controle-circulation-et-stationnement-routiers.pdf",
  "Amendes de la circulation et du stationnement : 2 070 M€ en 2024, dont 658 M€ d'amendes radars non majorées (−14 % par rapport à la prévision). Dépenses : programme 751 (radars et sécurité routière) 341,2 M€ ; programme 754 (collectivités) 735,7 M€ ; programme 755 (désendettement de l'État) 715,1 M€. Seulement 62 % des crédits servent la sécurité routière ; le programme 755 n'a aucun lien avec elle ; la Cour recommande de supprimer le compte.",
  "Juridiction financière."))
SENAT_RADARS = ('senat_radars', src("Rapport général n° 144 (2024-2025), mission « Sécurités » — compte « Contrôle de la circulation »", "Sénat, commission des finances (Bruno Belin)", "21 novembre 2024",
  "https://www.senat.fr/rap/l24-144-329-1/l24-144-329-115.html",
  "Projet de loi de finances pour 2025 : 2,193 Md€ de recettes d'amendes attendues ; 725 M€ affectés au désendettement, soit 38,9 % du compte ; au moins 770 M€ (35,1 %) n'ont aucun lien avec la sécurité ou les infrastructures routières ; architecture jugée « trop complexe ».",
  "Rapport parlementaire."))
AN_RADARS = ('an_radars', src("Question écrite n° 3437 et réponse du ministère de l'Intérieur", "Assemblée nationale / ministère de l'Intérieur", "21 mars 2023",
  "https://questions.assemblee-nationale.fr/dyn/16/questions/QANR5L16QE3437.pdf",
  "5 737 morts sur les routes en 2003, 3 268 dix ans plus tard, 3 219 en 2021 ; une évaluation de 2013 attribue 75 % de la baisse de la mortalité entre 2003 et 2010 au contrôle automatisé ; selon l'Inspection générale de l'administration, « le contrôle sanction automatisé des vitesses a une efficacité avérée » ; « la vitesse est donc le facteur d'accident principal ».",
  "Réponse officielle du ministère compétent."))
SENAT_RADARS17 = ('senat_radars17', src("Rapport d'information n° 644 (2016-2017) sur la politique d'implantation des radars", "Sénat (Vincent Delahaye)", "18 juillet 2017",
  "https://www.senat.fr/rap/r16-644/r16-64410.html",
  "Le rapport reconnaît aux radars « un véritable impact, très positif, sur l'accidentologie et sur la mortalité routière », mais attribue une partie de la baisse aux véhicules et à la prévention, et juge non concluante la corrélation entre le taux d'accident par département et le nombre d'équipements.",
  "Rapport parlementaire (2017)."))
# ── Sources : Europe et alimentation ───────────────────────────────────────
EU_2023_58 = ('eu_2023_58', src("Règlement d'exécution (UE) 2023/58 autorisant les larves d'Alphitobius diaperinus (petit ténébrion) comme nouvel aliment", "Commission européenne (EUR-Lex)", "5 janvier 2023",
  "https://eur-lex.europa.eu/eli/reg/2023/58/oj",
  "Autorise la mise sur le marché des formes congelées, en pâte, séchées et en poudre des larves de petit ténébrion, au profit d'un demandeur (Ynsect NL B.V.) avec protection des données jusqu'au 26 janvier 2028 ; l'étiquette doit porter le nom de l'insecte et la mention d'un risque d'allergie pour les personnes allergiques aux crustacés et aux acariens, à proximité de la liste des ingrédients.",
  "Texte juridique de l'Union européenne."))
CE_INSECTES = ('ce_insectes', src("Petits insectes — Grande utilité. L'UE autorise l'utilisation des insectes comme denrées alimentaires", "Commission européenne (DG Santé)", "2 juin 2021",
  "https://ec.europa.eu/newsroom/sante/items/712990/fr",
  "« c'est aux consommateurs de décider s'ils veulent ou non manger des insectes » ; « ces produits seront clairement étiquetés » ; le ver de farine jaune est le premier insecte autorisé ; la Commission présente les insectes comme une source de protéines plus durable.",
  "Institution européenne (2021)."))
AFP_INSECTES = ('afp_insectes', src("Misinformation swirls over EU edible insects (fact-check)", "AFP via European Newsroom (Laura Mannering et al.)", "22 février 2023",
  "https://europeannewsroom.com/misinformation-swirls-over-eu-edible-insects/",
  "Les autorisations « do not make insect ingredients mandatory in any food product » ; les ingrédients doivent figurer sous leur nom scientifique et usuel, avec un avertissement sur le risque de réaction allergique ; l'EFSA les a jugés sûrs.",
  "Fact-check d'agence de presse.", 'media'))
ALVA_INSECTES = ('alva_insectes', src("Larves séchées de Tenebrio molitor et autres insectes comme denrée alimentaire (fiche, version 4)", "Administration luxembourgeoise vétérinaire et alimentaire (ALVA)", "3 mars 2025",
  "https://securite-alimentaire.public.lu/dam-assets/fr/publications/fiches/insectes.pdf",
  "Autorisations recensées : Tenebrio molitor (2021/882, 2022/169, 2025/89), Locusta migratoria (2021/1975), Acheta domesticus (2022/188, 2023/5), Alphitobius diaperinus (2023/58). Pour les denrées préemballées, le nom de l'insecte doit figurer dans la liste des ingrédients avec une mise en garde contre les réactions allergiques croisées.",
  "Autorité publique de sécurité alimentaire d'un État membre."))
# ── Sources : asile, chômage, social ───────────────────────────────────────
SP_ADA = ('sp_ada', src("En quoi consiste l'allocation pour demandeur d'asile (Ada) ?", "Service-public.gouv.fr (DILA)", "Vérifié le 1er avril 2026",
  "https://www.service-public.gouv.fr/particuliers/vosdroits/F16118",
  "Montant journalier : 6,80 € pour une personne, 10,20 € pour un couple, 13,60 € pour trois personnes, jusqu'à 37,40 € pour dix personnes ; si aucun hébergement n'est proposé, « le montant supplémentaire est de 7,40 € » par jour pour une personne seule. Conditions : ressources inférieures au RSA et acceptation des conditions matérielles d'accueil ; l'allocation est versée sur une carte de paiement délivrée par l'Ofii.",
  "Site officiel de l'administration."))
DREES_RETR = ('drees_retr', src("Les retraités et les retraites — édition 2025 (communiqué)", "DREES", "31 juillet 2025",
  "https://drees.solidarites-sante.gouv.fr/publications-communique-de-presse-documents-de-reference/250731_PANORAMAS-retraites",
  "Fin 2023, la pension moyenne de droit direct « s'élève à 1 666 euros bruts, soit 1 541 euros nets des prélèvements sociaux » ; 17,2 millions de personnes sont retraitées de droit direct.",
  "Service statistique du ministère des Solidarités."))
CNAV_ASPA = ('cnav_aspa', src("Les allocations de solidarité aux personnes âgées (Aspa) et allocations supplémentaires d'invalidité (ASI) — recueil statistique, données 2024", "Assurance retraite (Cnav)", "Février 2026",
  "https://www.statistiques-recherche.lassuranceretraite.fr/app/uploads/2026/02/2.4-Les-allocations-de-solidarite-aux-personnes-agees-Aspa-et-allocations-supplementaires-dinvalidite-ASI-1.pdf",
  "Montant maximal de l'Aspa au 1er janvier 2024 : 1 012,02 € par mois pour une personne seule et 1 571,16 € pour un couple, revalorisé chaque 1er janvier.",
  "Caisse nationale d'assurance vieillesse."))
SP_TRAVAIL_ASILE = ('sp_travail_asile', src("Accès au travail du demandeur d'asile (fiche F2741)", "Service-public.gouv.fr (DILA)", "Vérifié le 16 septembre 2026",
  "https://www.service-public.gouv.fr/particuliers/vosdroits/F2741?lang=en",
  "Pendant les six premiers mois suivant la demande, le demandeur d'asile ne peut pas obtenir d'autorisation de travail ; il peut ensuite en demander une si l'Ofpra n'a pas statué dans ce délai. Pour les demandes déposées depuis le 12 juin 2026, le délai court à partir de l'enregistrement au guichet unique.",
  "Site officiel de l'administration."))
INSEE_CHOM = ('insee_chom', src("Au deuxième trimestre 2026, le taux de chômage augmente de 0,2 point et atteint 8,3 % (Informations rapides n° 192)", "Insee", "7 août 2026",
  "https://www.insee.fr/fr/statistiques/9032359",
  "Taux de chômage au sens du BIT : 8,3 % de la population active (France, Mayotte incluse), soit 2 677 000 chômeurs ; +261 000 sur un an. Halo autour du chômage : environ 1,9 million de personnes, soit 4,4 % des 15-64 ans. Taux d'emploi : 69,0 %.",
  "Statistique publique de référence."))
FT_STMT = ('ft_stmt', src("Inscrits à France Travail au 3e trimestre 2026", "France Travail / Dares (statistiques du marché du travail)", "28 octobre 2026",
  "https://www.francetravail.org/statistiques-analyses/breve-chiffres-stmt/inscrits-a-france-travail-au-3e-trimestre-2026.html?type=article",
  "Catégorie A : 3 353 400 ; catégories B et C : 2 494 000 ; catégories A, B, C : 5 847 500 ; catégories A à E : 6 587 600 (France hors Mayotte). Depuis janvier 2025, la loi pour le plein emploi inscrit automatiquement les allocataires du RSA et les jeunes suivis par les missions locales, avec deux nouvelles catégories F (597 000) et G (386 100).",
  "Statistique publique (opérateur et service statistique du ministère du Travail)."))
FT_DEF = ('ft_def', src("Comment sont calculés les chiffres du chômage ?", "France Travail (ex-Pôle emploi)", "23 mai 2019",
  "https://www.francetravail.org/accueil/actualites/infographies/comment-sont-calcules-les-chiffres-du-chomage.html?type=article",
  "Catégorie A : personnes sans emploi pendant le mois ; catégorie B : activité réduite de 78 heures ou moins ; catégorie C : plus de 78 heures. Un chômeur au sens du BIT est sans emploi pendant la semaine de référence, disponible sous 15 jours et en recherche active. « Un chômeur au sens du BIT n'est donc pas forcément inscrit à Pôle emploi, et l'inverse est aussi vrai. »",
  "Opérateur public (2019)."))
INSEE_APPARIEMENT = ('insee_appariement', src("Appariement entre l'enquête Emploi et le fichier historique de Pôle emploi sur la période 2012-2017 (document de travail F1904)", "Insee", "2 juillet 2019",
  "https://www.insee.fr/fr/statistiques/4182193",
  "En 2017, 2,6 millions de chômeurs BIT contre 3,4 millions d'inscrits en catégorie A ; 56 % des inscrits en catégorie A sont chômeurs au sens du BIT, 20 % dans le halo et 9 % en emploi ; « 22 % des chômeurs au sens du BIT en 2017 ne sont pas inscrits à Pôle emploi ».",
  "Statistique publique (2019).", 'etude'))
OI_CO2 = ('oi_co2', src("Riches et pauvres, inégaux dans la capacité à polluer", "Observatoire des inégalités (d'après Paul Malliet, OFCE, 2020)", "22 décembre 2022",
  "https://inegalites.fr/emissions-co2",
  "Les 10 % de ménages les plus riches émettent en moyenne environ 40 tonnes d'équivalent CO2 par an en France, contre 15,2 tonnes pour les 10 % les plus pauvres (données de 2011, ordres de grandeur).",
  "Association indépendante reprenant une étude de l'OFCE.", 'secondaire'))
INSEE_TAXECARB = ('insee_taxecarb', src("Taxer les émissions des entreprises ou taxer celles des ménages : effets selon les revenus et les territoires (Insee Analyses n° 117)", "Insee (Charles Labrousse, Yann Perdereau)", "26 mars 2026",
  "https://www.insee.fr/fr/statistiques/8887123",
  "Les 20 % de ménages les plus modestes consacrent 11,3 % de leurs dépenses totales à l'énergie, contre 9,2 % pour les 20 % les plus aisés ; les ménages du rural non périurbain dépensent 2,7 fois plus en énergies fossiles que ceux du grand centre urbain de Paris.",
  "Statistique publique de référence.", 'etude'))
CAE_CARBONE = ('cae_carbone', src("Pour le climat : une taxe juste, pas juste une taxe (note n° 50)", "Conseil d'analyse économique (D. Bureau, F. Henriet, K. Schubert)", "Mars 2019",
  "https://cae-eco.fr/static/pdf/cae-note050v2.pdf",
  "La hausse de la taxe carbone étudiée est « régressive ex ante » : taux d'effort de près de 1 % du revenu disponible pour les 10 % les plus pauvres, contre 0,3 % pour les 10 % les plus riches ; un ménage rural perd environ 130 € de plus par unité de consommation qu'un Parisien. Le mouvement des Gilets jaunes est parti de ce relèvement, gelé fin 2018. En redistribuant l'intégralité des recettes, plus de 90 % des ménages des cinq ou six premiers déciles seraient gagnants.",
  "Conseil d'économistes placé auprès du Premier ministre (2019).", 'etude'))
INSEE_CHALEUR = ('insee_chaleur', src("Îlots de chaleur urbains : exposition selon le niveau de vie (Insee Analyses n° 99)", "Insee et Banque de France (Grislain-Letrémy, Sixou, Sotura)", "Novembre 2024",
  "https://www.insee.fr/fr/statistiques/fichier/8283129/IA99.pdf",
  "À Lyon, Marseille, Montpellier, Nice et Strasbourg, plus le niveau de vie est faible, plus l'exposition à la chaleur est forte (écart de 0,41 °C à Lyon) ; 4 % des 10 % les plus modestes ont une climatisation, contre 11 % des 10 % les plus aisés (2013) ; à Paris, les ménages les plus aisés sont plus exposés que les ménages médians.",
  "Statistique publique (données de l'été 2017).", 'etude'))
INSEE_FP21 = ('insee_fp21', src("À volume annuel de travail égal, le salaire net moyen de la fonction publique est inférieur de 3,7 % à celui du secteur privé (Insee Première n° 2043)", "Insee (Fanny Godet, Tung Anh Tran)", "20 mars 2025",
  "https://www.insee.fr/fr/statistiques/8386049",
  "Données 2021 : salaire net annuel en équivalent temps plein de 29 450 € dans le public contre 30 600 € dans le privé (−3,7 %) ; revenu salarial annuel moyen de 24 070 € contre 22 040 € (+9,3 % pour le public), en raison d'un volume de travail supérieur de 13,5 % ; les écarts tiennent à la structure de l'emploi par diplôme et à des modes de fixation des salaires différents.",
  "Statistique publique de référence."))
INSEE_PRIVE24 = ('insee_prive24', src("Les salaires dans le secteur privé en 2024 (Insee Première n° 2079)", "Insee (Tom Duquesne, Ndeye Penda Sokhna)", "23 octobre 2025",
  "https://www.insee.fr/fr/statistiques/8657156",
  "Un salarié du secteur privé gagne en moyenne 2 733 € nets par mois en équivalent temps plein ; salaire médian 2 190 € ; cadres 4 629 €, ouvriers 2 051 €, employés 1 941 €.",
  "Statistique publique de référence."))
INSEE_FPE24 = ('insee_fpe24', src("Les salaires dans la fonction publique de l'État en 2024 (Insee Première n° 2100)", "Insee et DGAFP (Lino Galiana, Gaëlle Gateaud)", "6 mai 2026",
  "https://www.insee.fr/fr/statistiques/8986474",
  "Fonction publique de l'État : 3 018 € nets par mois en équivalent temps plein ; enseignants 3 188 € ; la catégorie A représente 48 % des effectifs ; salaires moyens : catégorie A 3 543 €, B 2 837 €, C 2 266 €.",
  "Statistique publique de référence."))
INSEE_FPT24 = ('insee_fpt24', src("Les salaires dans la fonction publique territoriale en 2024 (Insee Première n° 2101)", "Insee et DGCL (Téo Moreau, Julien Desclodure)", "6 mai 2026",
  "https://www.insee.fr/fr/statistiques/8984823",
  "Un agent territorial perçoit en moyenne 2 317 € nets par mois en équivalent temps plein ; ensemble de la fonction publique : 2 742 € ; 72 % des fonctionnaires territoriaux sont en catégorie C.",
  "Statistique publique de référence."))
INSEE_FPH24 = ('insee_fph24', src("Les salaires dans la fonction publique hospitalière en 2024 (Insee Première n° 2102)", "Insee et DREES (Léna Esbelin, Christophe Dixte)", "6 mai 2026",
  "https://www.insee.fr/fr/statistiques/8986438",
  "Personnels médicaux : 6 926 € nets par mois en équivalent temps plein ; personnels des services de soins (infirmiers, aides-soignants, agents de service) : 2 623 €.",
  "Statistique publique de référence."))
EN_GREVES = ('en_greves', src("Industrial action in France and the UK: Which countries have the most strikes in Europe?", "Euronews (Servet Yanatma, d'après l'ETUI)", "18 janvier 2023 (mis à jour le 8 septembre 2023)",
  "https://www.euronews.com/2023/03/07/industrial-action-in-france-and-the-uk-which-countries-have-the-most-strikes-in-europe",
  "Journées non travaillées pour 1 000 salariés, moyenne annuelle (ETUI) : 2000-2009, Espagne 153, France 127 ; 2010-2019, Chypre 275, France 128 ; 2020-2021, France 79, Belgique 57. Le nombre « varies highly from year to year » ; l'OCDE souligne que la comparabilité internationale est affectée par des différences de définitions et de mesures.",
  "Média européen reprenant l'Institut syndical européen (données jusqu'en 2021).", 'media'))
PM_GREVES = ('pm_greves', src("Incroyable mais vrai, la Belgique serait la championne européenne de la grève", "Paris Match Belgique (d'après Belga)", "26 mars 2023",
  "https://www.parismatch.be/actualites/societe/2023/03/26/incroyable-mais-vrai-la-belgique-serait-la-championne-europeenne-de-la-greve-3OJ3QYS3IZCLFHNYETMR2N7YIY/",
  "Selon l'institut allemand WSI, sur 2011-2020, « La Belgique a enregistré 97 jours de grève pour mille salariés par an », la France 93 (secteur privé seulement), la Finlande 52, l'Allemagne 18, l'Autriche et la Suède 2 ; le WSI note que les méthodes diffèrent selon les pays.",
  "Média reprenant une dépêche d'agence et un institut de recherche.", 'media'))
TISSOT_GREVES = ('tissot_greves', src("Grèves en entreprise : net recul de la conflictualité en 2024", "Éditions Tissot (Maylis Rio Lachaud), d'après Dares Résultats n° 6", "19 février 2026",
  "https://www.editions-tissot.fr/actualite/representants-du-personnel-ce/greves-en-entreprise-net-recul-de-la-conflictualite-en-2024",
  "En 2024, « 62 journées individuelles non travaillées pour 1 000 salariés », en baisse de 64 % sur un an ; « 1,6 % des entreprises ont connu au moins un arrêt collectif de travail » (entreprises de 10 salariés ou plus).",
  "Éditeur juridique reprenant une publication de la Dares.", 'secondaire'))
TPE_GREVES = ('tpe_greves', src("En 2024, les jours de grève chutent nettement", "TPE Actu, d'après la Dares", "8 février 2026",
  "https://tpeactu.fr/2026/02/08/baisse-jours-greve-2024-dares/",
  "Secteur privé non agricole : 62 jours de grève pour 1 000 salariés en 2024 contre 171 en 2023 ; transports et entreposage : 403 contre 894 ; motifs : rémunérations 56 %, réforme des retraites 13 %.",
  "Média professionnel reprenant la Dares.", 'secondaire'))
# ── Sources : nationalité, hébergement, asile ──────────────────────────────
CC_21_7 = ('cc_21_7', src("Code civil, article 21-7", "Légifrance", "Version en vigueur depuis le 1er janvier 2020",
  "https://www.legifrance.gouv.fr/codes/id/LEGIARTI000039366780/2020-01-01/",
  "« Tout enfant né en France de parents étrangers acquiert la nationalité française à sa majorité » si, à cette date, il réside en France et y a eu sa résidence habituelle pendant au moins cinq ans, continus ou discontinus, depuis l'âge de onze ans.",
  "Texte de loi."))
INSEE_NATIO = ('insee_natio', src("Acquisitions de la nationalité française — données annuelles de 2008 à 2025", "Insee (d'après les ministères de l'Intérieur et de la Justice)", "9 juillet 2026",
  "https://www.insee.fr/fr/statistiques/2381644",
  "2025 : 98 139 acquisitions, dont 42 063 naturalisations par décret, 32 923 déclarations anticipées de mineurs nés en France (33,5 %), 17 579 par mariage et 1 981 acquisitions sans formalité (2,0 %). 2024 : 33 727 déclarations anticipées et 2 152 acquisitions sans formalité.",
  "Statistique publique de référence."))
BDT_MAYOTTE = ('bdt_mayotte', src("Conditions renforcées pour qu'un enfant né à Mayotte de parents étrangers acquière la nationalité", "Banque des Territoires (Localtis)", "5 mai 2026",
  "https://www.banquedesterritoires.fr/conditions-renforcees-pour-quun-enfant-ne-mayotte-de-parents-etrangers-acquiere-la-nationalite",
  "La loi du 12 mai 2025 exige que les deux parents (et non plus un seul) résident régulièrement à Mayotte à la date de la naissance, depuis au moins un an au lieu de trois mois ; textes d'application : décret n° 2026-338 et arrêté du 30 avril 2026.",
  "Média des collectivités (Caisse des dépôts).", 'secondaire'))
PS_MAYOTTE = ('ps_mayotte', src("Mayotte : députés et sénateurs s'accordent pour durcir le droit du sol", "Public Sénat", "1er avril 2025",
  "https://www.publicsenat.fr/actualites/politique/mayotte-deputes-et-senateurs-saccordent-pour-durcir-le-droit-du-sol",
  "La durée de résidence régulière exigée passe à un an, « contre trois mois actuellement », pour les deux parents, sauf en cas de famille monoparentale ; l'exception mahoraise avait été créée par la loi immigration de 2018.",
  "Média parlementaire.", 'media'))
IM_DROITSOL = ('im_droitsol', src("Supprimer le droit du sol (programme du Rassemblement national, législatives 2024)", "Institut Montaigne", "2024 (fiche mise à jour avec une citation du 14 juin 2024)",
  "https://www.institutmontaigne.org/legislatives-2024/rassemblement-national/supprimer-le-droit-du-sol/",
  "Le RN propose de supprimer le droit du sol ; « La marge de manœuvre juridique est faible en matière d'immigration familiale et d'asile » ; la dérogation de 2018 pour Mayotte, prise « afin de limiter le nombre de femmes venant accoucher à Mayotte », a été validée par le Conseil constitutionnel.",
  "Think tank libéral (évaluation des programmes).", 'etude'))
AN_PLF303 = ('an_plf303', src("Rapport sur le projet de loi de finances pour 2026, annexe n° 27 « Immigration, asile et intégration »", "Assemblée nationale, commission des finances (Charles Rodwell)", "23 octobre 2025",
  "https://www.assemblee-nationale.fr/dyn/17/rapports/cion_fin/l17b1996-tiii-a27_rapport-fond.pdf",
  "L'action 02 du programme 303 « finance l'accueil et l'hébergement des demandeurs d'asile » : 957,6 M€ de crédits de paiement pour l'hébergement (CADA, HUDA, CAES) en 2026 ; le dispositif national d'accueil est programmé à 111 855 places, dont 61 903 en CADA ; l'allocation pour demandeur d'asile est gérée par l'Ofii.",
  "Rapport parlementaire sur le budget de l'État."))
SENAT_ASILE26 = ('senat_asile26', src("Asile : faire la lumière sur les coûts, redéfinir les protections (l'essentiel)", "Sénat, commission des finances (Marie-Carole Ciuntu)", "8 juillet 2026",
  "https://www.senat.fr/fileadmin/cru-1783325159/Commissions/Finances/2025-2026/Controles/Essentiel_post-commission_couts_de_l_asile.pdf",
  "Coût de l'asile estimé à au moins 1,85 Md€ en 2025, hors santé, scolarité, aide sociale et police, dont environ la moitié pour l'hébergement ; dépenses du dispositif national d'accueil : 1,1 Md€ en 2024 (+48 % depuis 2019). Le taux global de protection, CNDA incluse, « atteint désormais 52,1 % en 2025 » ; les obligations de quitter le territoire visant des déboutés ne sont exécutées qu'à 5,5 % en moyenne sur 2019-2025.",
  "Rapport parlementaire de contrôle (rapporteure LR)."))
SENAT_ROUVRAY = ('senat_rouvray', src("Question orale n° 0104S (frais de scolarité des enfants hébergés en CADA) et réponse du Gouvernement", "Sénat / Gouvernement", "6 octobre 2022",
  "https://www.senat.fr/questions/base/2022/qSEQ22070104S.html",
  "La commune de Rouvray supporte les frais de scolarité des enfants du CADA : « plus de 92 000 euros » depuis 2016 ; le Gouvernement répond que ces coûts sont « prises en compte dans la répartition de la dotation globale de fonctionnement (DGF) » ; la cantine et les fournitures sont à la charge des parents ou du gestionnaire du CADA.",
  "Réponse officielle du Gouvernement."))
SENAT_MNA = ('senat_mna', src("Question écrite n° 10787 (mineurs non accompagnés) et réponse du Gouvernement", "Sénat / Gouvernement", "2 mai 2024",
  "https://www.senat.fr/questions/base/2024/qSEQ240310787.html",
  "Les départements assument l'accueil des mineurs non accompagnés au titre de l'aide sociale à l'enfance ; l'État verse des contributions forfaitaires (500 € par évaluation, 90 € par jour de mise à l'abri pendant 14 jours au plus, puis 20 € par jour pendant 9 jours) et une aide exceptionnelle de 6 000 € par jeune supplémentaire (17,562 M€ en 2023).",
  "Réponse officielle du Gouvernement."))
HCR_CONNECT = ('hcr_connect', src("Connecting Refugees: How Internet and Mobile Connectivity can Improve Refugee Well-Being and Transform Humanitarian Action", "Haut-Commissariat des Nations unies pour les réfugiés (HCR), avec Accenture", "Septembre 2016",
  "https://www.unhcr.org/in/sites/en-in/files/legacy-pdf/5770d43c4.pdf",
  "Les réfugiés ont 50 % de chances en moins que la population générale d'avoir un téléphone connecté à Internet ; 29 % des ménages réfugiés n'ont aucun téléphone ; ils consacrent jusqu'à un tiers de leur revenu disponible à rester connectés ; « Refugees deem connectivity to be a critical survival tool in their daily lives. »",
  "Agence des Nations unies (2016)."))
SLATE_TEL = ('slate_tel', src("Non, les smartphones des migrants qui arrivent en Europe n'ont rien d'un luxe", "Slate.fr", "2015",
  "https://www.slate.fr/story/105425/pourquoi-migrants-ont-smartphones",
  "Le téléphone sert à se repérer (GPS), à traduire, à joindre la famille et à organiser le trajet, avec des cartes prépayées et des applications de messagerie ; une responsable du service social pour les réfugiés de Munich : « Ça n'a vraiment rien d'un luxe ».",
  "Média (2015).", 'media'))
OFPRA_24 = ('ofpra_24', src("Rapport d'activité 2024", "Office français de protection des réfugiés et apatrides (OFPRA)", "Juin 2025",
  "https://www.ofpra.gouv.fr/sites/default/files/2025-06/OFPRA_RA_2024_BD_PaP.pdf",
  "« un taux moyen de protection hissé à près de 39 % » à l'OFPRA en 2024 ; 70 284 personnes protégées dans l'année ; environ 663 241 personnes placées sous la protection de l'OFPRA au 31 décembre 2024.",
  "Établissement public chargé de l'asile."))
EUAA_OFPRA25 = ('euaa_ofpra25', src("OFPRA publishes its annual report for 2025", "Agence de l'Union européenne pour l'asile (EUAA)", "27 juillet 2026",
  "https://dip.euaa.europa.eu/node/13714",
  "145 270 demandes en 2025 (−5,5 %) ; 156 509 décisions ; taux de protection à l'OFPRA de 41 %, contre 39 % en 2024 ; principales nationalités : Ukraine, RD Congo, Afghanistan.",
  "Agence de l'Union européenne."))
EUROSTAT_ASILE = ('eurostat_asile', src("Asylum decisions down by 18% in 2025", "Eurostat", "24 avril 2026",
  "https://ec.europa.eu/eurostat/web/products-eurostat-news/w/ddn-20260424-1",
  "832 360 décisions de première instance dans l'Union en 2025 ; 325 765 personnes protégées, taux de reconnaissance de 39 % ; la France a protégé 72 930 personnes (toutes instances), 20 % du total de l'Union ; taux de reconnaissance en première instance de 73 % pour les Afghans et 92 % pour les Vénézuéliens.",
  "Office statistique de l'Union européenne."))

FICHES = []

# 1 ── 80 % des lois ──────────────────────────────────────────────────────────
FICHES.append(fiche(
 id='lois-bruxelles-80-pourcent', affirmation="80 % de nos lois sont décidées à Bruxelles.", volet='politique', sous_theme='Union européenne',
 mots_cles=['80 % de nos lois', '80 % des lois', 'lois decidees a bruxelles', 'lois viennent de bruxelles', 'lois europeennes', 'transposition', 'directives europeennes', 'bruxelles decide'],
 verdict='contredit', fiabilite='etabli',
 resume="Le chiffre de 80 % vient d'une prévision de Jacques Delors en 1988, qui portait sur la seule législation économique et n'a jamais été vérifiée. Les études disponibles situent la part du droit d'origine européenne en France autour de 13 % des lois (2006) à 28 % des normes en vigueur (2008) ; elle dépasse en revanche 50 % dans quelques domaines comme l'agriculture ou l'environnement.",
 contexte="Le chiffre est repris pour dire que voter en France ne servirait à rien ou que la souveraineté aurait disparu ; il circule à l'extrême droite comme chez des eurosceptiques de gauche.",
 explication="Compter la part « européenne » des lois est difficile : certaines lois transposent une directive, d'autres ratifient un traité, et les règlements européens s'appliquent sans loi française. Selon la méthode, on obtient des chiffres différents, mais aucune étude ne trouve 80 %.",
 sources=[PS_80, EN_80],
 faits=[
  fait("Jacques Delors avait annoncé qu'en 2000, « 80 % de la législation économique » serait d'origine communautaire : une prévision limitée à l'économie.", 'en_80', '1988', 'Union européenne', "Le chiffre d'origine n'est ni un constat ni une mesure de toutes les lois.", 'etabli', '80 %'),
  fait("Selon des chercheurs de Sciences Po Bordeaux, la part des lois françaises « européanisées » est passée de moins de 3 % en 1986 à 13,3 % en 2006.", 'ps_80', '1986-2006', 'France', "La grande majorité des lois sont votées sans contrainte européenne directe.", 'etabli', '13,3 %'),
  fait("Selon Yves Bertoncini (Notre Europe), 9 685 actes européens étaient en vigueur en 2008, soit 28,1 % des 34 476 normes applicables en France.", 'ps_80', '2008', 'France', "Même en comptant les règlements, on reste loin de 80 %.", 'etabli', '28,1 %'),
  fait("Selon Euronews, la part d'origine européenne dépasse 50 % dans l'agriculture, l'environnement et l'économie, mais elle est bien plus faible pour l'emploi, la sécurité intérieure ou la santé.", 'en_80', '2024', 'Union européenne', "L'influence européenne est forte dans certains domaines, faible dans d'autres.", 'estimation', '50 %'),
 ],
 court="Faux : le chiffre de 80 % est une prévision de Jacques Delors (1988) sur la seule législation économique. Les études mesurent 13 % des lois (2006) à 28 % des normes (2008) d'origine européenne en France.",
 moyen="Le « 80 % » vient d'une phrase de Jacques Delors en 1988 : il prévoyait que 80 % de la législation économique serait d'origine européenne. Ce n'était ni une mesure, ni une affirmation sur toutes les lois.\n\nLes chercheurs qui ont compté trouvent bien moins : 13 % des lois françaises étaient liées au droit européen en 2006, et 28 % des normes en vigueur en 2008. Dans certains domaines, comme l'agriculture ou l'environnement, l'Europe pèse en revanche plus de la moitié.",
 detaille="Le chiffre de 80 % est une prévision de Jacques Delors, alors président de la Commission européenne, qui annonçait en 1988 que d'ici 2000, 80 % de la législation économique serait d'origine communautaire. Il a ensuite été repris comme s'il s'agissait d'un constat portant sur toutes les lois.\n\nLes études qui ont réellement compté donnent d'autres ordres de grandeur. Pour Brouard, Costa et Kerrouche (Sciences Po Bordeaux), la part des lois françaises « européanisées » passe de moins de 3 % en 1986 à 13,3 % en 2006, avec des pointes de 39 % dans le secteur scientifique et technologique ; « dans 80 % des cas », écrivent-ils, les lois sont adoptées sans contrainte européenne directe. Yves Bertoncini compte 28,1 % de normes européennes parmi celles en vigueur en 2008.\n\nCela ne veut pas dire que l'Europe pèse peu : dans l'agriculture, l'environnement ou l'économie, plus de la moitié des règles viennent de l'Union. Le vrai débat porte sur le contenu de ces règles et sur leur contrôle démocratique, pas sur un pourcentage imaginaire.",
 empathie="Je comprends qu'on ait l'impression que tout se décide loin de nous, surtout quand des règles européennes changent notre quotidien. Mais les études qui ont compté trouvent bien moins de 80 % : la plupart de nos lois restent votées ici.",
 legitimes=["Dans certains domaines (agriculture, environnement, marché intérieur), la majorité des règles est bien d'origine européenne.", "Les règlements européens s'appliquent directement, sans loi française, ce qui rend leur poids moins visible."],
 contre=[
  ("Les règlements européens ne passent même pas par le Parlement français.", "C'est exact, et c'est pourquoi l'étude de Bertoncini les compte : on arrive à 28 % des normes, pas 80 %."),
  ("Les chiffres datent d'avant 2012.", "Oui, aucune étude récente n'a été lue ; mais rien n'indique un triplement de la part européenne."),
 ],
 questions=["Sais-tu d'où vient le chiffre de 80 % et sur quoi il portait ?", "Dans quels domaines penses-tu que l'Europe décide vraiment le plus ?"],
 limites=["Les études citées datent de 2008 à 2012 ; aucune mesure plus récente n'a été lue pour cette fiche.", "La part européenne varie fortement selon la méthode (lois, normes, décrets) et selon le domaine."],
 publics={'convaincus': "Le chiffre de 80 % vient d'une prévision de Jacques Delors en 1988, et elle ne portait que sur l'économie. Quand des chercheurs ont compté, ils ont trouvé 13 % des lois et 28 % des normes. Si tu veux critiquer l'Europe, et il y a de quoi, mieux vaut des chiffres solides.",
  'indecis': "L'Europe pèse vraiment dans certains domaines, comme l'agriculture ou l'environnement, où elle fixe plus de la moitié des règles. Mais au total, les études trouvent entre 13 % et 28 % de règles d'origine européenne. La plupart des décisions qui touchent ta vie se prennent encore à Paris."},
 a_actualiser='2028-06-30',
))

# 2 ── Le RN n'est plus d'extrême droite ──────────────────────────────────────
FICHES.append(fiche(
 id='rn-plus-extreme-droite', affirmation="Le RN a changé, ce n'est plus un parti d'extrême droite.", volet='politique', sous_theme='Rassemblement national',
 mots_cles=['plus d extreme droite', 'pas d extreme droite', 'n est plus d extreme droite', 'rn a change', 'le rn a change', 'dediabolisation', 'parti normal', 'nuancage', 'classement extreme droite'],
 verdict='trompeur', fiabilite='interpretation',
 resume="Le RN a changé d'image, mais le cœur de son programme reste la « priorité nationale », que le président du Conseil constitutionnel juge contraire à la Constitution si elle est appliquée systématiquement. En 2024, le Conseil d'État a refusé d'annuler le classement du RN dans le bloc « extrême droite » ; il n'a pas pour autant tranché le fond, et il a validé en 2026 le classement de LFI à « l'extrême gauche ».",
 contexte="Depuis les années 2010, la stratégie de « dédiabolisation » vise à faire du RN un parti comme les autres ; ses dirigeants contestent l'étiquette d'extrême droite et l'ont attaquée en justice.",
 explication="Pour les politistes, un parti d'extrême droite se définit notamment par la préférence donnée aux nationaux sur les étrangers (nativisme) et par le rejet du pluralisme. Changer de nom, de ton ou de dirigeants ne suffit pas si ce cœur programmatique demeure.",
 sources=[CE_RN, CDJ_RN, SCPO_RN, LCP_RN_IMMI, LANDOT],
 faits=[
  fait("Le Conseil d'État a rejeté en mars 2024 la requête du RN contre la circulaire qui classe sa nuance dans le bloc « extrême droite », sans y voir d'erreur manifeste d'appréciation.", 'ce_rn', '2024', 'France', "La justice n'a pas jugé ce classement abusif.", 'etabli'),
  fait("Selon le juriste Arnaud Gossement, « le Conseil d'Etat n'a pas affirmé que le RN est d'extrême-droite » : son contrôle était limité à l'erreur manifeste.", 'cdj_rn', '2024', 'France', "Il ne faut pas faire dire plus à cette décision qu'elle ne dit.", 'etabli'),
  fait("Pour la politiste Nonna Mayer, Marine Le Pen a « ripoliné » le parti, mais « rien n'a vraiment changé » : la priorité nationale reste au cœur du programme.", 'scpo_rn', '2022', 'France', "Le changement porte surtout sur l'image.", 'interpretation'),
  fait("En 2024, le RN voulait « mettre en place la priorité nationale », si nécessaire par référendum ; Laurent Fabius a jugé que la préférence nationale « appliquée de façon systématique, est contraire à la Constitution ».", 'lcp_rn_immi', '2024', 'France', "Le cœur du programme heurte l'égalité devant la loi.", 'etabli'),
  fait("En février 2026, le Conseil d'État a aussi jugé non manifestement erroné le classement de LFI à « l'extrême gauche » dans la circulaire des municipales.", 'landot', '2026', 'France', "Le même contrôle s'applique à la gauche radicale.", 'etabli'),
 ],
 court="Trompeur : le RN a changé d'image, mais la priorité nationale reste le cœur de son programme, et le Conseil d'État a refusé d'annuler son classement à l'extrême droite (2024).",
 moyen="Le RN a changé de nom, de ton et de visage. Mais pour les politistes, l'essentiel n'a pas bougé : la priorité nationale, c'est-à-dire réserver des droits aux Français, reste au cœur du programme. Le président du Conseil constitutionnel l'a jugée contraire à la Constitution si elle est appliquée systématiquement.\n\nEn 2024, le Conseil d'État a refusé d'annuler le classement du RN dans le bloc « extrême droite ». Ce n'est pas un jugement sur le fond ; il a d'ailleurs validé en 2026 le classement de LFI à « l'extrême gauche ».",
 detaille="La « dédiabolisation » est une réalité : exclusion de Jean-Marie Le Pen, changement de nom, programme économique remanié, candidats plus lisses. Florence Haegel rappelle que le RN est un parti « tout à fait légal ».\n\nMais pour Nonna Mayer, Marine Le Pen a surtout « ripoliné » le parti : la priorité nationale reste au cœur du programme. En 2024, le RN voulait encore la mettre en place, au besoin par référendum constitutionnel, et réserver les allocations familiales aux Français. Pour Laurent Fabius, cette préférence, appliquée de façon systématique, est contraire à la Constitution.\n\nSur le plan juridique, le Conseil d'État a rejeté en mars 2024 le recours du RN contre son classement dans le bloc « extrême droite ». Comme le souligne Arnaud Gossement, il n'a pas qualifié le parti sur le fond, seulement vérifié l'absence d'erreur manifeste. Le même contrôle a validé en 2026 le classement de LFI à « l'extrême gauche » : chacun peut contester ces étiquettes, mais ce qui compte, c'est le programme.",
 empathie="Je comprends que le RN te paraisse plus fréquentable qu'autrefois : le ton a changé, les visages aussi. Mais regarde le programme : réserver des droits aux seuls Français, c'est toujours le cœur du projet, et c'est ce qui le place à l'extrême droite.",
 legitimes=["Le RN a réellement changé de style, de dirigeants et de certaines positions économiques.", "Les classements politiques par le ministère de l'Intérieur sont des choix administratifs contestables, et ils s'appliquent aussi à LFI."],
 contre=[
  ("Le Conseil d'État n'a jamais dit que le RN était d'extrême droite.", "C'est exact : il a seulement refusé d'annuler ce classement ; l'argument de fond, c'est la priorité nationale."),
  ("Des millions de gens votent RN, ils ne sont pas tous d'extrême droite.", "Bien sûr : on parle du programme d'un parti, pas de chacun de ses électeurs."),
 ],
 questions=["Qu'est-ce qui, selon toi, a changé dans le programme du RN, au-delà du ton ?", "Que penses-tu d'un projet qui réserve certaines aides aux seuls Français, même à ceux qui cotisent depuis des années ?"],
 limites=["L'analyse de Nonna Mayer date de 2022 ; aucune étude de politiste postérieure à 2024 n'a été lue pour cette fiche.", "La décision de 2026 sur LFI est connue par le commentaire d'un avocat, pas par le texte de la décision."],
 publics={'convaincus': "Le RN a changé de ton, c'est vrai. Mais il propose toujours la priorité nationale : réserver des droits aux Français, même face à quelqu'un qui travaille et cotise ici. Le président du Conseil constitutionnel la juge contraire à la Constitution. Ce n'est pas une insulte de dire « extrême droite », c'est une description du programme.",
  'indecis': "Le RN a beaucoup travaillé son image, et beaucoup de ses électeurs ne se sentent pas d'extrême droite. Ce qui fait débat, c'est le programme : la priorité nationale, qui traite différemment les gens selon leur nationalité. Pour les politistes, ce cœur du projet n'a pas changé."},
 a_actualiser='2027-06-30',
))

# 3 ── Condamnation de Marine Le Pen ──────────────────────────────────────────
FICHES.append(fiche(
 id='le-pen-condamnation-juges', affirmation="La condamnation de Marine Le Pen est un complot des juges pour l'empêcher de se présenter.", volet='politique', sous_theme='Rassemblement national',
 mots_cles=['condamnation de marine le pen', 'marine le pen condamnee', 'le pen condamnee', 'assistants parlementaires', 'assistants du rn', 'parlement europeen detournement', 'ineligibilite', 'execution provisoire', 'gouvernement des juges', 'complot des juges'],
 verdict='contredit', fiabilite='etabli',
 resume="Deux juridictions ont reconnu le détournement de fonds du Parlement européen pour payer des assistants qui travaillaient pour le parti : le tribunal en mars 2025, puis la cour d'appel de Paris le 7 juillet 2026, après examen des contrats un par un. La cour d'appel a réduit la peine : Marine Le Pen reste éligible pour 2027, ce qui contredit l'idée d'un complot destiné à l'écarter. Elle s'est pourvue en cassation.",
 contexte="Après le jugement du 31 mars 2025 et son exécution provisoire, le RN a dénoncé une « tyrannie des juges » ; l'idée d'un procès politique circule largement sur les réseaux sociaux.",
 explication="L'affaire porte sur des contrats d'assistants parlementaires européens payés par le Parlement européen alors que ces personnes travaillaient pour le parti. Le juge pénal applique la loi sur le détournement de fonds publics ; l'inéligibilité est une peine prévue par cette loi.",
 sources=[TE_LEPEN, LCP_LEPEN, SIMONNET, LCP_QPC],
 faits=[
  fait("Le 31 mars 2025, le tribunal a condamné Marine Le Pen à quatre ans de prison dont deux ferme et cinq ans d'inéligibilité avec exécution provisoire, pour un détournement d'environ 2,9 millions d'euros.", 'te_lepen', '2025', 'France', "La première condamnation a été prononcée après des années d'enquête.", 'etabli', '2,9 M€'),
  fait("Le 7 juillet 2026, la cour d'appel de Paris a confirmé la culpabilité des 12 appelants après avoir examiné les 28 contrats un par un, avec des relaxes partielles ; le préjudice du Parlement européen est fixé à 1 943 696,31 €.", 'simonnet', '2026', 'France', "Une seconde juridiction, avec d'autres juges, arrive à la même conclusion.", 'etabli', '1,94 M€'),
  fait("En appel, Marine Le Pen est condamnée à trois ans de prison dont deux avec sursis, 100 000 € d'amende et 45 mois d'inéligibilité dont 30 avec sursis ; les 15 mois fermes sont déjà exécutés et elle reste éligible pour 2027.", 'lcp_lepen', '2026', 'France', "Si les juges voulaient l'écarter, ils ne lui auraient pas permis de se présenter.", 'etabli'),
  fait("Le RN, en tant que personne morale, est condamné à 2 M€ d'amende dont 1 M€ avec sursis ; Marine Le Pen a formé un pourvoi en cassation.", 'te_lepen', '2026', 'France', "La procédure n'est pas terminée.", 'etabli'),
  fait("Avant le premier jugement, le Conseil constitutionnel avait jugé conforme à la Constitution le régime de l'exécution provisoire de l'inéligibilité, à condition que le juge apprécie le caractère proportionné de l'atteinte à « la liberté de l'électeur ».", 'lcp_qpc', '2025', 'France', "L'exécution provisoire avait un fondement légal validé, mais encadré.", 'etabli'),
 ],
 court="Faux : deux juridictions ont reconnu le détournement de fonds européens. Et la cour d'appel a réduit la peine en 2026 : Marine Le Pen reste éligible pour 2027, ce qui contredit l'idée d'un complot pour l'écarter.",
 moyen="Le tribunal (mars 2025) puis la cour d'appel de Paris (juillet 2026) ont jugé que des assistants payés par le Parlement européen travaillaient en réalité pour le parti. La cour d'appel a examiné les 28 contrats un par un, avec des relaxes partielles, et fixé le préjudice à près de 1,94 million d'euros.\n\nSurtout, elle a réduit la peine : 45 mois d'inéligibilité dont 15 ferme, déjà exécutés. Marine Le Pen reste donc éligible pour 2027. Un complot destiné à l'empêcher de se présenter aurait mal fonctionné.",
 detaille="L'affaire des assistants parlementaires porte sur des contrats payés par le Parlement européen alors que les personnes travaillaient pour le Front national puis le RN. Le 31 mars 2025, le tribunal a condamné Marine Le Pen à quatre ans de prison dont deux ferme et cinq ans d'inéligibilité avec exécution provisoire, en évaluant le détournement à environ 2,9 millions d'euros.\n\nL'exécution provisoire, qui l'empêchait de se présenter avant l'appel, a été très débattue. Elle reposait sur un régime que le Conseil constitutionnel venait de juger conforme à la Constitution, à condition que le juge apprécie la proportionnalité de l'atteinte à la liberté de l'électeur.\n\nLe 7 juillet 2026, la cour d'appel de Paris a confirmé la culpabilité des 12 appelants et du parti, après un examen contrat par contrat, avec des relaxes partielles. Elle a tenu compte de l'absence d'enrichissement personnel et réduit la peine : trois ans dont deux avec sursis, 100 000 € d'amende, 45 mois d'inéligibilité dont 15 ferme, déjà exécutés. Marine Le Pen reste éligible pour 2027 et s'est pourvue en cassation. Deux juridictions, des magistrats différents et une peine allégée : ce n'est pas le profil d'un complot.",
 empathie="Je comprends que ça choque de voir une candidate menacée d'être écartée par un tribunal. Mais deux juridictions différentes ont reconnu les faits, et la cour d'appel l'a laissée éligible pour 2027 : si c'était un complot, il aurait échoué.",
 legitimes=["L'exécution provisoire de l'inéligibilité en première instance a réellement privé Marine Le Pen de candidatures possibles pendant 15 mois, et sa légitimité a été débattue par des juristes.", "La décision définitive dépend encore de la Cour de cassation."],
 contre=[
  ("Tous les partis faisaient pareil avec leurs assistants.", "D'autres affaires existent ou ont existé ; cela ne rend pas ces contrats légaux, et la cour les a examinés un par un."),
  ("Les juges sont de gauche.", "La cour d'appel a allégé la peine et laissé Marine Le Pen éligible : c'est l'inverse d'une décision partisane."),
 ],
 questions=["Si les juges voulaient l'empêcher de se présenter, pourquoi la cour d'appel l'a-t-elle laissée éligible ?", "Que penserais-tu d'un élu d'un autre parti condamné pour les mêmes faits ?"],
 limites=["L'arrêt d'appel lui-même n'a pas été lu : ses termes sont connus par la presse et le commentaire d'un avocat.", "La Cour de cassation n'a pas encore statué ; la date de sa décision n'est pas connue avec certitude."],
 publics={'convaincus': "Deux tribunaux différents ont reconnu que des assistants payés par l'Europe travaillaient pour le parti. Et la cour d'appel a allégé la peine : Marine Le Pen peut se présenter en 2027. Si des juges avaient voulu l'éliminer, ils s'y seraient pris autrement.",
  'indecis': "On peut trouver discutable qu'une peine d'inéligibilité s'applique avant l'appel, et des juristes en ont débattu. Mais sur le fond, deux juridictions ont reconnu les faits, avec un examen contrat par contrat. La peine a été réduite en appel, et la candidate reste éligible pour 2027."},
 a_actualiser='2027-04-30', raison="Décision attendue de la Cour de cassation.", stabilite='actualite',
))

# 4 ── LFI et la sortie de l'UE ───────────────────────────────────────────────
FICHES.append(fiche(
 id='lfi-sortie-ue-euro', affirmation="La France insoumise veut faire sortir la France de l'Union européenne et de l'euro.", volet='politique', sous_theme='France insoumise',
 mots_cles=['frexit', 'sortir de l euro', 'sortie de l euro', 'sortir de l union europeenne', 'sortie de l ue', 'plan b', 'desobeissance europeenne', 'desobeir aux traites', 'lfi europe', 'insoumis europe'],
 verdict='trompeur', fiabilite='etabli',
 resume="C'était en partie vrai en 2017 : le « plan B » de LFI prévoyait une sortie de l'euro, voire de l'UE, si la renégociation des traités échouait. Depuis 2022, LFI a remplacé cette menace par une stratégie de « désobéissance » à certaines règles européennes, et le programme du Nouveau Front populaire (2024) ne prévoit ni sortie de l'UE ni sortie de l'euro, mais le refus du pacte de stabilité budgétaire.",
 contexte="L'accusation de vouloir un « Frexit » est souvent adressée à LFI par la majorité présidentielle et la droite ; elle s'appuie sur le programme de 2017.",
 explication="Le « plan A » consistait à renégocier les traités ; le « plan B » était une sortie en dernier recours. La « désobéissance » consiste à ne pas appliquer certaines règles (budgétaires notamment) tout en restant dans l'Union, ce qui pose d'autres questions juridiques.",
 sources=[PS_LFI_UE, TN_LFI, LCP_NFP, EN_NFP_UE],
 faits=[
  fait("En 2017, le « plan B » de LFI prévoyait une sortie de l'euro, voire de l'UE, en cas d'échec de la renégociation ; un cofondateur jugeait ce plan B « caduc » dès 2018.", 'ps_lfi_ue', '2017-2018', 'France', "L'idée a existé, comme option de dernier recours.", 'etabli'),
  fait("Selon Terra Nova, en 2022, « cette menace de sortie se transforma en stratégie de désobéissance » ; en 2024, LFI défend une refonte des traités par la procédure prévue à l'article 48 du traité sur l'UE.", 'tn_lfi', '2022-2024', 'France', "LFI veut changer l'Union de l'intérieur, pas la quitter.", 'etabli'),
  fait("Le programme du Nouveau Front populaire (2024) prévoit de « refuser le pacte de stabilité budgétaire », sans sortie de l'Union.", 'lcp_nfp', '2024', 'France', "Le programme commun de la gauche ne contient pas de Frexit.", 'etabli'),
  fait("Selon Euronews, le programme du NFP « pourrait créer des tensions à Bruxelles sur les questions budgétaires », mais ses partis ne remettent pas frontalement en cause l'engagement européen de la France.", 'en_nfp_ue', '2024', 'Union européenne', "Le conflit porterait sur les règles budgétaires, pas sur l'appartenance.", 'interpretation'),
 ],
 court="Trompeur : le « plan B » de sortie de l'euro date de 2017. Depuis 2022, LFI parle de « désobéissance » à certaines règles, et le programme du NFP de 2024 ne prévoit ni sortie de l'UE ni sortie de l'euro.",
 moyen="En 2017, LFI menaçait de sortir de l'euro, voire de l'Union, si les autres pays refusaient de renégocier les traités : c'était le « plan B ». Cette option a été abandonnée.\n\nDepuis 2022, LFI propose de « désobéir » à certaines règles européennes, surtout budgétaires, tout en restant dans l'Union, et de refondre les traités. Le programme du Nouveau Front populaire de 2024 prévoit de refuser le pacte de stabilité, pas de quitter l'UE ou l'euro.",
 detaille="Le programme de 2017, L'Avenir en commun, reposait sur deux étapes : renégocier les traités européens (plan A), puis, en cas d'échec, envisager une sortie de l'euro, voire de l'Union (plan B). Dès 2018, un cofondateur du mouvement jugeait ce plan B « caduc ».\n\nEn 2022, selon l'analyse de Terra Nova, la menace de sortie s'est transformée en stratégie de désobéissance : ne pas appliquer certaines règles, utiliser le veto, conditionner la contribution au budget européen. En 2024, LFI défend une refonte des traités par la procédure prévue à l'article 48 du traité sur l'UE.\n\nLe programme commun du Nouveau Front populaire prévoit de refuser le pacte de stabilité budgétaire, de mettre fin aux traités de libre-échange et de réformer la PAC. Il ne prévoit pas de Frexit. Cette stratégie de désobéissance peut être critiquée : elle créerait des tensions budgétaires avec Bruxelles et pose des questions juridiques. Mais ce n'est pas une sortie de l'Union.",
 empathie="Je comprends que le mot « désobéissance » inquiète, et que tu aies entendu parler du plan B de 2017. Mais depuis, LFI a abandonné l'idée de sortir de l'euro : le programme commun de la gauche en 2024 prévoit de changer les règles budgétaires, pas de quitter l'Europe.",
 legitimes=["Le plan B de 2017 prévoyait bien une sortie possible de l'euro, voire de l'UE.", "Désobéir unilatéralement à des règles européennes poserait de vrais problèmes juridiques et budgétaires."],
 contre=[
  ("Désobéir aux traités, c'est en sortir de fait.", "Le programme prévoit de rester dans l'Union et de renégocier les traités ; c'est un conflit politique, pas une sortie."),
  ("Mélenchon l'a dit lui-même en 2017.", "C'est vrai pour 2017 ; le programme de 2024 ne le prévoit plus."),
 ],
 questions=["Sais-tu ce que prévoit le programme du Nouveau Front populaire sur l'Europe ?", "Faut-il, selon toi, appliquer les règles budgétaires européennes même quand elles imposent des coupes dans les services publics ?"],
 limites=["Le texte du programme actuel de LFI (2026-2027) n'a pas pu être lu ; la fiche s'appuie sur les programmes de 2017 et 2024 et sur des analyses.", "L'analyse de Terra Nova émane d'un think tank de centre gauche, critique de LFI."],
 publics={'convaincus': "Le « plan B » de sortie de l'euro, c'était 2017, et LFI l'a abandonné. Le programme commun de la gauche en 2024 prévoit de refuser les règles budgétaires, pas de quitter l'Europe. Critique l'Europe si tu veux, mais pas pour un projet qu'ils n'ont plus.",
  'indecis': "LFI critique durement l'Europe actuelle et veut changer ses règles, surtout budgétaires. Elle a envisagé une sortie de l'euro en 2017, mais l'a abandonnée. Aujourd'hui, elle propose de renégocier les traités et de ne pas appliquer certaines règles, ce qui peut créer des conflits avec Bruxelles."},
 a_actualiser='2027-06-30',
))

# 5 ── Cantines, halal et porc ────────────────────────────────────────────────
FICHES.append(fiche(
 id='cantines-halal-porc', affirmation="Les cantines scolaires imposent le halal et suppriment le porc.", volet='droits', sous_theme='Laïcité',
 mots_cles=['cantine', 'cantines', 'halal', 'menus sans porc', 'menu sans porc', 'menus de substitution', 'porc a la cantine', 'repas vegetarien', 'chalon sur saone'],
 verdict='contredit', fiabilite='etabli',
 resume="Aucune règle n'impose le halal à la cantine. Le Conseil d'État a jugé en 2020 qu'il n'est « ni obligatoire ni interdit » pour une commune de proposer des repas différenciés, comme un menu sans porc : c'est un choix local. Le cas le plus connu va dans l'autre sens : à Chalon-sur-Saône, c'est le maire qui a supprimé en 2015 les menus de substitution. Le repas végétarien hebdomadaire vient de la loi EGalim, pour des raisons de nutrition et d'environnement.",
 contexte="Des rumeurs récurrentes affirment que des écoles serviraient de la viande halal à tous les enfants ou interdiraient le porc ; elles s'appuient souvent sur des cas locaux déformés.",
 explication="La cantine est un service public facultatif organisé par les communes. Chacune décide de ses menus, dans le respect de la loi (nutrition, menu végétarien hebdomadaire). Proposer une alternative au porc est permis, pas obligatoire ; servir de la viande halal à tous ne repose sur aucune règle nationale.",
 sources=[CE_CANTINE, AFP_CANTINE, CNCDH_CANTINE, BDT_VEGE],
 faits=[
  fait("Le Conseil d'État juge qu'il « n'est ni obligatoire ni interdit » pour les collectivités de proposer aux élèves des repas différenciés, et qu'elles doivent veiller à ce que tous les enfants puissent accéder à ce service public.", 'ce_cantine', '2020', 'France', "Le menu sans porc est une simple faculté laissée aux communes.", 'etabli'),
  fait("À Chalon-sur-Saône, des menus de substitution existaient depuis 1984 ; le maire les a supprimés en 2015 et a annoncé qu'il ne les rétablirait pas.", 'afp_cantine', '1984-2020', 'Chalon-sur-Saône', "Le cas emblématique est une suppression du menu sans porc, pas une suppression du porc.", 'etabli'),
  fait("Selon la CNCDH, « la cantine n'est pas obligée de fournir un repas de substitution lorsqu'il y a de la viande de porc au menu », et les menus confessionnels ne sont « ni un droit pour les usagers ni une obligation pour les collectivités ».", 'cncdh_cantine', '2017', 'France', "Rien n'impose de menus religieux.", 'etabli'),
  fait("Les cantines doivent servir « un repas végétarien hebdomadaire », conformément à la loi EGalim.", 'bdt_vege', '2019', 'France', "Le repas sans viande est une mesure nutritionnelle et environnementale, pas religieuse.", 'etabli'),
 ],
 court="Faux : aucune règle n'impose le halal. Le Conseil d'État juge le menu sans porc « ni obligatoire ni interdit » : c'est un choix de chaque commune. Le repas végétarien hebdomadaire vient de la loi EGalim.",
 moyen="Chaque commune décide des menus de sa cantine. Le Conseil d'État l'a rappelé en 2020 : proposer un menu sans porc n'est « ni obligatoire ni interdit ». Rien n'impose de servir de la viande halal.\n\nLe cas le plus connu, à Chalon-sur-Saône, va même dans l'autre sens : le maire a supprimé en 2015 les menus de substitution qui existaient depuis 1984. Quant au repas végétarien hebdomadaire, il vient de la loi EGalim, pour la santé et l'environnement.",
 detaille="La restauration scolaire est un service public facultatif, organisé par les communes pour les écoles. Elles choisissent les menus, dans le cadre des règles nationales de nutrition.\n\nEn 2020, le Conseil d'État a tranché la question des menus sans porc à propos de Chalon-sur-Saône, où le maire avait supprimé en 2015 des menus de substitution proposés depuis 1984. Il a jugé qu'il n'est « ni obligatoire ni interdit » de proposer des repas différenciés, et annulé la délibération seulement parce qu'elle reposait uniquement sur la laïcité et la neutralité, sans tenir compte de l'accès de tous les enfants au service.\n\nLa CNCDH rappelle que les menus confessionnels ne sont ni un droit ni une obligation. Aucune règle nationale n'impose de viande halal. Le repas végétarien hebdomadaire, imposé par la loi EGalim, répond à des objectifs de nutrition et d'environnement, et il convient à tout le monde. Une commune peut proposer une alternative au porc pour que tous les enfants mangent : c'est un choix pratique, pas une islamisation.",
 empathie="Je comprends que ces histoires de cantine touchent, parce qu'il s'agit de nos enfants et de traditions auxquelles on tient. Mais aucune loi n'impose le halal : chaque commune choisit ses menus, et un menu sans porc est juste une option pour que tous les enfants mangent.",
 legitimes=["Certaines communes proposent effectivement des alternatives au porc ; c'est un choix local qui peut être débattu au conseil municipal.", "Aucune statistique nationale sur les menus proposés n'a été trouvée pour cette fiche."],
 contre=[
  ("Dans l'école de mon neveu, il n'y a plus de porc.", "C'est possible dans une commune donnée, mais ce n'est imposé par aucune règle ; il faut poser la question à la mairie."),
  ("Un menu sans porc, c'est céder à une religion.", "C'est un repas de plus proposé pour que tous les enfants mangent ; personne n'est privé de porc."),
 ],
 questions=["Sais-tu qui décide des menus de la cantine de ta commune ?", "Est-ce qu'un repas végétarien par semaine te paraît être une mesure religieuse ?"],
 limites=["Aucune statistique nationale sur les menus des cantines n'a été lue.", "Le texte de la loi EGalim n'a pas été lu directement sur Légifrance."],
 publics={'convaincus': "Aucune loi n'impose le halal à la cantine, et le Conseil d'État dit que le menu sans porc n'est « ni obligatoire ni interdit ». Le cas le plus célèbre, Chalon-sur-Saône, c'est un maire qui a supprimé le menu sans porc. Le repas végétarien vient de la loi EGalim, pour la santé.",
  'indecis': "Les menus de cantine sont décidés par chaque commune. Certaines proposent une alternative au porc pour que tous les enfants mangent, d'autres non : les deux sont légaux. Rien n'impose de viande halal, et le repas végétarien hebdomadaire est une mesure nutritionnelle prévue par la loi."},
 a_actualiser='2028-06-30', stabilite='historique',
))

# 6 ── Le RN et le voile ──────────────────────────────────────────────────────
FICHES.append(fiche(
 id='rn-voile-espace-public', affirmation="Le RN veut interdire le voile dans tout l'espace public.", type='idee_recue', volet='droits', sous_theme='Laïcité',
 mots_cles=['interdire le voile', 'interdiction du voile', 'voile dans la rue', 'voile dans l espace public', 'amende pour le voile', 'foulard', 'voile islamique', 'rn voile', 'le pen voile'],
 verdict='plutot_exact', fiabilite='etabli',
 resume="Oui, c'est une proposition ancienne du RN, reprise dans sa proposition de loi de 2021 et réaffirmée en 2026 avec une amende et l'idée d'un référendum. Jordan Bardella l'avait mise en retrait en 2024 en commençant par les bâtiments publics. Des juristes la jugent contraire à la Constitution et à la Convention européenne des droits de l'homme : l'arrêt S.A.S. c. France de 2014 n'a validé que l'interdiction de dissimuler le visage, pas celle du foulard.",
 contexte="La question est posée par des électeurs qui se demandent ce que ferait le RN au pouvoir ; certains soutiennent la mesure, d'autres la croient abandonnée.",
 explication="Le droit français interdit déjà la dissimulation du visage dans l'espace public (loi de 2010, validée par la Cour européenne en 2014). Interdire le foulard dans la rue irait beaucoup plus loin : cela viserait une pratique religieuse en tant que telle.",
 sources=[PS_VOILE26, PS_VOILE_REF, PS_VOILE22, CEDH_SAS],
 faits=[
  fait("En 2026, le député RN Jean-Philippe Tanguy a confirmé vouloir « sanctionner le port du voile » par « une amende », mesure annoncée pour le programme de 2027.", 'ps_voile26', '2026', 'France', "La proposition est toujours d'actualité.", 'etabli'),
  fait("La proposition de loi RN de 2021 visait, dans l'espace public, les signes ou tenues constituant une affirmation ostentatoire de l'« idéologie islamiste » ; en 2024, Jordan Bardella avait proposé de commencer par les bâtiments publics, la rue restant « un objectif à terme ».", 'ps_voile_ref', '2021-2024', 'France', "La mesure a varié selon les campagnes, mais n'a pas été abandonnée.", 'etabli'),
  fait("Selon des juristes cités par Public Sénat, une interdiction du voile dans l'espace public serait « disproportionnée » et violerait les articles 9 et 14 de la Convention européenne des droits de l'homme.", 'ps_voile26', '2026', 'France', "La mesure se heurte à la liberté religieuse et à l'interdiction des discriminations.", 'interpretation'),
  fait("En 2014, la Cour européenne a validé la loi française contre la dissimulation du visage parce qu'elle « n'est pas explicitement fondée sur la connotation religieuse des vêtements », et qu'elle n'affecte pas les tenues qui ne cachent pas le visage.", 'cedh_sas', '2014', 'Europe', "Cette jurisprudence ne peut pas justifier l'interdiction d'un foulard.", 'etabli'),
  fait("Selon le RN, la mesure serait soutenue par 60 à 70 % des Français ; ce chiffre n'a pas été vérifié par un sondage lu pour cette fiche.", 'ps_voile26', '2026', 'France', "L'argument de popularité ne règle pas la question de la constitutionnalité.", 'interpretation'),
 ],
 court="Plutôt exact : le RN propose bien d'interdire le voile dans l'espace public, avec une amende annoncée pour 2027. Mais des juristes la jugent contraire à la Constitution et à la Convention européenne des droits de l'homme.",
 moyen="Interdire le voile dans l'espace public est une proposition ancienne du RN. Elle figurait dans sa proposition de loi de 2021, et en 2026 le parti a annoncé une amende pour le programme de 2027, voire un référendum. En 2024, Jordan Bardella l'avait mise en retrait en commençant par les bâtiments publics.\n\nPour des constitutionnalistes, ce serait une atteinte disproportionnée à la liberté religieuse. L'interdiction de la burqa (2010) a été validée parce qu'elle vise le visage caché, pas la religion.",
 detaille="La mesure figure dans le programme de Marine Le Pen depuis des années. La proposition de loi RN de 2021 « visant à combattre les idéologies islamistes » visait, dans l'espace public, les signes ou tenues constituant une affirmation ostentatoire de cette idéologie. Après la dissolution de 2024, Jordan Bardella avait proposé de commencer par les bâtiments publics, la rue devenant « un objectif à terme ». En 2026, Jean-Philippe Tanguy a confirmé l'idée d'une amende, et Marine Le Pen a évoqué un référendum.\n\nLes juristes interrogés par Public Sénat sont critiques. Pour Jean-Philippe Derosier, l'interdiction serait « disproportionnée » ; pour Nicolas Hervieu, elle violerait la liberté de religion et l'interdiction des discriminations garanties par la Convention européenne. Mathieu Carpentier estime qu'un référendum de l'article 11 serait impossible sur ce sujet ; or le Conseil constitutionnel ne contrôle pas les lois adoptées par référendum depuis 1962.\n\nL'arrêt S.A.S. c. France (2014) est souvent cité : il a validé la loi contre la dissimulation du visage parce qu'elle ne visait pas la connotation religieuse des vêtements. Interdire un foulard qui laisse le visage visible, c'est viser une pratique religieuse : c'est tout l'inverse.",
 empathie="Je comprends que le voile puisse te mettre mal à l'aise et que tu veuilles savoir ce que ferait vraiment le RN. Il propose bien de l'interdire dans la rue, avec une amende ; mais ce serait la première fois qu'on sanctionne des femmes pour une tenue qui ne cache pas leur visage.",
 legitimes=["La mesure est présentée par le RN comme populaire ; aucun sondage n'a été lu pour le vérifier.", "La position du RN a varié (2022, 2024, 2026) : son contenu exact pour 2027 n'est pas encore connu."],
 contre=[
  ("On a bien interdit la burqa.", "La loi de 2010 vise la dissimulation du visage, pour toutes les tenues ; c'est pour cela que la Cour européenne l'a validée."),
  ("C'est pour libérer les femmes.", "Une amende frapperait d'abord les femmes elles-mêmes, y compris celles qui choisissent de le porter."),
 ],
 questions=["Qui paierait l'amende prévue par le RN, à ton avis ?", "Une loi qui vise une seule religion te semble-t-elle compatible avec la liberté de conscience ?"],
 limites=["Les textes du programme présidentiel de 2022 et de la proposition de loi de 2021 n'ont pas été lus directement : ils sont connus par Public Sénat.", "Le contenu exact de la mesure pour 2027 n'est pas encore publié."],
 publics={'convaincus': "Oui, le RN propose d'interdire le voile dans la rue, avec une amende. Mais pose-toi la question : ce sont les femmes qui paieraient. Et l'interdiction de la burqa a été validée justement parce qu'elle vise le visage caché, pas la religion ; viser un foulard, c'est autre chose.",
  'indecis': "Le RN propose bien cette interdiction, même si Jordan Bardella l'avait mise en retrait en 2024. Les juristes interrogés la jugent contraire à la liberté religieuse. Le droit actuel interdit déjà de dissimuler son visage dans la rue, quelle que soit la tenue."},
 a_actualiser='2027-06-30', stabilite='actualite',
))

# 7 ── Sortie du nucléaire ────────────────────────────────────────────────────
FICHES.append(fiche(
 id='sortie-nucleaire-penurie', affirmation="Si la gauche ferme les centrales nucléaires, on va manquer d'électricité.", volet='ecologie', sous_theme='Nucléaire',
 mots_cles=['fermer les centrales', 'sortie du nucleaire', 'sortir du nucleaire', 'fermeture des centrales', 'manquer d electricite', 'black out', 'penurie d electricite', '100 % renouvelables', 'futurs energetiques 2050', 'rte'],
 verdict='trompeur', fiabilite='interpretation',
 resume="Selon RTE, tous ses scénarios pour 2050, y compris celui sans nucléaire (M0), garantissent la sécurité d'approvisionnement. Mais M0 est le plus coûteux, exige un développement des renouvelables plus rapide que dans les pays européens les plus dynamiques et rend la France plus dépendante de ses voisins (environ 5 % du temps contre 1 %). Et « la gauche » n'est pas unanime : LFI et les écologistes veulent une sortie planifiée, le PCF défend le nucléaire et le PS veut prolonger les centrales.",
 contexte="La sortie du nucléaire défendue par LFI et les écologistes est souvent présentée comme une promesse de coupures de courant ; le débat est revenu avec la réactualisation des scénarios de RTE en 2026.",
 explication="Une sortie du nucléaire planifiée n'est pas une fermeture du jour au lendemain : les scénarios de RTE s'étalent jusqu'en 2050 et supposent de construire massivement de l'éolien, du solaire et des moyens de stockage. La question est surtout celle du coût et du rythme.",
 sources=[RTE_FE, LCP_RTE, RTE_2026, REPORTERRE_NUPES],
 faits=[
  fait("Selon le président de RTE, tous les scénarios étudiés, y compris la sortie du nucléaire en 2050, garantissent la sécurité d'approvisionnement.", 'lcp_rte', '2021', 'France', "Une sortie planifiée n'implique pas de pénurie, selon le gestionnaire du réseau.", 'etabli'),
  fait("Le scénario M0 suppose environ 208 GW de solaire, 74 GW d'éolien terrestre et 62 GW d'éolien en mer en 2050, et des rythmes de développement des renouvelables plus rapides que ceux des pays européens les plus dynamiques.", 'rte_fe', '2021', 'France', "Le défi est industriel et réel.", 'estimation', '208 GW'),
  fait("Selon RTE, sans nouveau nucléaire, la France dépendrait de ses voisins pour sa sécurité d'approvisionnement environ 5 % du temps, contre 1 % aujourd'hui, et le scénario M0 reste le plus coûteux.", 'rte_fe', '2021', 'France', "La sortie du nucléaire coûte plus cher et accroît la dépendance aux importations.", 'estimation', '5 %'),
  fait("Selon le président de RTE, en coûts complets, les scénarios avec nouveau nucléaire reviendraient environ 10 Md€ moins cher en 2050.", 'lcp_rte', '2021', 'France', "L'écart de coût est réel, même s'il dépend des hypothèses.", 'estimation', '10 Md€'),
  fait("Dans le programme de la Nupes (2022), LFI et les écologistes voulaient « planifier » la sortie du nucléaire, le PCF défendait un mix avec le nucléaire et le PS voulait optimiser la durée de vie des centrales.", 'reporterre_nupes', '2022', 'France', "La gauche est divisée sur le sujet.", 'etabli'),
  fait("En 2026, RTE rehausse ses trajectoires de consommation d'électricité, envisage de prolonger l'essentiel du parc au-delà de 60 ans et maintient le scénario sans nouveau nucléaire.", 'rte_2026', '2026', 'France', "Les hypothèses évoluent : le débat reste ouvert.", 'etabli'),
 ],
 court="Trompeur : selon RTE, même le scénario sans nucléaire en 2050 garantit l'approvisionnement. Mais il est le plus coûteux et le plus exigeant. Et toute la gauche ne veut pas sortir du nucléaire : le PCF le défend.",
 moyen="Personne à gauche ne propose de fermer les centrales du jour au lendemain. LFI et les écologistes veulent une sortie planifiée d'ici 2050 ; le PCF défend le nucléaire et le PS veut prolonger les centrales.\n\nRTE, le gestionnaire du réseau, a étudié une sortie complète en 2050 : elle garantit l'approvisionnement, mais coûte plus cher que les scénarios avec nouveaux réacteurs, demande de construire très vite de l'éolien et du solaire et rend la France plus dépendante de ses voisins.",
 detaille="En 2021, RTE a publié six scénarios pour atteindre la neutralité carbone en 2050. Le scénario M0 prévoit la sortie du nucléaire en 2050, avec environ 208 GW de solaire, 74 GW d'éolien terrestre et 62 GW d'éolien en mer. Selon le président de RTE, tous les scénarios garantissent la sécurité d'approvisionnement.\n\nMais M0 a des inconvénients sérieux : il suppose des rythmes de développement des renouvelables supérieurs à ceux des pays européens les plus dynamiques, il reste le plus coûteux (selon le président de RTE, les scénarios avec nouveau nucléaire reviendraient environ 10 Md€ moins cher en 2050) et il rend la France dépendante de ses voisins environ 5 % du temps, contre 1 % aujourd'hui. Son coût ne se rapproche des autres qu'à plusieurs conditions (éolien flottant, financement favorable, hydrogène compétitif).\n\nÀ gauche, le sujet divise : LFI et les écologistes défendent une sortie planifiée, le PCF un mix avec le nucléaire, le PS la prolongation des centrales. En 2026, RTE rehausse ses prévisions de consommation et envisage de prolonger l'essentiel du parc au-delà de 60 ans. Le vrai débat porte sur le coût, le rythme et les risques, pas sur des coupures de courant promises par un camp.",
 empathie="Je comprends qu'on s'inquiète pour sa facture et pour le risque de coupures, surtout après les hivers tendus. Mais personne ne propose de tout fermer d'un coup : RTE a montré qu'une sortie planifiée tient l'approvisionnement, même si elle coûterait plus cher.",
 legitimes=["Le scénario sans nucléaire est le plus coûteux et le plus risqué industriellement selon RTE.", "Il augmente la dépendance aux importations d'électricité."],
 contre=[
  ("L'Allemagne a fermé ses centrales et brûle du charbon.", "Le scénario étudié par RTE pour la France est neutre en carbone ; la comparaison avec l'Allemagne n'a pas été étudiée par les sources lues."),
  ("Les renouvelables sont intermittents.", "C'est pourquoi le scénario M0 prévoit stockage, flexibilités et interconnexions, et coûte plus cher."),
 ],
 questions=["Sais-tu que le PCF, à gauche, défend le nucléaire ?", "Qu'est-ce qui te paraît le plus important : le coût, la sûreté ou la dépendance aux importations ?"],
 limites=["L'étude de RTE date de 2021 ; sa réactualisation est en cours en 2026 et pourrait modifier les chiffres.", "La position actuelle de chaque parti de gauche pour 2027 n'a pas été vérifiée ; la fiche s'appuie sur le programme de 2022."],
 publics={'convaincus': "RTE, qui gère le réseau électrique, a étudié la sortie du nucléaire en 2050 : l'approvisionnement est garanti, mais ça coûterait plus cher. Et la gauche n'est pas d'accord sur le sujet : le PCF est pour le nucléaire. Parler de coupures de courant, c'est déformer le débat.",
  'indecis': "Ton inquiétude sur le prix et les coupures est légitime. Selon RTE, une sortie du nucléaire en 2050 tiendrait l'approvisionnement mais coûterait plus cher et nous rendrait plus dépendants de nos voisins. À gauche, les avis sont partagés : c'est un vrai choix de société, pas une menace de black-out."},
 a_actualiser='2027-06-30',
))

# 8 ── Dette et Grèce ─────────────────────────────────────────────────────────
FICHES.append(fiche(
 id='dette-france-grece', affirmation="La France a la dette la plus élevée d'Europe, elle va faire faillite comme la Grèce.", volet='economie', sous_theme='Dette publique',
 mots_cles=['faillite', 'faire faillite', 'comme la grece', 'dette la plus elevee', 'dette record', 'banqueroute', 'dette publique', 'dette de la france', 'notation de la france', 'fitch'],
 verdict='trompeur', fiabilite='etabli',
 resume="La France n'a pas la dette la plus élevée d'Europe : au deuxième trimestre 2026, elle est troisième de la zone euro (119,1 % du PIB), derrière la Grèce (140,8 %) et l'Italie (139,9 %). Sa dette est longue (plus de huit ans de durée de vie moyenne) et la France reste un emprunteur de bonne qualité, noté A+. La situation est pourtant préoccupante : la dette augmente, la note a été abaissée en 2025 et la charge d'intérêts pourrait dépasser 100 milliards d'euros avant 2030.",
 contexte="La dégradation des finances publiques depuis 2023 et la baisse de la note de la France nourrissent des discours catastrophistes, utilisés pour justifier des coupes dans les dépenses sociales ou pour annoncer une faillite.",
 explication="Un État comme la France ne « fait pas faillite » comme une entreprise : il refinance sa dette en continu. Le risque est que les taux d'intérêt montent et que les intérêts pèsent de plus en plus sur le budget, ce qui réduit les marges pour les services publics.",
 sources=[EN_DETTE, EUROSTAT_DETTE, INSEE_DETTE, AFT_DETTE, PS_DETTE, FPT_FITCH],
 faits=[
  fait("Au deuxième trimestre 2026, la dette publique atteint 140,8 % du PIB en Grèce, 139,9 % en Italie et 119,1 % en France, pour 88,8 % en moyenne dans la zone euro.", 'en_dette', '2026', 'Zone euro', "La France est troisième, pas première.", 'etabli', '119,1 %'),
  fait("Selon Eurostat, le classement était le même au premier trimestre 2025 : Grèce 152,5 %, Italie 137,9 %, France 114,1 %.", 'eurostat_dette', '2025', 'Zone euro', "La France est durablement derrière la Grèce et l'Italie.", 'etabli', '114,1 %'),
  fait("Selon l'Agence France Trésor, la durée de vie moyenne de la dette négociable de l'État est de 8 ans et 163 jours fin juillet 2026.", 'aft_dette', '2026', 'France', "Une dette longue amortit les hausses de taux : il n'y a pas de mur de remboursement immédiat.", 'etabli'),
  fait("Selon la Cour des comptes, la charge de la dette atteint 60,2 Md€ en 2024 et pourrait dépasser 100 Md€ avant la fin de la décennie.", 'ps_dette', '2024', 'France', "Le poids des intérêts est un vrai problème budgétaire.", 'estimation', '60,2 Md€'),
  fait("Fitch a abaissé la note de la France de AA- à A+ en septembre 2025 ; la France reste « un émetteur de bonne qualité », mais son coussin de crédibilité s'est réduit.", 'fpt_fitch', '2025', 'France', "La confiance des prêteurs s'érode, sans rupture.", 'etabli'),
 ],
 court="Faux pour le classement : la France est troisième de la zone euro (119,1 % du PIB), derrière la Grèce (140,8 %) et l'Italie (139,9 %). Sa dette, longue et bien notée (A+), ne la menace pas de faillite, même si les intérêts pèsent de plus en plus.",
 moyen="La France n'est pas la plus endettée d'Europe : la Grèce (140,8 % du PIB) et l'Italie (139,9 %) font plus, contre 119,1 % pour la France en 2026. Sa dette est remboursée en moyenne sur plus de huit ans et elle reste un emprunteur bien noté.\n\nCela dit, la situation se dégrade : la dette monte, Fitch a abaissé la note en 2025 et les intérêts ont atteint 60 milliards en 2024, avec un risque de dépasser 100 milliards avant 2030. Le débat porte sur la manière de rééquilibrer : couper dans les dépenses ou augmenter les recettes.",
 detaille="Selon Eurostat, au deuxième trimestre 2026, la Grèce (140,8 % du PIB) et l'Italie (139,9 %) restent devant la France (119,1 %), suivie de la Belgique (110,2 %) et de l'Espagne (101,4 %). La dette grecque baisse, de 177,8 % en 2022 à 140,8 %, quand celle de la France augmente de 3,7 points sur un an. L'Insee chiffre la dette française à 3 595,5 milliards d'euros mi-2026.\n\nUne faillite « à la grecque » n'est pas en vue : la dette de l'État est majoritairement à long terme, avec une durée de vie moyenne de 8 ans et 163 jours, et la France reste notée A+. Mais la note a été abaissée en 2025, les taux se rapprochent de ceux de l'Italie, et la Cour des comptes alerte sur un possible « effet boule de neige » : la charge d'intérêts, 60,2 milliards en 2024, pourrait dépasser 100 milliards avant la fin de la décennie.\n\nLe vrai débat est donc politique : faut-il réduire la dette en coupant dans les services publics et la protection sociale, ou en augmentant les recettes, notamment sur les plus hauts revenus et patrimoines ? Brandir la faillite sert souvent à imposer la première option.",
 empathie="Je comprends que les chiffres de la dette fassent peur, et c'est un vrai sujet. Mais la France n'est pas la plus endettée d'Europe et elle n'est pas au bord de la faillite : la question est de savoir qui va payer pour la réduire.",
 legitimes=["La dette française augmente alors que celle de la Grèce baisse.", "La hausse des intérêts réduit réellement les marges budgétaires, et la note de la France a été dégradée."],
 contre=[
  ("La dette, ce sont nos enfants qui vont la payer.", "Elle se refinance en continu ; ce qui pèse, ce sont les intérêts, et le choix des recettes pour les payer est politique."),
  ("La Grèce aussi était bien notée avant la crise.", "La comparaison avec la crise grecque de 2010 n'a pas été étudiée par les sources lues ; la situation actuelle de la France reste très différente selon les agences de notation."),
 ],
 questions=["Sais-tu quels pays de la zone euro sont plus endettés que la France ?", "Pour réduire la dette, préfères-tu couper dans les services publics ou faire contribuer les plus riches ?"],
 limites=["Les chiffres Eurostat de 2026 sont repris par Euronews ; le communiqué d'Eurostat lui-même a été lu pour 2025.", "Aucune source lue ne compare directement la situation actuelle de la France à la crise grecque de 2010-2012."],
 publics={'convaincus': "Les chiffres européens sont clairs : la Grèce et l'Italie sont plus endettées que la France. Et la dette française se rembourse sur plus de huit ans en moyenne, avec une note A+. Le problème est réel, mais parler de faillite, c'est surtout préparer des coupes dans la Sécu et les retraites.",
  'indecis': "La dette inquiète à juste titre : elle augmente et les intérêts pèsent de plus en plus lourd. Mais la France reste un emprunteur de bonne qualité, et elle n'est pas la plus endettée d'Europe. Le vrai choix, c'est comment réduire le déficit : en coupant des services ou en augmentant certaines recettes."},
 a_actualiser='2027-03-31', raison="Nouvelles données trimestrielles d'Eurostat et de l'Insee.",
))

# 9 ── Ouvriers et vote RN ────────────────────────────────────────────────────
FICHES.append(fiche(
 id='ouvriers-vote-rn', affirmation="Les ouvriers votent RN parce que la gauche les a abandonnés.", volet='politique', sous_theme='Droite et extrême droite',
 mots_cles=['ouvriers votent rn', 'vote ouvrier', 'les ouvriers', 'classes populaires votent rn', 'gauche a abandonne', 'abandonne les ouvriers', 'abandonne le peuple', 'premier parti ouvrier', 'electorat ouvrier'],
 verdict='trompeur', fiabilite='interpretation',
 resume="Le constat est en partie exact : au premier tour des législatives de 2024, 57 % des ouvriers qui ont voté ont choisi le RN, contre 21 % le Nouveau Front populaire, et un tiers des Français estiment que la gauche a déçu au pouvoir. Mais près d'un ouvrier sur deux s'est abstenu, si bien que le RN rassemble environ trois ouvriers inscrits sur dix ; et les enquêtes montrent des causes multiples : peur du déclassement, sécurité, immigration, déception envers la gauche.",
 contexte="Le RN se présente comme le « premier parti ouvrier de France » ; à gauche aussi, beaucoup expliquent ce vote par un abandon des classes populaires.",
 explication="Un sondage de sortie des urnes mesure le vote des personnes qui ont voté. Pour connaître le comportement de toute une catégorie, il faut aussi tenir compte de l'abstention, très forte chez les ouvriers.",
 sources=[IPSOS_SOCIO, IPSOS_PARTI, FJJ_RN],
 faits=[
  fait("Selon Ipsos, au premier tour des législatives de 2024, 57 % des ouvriers votants ont choisi le RN et ses alliés (+12 points par rapport à 2022), contre 21 % le NFP.", 'ipsos_socio', '2024', 'France', "Le RN est bien le premier choix des ouvriers qui votent.", 'estimation', '57 %'),
  fait("Selon Ipsos, la participation des ouvriers au premier tour de 2024 n'était que de 54 %, contre 65 % chez les cadres et 79 % chez les retraités.", 'ipsos_parti', '2024', 'France', "Près d'un ouvrier sur deux ne vote pas : le RN ne représente qu'environ trois ouvriers inscrits sur dix (calcul à partir des deux enquêtes).", 'estimation', '54 %'),
  fait("Selon Ipsos, le vote RN a aussi doublé chez les cadres, de 11 % en 2022 à 22 % en 2024.", 'ipsos_socio', '2022-2024', 'France', "La progression du RN ne concerne pas que les ouvriers.", 'estimation', '22 %'),
  fait("Selon une enquête pour la Fondation Jean-Jaurès, 33 % des personnes interrogées estiment que « la gauche a déçu lorsqu'elle était au pouvoir », 28 % la jugent déconnectée des classes populaires, 28 % trouvent qu'elle ne parle pas assez de sécurité et 27 % pas assez d'immigration.", 'fjj_rn', '2024', 'France', "La déception envers la gauche est réelle, mais elle n'est qu'un motif parmi d'autres.", 'estimation', '33 %'),
 ],
 court="En partie seulement : 57 % des ouvriers qui ont voté ont choisi le RN en 2024, mais près d'un sur deux s'est abstenu. Et les enquêtes trouvent plusieurs causes : déclassement, sécurité, immigration, déception envers la gauche.",
 moyen="Parmi les ouvriers qui ont voté au premier tour de 2024, 57 % ont choisi le RN. Mais seulement 54 % des ouvriers sont allés voter : le RN rassemble donc environ trois ouvriers sur dix, pas la classe ouvrière entière.\n\nLa déception envers la gauche compte : un tiers des Français jugent qu'elle a déçu au pouvoir. Mais les enquêtes citent aussi la peur du déclassement, la sécurité et l'immigration. Le RN progresse d'ailleurs aussi chez les cadres.",
 detaille="Selon Ipsos, au premier tour des législatives de 2024, le RN et ses alliés ont obtenu 57 % des voix des ouvriers votants, 12 points de plus qu'en 2022, contre 21 % pour le Nouveau Front populaire. Le RN est donc le premier choix des ouvriers qui votent.\n\nMais il faut regarder l'abstention : seuls 54 % des ouvriers ont voté, la participation la plus faible de toutes les catégories. Rapporté à l'ensemble des ouvriers inscrits, le vote RN représente environ trois ouvriers sur dix. Une grande partie du monde ouvrier ne se reconnaît dans aucun parti.\n\nL'explication par « l'abandon » a une part de vérité, reconnue jusque dans la gauche : selon l'enquête de la Fondation Jean-Jaurès, un tiers des Français estiment que la gauche a déçu au pouvoir, et 28 % la jugent déconnectée des classes populaires. Mais la sécurité et l'immigration sont citées presque aussi souvent, et les auteurs décrivent surtout la peur du « grand déclassement ». Le RN progresse aussi chez les cadres. Reconquérir le vote populaire passe par des réponses concrètes sur les salaires, les services publics et la dignité au travail, pas seulement par un mea culpa.",
 empathie="Je comprends le sentiment d'avoir été laissé de côté, et la gauche a sa part de responsabilité. Mais regarde les chiffres : près d'un ouvrier sur deux ne vote plus du tout, et les raisons du vote RN sont multiples.",
 legitimes=["La gauche au pouvoir a déçu une partie des classes populaires, et des responsables de gauche le reconnaissent.", "Le RN est bien le premier parti chez les ouvriers qui votent."],
 contre=[
  ("Le RN est le premier parti ouvrier, point.", "Chez les votants, oui ; mais l'abstention reste la première attitude des ouvriers."),
  ("La gauche ne parle plus qu'aux bobos.", "Une partie des sondés le pense ; les enquêtes montrent aussi que la sécurité et l'immigration pèsent autant dans le vote RN."),
 ],
 questions=["Sais-tu combien d'ouvriers sont allés voter en 2024 ?", "Qu'est-ce qu'un parti devrait proposer concrètement pour que les ouvriers se sentent défendus ?"],
 limites=["Les chiffres sont des estimations par sondage, avec une marge d'erreur.", "Aucune étude lue n'isole « l'abandon » comme cause du vote ; aucun travail du Cevipof n'a été lu pour cette fiche."],
 publics={'convaincus': "C'est vrai, 57 % des ouvriers qui ont voté en 2024 ont choisi le RN. Mais presque un ouvrier sur deux n'a pas voté du tout. Et qu'a fait le RN pour les salaires ouvriers là où il a voté ? Il ne suffit pas de dire qu'on défend les ouvriers.",
  'indecis': "La déception envers la gauche est réelle, et la gauche doit l'entendre. Mais le vote RN des ouvriers a plusieurs causes : peur du déclassement, sécurité, immigration. Et la première attitude des ouvriers reste l'abstention : beaucoup ne se sentent représentés par personne."},
 a_actualiser='2027-06-30',
))

# 10 ── Écriture inclusive ────────────────────────────────────────────────────
FICHES.append(fiche(
 id='ecriture-inclusive-ecole', affirmation="L'écriture inclusive est imposée aux enfants à l'école.", volet='services', sous_theme='École publique',
 mots_cles=['ecriture inclusive', 'point median', 'inclusive a l ecole', 'iel', 'langage inclusif', 'imposee aux enfants', 'circulaire blanquer'],
 verdict='contredit', fiabilite='etabli',
 resume="C'est l'inverse : depuis la circulaire du 5 mai 2021, l'usage et l'enseignement de l'écriture inclusive, notamment du point médian, sont proscrits à l'école, et le Conseil d'État a jugé cette interdiction légale en décembre 2024. L'école demande seulement de féminiser les noms de fonctions. L'usage existe en revanche à l'université, ce qui a conduit le Sénat à voter en 2023 une proposition de loi pour l'interdire plus largement.",
 contexte="L'écriture inclusive est devenue un symbole du « wokisme » supposé de l'école ; des rumeurs évoquent des manuels ou des cours qui l'imposeraient aux élèves.",
 explication="L'« écriture inclusive » regroupe plusieurs pratiques : le point médian (« les élu·es »), la double flexion (« les Françaises et les Français ») et la féminisation des noms de métiers. L'interdiction scolaire vise surtout le point médian.",
 sources=[CE_INCLUSIVE, SENAT_INCLUSIVE, PS_INCLUSIVE],
 faits=[
  fait("La circulaire du 5 mai 2021 « proscrit l'usage et l'enseignement de certaines règles relevant de l'écriture inclusive, et notamment le point médian » à l'école.", 'ce_inclusive', '2021', 'France', "La règle officielle interdit ce qu'on accuse l'école d'imposer.", 'etabli'),
  fait("Le Conseil d'État a jugé cette interdiction légale le 20 décembre 2024, en retenant l'objectif de faciliter l'apprentissage de la lecture.", 'ce_inclusive', '2024', 'France', "L'interdiction a été confirmée par la justice.", 'etabli'),
  fait("La même circulaire demande aux enseignants de féminiser systématiquement les noms de fonctions.", 'ce_inclusive', '2021', 'France', "L'école demande « la directrice », pas le point médian.", 'etabli'),
  fait("Le Sénat relève une progression de l'écriture inclusive à l'université et a adopté le 30 octobre 2023, par 221 voix contre 82, une proposition de loi pour l'interdire plus largement ; son adoption à l'Assemblée restait incertaine.", 'ps_inclusive', '2023', 'France', "Le débat existe, mais il concerne surtout l'enseignement supérieur.", 'etabli'),
 ],
 court="Faux : depuis 2021, une circulaire interdit le point médian à l'école, et le Conseil d'État l'a jugée légale en 2024. L'école demande seulement de féminiser les noms de fonctions.",
 moyen="Les élèves n'apprennent pas l'écriture inclusive : depuis la circulaire du 5 mai 2021, son usage et son enseignement, notamment le point médian, sont interdits à l'école. Le Conseil d'État a validé cette interdiction en décembre 2024.\n\nCe que l'école demande, c'est de féminiser les noms de fonctions (« la directrice »). Le débat porte surtout sur l'université, où certains enseignants l'utilisent ; le Sénat a voté en 2023 une proposition de loi pour l'interdire aussi.",
 detaille="Le ministre de l'Éducation nationale a signé le 5 mai 2021 une circulaire qui proscrit l'usage et l'enseignement de l'écriture inclusive, notamment du point médian, dans les pratiques d'enseignement, au nom de l'apprentissage de la lecture et du respect des règles grammaticales. Un parent d'élève l'a contestée ; le Conseil d'État a rejeté son recours le 20 décembre 2024.\n\nLa circulaire demande en revanche de féminiser systématiquement les noms de fonctions. Une circulaire du Premier ministre de 2017 ne visait que les textes publiés au Journal officiel.\n\nLe Sénat constate une progression de ces usages à l'université et a adopté en octobre 2023 une proposition de loi pour interdire l'écriture inclusive dans les cours, examens et thèses ; la double flexion (« les Françaises et les Français ») resterait permise. On peut débattre de l'écriture inclusive ; mais elle n'est pas imposée aux enfants, elle leur est interdite.",
 empathie="Je comprends qu'on s'inquiète de ce que les enfants apprennent, surtout quand on lit des histoires de points médians dans les cahiers. Mais la règle est claire depuis 2021 : l'écriture inclusive est interdite à l'école, et la justice l'a confirmé.",
 legitimes=["Des usages existent à l'université, selon le Sénat.", "Aucune donnée ne mesure les pratiques réelles de chaque enseignant en classe."],
 contre=[
  ("Mon enfant a reçu un document avec des points médians.", "C'est possible ponctuellement, mais c'est contraire à la circulaire ; on peut le signaler à l'établissement."),
  ("Dire « les Françaises et les Français », c'est déjà de l'inclusif.", "C'est une double flexion, que l'usage ancien connaît et que même la proposition du Sénat n'interdit pas."),
 ],
 questions=["Sais-tu que l'écriture inclusive est interdite à l'école depuis 2021 ?", "Qu'est-ce qui te gêne : le point médian ou le fait de dire « la directrice » ?"],
 limites=["Le texte du Bulletin officiel de 2021 n'a pas pu être lu directement ; son contenu est connu par la décision du Conseil d'État et le Sénat.", "Le sort de la proposition de loi du Sénat à l'Assemblée n'a pas été vérifié."],
 publics={'convaincus': "C'est l'inverse : une circulaire de 2021 interdit l'écriture inclusive à l'école, et le Conseil d'État l'a validée en 2024. Si tu as vu un cas, c'est une exception contraire aux règles, pas une politique imposée aux enfants.",
  'indecis': "La règle est simple : à l'école, le point médian est interdit depuis 2021, et la justice l'a confirmé. On demande seulement de féminiser les noms de métiers. Le débat existe surtout à l'université, où le Sénat a voté en 2023 un texte pour l'interdire aussi."},
 a_actualiser='2028-06-30', stabilite='historique',
))

# 11 ── Radars ────────────────────────────────────────────────────────────────
FICHES.append(fiche(
 id='radars-pompe-a-fric', affirmation="Les radars sont une pompe à fric pour l'État.", volet='securite', sous_theme='Prévention et politiques publiques',
 mots_cles=['radars', 'radar', 'pompe a fric', 'amendes radar', 'flash', 'controle automatise', 'limitation de vitesse', 'amendes routieres', 'securite routiere'],
 verdict='trompeur', fiabilite='interpretation',
 resume="En partie : en 2024, les amendes de la circulation ont rapporté 2,07 milliards d'euros, dont 658 millions pour les seuls radars, et environ 715 millions sont allés au désendettement de l'État, ce que la Cour des comptes et le Sénat critiquent. Mais environ 736 millions vont aux collectivités, et les évaluations officielles attribuent aux radars 75 % de la baisse de la mortalité routière entre 2003 et 2010 : de 5 737 morts en 2003 à 3 268 dix ans plus tard.",
 contexte="Les radars sont l'un des symboles de la défiance envers l'État.",
 explication="Les amendes alimentent un compte spécial du budget de l'État, réparti entre le financement des radars et de la sécurité routière, les collectivités (voirie, transports) et le remboursement de la dette. Cette répartition est un choix budgétaire, distinct de l'efficacité des radars sur la sécurité.",
 sources=[CC_RADARS, SENAT_RADARS, AN_RADARS, SENAT_RADARS17],
 faits=[
  fait("Selon la Cour des comptes, les amendes de la circulation et du stationnement ont rapporté 2 070 M€ en 2024, dont 658 M€ d'amendes radars non majorées.", 'cc_radars', '2024', 'France', "Les radars ne représentent qu'environ un tiers des amendes.", 'etabli', '658 M€'),
  fait("En 2024, 715,1 M€ ont été affectés au désendettement de l'État, 735,7 M€ aux collectivités et 341,2 M€ aux radars et à la sécurité routière ; la Cour juge que seuls 62 % des crédits servent la sécurité routière.", 'cc_radars', '2024', 'France', "La critique d'une recette qui finance la dette est fondée.", 'etabli', '715 M€'),
  fait("Selon le Sénat, pour 2025, 38,9 % du compte vont au désendettement et au moins 35,1 % des crédits n'ont aucun lien avec la sécurité ou les infrastructures routières.", 'senat_radars', '2025', 'France', "Le Parlement lui-même pointe ce problème.", 'etabli', '38,9 %'),
  fait("Selon le ministère de l'Intérieur, la mortalité routière est passée de 5 737 morts en 2003 à 3 268 dix ans plus tard ; une évaluation de 2013 attribue 75 % de la baisse entre 2003 et 2010 au contrôle automatisé.", 'an_radars', '2003-2021', 'France', "Les radars sauvent des vies.", 'etabli', '75 %'),
  fait("Le Sénat (2017) reconnaît aux radars « un véritable impact, très positif » sur la mortalité, mais attribue une partie de la baisse aux véhicules et à la prévention.", 'senat_radars17', '2017', 'France', "L'effet est réel, même s'il n'explique pas tout.", 'interpretation'),
 ],
 court="En partie : environ 39 % du produit des amendes routières va au désendettement de l'État, ce que critique la Cour des comptes. Mais les radars ont contribué à 75 % de la baisse de la mortalité de 2003 à 2010.",
 moyen="Les amendes routières rapportent environ 2 milliards par an, dont 658 millions pour les radars en 2024. La Cour des comptes et le Sénat critiquent le fait qu'une grosse part, environ 715 millions, serve à rembourser la dette de l'État plutôt que la sécurité routière.\n\nMais les radars fonctionnent : les morts sur la route sont passés de 5 737 en 2003 à 3 268 dix ans plus tard, et une évaluation officielle attribue 75 % de la baisse entre 2003 et 2010 au contrôle automatisé.",
 detaille="En 2024, les amendes de la circulation et du stationnement ont rapporté 2 070 millions d'euros, dont 658 millions d'amendes radars non majorées. Le compte spécial qui les reçoit finance le contrôle automatisé et la sécurité routière (341 millions), les collectivités pour la voirie et les transports (736 millions) et le désendettement de l'État (715 millions). La Cour des comptes juge que seuls 62 % des crédits servent la sécurité routière et recommande de supprimer ce compte ; le Sénat estime qu'au moins 35 % des crédits n'ont aucun lien avec la route.\n\nCette critique budgétaire est fondée. Mais elle ne dit rien de l'efficacité des radars. Selon le ministère de l'Intérieur, la mortalité routière est passée de 5 737 morts en 2003 à 3 268 dix ans plus tard ; une évaluation de 2013 attribue 75 % de la baisse 2003-2010 au contrôle automatisé, et l'Inspection générale de l'administration juge son efficacité « avérée ». Le Sénat note que d'autres facteurs ont joué (véhicules plus sûrs, prévention).\n\nOn peut donc défendre les radars et demander que tout l'argent des amendes serve à la sécurité routière et aux transports du quotidien, plutôt qu'au remboursement de la dette.",
 empathie="Je comprends l'agacement quand on se fait flasher à quelques kilomètres-heure près, et c'est vrai qu'une partie de l'argent sert à rembourser la dette. Mais les radars ont fortement contribué à la baisse des morts sur la route depuis 2003 : le problème, c'est l'usage de l'argent, pas leur existence.",
 legitimes=["Environ 39 % du compte des amendes finance le désendettement de l'État, sans lien avec la route.", "La mortalité routière stagne depuis le début des années 2010."],
 contre=[
  ("Les radars sont placés là où ils rapportent, pas là où c'est dangereux.", "Le Sénat a jugé non concluante la corrélation entre accidents et nombre de radars par département ; ce point mérite d'être débattu."),
  ("La baisse des morts vient des voitures plus sûres.", "Elle y contribue, mais l'évaluation officielle attribue l'essentiel de la baisse 2003-2010 aux radars."),
 ],
 questions=["Sais-tu combien de morts il y avait sur les routes avant les radars automatiques ?", "Serais-tu d'accord pour que tout l'argent des amendes aille à la sécurité routière ?"],
 limites=["L'évaluation de l'effet des radars date de 2013 ; la mortalité récente (2024-2025) n'a pas été vérifiée.", "Les données de l'ONISR n'ont pas été lues directement : elles sont reprises par une réponse ministérielle."],
 publics={'convaincus': "Tu as raison sur un point : près de 40 % de l'argent des amendes sert à rembourser la dette, et la Cour des comptes le critique. Mais les radars ont fait passer les morts sur la route de 5 737 en 2003 à 3 268 dix ans plus tard. Exige que l'argent serve aux routes, mais ne jette pas les radars.",
  'indecis': "Les radars rapportent de l'argent, et une partie finance la dette de l'État, ce qui est contestable. Mais leur effet sur la sécurité est établi : ils expliquent l'essentiel de la baisse des morts entre 2003 et 2010. On peut défendre les radars et une meilleure utilisation des amendes."},
 a_actualiser='2027-06-30',
))

# 12 ── Georges Marchais et l'immigration ─────────────────────────────────────
FICHES.append(fiche(
 id='marchais-immigration-1981', affirmation="Même Georges Marchais voulait arrêter l'immigration.", volet='politique', sous_theme='Histoire politique contemporaine',
 mots_cles=['georges marchais', 'marchais', 'bulldozer de vitry', 'vitry', 'pcf immigration', 'communistes immigration', 'lettre au recteur', 'mosquee de paris 1981'],
 verdict='plutot_exact', fiabilite='etabli', stabilite='historique',
 resume="C'est en partie exact : fin 1980, le PCF de Georges Marchais a soutenu l'opération de Vitry, où des militants communistes ont bloqué au bulldozer l'installation de travailleurs maliens, et Marchais a approuvé le refus de « laisser s'accroître » le nombre d'immigrés dans la commune. Mais l'épisode a été condamné à gauche dès 1981, et des historiens y voient un calcul électoral qui a contribué à banaliser la stigmatisation des immigrés dans toute la classe politique : c'est un contre-exemple, pas un modèle.",
 contexte="La phrase est souvent utilisée pour montrer que l'opposition à l'immigration serait aussi une valeur de gauche, ou que le RN reprendrait l'héritage du PCF.",
 explication="Fin 1980, avant la présidentielle de 1981, le PCF est en recul. Il dénonce la concentration des immigrés dans les communes ouvrières qu'il dirige. L'opération de Vitry et l'affaire de Montigny-lès-Cormeilles marquent une rupture avec sa ligne antérieure d'unité des travailleurs français et immigrés.",
 sources=[HARGREAVES, CSM_1981, TS_1981],
 faits=[
  fait("En décembre 1980, le maire communiste de Vitry, « soutenu par Georges Marchais et le Comité central du PCF », fait bloquer par un bulldozer l'installation de travailleurs maliens dans un foyer.", 'hargreaves', '1980', 'Vitry-sur-Seine', "Le fait est établi, et il engage la direction du PCF.", 'etabli'),
  fait("Le 10 janvier 1981, Georges Marchais déclare : « J'approuve son refus [...] de laisser s'accroître dans sa commune le nombre élevé de travailleurs immigrés ».", 'ts_1981', '1981', 'France', "La position de Marchais est documentée.", 'etabli'),
  fait("À l'époque, le PSU juge que « cela ne justifie pas les moyens employés contre les travailleurs maliens ».", 'ts_1981', '1981', 'France', "L'épisode est condamné à gauche dès 1981.", 'etabli'),
  fait("Selon le Christian Science Monitor (1981), à Montigny-lès-Cormeilles, l'accusation de trafic de drogue qui visait un habitant marocain, fondée sur une lettre anonyme, s'est révélée infondée ; le journal juge ce virage incohérent avec la ligne d'unité des travailleurs.", 'csm_1981', '1981', 'France', "La campagne du PCF s'appuyait aussi sur des accusations fausses.", 'etabli'),
  fait("Pour le chercheur Alec Hargreaves, ces épisodes relèvent de calculs électoraux au détriment des immigrés et ont préparé leur stigmatisation dans l'ensemble de la classe politique.", 'hargreaves', '2016', 'France', "Ce n'est pas un héritage dont la gauche peut être fière.", 'interpretation'),
 ],
 court="En partie exact : en 1980-1981, le PCF de Marchais a soutenu l'opération du bulldozer de Vitry contre un foyer de travailleurs maliens. Mais l'épisode a été condamné à gauche, et les historiens y voient un calcul électoral qui a aidé à banaliser la stigmatisation des immigrés.",
 moyen="C'est un épisode réel : en décembre 1980, des militants communistes de Vitry ont bloqué au bulldozer un foyer destiné à des travailleurs maliens, avec le soutien de Georges Marchais, qui a approuvé le refus d'accueillir plus d'immigrés dans la commune.\n\nMais à l'époque déjà, une partie de la gauche l'a condamné, et la presse y voyait une rupture avec la tradition d'unité ouvrière. Des historiens y voient un calcul électoral qui a ouvert la voie à la stigmatisation des immigrés. Citer Marchais, c'est citer une faute, pas une caution.",
 detaille="Fin décembre 1980, à Vitry-sur-Seine, une cinquantaine de militants communistes menés par le maire enfoncent au bulldozer l'entrée d'un foyer où venaient d'être transférés quelque trois cents travailleurs maliens, et coupent l'eau, le gaz et l'électricité. Le 10 janvier 1981, Georges Marchais déclare approuver le refus du maire de « laisser s'accroître » le nombre de travailleurs immigrés dans sa commune. Deux mois plus tard, à Montigny-lès-Cormeilles, des militants communistes manifestent contre une famille marocaine accusée, à tort, de trafic de drogue.\n\nLa gauche de l'époque réagit : le PSU juge que rien ne justifie « les moyens employés contre les travailleurs maliens ». La presse étrangère note la rupture avec la ligne d'unité des travailleurs français et immigrés. Pour l'historien Alec Hargreaves, ces épisodes relèvent de calculs électoraux et ont préparé la stigmatisation des immigrés dans toute la classe politique.\n\nL'argument « même Marchais » montre surtout qu'un parti de gauche peut céder à la tentation de désigner des boucs émissaires, et que cela n'a servi ni les ouvriers ni la gauche. Le PCF dénonçait alors la concentration des immigrés dans les communes ouvrières : la question de la répartition du logement social est réelle, mais elle ne se règle pas au bulldozer.",
 empathie="Je comprends que tu t'appuies sur Marchais pour dire que la gauche aussi voulait limiter l'immigration. C'est vrai qu'il l'a soutenu en 1980-1981 ; mais même à gauche, on l'a condamné, et cet épisode a surtout servi ceux qui désignaient les immigrés comme coupables.",
 legitimes=["Le PCF de Georges Marchais a bien soutenu l'opération de Vitry et défendu l'arrêt de nouvelles arrivées.", "Le PCF dénonçait une concentration réelle des immigrés dans certaines communes ouvrières."],
 contre=[
  ("Le PCF était le parti des ouvriers, donc il avait raison.", "Une partie de la gauche l'a condamné dès 1981, et cette stratégie n'a pas empêché le recul du PCF."),
  ("C'est la gauche d'aujourd'hui qui a trahi Marchais.", "C'est surtout Marchais qui avait rompu avec la ligne d'unité des travailleurs, selon la presse de l'époque."),
 ],
 questions=["Sais-tu comment la gauche de l'époque a réagi à l'opération de Vitry ?", "Bloquer un foyer de travailleurs, est-ce que ça règle le problème du logement dans une ville ?"],
 limites=["Le texte original de la lettre de Georges Marchais publiée dans L'Humanité en janvier 1981 n'a pas été lu dans une source d'archives ; ses formules exactes ne sont pas citées.", "L'évolution ultérieure du PCF sur l'immigration n'a pas été documentée par les sources lues.", "Un témoignage militant conteste certains détails de l'opération (rôle du bulldozer, présence du maire) ; il n'a pas été retenu, faute de corroboration."],
 publics={'convaincus': "Oui, Marchais a soutenu l'opération du bulldozer de Vitry en 1980. Mais à l'époque déjà, une partie de la gauche l'a condamné, et l'accusation lancée contre une famille marocaine à Montigny s'est révélée fausse. Si c'est l'exemple qu'on cite, c'est celui d'une erreur qui a surtout servi l'extrême droite.",
  'indecis': "L'épisode est réel : en 1980-1981, le PCF a voulu limiter l'arrivée d'immigrés dans ses villes ouvrières. Il dénonçait une concentration réelle dans certaines communes. Mais les historiens y voient un calcul électoral qui a contribué à banaliser la stigmatisation des immigrés, sans régler les problèmes de logement."},
 a_actualiser='2030-12-31',
))

# 13 ── Émeutes de 2023 ───────────────────────────────────────────────────────
FICHES.append(fiche(
 id='emeutes-2023-etrangers', affirmation="Les émeutes de 2023 ont été commises par des étrangers.", volet='securite', sous_theme='Violences',
 mots_cles=['emeutes', 'emeutes de 2023', 'emeutiers', 'violences urbaines', 'nahel', 'emeutes nahel', 'banlieues en feu', 'emeutiers etrangers'],
 verdict='contredit', fiabilite='etabli',
 resume="Non : selon le rapport des inspections de la justice et de l'administration, 79 % des personnes mises en cause lors des violences urbaines de juin-juillet 2023 étaient de nationalité française et 75 % étaient nées en France. Le profil type est un jeune homme français d'environ 23 ans, sans antécédent judiciaire dans 57 % des cas, et près de trois mis en cause sur dix étaient mineurs. Les étrangers restent surreprésentés par rapport à leur part dans la population, mais très minoritaires.",
 contexte="Après la mort de Nahel, fin juin 2023, des violences ont touché de nombreuses villes du 27 juin au 7 juillet ; elles ont été attribuées à l'immigration par une partie de la classe politique.",
 explication="Les inspections ont étudié les personnes interpellées et condamnées. La nationalité dit si une personne est française ou étrangère ; elle ne dit rien de l'origine de ses parents, que les statistiques judiciaires ne mesurent pas.",
 sources=[IGA_EMEUTES, PS_EMEUTES23, PS_EMEUTES24, INSEE_IMMI],
 faits=[
  fait("Selon le rapport IGJ-IGA, 79 % des mis en cause sont de nationalité française et 75 % sont nés en France ; sur un échantillon de 395 condamnés, 78 % sont français.", 'iga_emeutes', '2023', 'France', "Les émeutiers sont très majoritairement français.", 'etabli', '79 %'),
  fait("Selon le même rapport, 57 % des condamnés n'avaient aucun antécédent judiciaire, l'âge moyen des hommes est de 23 ans et les mineurs représentent 28 % des mis en cause.", 'iga_emeutes', '2023', 'France', "Beaucoup de très jeunes primo-délinquants.", 'etabli', '57 %'),
  fait("Selon la commission d'enquête du Sénat, 71 % des émeutiers sont de nationalité française et 91 % sont des hommes ; elle juge les données disponibles « fort insuffisantes ».", 'ps_emeutes24', '2024', 'France', "Les chiffres varient selon les sources, mais la conclusion est la même.", 'estimation', '71 %'),
  fait("Selon l'Insee, les étrangers représentent 9,1 % de la population en 2025.", 'insee_immi', '2025', 'France', "Avec environ 21 % de mis en cause étrangers, ils sont surreprésentés, mais restent très minoritaires (comparaison indicative, années différentes).", 'etabli', '9,1 %'),
 ],
 court="Faux : 79 % des personnes mises en cause en 2023 étaient françaises et 75 % nées en France, selon les inspections de l'État. Le profil type : un jeune Français de 23 ans, sans antécédent dans 57 % des cas.",
 moyen="Les inspections de la justice et de l'administration ont étudié les personnes interpellées pendant les violences de l'été 2023 : 79 % étaient françaises et 75 % nées en France. Le profil type est un jeune homme de 23 ans, souvent sans casier, et près de trois sur dix étaient mineurs.\n\nLes étrangers, environ 21 % des mis en cause, sont surreprésentés par rapport à leur part dans la population (9 %), mais ils sont loin d'être majoritaires. Ces émeutes sont d'abord celles de jeunes Français de quartiers populaires.",
 detaille="Après la mort de Nahel, fin juin 2023, des violences ont éclaté dans de nombreuses villes. L'Inspection générale de la justice et l'Inspection générale de l'administration ont analysé le profil des personnes interpellées. Selon leurs chiffres, 79 % des mis en cause étaient de nationalité française et 75 % étaient nés en France ; sur 395 condamnés étudiés, 78 % étaient français. L'âge moyen des hommes était de 23 ans, 57 % des condamnés n'avaient aucun antécédent, et les mineurs représentaient 28 % des mis en cause.\n\nLa commission d'enquête du Sénat arrive à une conclusion proche (71 % de Français), tout en jugant les données « fort insuffisantes ». Les inspecteurs parlent d'une « photographie à l'instant T ».\n\nLes étrangers, environ un mis en cause sur cinq, sont surreprésentés par rapport à leur part dans la population (9,1 % en 2025). Mais attribuer ces émeutes à l'immigration ne tient pas : ce sont surtout de jeunes Français, souvent des primo-délinquants. Comprendre ces violences suppose de regarder la relation avec la police, l'échec scolaire et la relégation de certains quartiers.",
 empathie="Je comprends la colère devant des voitures brûlées et des commerces pillés : ces violences ont fait de vraies victimes. Mais les chiffres de l'État montrent que les émeutiers étaient surtout de jeunes Français, nés ici : chercher la cause dans l'immigration, c'est passer à côté du problème.",
 legitimes=["Les étrangers sont surreprésentés parmi les mis en cause par rapport à leur part dans la population.", "Les statistiques ne mesurent pas l'origine des parents des personnes françaises."],
 contre=[
  ("Ils sont français sur le papier.", "Ils sont français, nés en France pour 75 % d'entre eux : c'est une réalité juridique, et leurs problèmes se sont formés ici."),
  ("Les chiffres ne portent que sur ceux qui ont été arrêtés.", "C'est vrai, et le Sénat juge les données insuffisantes ; mais aucune source ne montre une majorité d'étrangers."),
 ],
 questions=["Sais-tu quelle part des émeutiers étaient nés en France ?", "Qu'est-ce qui, selon toi, pousse des adolescents sans casier à participer à des émeutes ?"],
 limites=["Les données portent sur les personnes interpellées et poursuivies, pas sur l'ensemble des participants.", "La nationalité des mineurs, étudiée en annexe du rapport, n'a pas été lue.", "La comparaison avec la part des étrangers dans la population est indicative (années et champs différents)."],
 publics={'convaincus': "Ce sont les chiffres de l'État, pas d'une association : 79 % des émeutiers étaient français, 75 % nés en France. Les étrangers sont un peu surreprésentés, mais ce sont surtout de jeunes Français de 23 ans, sans casier. Expulser des étrangers n'aurait pas empêché ces émeutes.",
  'indecis': "Ces violences ont choqué, et c'est normal de chercher à comprendre. Les inspections montrent un profil clair : des jeunes hommes, surtout français et nés en France, souvent sans antécédent. Les étrangers sont un peu surreprésentés, mais les causes sont à chercher dans les quartiers eux-mêmes."},
 a_actualiser='2028-06-30', stabilite='historique',
))

# 14 ── Passage à l'euro ──────────────────────────────────────────────────────
FICHES.append(fiche(
 id='euro-hausse-prix', affirmation="Le passage à l'euro a fait exploser les prix.", volet='economie', sous_theme='Inflation',
 mots_cles=['passage a l euro', 'l euro a fait', 'avec l euro', 'depuis l euro', 'euro prix', 'retour au franc', 'arrondis euro', 'inflation percue', 'baguette euro'],
 verdict='contredit', fiabilite='etabli', stabilite='historique',
 resume="L'Insee et la Banque de France estiment l'effet du passage à l'euro, en 2002, à +0,1 à +0,2 % sur les prix, concentré sur janvier 2002 et sur quelques services comme les cafés et restaurants. L'inflation a même été plus faible après l'euro (1,4 % par an de 2002 à 2016) qu'avant (2,1 % de 1986 à 2001). Le sentiment de hausse n'est pourtant pas absurde : les petits achats fréquents ont augmenté, et l'inflation perçue est restée environ deux fois supérieure à l'inflation mesurée.",
 contexte="Plus de vingt ans après, l'idée que l'euro aurait fait flamber les prix reste répandue et nourrit les appels à revenir au franc.",
 explication="L'indice des prix mesure l'évolution du prix d'un panier moyen de biens et services. Les arrondis à la conversion ont touché des produits achetés souvent (café, pain), ce qui marque la mémoire, alors que d'autres prix (biens durables) ont baissé.",
 sources=[INSEE_EURO17, INSEE_EURO02, BDF_EURO],
 faits=[
  fait("Selon l'Insee, le passage à l'euro a eu « un impact modéré », « de l'ordre de + 0,1 % à + 0,2 % sur les prix ».", 'insee_euro17', '2002', 'France', "L'effet global est très faible.", 'etabli', '+0,1 à +0,2 %'),
  fait("Selon l'Insee, l'inflation a été de 1,4 % par an en moyenne de 2002 à 2016, contre 2,1 % de 1986 à 2001.", 'insee_euro17', '1986-2016', 'France', "Les prix ont augmenté moins vite après l'euro qu'avant.", 'etabli', '1,4 %'),
  fait("Selon l'Insee (2002), l'effet est concentré sur janvier 2002 et sur les services : les cafés-restaurants représentent près de la moitié de l'effet de ce mois.", 'insee_euro02', '2002', 'France', "Les hausses ont touché des achats très visibles.", 'etabli'),
  fait("Selon la Banque de France, le café en salle a augmenté de 6 % entre août 2001 et avril 2002, et l'inflation perçue en France atteignait environ le double de l'indice de l'Insee.", 'bdf_euro', '2001-2007', 'France', "Le ressenti s'explique par les petits achats fréquents.", 'etabli', '6 %'),
  fait("Selon la Banque de France, de 1996 à 2006, 40 % des ménages ont connu une inflation supérieure à l'indice moyen.", 'bdf_euro', '1996-2006', 'France', "L'indice moyen ne reflète pas la situation de chaque ménage.", 'estimation', '40 %'),
 ],
 court="Faux : selon l'Insee, le passage à l'euro a augmenté les prix de 0,1 à 0,2 % seulement, et l'inflation a été plus faible après 2002 qu'avant. Les hausses ont surtout touché des achats très visibles, comme le café.",
 moyen="L'Insee a mesuré l'effet du passage à l'euro : entre +0,1 et +0,2 % sur les prix, surtout en janvier 2002. L'inflation a même été plus basse après l'euro (1,4 % par an) qu'avant (2,1 %).\n\nMais le ressenti s'explique : les arrondis ont touché des produits achetés tous les jours, comme le café (+6 % en quelques mois) ou la baguette. C'est pourquoi l'inflation perçue est restée bien supérieure à l'inflation mesurée.",
 detaille="Dès 2002, l'Insee a estimé l'effet du passage à l'euro à environ +0,1 point sur l'inflation de janvier, puis presque rien en février et mars. Les services ont augmenté davantage (restauration, cafés, loisirs, réparation automobile), alors que les prix des biens durables ont baissé. En 2017, l'Insee confirme un effet « de l'ordre de + 0,1 % à + 0,2 % » et note que l'inflation a été plus faible de 2002 à 2016 (1,4 % par an) que de 1986 à 2001 (2,1 %).\n\nLa Banque de France arrive au même ordre de grandeur (environ 0,2 %). Elle explique l'écart avec le ressenti : le café en salle a pris 6 % entre août 2001 et avril 2002, et l'inflation perçue est restée environ le double de l'inflation mesurée, plus longtemps en France qu'en Allemagne. Elle souligne aussi que 40 % des ménages ont connu une inflation supérieure à l'indice moyen.\n\nLe malaise sur les prix est donc réel, mais l'euro n'en est pas la cause. La question du pouvoir d'achat passe par les salaires et le partage de la valeur, pas par le retour au franc.",
 empathie="Je comprends qu'on ait l'impression que tout a augmenté avec l'euro : le café ou la baguette ont pris des centimes qu'on a remarqués. Mais l'Insee a mesuré l'effet réel : quelques dixièmes de pour cent, et une inflation plus faible après 2002 qu'avant.",
 legitimes=["Des prix de petits achats fréquents (café, restauration, pain) ont réellement augmenté au moment de la conversion.", "Une partie importante des ménages a connu une inflation supérieure à l'indice moyen."],
 contre=[
  ("Avant, une baguette coûtait 4 francs.", "Les prix montent avec le temps dans toutes les monnaies ; l'inflation a été plus rapide avant l'euro qu'après selon l'Insee."),
  ("L'Insee sous-estime l'inflation.", "La Banque de France arrive au même résultat ; l'écart avec le ressenti tient au choix des produits que l'on remarque."),
 ],
 questions=["Sais-tu si les prix augmentaient plus vite avant ou après l'euro ?", "Quels achats te font dire que tout a augmenté ?"],
 limites=["Les sources datent de 2002, 2007 et 2017 ; la période d'inflation de 2022-2023 n'est pas couverte.", "Les prix de l'immobilier ne sont pas inclus dans l'indice des prix à la consommation."],
 publics={'convaincus': "L'Insee et la Banque de France ont mesuré : l'euro a fait monter les prix de 0,1 à 0,2 % en 2002, pas plus. Et les prix ont augmenté moins vite après l'euro qu'avant. Le café a pris quelques centimes, c'est vrai, mais ce n'est pas l'euro qui a fait exploser ton budget.",
  'indecis': "Le sentiment de hausse est réel, parce que les arrondis ont touché les achats du quotidien, comme le café. Mais l'effet global de l'euro a été minime, et l'inflation a été plus faible après 2002. Si les fins de mois sont dures, c'est surtout une question de salaires."},
 a_actualiser='2030-12-31',
))

# 15 ── Statistiques sur les immigrés ─────────────────────────────────────────
FICHES.append(fiche(
 id='statistiques-immigres-cachees', affirmation="On n'a pas le droit de compter les immigrés en France, l'État cache les chiffres.", volet='immigration', sous_theme='Immigration et démographie',
 mots_cles=['statistiques ethniques', 'cache les chiffres', 'chiffres caches', 'nombre d immigres', 'chiffres de l immigration', 'compter les immigres'],
 verdict='contredit', fiabilite='etabli',
 resume="Faux : l'Insee publie chaque année le nombre d'immigrés et d'étrangers, avec une série depuis 1921 (7,97 millions d'immigrés en 2025, soit 11,6 % de la population), et compte aussi les descendants d'immigrés (8,0 millions en 2024). Ce qui est interdit depuis une décision du Conseil constitutionnel de 2007, ce sont les catégories « ethno-raciales » et les variables de race ou de religion dans les fichiers administratifs, pas le comptage des immigrés.",
 contexte="L'idée que l'État cacherait l'ampleur de l'immigration est très répandue ; elle se mêle au débat sur les « statistiques ethniques ».",
 explication="Un immigré est une personne née étrangère à l'étranger et résidant en France ; un étranger est une personne qui n'a pas la nationalité française. Ces deux catégories, et les descendants d'immigrés, sont mesurées à partir du pays de naissance et de la nationalité, qui sont collectés par le recensement.",
 sources=[INSEE_IMMI, INSEE_DESC, INSEE_ETHN, PLEINDROIT_2007],
 faits=[
  fait("Selon l'Insee, la France compte en 2025 (données provisoires) 7 970 000 immigrés, soit 11,6 % de la population, et 6 297 000 étrangers, soit 9,1 %.", 'insee_immi', '2025', 'France', "Les chiffres sont publiés chaque année.", 'etabli', '11,6 %'),
  fait("L'Insee dénombre aussi 8,0 millions de descendants d'immigrés en 2024, soit 12 % de la population vivant en logement ordinaire.", 'insee_desc', '2024', 'France', "Même la « deuxième génération » est comptée.", 'etabli', '8,0 millions'),
  fait("Selon l'Insee, la décision du Conseil constitutionnel du 15 novembre 2007 interdit un référentiel ethno-racial et les variables de race ou de religion dans les fichiers administratifs, mais autorise les études sur la diversité, les discriminations et l'intégration fondées sur des données objectives.", 'insee_ethn', '2007-2020', 'France', "L'interdiction vise la race et l'ethnie, pas l'origine migratoire.", 'etabli'),
  fait("Selon une juriste, les traitements nécessaires aux études sur la diversité des origines « peuvent porter sur des données objectives » mais « ne sauraient [...] reposer sur l'origine ethnique ou la race ».", 'pleindroit_2007', '2007', 'France', "La frontière est claire en droit.", 'etabli'),
  fait("L'enquête Trajectoires et Origines (2009, puis 2019-2020) a été menée par l'Ined et l'Insee avec l'accord de la CNIL.", 'insee_ethn', '2019-2020', 'France', "Il existe de grandes enquêtes publiques sur les origines.", 'etabli'),
 ],
 court="Faux : l'Insee publie chaque année le nombre d'immigrés (7,97 millions en 2025, 11,6 % de la population) et compte aussi les descendants d'immigrés. Seules les catégories « ethno-raciales » sont interdites.",
 moyen="L'Insee publie chaque année le nombre d'immigrés et d'étrangers, avec une série qui remonte à 1921 : 7,97 millions d'immigrés en 2025, soit 11,6 % de la population. Il compte aussi les enfants d'immigrés : 8 millions en 2024.\n\nCe qui est interdit depuis 2007, ce sont les statistiques par « race » ou « ethnie » dans les fichiers administratifs. Mais les chercheurs peuvent étudier les origines à partir du pays de naissance, comme le fait la grande enquête Trajectoires et Origines.",
 detaille="Le recensement collecte le pays de naissance et la nationalité de chaque habitant. C'est ce qui permet à l'Insee de publier une série annuelle sur les immigrés et les étrangers depuis 1921 : en 2025, 7 970 000 immigrés (11,6 % de la population) et 6 297 000 étrangers (9,1 %), contre 6 028 000 immigrés en 2014. Les descendants d'immigrés sont aussi mesurés : 8,0 millions en 2024.\n\nLe débat sur les « statistiques ethniques » porte sur autre chose. Le 15 novembre 2007, le Conseil constitutionnel a censuré une disposition qui aurait permis des études fondées sur l'origine ethnique ou la race. Il a précisé que les études sur la diversité, les discriminations et l'intégration restent possibles à partir de données objectives (pays de naissance, nationalité antérieure, nom) et du ressenti d'appartenance.\n\nL'enquête Trajectoires et Origines, réalisée par l'Ined et l'Insee avec l'accord de la CNIL, mesure ainsi les parcours et les discriminations des immigrés et de leurs descendants. Les chiffres existent, ils sont publics et réguliers : chacun peut les consulter.",
 empathie="Je comprends qu'on se méfie quand on a l'impression qu'on nous cache des choses sur un sujet aussi sensible. Mais les chiffres sont publics : l'Insee publie chaque année le nombre d'immigrés et même celui de leurs enfants.",
 legitimes=["Il n'existe pas de statistique officielle par origine ethnique, par race ou par religion dans les fichiers administratifs.", "Les chiffres de 2024 et 2025 sont provisoires."],
 contre=[
  ("On ne compte pas les petits-enfants d'immigrés.", "Les sources lues ne donnent pas de chiffre sur la troisième génération ; c'est une limite réelle de la statistique."),
  ("Les clandestins ne sont pas comptés.", "Les sources lues n'indiquent pas comment les personnes sans titre de séjour sont comptées ; c'est une question légitime, mais pas la preuve d'un secret."),
 ],
 questions=["Sais-tu que l'Insee publie chaque année le nombre d'immigrés depuis 1921 ?", "Quelle information te manque vraiment pour te faire une idée ?"],
 limites=["Les chiffres de 2024-2025 sont provisoires.", "Le texte de la décision 2007-557 DC n'a pas été lu directement ; son contenu est connu par l'Insee et une analyse juridique.", "La manière dont le recensement compte les personnes sans titre de séjour n'a pas été vérifiée."],
 publics={'convaincus': "Les chiffres sont sur le site de l'Insee : 7,97 millions d'immigrés en 2025, 11,6 % de la population, et même 8 millions de descendants d'immigrés. Personne ne les cache. Ce qui est interdit, c'est de classer les gens par race, et c'est une protection pour tout le monde.",
  'indecis': "Tu peux vérifier toi-même : l'Insee publie chaque année le nombre d'immigrés et d'étrangers, avec une série depuis 1921. Ce que la loi interdit, ce sont les fichiers classant les gens par race ou religion. Les chercheurs étudient quand même les origines grâce au pays de naissance."},
 a_actualiser='2027-06-30',
))

# 16 ── Enfants d'immigrés et sentiment d'être français ───────────────────────
FICHES.append(fiche(
 id='enfants-immigres-sentiment-francais', affirmation="Les enfants d'immigrés ne se sentent pas français.", volet='immigration', sous_theme='Intégration',
 mots_cles=['enfants d immigres', 'descendants d immigres', 'deuxieme generation', 'se sentent pas francais', 'se sentir francais', 'sentiment d etre francais', 'rejettent la france', 'trajectoires et origines'],
 verdict='contredit', fiabilite='etabli',
 resume="Selon l'enquête Trajectoires et Origines (Ined-Insee, 2019-2020), 94 % des descendants de deux parents immigrés et 98 % des enfants de couples mixtes se sentent français, contre 97 % des personnes sans ascendance migratoire, et 95 % des descendants d'immigrés se sentent « chez eux » en France. Le problème mis en évidence est l'inverse : 20 % d'entre eux ne se sentent pas vus comme français, jusqu'à 35-39 % pour les origines d'Afrique subsaharienne, et les discriminations déclarées persistent à la deuxième génération.",
 contexte="L'idée d'une deuxième génération qui rejetterait la France est récurrente après des émeutes, des matchs de football ou des débats sur l'islam.",
 explication="Un descendant d'immigré est une personne née en France d'au moins un parent immigré. L'enquête Trajectoires et Origines, réalisée auprès de plus de 27 000 personnes, mesure à la fois le sentiment d'appartenance et le regard que les autres portent sur elles.",
 sources=[INED_TEO, INSEE_TEO_SENT, INSEE_TEO_DISCRI],
 faits=[
  fait("Selon l'Ined, 94 % des descendants de deux parents immigrés et 98 % des descendants d'un couple mixte se sentent français, contre 97 % de la population sans ascendance migratoire et 71 % des immigrés eux-mêmes.", 'ined_teo', '2019-2020', 'France métropolitaine, 18-59 ans', "La quasi-totalité des enfants d'immigrés se sentent français.", 'etabli', '94 %'),
  fait("Selon l'Insee, 95 % des descendants d'immigrés se disent d'accord avec la phrase « Je me sens chez moi en France », contre 93 % des personnes sans ascendance migratoire.", 'insee_teo_sent', '2019-2020', 'France métropolitaine, 18-59 ans', "Ils se sentent autant chez eux que les autres.", 'etabli', '95 %'),
  fait("Selon l'Insee, 20 % des descendants d'immigrés ne se sentent pas vus comme français ; c'est le cas de 29 à 30 % des descendants d'origine maghrébine et de 35 à 39 % de ceux d'Afrique sahélienne, guinéenne ou centrale.", 'insee_teo_sent', '2019-2020', 'France métropolitaine, 18-59 ans', "Le problème est le regard des autres, pas leur attachement.", 'etabli', '20 %'),
  fait("Selon l'Insee et l'Ined, 34 % des descendants d'immigrés d'origine non européenne déclarent avoir subi des discriminations sur cinq ans, et 29 % un « déni de la qualité de Français ».", 'insee_teo_discri', '2019-2020', 'France métropolitaine', "Les discriminations persistent à la deuxième génération.", 'etabli', '34 %'),
 ],
 court="Faux : 94 % des enfants de deux parents immigrés se sentent français, presque autant que le reste de la population (97 %), selon l'enquête Trajectoires et Origines. Le problème, c'est que 20 % ne se sentent pas vus comme français.",
 moyen="La grande enquête publique Trajectoires et Origines (Ined-Insee) a posé la question : 94 % des enfants de deux parents immigrés se sentent français, contre 97 % des personnes sans origine migratoire. Et 95 % se sentent « chez eux » en France.\n\nLe vrai problème est dans l'autre sens : 20 % d'entre eux ont l'impression qu'on ne les voit pas comme français, jusqu'à plus d'un tiers pour les origines africaines. Et un tiers des descendants d'origine non européenne déclarent avoir subi des discriminations.",
 detaille="L'enquête Trajectoires et Origines 2, menée par l'Ined et l'Insee en 2019-2020 auprès de plus de 27 000 personnes de 18 à 59 ans, permet de répondre précisément. 94 % des descendants de deux parents immigrés et 98 % des descendants de couples mixtes se sentent français, contre 97 % des personnes sans ascendance migratoire. Chez les immigrés eux-mêmes, nés à l'étranger, la proportion est de 71 %. Par ailleurs, 95 % des descendants d'immigrés se sentent chez eux en France, un peu plus que la population majoritaire (93 %).\n\nCe que l'enquête révèle, c'est un décalage entre ce que ces personnes ressentent et le regard des autres : 20 % ne se sentent pas vus comme français, 29 à 30 % chez les descendants d'origine maghrébine et 35 à 39 % chez ceux d'Afrique sahélienne, guinéenne ou centrale. 34 % des descendants d'origine non européenne déclarent des discriminations sur cinq ans, et 29 % disent qu'on leur a nié leur qualité de Français.\n\nAutrement dit, l'immense majorité des enfants d'immigrés se sentent français ; c'est une partie de la société qui leur refuse cette identité. Répéter qu'ils « ne se sentent pas français » alimente précisément ce rejet.",
 empathie="Je comprends que certaines images, des drapeaux étrangers après un match par exemple, donnent cette impression. Mais quand on pose la question à des dizaines de milliers de personnes, 94 % des enfants d'immigrés répondent qu'ils se sentent français.",
 legitimes=["Les immigrés eux-mêmes (nés à l'étranger) sont moins nombreux à se sentir français (71 %).", "Les données datent de 2019-2020 et portent sur les 18-59 ans de métropole."],
 contre=[
  ("Ils répondent ce qu'on attend d'eux.", "Les mêmes personnes déclarent aussi des discriminations et un sentiment de rejet : elles ne disent pas seulement ce qui plaît."),
  ("Et ceux qui sifflent la Marseillaise ?", "Ils existent, mais ils ne représentent pas les 94 % qui se disent français dans une enquête de grande ampleur."),
 ],
 questions=["Sais-tu combien d'enfants d'immigrés se disent français dans les enquêtes publiques ?", "Comment te sentirais-tu si on te répétait que tu n'es pas vraiment d'ici ?"],
 limites=["Le chiffre de 94 % vient du dossier de presse de l'Ined (copie hébergée par un tiers) ; les pages de l'Ined n'ont pas pu être lues directement.", "Les données datent de 2019-2020 et ne couvrent ni les outre-mer ni les plus de 59 ans."],
 publics={'convaincus': "Une enquête publique auprès de 27 000 personnes a posé la question : 94 % des enfants d'immigrés se sentent français, presque autant que les autres. Ce qui les blesse, c'est qu'un sur cinq a l'impression qu'on ne les voit pas comme français. Leur répéter qu'ils ne le sont pas, c'est créer le problème qu'on dénonce.",
  'indecis': "C'est une question légitime, et les chiffres sont rassurants : l'immense majorité des enfants d'immigrés se sentent français et chez eux en France. En revanche, beaucoup se sentent rejetés ou discriminés, surtout ceux d'origine africaine. L'intégration se joue aussi dans le regard des autres."},
 a_actualiser='2028-06-30',
))

# 17 ── Insectes et Union européenne ──────────────────────────────────────────
FICHES.append(fiche(
 id='insectes-union-europeenne', affirmation="L'Union européenne veut nous faire manger des insectes.", volet='politique', sous_theme='Désinformation',
 mots_cles=['insectes', 'manger des insectes', 'farine d insectes', 'poudre de grillon', 'grillons', 'vers de farine', 'nouvel aliment', 'novel food'],
 verdict='trompeur', fiabilite='etabli',
 resume="L'Union européenne a autorisé depuis 2021 la vente de quelques insectes comme « nouvel aliment » (ver de farine, criquet, grillon, petit ténébrion), mais ces autorisations n'obligent personne à en manger ni à en mettre dans les produits. L'étiquette doit indiquer le nom de l'insecte et le risque d'allergie : « c'est aux consommateurs de décider », selon la Commission. Elle présente pourtant bien les insectes comme une source de protéines plus durable.",
 contexte="Depuis 2023, des publications affirment que de la poudre d'insectes serait cachée dans le pain ou les pâtes sur ordre de Bruxelles ; elles ont été démenties, notamment par l'AFP.",
 explication="Tout aliment nouveau dans l'Union doit être autorisé après une évaluation de sécurité par l'EFSA. Une autorisation permet à une entreprise de vendre un produit ; elle n'impose rien aux autres producteurs ni aux consommateurs.",
 sources=[EU_2023_58, CE_INSECTES, AFP_INSECTES, ALVA_INSECTES],
 faits=[
  fait("Selon l'administration alimentaire luxembourgeoise, plusieurs règlements autorisent depuis 2021 le ver de farine jaune, le criquet migrateur, le grillon domestique et le petit ténébrion comme denrées alimentaires.", 'alva_insectes', '2021-2025', 'Union européenne', "Il s'agit d'autorisations de vente, produit par produit.", 'etabli'),
  fait("Le règlement 2023/58 autorise les larves de petit ténébrion au profit d'une entreprise précise et impose d'indiquer sur l'étiquette le nom de l'insecte et le risque d'allergie pour les personnes allergiques aux crustacés et aux acariens.", 'eu_2023_58', '2023', 'Union européenne', "Impossible d'en manger sans le savoir dans un produit emballé.", 'etabli'),
  fait("Selon l'AFP, ces autorisations « do not make insect ingredients mandatory in any food product » (ne rendent les ingrédients à base d'insectes obligatoires dans aucun produit).", 'afp_insectes', '2023', 'Union européenne', "Aucune obligation n'existe.", 'etabli'),
  fait("Selon la Commission, « c'est aux consommateurs de décider s'ils veulent ou non manger des insectes » ; elle les présente aussi comme une source de protéines plus durable.", 'ce_insectes', '2021', 'Union européenne', "L'UE encourage cette filière, sans contraindre personne.", 'etabli'),
 ],
 court="Trompeur : l'UE a autorisé la vente de quelques insectes, mais n'oblige personne à en manger ni à en mettre dans les produits. Leur présence doit être indiquée sur l'étiquette, avec un avertissement sur les allergies.",
 moyen="Depuis 2021, l'Union européenne a autorisé quelques insectes comme aliments : ver de farine, criquet, grillon, petit ténébrion. Ce sont des autorisations de vente, après une évaluation de sécurité, comme pour tout nouvel aliment.\n\nPersonne n'est obligé d'en produire ni d'en manger. Les produits emballés doivent indiquer le nom de l'insecte dans la liste des ingrédients, avec un avertissement sur les allergies. La Commission l'écrit : « c'est aux consommateurs de décider ».",
 detaille="Dans l'Union européenne, un aliment nouveau doit être autorisé avant d'être vendu ; l'EFSA a jugé sûrs les insectes autorisés. Depuis 2021, plusieurs règlements ont ainsi autorisé le ver de farine jaune, le criquet migrateur, le grillon domestique (règlements de 2022 et 2023) et le petit ténébrion (2023).\n\nCes textes autorisent une entreprise donnée à commercialiser un produit précis ; ils n'imposent rien. L'AFP rappelle qu'ils ne rendent les insectes obligatoires dans aucun aliment. Ils imposent au contraire un étiquetage : nom de l'insecte dans la liste des ingrédients et mise en garde pour les personnes allergiques aux crustacés et aux acariens.\n\nLa Commission défend bien l'intérêt des insectes comme source de protéines plus durable, et l'on peut débattre de cette orientation. Mais l'idée qu'on nous en ferait manger en cachette ne tient pas : l'étiquetage est obligatoire et le choix reste au consommateur.",
 empathie="Je comprends que l'idée de manger des insectes dégoûte, et qu'on se méfie des décisions prises à Bruxelles. Mais il s'agit seulement d'autoriser certaines entreprises à en vendre : personne n'est obligé d'en manger, et c'est indiqué sur l'étiquette.",
 legitimes=["La Commission promeut les insectes comme source de protéines plus durable.", "Dans la restauration et pour les produits non emballés, l'information n'est pas sur un emballage ; elle doit être disponible auprès du vendeur."],
 contre=[
  ("Ils en mettent en cachette dans le pain.", "Les règlements imposent de l'indiquer dans la liste des ingrédients ; les sources lues ne signalent aucun produit où il serait caché."),
  ("C'est la première étape avant de nous l'imposer.", "Rien dans les textes ne prévoit d'obligation ; c'est une crainte, pas une décision."),
 ],
 questions=["As-tu déjà vu un produit contenant des insectes dans ton supermarché ?", "Qu'est-ce qui te dérange le plus : l'autorisation elle-même ou l'idée qu'on te le cache ?"],
 limites=["Le nombre de produits contenant des insectes en vente en France n'est pas connu des sources lues.", "Le texte intégral en français du règlement 2023/5 n'a pas pu être lu."],
 publics={'convaincus': "Bruxelles a autorisé quelques entreprises à vendre des insectes, elle n'oblige personne à en manger. Et c'est écrit sur l'étiquette, avec un avertissement pour les allergiques. Si tu n'en veux pas, il te suffit de lire la liste des ingrédients.",
  'indecis': "L'Union européenne a autorisé la vente de quelques insectes après des évaluations de sécurité, comme pour tout nouvel aliment. Elle les voit comme une source de protéines d'avenir, ce qu'on peut discuter. Mais rien n'est obligatoire et leur présence doit être indiquée sur les emballages."},
 a_actualiser='2028-06-30',
))

# 18 ── Allocation des demandeurs d'asile ─────────────────────────────────────
FICHES.append(fiche(
 id='demandeurs-asile-allocation-retraites', affirmation="Les demandeurs d'asile touchent plus que nos retraités.", volet='immigration', sous_theme='Immigration et aides sociales',
 mots_cles=['demandeurs d asile touchent', 'allocation pour demandeur d asile', 'ada', 'plus que nos retraites', 'plus que les retraites', 'migrants touchent', 'allocation des migrants', 'carte de paiement ofii'],
 verdict='contredit', fiabilite='etabli',
 resume="Non : l'allocation pour demandeur d'asile (ADA) est de 6,80 € par jour pour une personne seule hébergée, soit environ 204 € par mois, et de 14,20 € par jour sans hébergement, soit environ 426 € par mois. La pension moyenne nette de droit direct était de 1 541 € fin 2023, et le minimum vieillesse de 1 012,02 € par mois au 1er janvier 2024. Les demandeurs d'asile n'ont en outre pas le droit de travailler pendant leurs six premiers mois en France.",
 contexte="Des messages viraux comparent les « migrants » à des retraités pauvres qui toucheraient moins ; la comparaison mélange souvent l'ADA, le RSA et le coût de l'hébergement.",
 explication="L'ADA est versée par l'Ofii, sur une carte de paiement, aux demandeurs d'asile qui acceptent les conditions d'accueil et dont les ressources sont inférieures au RSA, pendant l'examen de leur demande. Elle s'ajoute, le cas échéant, à un hébergement en centre.",
 sources=[SP_ADA, DREES_RETR, CNAV_ASPA, SP_TRAVAIL_ASILE],
 faits=[
  fait("Selon Service-public.fr, l'ADA est de 6,80 € par jour pour une personne seule, majorés de 7,40 € si aucun hébergement n'est proposé, et de 37,40 € par jour pour une famille de dix personnes.", 'sp_ada', '2026', 'France', "Soit environ 204 € par mois pour une personne hébergée et 426 € sans hébergement (calcul sur 30 jours).", 'etabli', '6,80 €'),
  fait("Selon la DREES, la pension moyenne de droit direct s'élève fin 2023 à 1 541 € nets par mois, pour 17,2 millions de retraités.", 'drees_retr', '2023', 'France', "Une retraite moyenne vaut plusieurs fois l'ADA.", 'etabli', '1 541 €'),
  fait("Selon l'Assurance retraite, le minimum vieillesse (Aspa) est de 1 012,02 € par mois pour une personne seule au 1er janvier 2024.", 'cnav_aspa', '2024', 'France', "Même le minimum vieillesse est plus de deux fois supérieur à l'ADA sans hébergement.", 'etabli', '1 012 €'),
  fait("Selon Service-public.fr, un demandeur d'asile ne peut pas obtenir d'autorisation de travail pendant les six premiers mois de sa demande.", 'sp_travail_asile', '2026', 'France', "Les demandeurs d'asile sont contraints de vivre de cette allocation au début.", 'etabli', '6 mois'),
 ],
 court="Faux : l'allocation d'un demandeur d'asile seul est d'environ 204 € par mois s'il est hébergé, 426 € sinon. La retraite moyenne est de 1 541 € nets et le minimum vieillesse de 1 012 € par mois.",
 moyen="Un demandeur d'asile seul touche 6,80 € par jour s'il est hébergé, soit environ 204 € par mois, et 14,20 € par jour sinon, soit environ 426 €. La pension moyenne d'un retraité est de 1 541 € nets, et le minimum vieillesse de 1 012 € par mois.\n\nEn plus, les demandeurs d'asile n'ont pas le droit de travailler pendant leurs six premiers mois. On peut défendre les petites retraites sans opposer les retraités à des gens qui vivent avec quelques euros par jour.",
 detaille="L'allocation pour demandeur d'asile (ADA) est versée par l'Ofii, pendant l'examen de la demande, aux personnes qui acceptent les conditions d'accueil et dont les ressources sont inférieures au RSA. Son montant est de 6,80 € par jour pour une personne seule, 10,20 € pour un couple, jusqu'à 37,40 € pour dix personnes ; il est majoré de 7,40 € par jour pour une personne seule si aucun hébergement n'est proposé. Cela fait environ 204 € par mois pour une personne hébergée et 426 € pour une personne sans hébergement.\n\nEn comparaison, la pension moyenne de droit direct était de 1 666 € bruts, soit 1 541 € nets, fin 2023, et le minimum vieillesse de 1 012,02 € par mois pour une personne seule au 1er janvier 2024.\n\nLes demandeurs d'asile ne peuvent pas obtenir d'autorisation de travail pendant les six premiers mois. Il faut ajouter, pour ceux qui sont hébergés, le logement en centre, qui a un coût pour l'État. Mais aucune comparaison honnête ne permet de dire qu'ils « touchent plus » que les retraités. Beaucoup de retraités ont de petites pensions : c'est un vrai combat, qui se mène contre les réformes qui les fragilisent, pas contre les demandeurs d'asile.",
 empathie="Je comprends la colère des retraités qui ont travaillé toute leur vie et vivent avec peu. Mais un demandeur d'asile seul touche environ 200 à 400 € par mois, et il n'a pas le droit de travailler au début : il ne vit pas mieux qu'un retraité.",
 legitimes=["Les demandeurs d'asile hébergés bénéficient aussi d'un logement et d'un accès aux soins, qui ne figurent pas dans le montant de l'ADA.", "Une famille nombreuse touche davantage, et de nombreux retraités ont une pension inférieure à la moyenne."],
 contre=[
  ("Avec le logement payé, ils ont plus.", "Un hébergement en centre collectif n'est pas un revenu, et l'allocation reste de 6,80 € par jour pour une personne seule."),
  ("Une famille de migrants touche plus de 1 000 €.", "Pour dix personnes, l'ADA est de 37,40 € par jour, soit environ 1 122 € par mois, moins de 4 € par personne et par jour."),
 ],
 questions=["Sais-tu combien touche par jour un demandeur d'asile seul ?", "Qui a vraiment fait baisser le niveau de vie de certains retraités, à ton avis ?"],
 limites=["Le montant du minimum vieillesse en 2026 n'a pas été lu dans une source officielle ; le chiffre cité est celui de 2024.", "Le coût de l'hébergement des demandeurs d'asile n'est pas inclus dans la comparaison."],
 publics={'convaincus': "Un demandeur d'asile seul touche 6,80 € par jour s'il est hébergé, environ 200 € par mois. Le minimum vieillesse, c'est plus de 1 000 €, et la retraite moyenne 1 541 €. Ceux qui t'ont dit le contraire veulent que tu en veuilles aux migrants plutôt qu'à ceux qui décident des pensions.",
  'indecis': "Les petites retraites sont un vrai problème, et c'est normal d'être choqué par les comparaisons qui circulent. Mais les chiffres officiels sont clairs : l'allocation d'un demandeur d'asile seul est de 200 à 400 € par mois, sans droit de travailler au début. Les deux situations sont difficiles, aucune n'est enviable."},
 a_actualiser='2027-06-30',
))

# 19 ── Chiffres du chômage ───────────────────────────────────────────────────
FICHES.append(fiche(
 id='chomage-chiffres-truques', affirmation="Les chiffres du chômage sont truqués : en réalité, il y en aurait six millions.", volet='social', sous_theme='Chômage',
 mots_cles=['chiffres du chomage', 'chomage truque', 'chiffres truques', 'vrai chiffre du chomage', 'categories a b c', 'chomage bit', 'halo du chomage'],
 verdict='trompeur', fiabilite='etabli',
 resume="Les chiffres ne sont pas truqués : deux mesures officielles, publiques, coexistent. Au sens du Bureau international du travail, l'Insee compte 2,7 millions de chômeurs (8,3 %) au deuxième trimestre 2026. France Travail compte 5,85 millions d'inscrits en catégories A, B et C, et 6,59 millions avec les catégories D et E, mais beaucoup travaillent en partie ou ne sont pas disponibles. Le chômage officiel sous-estime pourtant le manque d'emploi : 1,9 million de personnes forment le « halo » autour du chômage.",
 contexte="L'écart entre le taux de chômage de l'Insee et le nombre d'inscrits à France Travail nourrit l'idée d'une manipulation ; l'inscription automatique des allocataires du RSA depuis 2025 a encore brouillé les repères.",
 explication="Un chômeur au sens du BIT est sans emploi pendant une semaine donnée, disponible sous 15 jours et en recherche active. Un inscrit à France Travail peut avoir travaillé dans le mois (catégories B et C) ou ne pas être disponible (D, E). Les deux mesures ne comptent pas les mêmes personnes.",
 sources=[INSEE_CHOM, FT_STMT, FT_DEF, INSEE_APPARIEMENT],
 faits=[
  fait("Selon l'Insee, le taux de chômage au sens du BIT atteint 8,3 % au deuxième trimestre 2026, soit 2 677 000 chômeurs, en hausse de 261 000 sur un an.", 'insee_chom', '2026', 'France', "Le chiffre officiel montre une hausse : il ne masque pas la dégradation.", 'etabli', '8,3 %'),
  fait("Selon l'Insee, environ 1,9 million de personnes forment le « halo autour du chômage » : elles souhaitent travailler sans être comptées comme chômeuses.", 'insee_chom', '2026', 'France', "Le manque d'emploi dépasse le seul chiffre du chômage.", 'etabli', '1,9 million'),
  fait("Selon France Travail et la Dares, au troisième trimestre 2026, 3 353 400 personnes sont inscrites en catégorie A, 5 847 500 en catégories A, B, C et 6 587 600 en catégories A à E.", 'ft_stmt', '2026', 'France hors Mayotte', "Le chiffre de six millions correspond aux inscrits, pas aux chômeurs sans aucun emploi.", 'etabli', '5,85 millions'),
  fait("Selon France Travail, les catégories B et C regroupent des personnes qui ont travaillé dans le mois, moins ou plus de 78 heures.", 'ft_def', '2019', 'France', "Une partie des inscrits a un emploi, souvent précaire.", 'etabli'),
  fait("Selon l'Insee, en 2017, seuls 56 % des inscrits en catégorie A étaient chômeurs au sens du BIT, et 22 % des chômeurs BIT n'étaient pas inscrits à Pôle emploi.", 'insee_appariement', '2017', 'France', "Les deux mesures se recoupent seulement en partie.", 'etabli', '56 %'),
 ],
 court="Trompeur : il y a deux chiffres officiels et publics. 2,7 millions de chômeurs au sens du BIT (Insee, 2026) et 5,85 millions d'inscrits à France Travail en catégories A, B, C, dont beaucoup travaillent en partie.",
 moyen="Il n'y a pas de trucage, mais deux mesures. L'Insee compte 2,7 millions de chômeurs au sens international (8,3 %) : des personnes sans aucun emploi, disponibles et qui cherchent. France Travail compte 5,85 millions d'inscrits en catégories A, B et C, dont beaucoup ont travaillé un peu dans le mois.\n\nLe vrai problème, c'est que le chômage officiel ne dit pas tout : 1,9 million de personnes voudraient travailler sans être comptées, et une partie des inscrits enchaîne les petits boulots.",
 detaille="L'Insee mesure le chômage au sens du Bureau international du travail par une enquête : est chômeur celui qui n'a pas travaillé du tout pendant la semaine de référence, est disponible sous quinze jours et cherche activement. Au deuxième trimestre 2026, cela représente 2,7 millions de personnes, 8,3 % des actifs, en hausse de 261 000 sur un an.\n\nFrance Travail compte, lui, les inscrits : 3,35 millions en catégorie A (sans emploi dans le mois), 5,85 millions en ajoutant les catégories B et C (activité réduite), 6,59 millions avec les catégories D et E (personnes non immédiatement disponibles). Les deux mesures se recoupent mal : en 2017, seuls 56 % des inscrits en catégorie A étaient chômeurs au sens du BIT, et 22 % des chômeurs BIT n'étaient pas inscrits.\n\nAucun des deux chiffres n'est truqué ; ils sont publiés et documentés. Mais le chiffre de l'Insee, strict, ne mesure pas tout le sous-emploi : 1,9 million de personnes sont dans le « halo » du chômage, et les inscrits en catégories B et C n'ont souvent qu'une activité réduite. La loi pour le plein emploi, qui inscrit automatiquement les allocataires du RSA depuis 2025, modifie aussi les séries. Le débat utile porte sur la précarité et le sous-emploi, pas sur une manipulation.",
 empathie="Je comprends le doute quand on entend 2,7 millions d'un côté et six millions de l'autre, surtout quand on connaît autour de soi des gens qui galèrent. Les deux chiffres sont vrais, ils ne comptent pas la même chose : et ensemble, ils montrent que le manque d'emploi est plus large que le seul taux de chômage.",
 legitimes=["Le chômage au sens du BIT, strict, ne mesure pas tout le sous-emploi : le halo représente 1,9 million de personnes.", "Les changements d'inscription (loi pour le plein emploi, sanctions) rendent les séries de France Travail plus difficiles à lire."],
 contre=[
  ("On radie les chômeurs pour faire baisser les chiffres.", "Les radiations jouent sur le nombre d'inscrits, pas sur le chômage mesuré par l'enquête de l'Insee ; leur volume n'a pas été vérifié ici."),
  ("Quelqu'un qui travaille deux heures n'est pas chômeur, c'est absurde.", "C'est la définition internationale ; c'est pourquoi il faut aussi regarder le halo et les catégories B et C."),
 ],
 questions=["Sais-tu quelle différence il y a entre un chômeur au sens de l'Insee et un inscrit à France Travail ?", "Que penses-tu des personnes qui travaillent quelques heures par mois et restent inscrites ?"],
 limites=["Le taux de chômage du troisième trimestre 2026 n'était pas encore publié à la date de la fiche.", "Le volume des radiations de France Travail n'a pas été vérifié dans une source officielle.", "La comparaison entre inscrits et chômeurs BIT date de 2017."],
 publics={'convaincus': "Personne ne cache rien : l'Insee publie 2,7 millions de chômeurs, France Travail 5,85 millions d'inscrits, et les deux chiffres sont sur Internet. La différence, c'est que beaucoup d'inscrits travaillent quelques heures. Si tu veux dénoncer quelque chose, dénonce la précarité : là, tu as raison.",
  'indecis': "Les deux chiffres sont vrais : 2,7 millions de personnes sans aucun emploi selon la définition internationale, près de 6 millions d'inscrits à France Travail, dont beaucoup en emploi précaire. Le taux officiel ne mesure pas tout : 1,9 million de personnes voudraient travailler sans être comptées. C'est la précarité qu'il faut regarder."},
 a_actualiser='2027-03-31', raison="Nouvelles données trimestrielles de l'Insee et de France Travail.",
))

# 20 ── Écologie et classes populaires ────────────────────────────────────────
FICHES.append(fiche(
 id='ecologie-bobos-classes-populaires', affirmation="L'écologie, c'est un truc de bobos qui punit les classes populaires.", volet='ecologie', sous_theme='Justice climatique',
 mots_cles=['ecologie punitive', 'bobos', 'ecolos bobos', 'truc de bobos', 'punit les pauvres', 'taxe carbone', 'gilets jaunes', 'ecologie des riches', 'empreinte carbone des riches'],
 verdict='trompeur', fiabilite='interpretation',
 resume="En partie seulement : une taxe carbone sans redistribution pèse proportionnellement plus sur les ménages modestes et ruraux, comme l'a montré la crise des Gilets jaunes. Mais les ménages les plus riches émettent beaucoup plus (environ 40 tonnes de CO2 par an pour les 10 % les plus riches contre 15 pour les 10 % les plus pauvres, données de 2011), et les ménages modestes sont souvent plus exposés à la chaleur, tout en étant moins bien protégés. Une écologie qui redistribue peut faire gagner la majorité des ménages modestes.",
 contexte="L'expression « écologie punitive » est utilisée par le RN et une partie de la droite contre les ZFE, la taxe carbone ou les normes ; elle s'appuie sur le souvenir des Gilets jaunes.",
 explication="Une taxe sur l'énergie est dite « régressive » quand elle pèse plus lourd, en proportion du revenu, sur les ménages modestes. Elle peut être compensée si les recettes sont reversées en priorité à ces ménages. Par ailleurs, les émissions de gaz à effet de serre augmentent avec le niveau de vie.",
 sources=[CAE_CARBONE, INSEE_TAXECARB, OI_CO2, INSEE_CHALEUR],
 faits=[
  fait("Selon le Conseil d'analyse économique, la hausse de la taxe carbone étudiée était « régressive » : près de 1 % du revenu disponible pour les 10 % les plus pauvres, contre 0,3 % pour les 10 % les plus riches ; le mouvement des Gilets jaunes est parti de ce relèvement.", 'cae_carbone', '2019', 'France', "La critique d'une écologie qui pèse sur les modestes est fondée quand les mesures ne sont pas compensées.", 'etabli', '1 %'),
  fait("Selon l'Insee, les 20 % de ménages les plus modestes consacrent 11,3 % de leurs dépenses à l'énergie, contre 9,2 % pour les 20 % les plus aisés ; les ménages ruraux dépensent 2,7 fois plus en énergies fossiles que ceux du centre de Paris.", 'insee_taxecarb', '2026', 'France', "Les modestes et les ruraux sont plus exposés au prix de l'énergie.", 'etabli', '11,3 %'),
  fait("Selon l'Observatoire des inégalités, d'après l'OFCE, les 10 % de ménages les plus riches émettent environ 40 tonnes d'équivalent CO2 par an, contre 15,2 tonnes pour les 10 % les plus pauvres (données de 2011).", 'oi_co2', '2011', 'France', "Ce sont les plus aisés qui polluent le plus.", 'estimation', '40 t'),
  fait("Selon l'Insee et la Banque de France, dans plusieurs grandes villes, plus le niveau de vie est faible, plus l'exposition à la chaleur est forte, et 4 % des 10 % les plus modestes ont une climatisation, contre 11 % des plus aisés.", 'insee_chaleur', '2017', 'Grandes villes françaises', "Les classes populaires subissent davantage le réchauffement.", 'etabli', '4 %'),
  fait("Selon le CAE, en redistribuant l'intégralité des recettes de la taxe carbone, plus de 90 % des ménages des cinq ou six premiers déciles y gagneraient.", 'cae_carbone', '2019', 'France', "Une écologie juste est possible.", 'estimation', '90 %'),
 ],
 court="En partie seulement : une taxe carbone non compensée pèse plus sur les modestes, comme l'a montré la crise des Gilets jaunes. Mais les plus riches polluent bien plus, les modestes subissent davantage la chaleur, et une écologie qui redistribue peut leur faire gagner de l'argent.",
 moyen="Il y a du vrai : la taxe carbone de 2018 pesait près de 1 % du revenu des plus pauvres contre 0,3 % pour les plus riches, et elle a déclenché la crise des Gilets jaunes. Les ménages ruraux, qui dépendent de la voiture, sont les plus touchés.\n\nMais l'écologie ne concerne pas que les bobos : les 10 % les plus riches émettent environ 40 tonnes de CO2 par an, contre 15 pour les plus pauvres, et ce sont les ménages modestes qui souffrent le plus de la chaleur. Le problème, ce n'est pas l'écologie, c'est une écologie qui ne fait pas payer les plus gros pollueurs.",
 detaille="La critique a un fondement. Le Conseil d'analyse économique a montré que la hausse de la taxe carbone prévue en 2018-2019 était régressive : elle représentait près de 1 % du revenu disponible des 10 % les plus pauvres, contre 0,3 % pour les 10 % les plus riches, et pénalisait les ruraux et les ménages roulant au diesel. C'est ce relèvement qui a déclenché le mouvement des Gilets jaunes. L'Insee confirme que les ménages modestes consacrent une part plus grande de leurs dépenses à l'énergie, et que les ruraux dépensent 2,7 fois plus en énergies fossiles que les habitants du centre de Paris.\n\nMais les classes populaires ne sont pas les responsables de la crise climatique : d'après l'OFCE, les 10 % les plus riches émettent environ 40 tonnes d'équivalent CO2 par ménage et par an, contre 15 tonnes pour les 10 % les plus pauvres (données de 2011). Et elles en sont souvent les premières victimes : dans plusieurs grandes villes, l'exposition à la chaleur augmente quand le niveau de vie baisse, et les plus modestes sont moins équipés pour s'en protéger.\n\nLe CAE montre qu'en redistribuant toutes les recettes, la grande majorité des ménages modestes serait gagnante. L'enjeu est donc de faire une écologie qui protège les classes populaires et fait contribuer les plus gros émetteurs, pas de renoncer à l'écologie.",
 empathie="Je comprends le ras-le-bol quand on habite à la campagne, qu'on n'a pas d'autre choix que la voiture et qu'on voit le prix du carburant grimper. Tu as raison sur un point : une écologie qui taxe sans compenser frappe d'abord les modestes. Mais ce sont aussi eux qui souffrent le plus des canicules.",
 legitimes=["Une fiscalité carbone sans redistribution est régressive et pénalise les ruraux.", "Les ménages modestes ont moins de moyens pour changer de voiture, de chauffage ou isoler leur logement."],
 contre=[
  ("Les écolos vivent en ville et ne savent pas ce qu'est la campagne.", "Les études citées montrent justement que les ruraux sont plus touchés : c'est un argument pour des mesures compensées, pas contre l'écologie."),
  ("Les riches polluent plus, mais ils sont moins nombreux.", "Les écarts sont de un à près de trois par ménage ; faire contribuer les plus gros émetteurs est donc à la fois juste et efficace."),
 ],
 questions=["Sais-tu qui émet le plus de CO2 en France, selon le niveau de vie ?", "Une taxe carbone dont l'argent serait reversé aux ménages modestes te paraîtrait-elle juste ?"],
 limites=["Les émissions par niveau de vie datent de 2011 ; aucune donnée plus récente n'a été lue.", "L'exposition à la chaleur et à la pollution varie selon les villes : à Paris, les ménages les plus aisés sont plus exposés à la chaleur que les ménages médians."],
 publics={'convaincus': "Tu as raison : la taxe carbone de 2018 pesait plus lourd sur les pauvres, et c'est pour ça que les Gilets jaunes se sont levés. Mais les plus riches émettent près de trois fois plus de CO2, et ce sont les quartiers populaires qui étouffent pendant les canicules. Le problème, c'est qui paie, pas l'écologie.",
  'indecis': "La crainte d'une écologie qui fait payer les modestes est fondée : une taxe carbone sans compensation pèse plus sur eux. Mais les classes populaires sont aussi les premières victimes du réchauffement. Une écologie juste, qui redistribue et fait contribuer les plus gros pollueurs, peut leur être favorable."},
 a_actualiser='2027-12-31',
))

# 21 ── Fonctionnaires et salaires ────────────────────────────────────────────
FICHES.append(fiche(
 id='fonctionnaires-salaires-prive', affirmation="Les fonctionnaires sont mieux payés que les salariés du privé.", volet='services', sous_theme='Fonction publique',
 mots_cles=['fonctionnaires mieux payes', 'salaire des fonctionnaires', 'fonctionnaires gagnent plus', 'salaire public prive', 'fonctionnaires privilegies', 'paie des fonctionnaires', 'salaires fonction publique'],
 verdict='trompeur', fiabilite='etabli',
 resume="En moyenne, les salaires sont presque identiques : en 2024, 2 742 € nets par mois en équivalent temps plein dans la fonction publique, contre 2 733 € dans le privé. Mais la fonction publique emploie beaucoup plus de diplômés : à volume de travail égal, son salaire moyen est inférieur de 3,7 % à celui du privé (données 2021). Et les écarts internes sont énormes : 2 317 € dans la territoriale, 2 623 € pour les soignants hospitaliers, 3 018 € dans la fonction publique de l'État.",
 contexte="L'idée de fonctionnaires privilégiés revient à chaque débat budgétaire, avec les propositions de supprimer des postes ou de geler le point d'indice.",
 explication="Comparer deux moyennes ne suffit pas : si un secteur emploie plus de cadres et de diplômés, sa moyenne est mécaniquement plus haute. L'Insee compare donc aussi les salaires à structure de diplômes et à volume de travail comparables.",
 sources=[INSEE_FP21, INSEE_PRIVE24, INSEE_FPE24, INSEE_FPT24, INSEE_FPH24],
 faits=[
  fait("Selon l'Insee, un salarié du privé gagne en moyenne 2 733 € nets par mois en équivalent temps plein en 2024 ; la moyenne de la fonction publique est de 2 742 €.", 'insee_prive24', '2024', 'France', "Les moyennes sont presque identiques.", 'etabli', '2 733 €'),
  fait("Selon l'Insee, à volume annuel de travail égal, le salaire net moyen de la fonction publique est inférieur de 3,7 % à celui du privé en 2021 (29 450 € contre 30 600 € par an), l'écart tenant notamment à la structure des diplômes.", 'insee_fp21', '2021', 'France', "À diplômes équivalents, la fonction publique paie plutôt moins.", 'etabli', '−3,7 %'),
  fait("Selon l'Insee, un agent territorial gagne en moyenne 2 317 € nets par mois en équivalent temps plein, et 72 % des fonctionnaires territoriaux sont en catégorie C.", 'insee_fpt24', '2024', 'France', "La majorité des agents des collectivités est nettement sous la moyenne du privé.", 'etabli', '2 317 €'),
  fait("Selon l'Insee et la DREES, les personnels des services de soins de la fonction publique hospitalière (infirmiers, aides-soignants, agents de service) gagnent en moyenne 2 623 € nets par mois.", 'insee_fph24', '2024', 'France', "Les soignants ne sont pas des privilégiés.", 'etabli', '2 623 €'),
  fait("Selon l'Insee, le revenu salarial annuel moyen est supérieur de 9,3 % dans le public en 2021, parce que le volume de travail y est plus élevé de 13,5 %.", 'insee_fp21', '2021', 'France', "Sur l'année, un agent public touche en moyenne plus, parce qu'il travaille plus souvent toute l'année.", 'etabli', '+9,3 %'),
  fait("Selon l'Insee, la fonction publique de l'État paie 3 018 € nets par mois en moyenne en 2024, avec 48 % d'agents de catégorie A.", 'insee_fpe24', '2024', 'France', "Les fonctionnaires d'État gagnent en moyenne plus, parce qu'ils sont plus qualifiés.", 'etabli', '3 018 €'),
 ],
 court="Trompeur : en moyenne, salaires publics (2 742 €) et privés (2 733 €) sont presque égaux en 2024. À diplôme et temps de travail comparables, le public paie 3,7 % de moins (2021), et les agents territoriaux gagnent 2 317 € en moyenne.",
 moyen="En 2024, un salarié du privé gagne en moyenne 2 733 € nets par mois en équivalent temps plein, un agent public 2 742 € : c'est presque pareil. Mais la fonction publique compte beaucoup plus de diplômés, comme les enseignants. À volume de travail égal, l'Insee trouve même un salaire public inférieur de 3,7 %.\n\nEt il y a fonctionnaire et fonctionnaire : un agent territorial gagne 2 317 € en moyenne, un soignant hospitalier 2 623 €. L'avantage réel du public, c'est la stabilité de l'emploi, pas la paie.",
 detaille="Selon l'Insee, en 2024, le salaire net moyen en équivalent temps plein est de 2 733 € par mois dans le secteur privé et de 2 742 € dans l'ensemble de la fonction publique. Mais la moyenne cache des réalités très différentes : 3 018 € dans la fonction publique de l'État, où 48 % des agents sont de catégorie A (dont les enseignants, à 3 188 €), 2 317 € dans la territoriale, où 72 % des fonctionnaires sont en catégorie C, et 2 623 € pour les personnels soignants des hôpitaux.\n\nPour comparer à situation égale, l'Insee tient compte du volume de travail et de la structure des diplômes. En 2021, à volume annuel de travail égal, le salaire net moyen du public était inférieur de 3,7 % à celui du privé. En revanche, le revenu salarial annuel moyen était supérieur de 9,3 % dans le public, parce que leur volume de travail annuel est plus élevé (+13,5 %).\n\nLes fonctionnaires ne sont donc pas « mieux payés » à qualification égale : ce qui les distingue, c'est surtout la stabilité de l'emploi. C'est un argument pour améliorer les conditions de travail dans le privé, pas pour baisser les salaires des infirmières ou des agents municipaux.",
 empathie="Je comprends que la sécurité de l'emploi des fonctionnaires puisse paraître injuste quand on est soi-même précaire. Mais sur les salaires, les chiffres de l'Insee sont clairs : à diplôme égal, le public ne paie pas mieux, et les agents des mairies ou des hôpitaux gagnent souvent moins que la moyenne du privé.",
 legitimes=["Le revenu salarial annuel moyen est plus élevé dans le public, grâce à un volume de travail annuel plus élevé.", "Les agents de la fonction publique de l'État gagnent en moyenne plus que la moyenne du privé, en raison de leur niveau de qualification."],
 contre=[
  ("Les fonctionnaires ont la sécurité de l'emploi en plus.", "C'est un avantage réel, que les sources lues ne chiffrent pas ; mais il ne se traduit pas par des salaires plus élevés à diplôme égal."),
  ("Les hauts fonctionnaires gagnent des fortunes.", "Ils existent, mais la majorité des agents territoriaux sont en catégorie C, à 2 317 € de moyenne."),
 ],
 questions=["Sais-tu combien gagne en moyenne un agent de mairie, par rapport à un salarié du privé ?", "À ton avis, pourquoi les hôpitaux ont-ils du mal à recruter des infirmières ?"],
 limites=["La comparaison à volume de travail égal date de 2021.", "Les pensions de retraite et la sécurité de l'emploi ne sont pas prises en compte dans la comparaison."],
 publics={'convaincus': "Les chiffres de l'Insee sont clairs : 2 742 € en moyenne dans le public, 2 733 € dans le privé, c'est presque pareil, alors que le public emploie bien plus de diplômés. À travail égal, le public paie même un peu moins. L'aide-soignante ou l'agent de mairie ne sont pas des privilégiés.",
  'indecis': "La sécurité de l'emploi est un vrai avantage du public, c'est compréhensible que ça fasse envie. Mais côté salaire, la moyenne est la même que dans le privé, et à diplôme égal, le public paie un peu moins. Les agents territoriaux et les soignants gagnent souvent moins que la moyenne."},
 a_actualiser='2027-06-30',
))

# 22 ── Grèves ────────────────────────────────────────────────────────────────
FICHES.append(fiche(
 id='france-championne-greves', affirmation="La France est le pays qui a le plus de jours de grève.", volet='droits', sous_theme='Droits des travailleurs',
 mots_cles=['jours de greve', 'championne de la greve', 'champions de la greve', 'toujours en greve', 'greves en france', 'conflictualite'],
 verdict='plutot_exact', fiabilite='estimation',
 resume="Plutôt exact, avec des nuances : la France fait partie des pays européens qui font le plus grève, mais elle n'est pas toujours la première. Selon l'Institut syndical européen, elle était deuxième en 2000-2009 (derrière l'Espagne) et en 2010-2019 (derrière Chypre), puis première en 2020-2021 ; un autre institut place la Belgique devant elle sur 2011-2020. Et les grèves varient beaucoup : 62 jours pour 1 000 salariés en 2024 dans le privé, contre 171 en 2023, année de la réforme des retraites.",
 contexte="L'image d'une France « championne de la grève » est utilisée pour critiquer les syndicats ou le « blocage » du pays, notamment lors des mouvements sur les retraites.",
 explication="On compare les pays en journées de travail perdues pour 1 000 salariés. Mais chaque pays compte à sa façon (secteurs couverts, grèves courtes, fonction publique), ce qui rend les classements fragiles.",
 sources=[EN_GREVES, PM_GREVES, TISSOT_GREVES, TPE_GREVES],
 faits=[
  fait("Selon l'Institut syndical européen, cité par Euronews, la France comptait en moyenne 127 journées non travaillées pour 1 000 salariés en 2000-2009 (Espagne 153) et 128 en 2010-2019 (Chypre 275), puis 79 en 2020-2021, au premier rang devant la Belgique (57).", 'en_greves', '2000-2021', 'Europe', "La France est régulièrement sur le podium.", 'estimation', '128'),
  fait("Selon l'institut allemand WSI, la Belgique compte 97 jours de grève pour 1 000 salariés par an sur 2011-2020, contre 93 pour la France (secteur privé seulement) et 18 pour l'Allemagne.", 'pm_greves', '2011-2020', 'Europe', "Selon la méthode, la France n'est pas première.", 'estimation', '93'),
  fait("Selon la Dares, citée par TPE Actu, le secteur privé non agricole a compté 62 jours de grève pour 1 000 salariés en 2024, contre 171 en 2023.", 'tpe_greves', '2023-2024', 'France', "Les grèves varient fortement selon l'actualité sociale.", 'etabli', '62'),
  fait("Selon la Dares, citée par les Éditions Tissot, seules 1,6 % des entreprises de 10 salariés ou plus ont connu au moins un arrêt collectif de travail en 2024.", 'tissot_greves', '2024', 'France', "Dans l'immense majorité des entreprises, il n'y a aucune grève.", 'etabli', '1,6 %'),
  fait("Selon Euronews, l'OCDE souligne que la comparabilité internationale des données sur les grèves est affectée par des différences de définitions et de mesures.", 'en_greves', '2023', 'Europe', "Les classements sont à manier avec prudence.", 'etabli'),
 ],
 court="Plutôt exact : la France est souvent sur le podium européen des jours de grève, mais pas toujours première (Espagne, Chypre ou Belgique selon les périodes). Et en 2024, seules 1,6 % des entreprises ont connu une grève.",
 moyen="La France fait partie des pays où l'on fait le plus grève en Europe : environ 128 jours pour 1 000 salariés par an entre 2010 et 2019 selon l'Institut syndical européen. Mais elle n'est pas toujours première : Chypre, l'Espagne ou la Belgique la devancent selon les périodes et les méthodes.\n\nSurtout, la grève reste rare dans les entreprises : en 2024, seules 1,6 % des entreprises de 10 salariés ou plus en ont connu une. Les pics correspondent à de grands conflits, comme la réforme des retraites en 2023.",
 detaille="Comparer les grèves entre pays est difficile : chaque pays a ses propres méthodes de comptage. Avec ces précautions, la France apparaît régulièrement parmi les pays les plus grévistes d'Europe. Selon l'Institut syndical européen, elle comptait en moyenne 127 journées non travaillées pour 1 000 salariés par an en 2000-2009, derrière l'Espagne (153), puis 128 en 2010-2019, derrière Chypre (275), avant de passer au premier rang en 2020-2021 (79). Selon l'institut allemand WSI, sur 2011-2020, la Belgique (97) devance la France (93, privé seulement), loin devant l'Allemagne (18).\n\nLes chiffres varient beaucoup d'une année à l'autre. Dans le secteur privé, la Dares compte 171 jours de grève pour 1 000 salariés en 2023, année de la réforme des retraites, et 62 en 2024. Les salaires sont le premier motif de grève (56 % en 2024). Et la grève reste un événement rare : seules 1,6 % des entreprises de 10 salariés ou plus ont connu un arrêt collectif en 2024.\n\nLa grève est un droit, souvent le dernier moyen pour des salariés d'obtenir une augmentation : les chiffres montrent un recours concentré sur quelques grands conflits, pas un pays en grève permanente.",
 empathie="Je comprends l'agacement quand une grève bloque les trains ou les écoles. C'est vrai que la France fait partie des pays où l'on fait le plus grève ; mais plus de 98 % des entreprises de 10 salariés ou plus n'ont connu aucune grève en 2024, et la plupart portent sur les salaires.",
 legitimes=["La France est régulièrement parmi les trois pays européens qui comptent le plus de jours de grève.", "Les grèves dans les transports pèsent fortement sur les usagers."],
 contre=[
  ("Les grèves, ce sont toujours les mêmes privilégiés.", "En 2024, la première cause de grève dans le privé était la rémunération (56 %)."),
  ("Les Allemands ne font jamais grève et leur économie va mieux.", "L'Allemagne fait beaucoup moins grève (18 jours), mais la comparaison des économies dépasse cette fiche."),
 ],
 questions=["Sais-tu quelle part des entreprises a connu une grève en 2024 ?", "Quels autres moyens ont des salariés pour obtenir une augmentation quand la négociation échoue ?"],
 limites=["Les comparaisons européennes s'arrêtent en 2021 et reposent sur des méthodes non harmonisées.", "Les publications de la Dares et la carte de l'Institut syndical européen n'ont pas été lues directement, mais à travers des relais de presse."],
 publics={'convaincus': "C'est vrai, la France est souvent sur le podium européen de la grève, mais pas toujours première : Chypre, l'Espagne ou la Belgique font plus selon les périodes. Et en 2024, plus de 98 % des entreprises de 10 salariés ou plus n'ont connu aucune grève. Quand des salariés débrayent, c'est le plus souvent pour leur salaire.",
  'indecis': "La France fait effectivement partie des pays européens qui font le plus grève, surtout lors de grands conflits comme celui des retraites. Mais les chiffres varient beaucoup selon les années, et la grève reste rare dans la plupart des entreprises. C'est un droit, utilisé surtout pour les salaires."},
 a_actualiser='2027-06-30',
))

# 23 ── Droit du sol ──────────────────────────────────────────────────────────
FICHES.append(fiche(
 id='droit-du-sol-suppression', affirmation="Il suffit de supprimer le droit du sol pour régler le problème de l'immigration.", volet='immigration', sous_theme='Nationalité et accès aux droits',
 mots_cles=['supprimer le droit du sol', 'suppression du droit du sol', 'fin du droit du sol', 'abolir le droit du sol', 'droit du sol', 'ne en france', 'droit du sang', 'mayotte droit du sol'],
 verdict='trompeur', fiabilite='etabli',
 resume="En France, naître sur le sol ne donne pas la nationalité : un enfant né en France de parents étrangers devient français à sa majorité, s'il y vit et y a résidé au moins cinq ans depuis ses 11 ans (ou plus tôt, par déclaration anticipée). Cette voie concerne environ 35 000 jeunes par an (2025), qui vivent déjà en France, et elle ne donne aucun droit de séjour à leurs parents. La supprimer changerait la nationalité de ces jeunes, pas le nombre d'arrivées.",
 contexte="La suppression du droit du sol figure au programme du RN ; il a été restreint à Mayotte en 2018 puis en 2025, et la question revient dans le débat national.",
 explication="Le droit du sol français est « différé » : il récompense une enfance passée en France. Le droit d'entrer et de séjourner en France dépend d'autres règles (visas, titres de séjour, asile), que le droit du sol ne modifie pas.",
 sources=[CC_21_7, INSEE_NATIO, BDT_MAYOTTE, PS_MAYOTTE, IM_DROITSOL],
 faits=[
  fait("Selon l'article 21-7 du Code civil, « tout enfant né en France de parents étrangers acquiert la nationalité française à sa majorité » s'il réside en France et y a eu sa résidence habituelle pendant au moins cinq ans depuis l'âge de 11 ans.", 'cc_21_7', '2020', 'France', "Il n'y a pas de nationalité automatique à la naissance.", 'etabli'),
  fait("Selon l'Insee, en 2025, 32 923 mineurs nés en France sont devenus français par déclaration anticipée et 1 981 personnes par acquisition sans formalité, sur 98 139 acquisitions de la nationalité.", 'insee_natio', '2025', 'France', "Le droit du sol concerne environ un tiers des acquisitions, et des jeunes qui ont grandi en France.", 'etabli', '32 923'),
  fait("Selon l'Insee, les naturalisations par décret (42 063) et les mariages (17 579) représentent la majorité des acquisitions de la nationalité en 2025.", 'insee_natio', '2025', 'France', "Supprimer le droit du sol ne toucherait pas la principale voie d'accès.", 'etabli', '42 063'),
  fait("À Mayotte, la loi de 2018 a exigé qu'un parent réside régulièrement depuis trois mois ; la loi du 12 mai 2025 exige que les deux parents résident régulièrement depuis au moins un an à la naissance.", 'bdt_mayotte', '2018-2026', 'Mayotte', "Le droit du sol peut être restreint par la loi.", 'etabli'),
  fait("Selon l'Institut Montaigne, la dérogation de 2018 pour Mayotte, prise « afin de limiter le nombre de femmes venant accoucher à Mayotte », a été validée par le Conseil constitutionnel ; la marge de manœuvre juridique reste « faible en matière d'immigration familiale et d'asile ».", 'im_droitsol', '2024', 'France', "Restreindre la nationalité ne règle pas les flux d'entrée, qui relèvent d'autres règles.", 'interpretation'),
 ],
 court="Trompeur : en France, le droit du sol ne joue qu'à l'adolescence, pour des jeunes nés et élevés ici (environ 35 000 par an), et il ne donne aucun titre de séjour aux parents. Le supprimer ne réduirait pas les arrivées.",
 moyen="Naître en France ne rend pas français. Un enfant né en France de parents étrangers peut le devenir à sa majorité, ou un peu avant par déclaration anticipée, s'il a vécu au moins cinq ans en France. En 2025, cela concerne environ 35 000 jeunes, qui ont grandi ici.\n\nCe droit ne donne aucun papier aux parents. Le supprimer ne changerait rien au nombre de personnes qui arrivent ; il ferait seulement de ces jeunes des étrangers dans le pays où ils ont grandi. À Mayotte, il a été restreint en 2018 et 2025, mais les sources lues ne montrent pas d'effet sur les arrivées.",
 detaille="Le droit du sol français n'est pas automatique. Selon l'article 21-7 du Code civil, un enfant né en France de parents étrangers devient français à sa majorité s'il réside en France et y a vécu au moins cinq ans depuis l'âge de 11 ans ; il peut aussi le devenir avant sa majorité, par déclaration anticipée. En 2025, 32 923 mineurs nés en France sont devenus français par déclaration anticipée, et 1 981 personnes sans formalité, sur 98 139 acquisitions. La majorité des acquisitions passe par la naturalisation (42 063) et le mariage (17 579).\n\nLe droit du sol ne crée aucun droit au séjour pour les parents : l'entrée et le séjour relèvent des visas, des titres de séjour et de l'asile. L'Institut Montaigne souligne d'ailleurs que la marge de manœuvre juridique est faible en matière d'immigration familiale et d'asile.\n\nÀ Mayotte, le législateur a restreint le droit du sol en 2018, puis en 2025 : les deux parents doivent désormais résider régulièrement depuis au moins un an. Le Conseil constitutionnel a validé la mesure de 2018. Mais aucune source lue ne mesure un effet sur les arrivées. Supprimer le droit du sol, c'est surtout fabriquer des étrangers nés et élevés en France.",
 empathie="Je comprends qu'on cherche une mesure simple face à une question qui inquiète. Mais le droit du sol ne concerne que des jeunes qui ont grandi ici, et il ne donne aucun papier à leurs parents : le supprimer ne changerait pas le nombre d'arrivées.",
 legitimes=["Le droit du sol peut être restreint par la loi : le Conseil constitutionnel a validé l'exception mahoraise de 2018.", "La ligne « acquisitions sans formalité » de l'Insee peut inclure d'autres cas que le droit du sol."],
 contre=[
  ("Des femmes viennent accoucher en France pour que leur enfant soit français.", "L'enfant ne devient français qu'à l'adolescence, après cinq ans de résidence ; à Mayotte, cette crainte a justifié une exception dont l'effet n'est pas mesuré ici."),
  ("Les autres pays n'ont pas le droit du sol.", "Les comparaisons internationales n'ont pas été étudiées par les sources lues ; en France, il s'agit d'un droit du sol différé, déjà conditionné."),
 ],
 questions=["Savais-tu qu'un enfant né en France de parents étrangers n'est pas français à la naissance ?", "Que deviendrait un jeune qui a passé toute sa vie en France si on lui refusait la nationalité ?"],
 limites=["Aucune source lue ne mesure l'effet des restrictions de 2018 et 2025 sur les naissances ou les arrivées à Mayotte.", "La décision du Conseil constitutionnel sur la loi de 2025 n'a pas été lue."],
 publics={'convaincus': "Un enfant né en France de parents étrangers n'est pas français à la naissance : il peut le devenir à l'adolescence, s'il a grandi ici. Et ça ne donne aucun papier à ses parents. Supprimer le droit du sol ne ferait pas venir une personne de moins ; ça ferait juste des étrangers de jeunes qui ont grandi en France.",
  'indecis': "Le droit du sol est souvent mal compris : il ne joue qu'à l'adolescence, pour des jeunes qui ont vécu au moins cinq ans en France, environ 35 000 par an. Il ne donne aucun droit au séjour aux parents. On peut débattre des règles de la nationalité, mais ce n'est pas un levier pour réduire l'immigration."},
 a_actualiser='2027-07-31', raison="Nouvelles données annuelles d'acquisition de la nationalité.",
))

# 24 ── Hébergement des demandeurs d'asile et impôts locaux ───────────────────
FICHES.append(fiche(
 id='hebergement-migrants-impots-locaux', affirmation="Les communes paient avec nos impôts locaux l'hébergement des migrants.", volet='immigration', sous_theme='Immigration et finances publiques',
 mots_cles=['impots locaux', 'hebergement des migrants', 'centre de migrants', 'cada', 'centre d accueil', 'commune paie', 'mairie paie les migrants', 'taxe fonciere migrants', 'huda'],
 verdict='trompeur', fiabilite='etabli',
 resume="Non pour l'essentiel : l'hébergement des demandeurs d'asile (CADA, HUDA, CAES) est financé par l'État, sur le budget « Immigration, asile et intégration », pour environ 958 millions d'euros en 2026 et 111 855 places. Les communes supportent toutefois certains coûts indirects, comme la scolarisation des enfants accueillis, et les départements financent l'essentiel de la prise en charge des mineurs non accompagnés, avec une aide forfaitaire de l'État.",
 contexte="L'ouverture d'un centre d'accueil dans une commune suscite souvent des inquiétudes sur les impôts locaux.",
 explication="L'accueil des demandeurs d'asile relève de l'État, qui finance les centres et l'allocation pour demandeur d'asile, gérée par l'Ofii. Les collectivités gardent leurs compétences habituelles : les communes pour les écoles, les départements pour la protection de l'enfance.",
 sources=[AN_PLF303, SENAT_ASILE26, SENAT_ROUVRAY, SENAT_MNA],
 faits=[
  fait("Selon l'Assemblée nationale, le programme 303 de l'État finance l'hébergement des demandeurs d'asile pour 957,6 M€ de crédits de paiement en 2026, avec 111 855 places, dont 61 903 en CADA.", 'an_plf303', '2026', 'France', "L'hébergement est payé par le budget de l'État, pas par les impôts locaux.", 'etabli', '957,6 M€'),
  fait("Selon le Sénat, le coût de l'asile est d'au moins 1,85 Md€ en 2025, dont environ la moitié pour l'hébergement ; ce chiffre exclut les dépenses de santé, de scolarité et d'aide sociale.", 'senat_asile26', '2025', 'France', "Le coût est réel et principalement à la charge de l'État.", 'estimation', '1,85 Md€'),
  fait("Selon une question au Sénat, la commune de Rouvray a supporté « plus de 92 000 euros » de frais de scolarité pour les enfants d'un CADA depuis 2016 ; le Gouvernement répond que ces coûts sont pris en compte dans la dotation globale de fonctionnement.", 'senat_rouvray', '2016-2022', 'Rouvray', "Les communes paient bien certains coûts indirects, compensés seulement en partie.", 'etabli', '92 000 €'),
  fait("Selon le Gouvernement, les départements assurent l'accueil des mineurs non accompagnés au titre de l'aide sociale à l'enfance, avec des contributions forfaitaires de l'État (500 € par évaluation, 90 € par jour de mise à l'abri pendant 14 jours au plus).", 'senat_mna', '2024', 'France', "Pour les mineurs isolés, ce sont surtout les départements qui paient.", 'etabli', '500 €'),
 ],
 court="Trompeur : l'hébergement des demandeurs d'asile est payé par l'État (environ 958 millions d'euros en 2026), pas par les impôts locaux. Les communes paient en revanche la scolarisation des enfants accueillis, et les départements les mineurs isolés.",
 moyen="Les centres d'accueil des demandeurs d'asile (CADA, HUDA, CAES) sont financés par l'État, sur le budget « Immigration, asile et intégration » : environ 958 millions d'euros en 2026 pour près de 112 000 places. Ce n'est pas la commune qui paie l'hébergement.\n\nIl y a deux nuances honnêtes : une commune scolarise les enfants accueillis, ce qui a un coût (92 000 € en six ans pour une petite commune), compensé en partie par la dotation de l'État. Et les départements prennent en charge les mineurs non accompagnés, avec une aide forfaitaire de l'État.",
 detaille="L'accueil des demandeurs d'asile est une compétence de l'État. Le programme 303 du budget finance l'hébergement en centres d'accueil (CADA), en hébergement d'urgence (HUDA) et en centres d'accueil et d'examen des situations (CAES) : 957,6 millions d'euros de crédits de paiement en 2026, pour 111 855 places. L'allocation pour demandeur d'asile est gérée par l'Ofii. Le Sénat estime le coût total de l'asile à au moins 1,85 milliard d'euros en 2025, dont la moitié environ pour l'hébergement.\n\nLes collectivités ne sont pas pour autant hors du circuit. Une commune qui accueille un CADA scolarise les enfants : à Rouvray, plus de 92 000 euros depuis 2016, que l'État dit prendre en compte dans la dotation globale de fonctionnement ; la cantine et les fournitures restent à la charge des familles ou du gestionnaire. Les départements, eux, financent l'accueil des mineurs non accompagnés au titre de l'aide sociale à l'enfance, avec des contributions forfaitaires de l'État.\n\nDire que « nos impôts locaux paient l'hébergement des migrants » est donc inexact. La vraie question est celle d'une compensation suffisante pour les petites communes et les départements, comme l'a demandé la sénatrice qui a interrogé le Gouvernement sur Rouvray.",
 empathie="Je comprends l'inquiétude quand un centre ouvre près de chez soi et qu'on se demande qui va payer. L'hébergement lui-même est financé par l'État ; la commune paie surtout l'école des enfants, comme pour tout enfant qui arrive.",
 legitimes=["Les communes supportent des coûts de scolarité qui ne sont compensés qu'indirectement.", "Les départements financent l'essentiel de la prise en charge des mineurs non accompagnés."],
 contre=[
  ("Notre mairie a voté une subvention à une association d'aide aux migrants.", "C'est possible, mais c'est un choix local, distinct du financement de l'hébergement par l'État."),
  ("Les impôts de l'État, ce sont aussi nos impôts.", "C'est vrai : le coût existe, environ un milliard pour l'hébergement ; mais il n'augmente pas les impôts locaux de la commune d'accueil."),
 ],
 questions=["Sais-tu qui finance un centre d'accueil de demandeurs d'asile ?", "Que penserais-tu d'une meilleure compensation de l'État pour les écoles des communes d'accueil ?"],
 limites=["Le coût total des mineurs non accompagnés pour les départements n'a pas été chiffré par les sources lues.", "Le cofinancement éventuel de l'hébergement d'urgence de droit commun par certaines collectivités n'a pas été vérifié."],
 publics={'convaincus': "Les centres pour demandeurs d'asile sont payés par l'État, près d'un milliard d'euros en 2026, pas par ta taxe foncière. La commune paie l'école des enfants, comme pour n'importe quel enfant qui s'installe. Si tu veux une meilleure compensation pour les petites communes, c'est une demande légitime, à adresser à l'État.",
  'indecis': "C'est normal de se demander qui paie quand un centre ouvre dans sa commune. L'hébergement des demandeurs d'asile est financé par l'État ; la commune assume surtout la scolarisation des enfants, en partie compensée. Les départements paient, eux, la prise en charge des mineurs isolés."},
 a_actualiser='2027-06-30',
))

# 25 ── Smartphones et « vrais réfugiés » ─────────────────────────────────────
FICHES.append(fiche(
 id='migrants-smartphones-refugies', affirmation="Les migrants ont tous des smartphones, ce ne sont pas de vrais réfugiés.", volet='immigration', sous_theme='Immigration et asile',
 mots_cles=['smartphones', 'smartphone', 'telephones portables', 'iphone', 'vrais refugies', 'faux refugies', 'migrants economiques', 'taux de protection', 'ofpra'],
 verdict='contredit', fiabilite='etabli',
 resume="Avoir un téléphone ne dit rien du besoin de protection : pour les exilés, c'est un outil de survie (se repérer, joindre sa famille, traduire). Selon le HCR, les réfugiés ont même deux fois moins de chances que la population générale d'avoir un téléphone connecté, et 29 % des ménages réfugiés n'en ont aucun. En France, l'OFPRA a accordé une protection à 41 % des demandeurs en 2025, et le taux global atteint 52,1 % avec les recours : plus d'un demandeur sur deux est reconnu comme ayant besoin de protection.",
 contexte="Les images de personnes migrantes photographiant leur arrivée avec un téléphone ont nourri, depuis 2015, l'idée qu'il s'agirait de migrants aisés et non de réfugiés.",
 explication="La protection (statut de réfugié ou autre protection) est examinée au cas par cas par l'OFPRA, puis par la Cour nationale du droit d'asile en cas de recours, en fonction des menaces que la personne fuit ; la possession d'un objet n'entre pas en compte.",
 sources=[HCR_CONNECT, SLATE_TEL, EUAA_OFPRA25, SENAT_ASILE26, EUROSTAT_ASILE],
 faits=[
  fait("Selon le HCR, les réfugiés ont 50 % de chances en moins que la population générale d'avoir un téléphone connecté à Internet, et 29 % des ménages réfugiés n'ont aucun téléphone.", 'hcr_connect', '2016', 'Monde', "« Ils ont tous des smartphones » est faux.", 'estimation', '29 %'),
  fait("Selon le HCR, les réfugiés consacrent jusqu'à un tiers de leur revenu disponible à rester connectés et considèrent la connexion comme un outil de survie.", 'hcr_connect', '2016', 'Monde', "Le téléphone n'est pas un luxe mais une nécessité.", 'estimation'),
  fait("Selon l'Agence de l'UE pour l'asile, l'OFPRA a accordé une protection à 41 % des demandeurs en 2025 (39 % en 2024), sur 156 509 décisions.", 'euaa_ofpra25', '2025', 'France', "Une part importante des demandeurs est reconnue en première instance.", 'etabli', '41 %'),
  fait("Selon le Sénat, le taux global de protection, recours devant la CNDA inclus, « atteint désormais 52,1 % en 2025 ».", 'senat_asile26', '2025', 'France', "Plus d'un demandeur sur deux obtient une protection.", 'etabli', '52,1 %'),
  fait("Selon Eurostat, le taux de reconnaissance en première instance dans l'Union est de 39 % en 2025, mais de 73 % pour les Afghans et de 92 % pour les Vénézuéliens.", 'eurostat_asile', '2025', 'Union européenne', "Pour certaines nationalités, presque tous les demandeurs sont reconnus.", 'etabli', '39 %'),
 ],
 court="Faux : le téléphone est un outil de survie pour les exilés, et selon le HCR, 29 % des ménages réfugiés n'en ont même pas. En France, plus d'un demandeur d'asile sur deux (52,1 % en 2025) obtient une protection.",
 moyen="Pour quelqu'un qui fuit son pays, le téléphone sert à tout : trouver son chemin, joindre sa famille, traduire, appeler à l'aide. Ce n'est pas un signe de richesse : selon le HCR, les réfugiés sont même moins équipés que le reste de la population, et près d'un ménage réfugié sur trois n'a pas de téléphone.\n\nEn France, la protection est décidée au cas par cas : en 2025, 41 % des demandeurs ont été protégés par l'OFPRA, et 52,1 % au total avec les recours. Ce sont des personnes reconnues en danger, téléphone ou pas.",
 detaille="L'image de migrants arrivant avec un smartphone a beaucoup circulé depuis 2015. Pourtant, pour les personnes exilées, le téléphone est un outil vital : GPS pour se repérer, messagerie pour joindre la famille, traduction, organisation du trajet. Une responsable du service social pour les réfugiés de Munich résumait : « Ça n'a vraiment rien d'un luxe ». Selon le HCR, les réfugiés ont deux fois moins de chances que la population générale d'avoir un téléphone connecté, 29 % des ménages réfugiés n'en ont aucun, et ils consacrent jusqu'à un tiers de leur revenu à rester connectés.\n\nLe statut de réfugié ne dépend pas de ce qu'on possède, mais des menaces qu'on fuit. En France, l'OFPRA a accordé une protection à 41 % des demandeurs en 2025, et le Sénat évalue le taux global, recours inclus, à 52,1 %. Dans l'Union, 39 % des décisions de première instance sont positives, et jusqu'à 73 % pour les Afghans ou 92 % pour les Vénézuéliens.\n\nIl est vrai qu'environ la moitié des demandeurs sont finalement déboutés, et que les décisions d'éloignement sont rarement exécutées. Mais c'est un autre débat, qui n'a rien à voir avec le fait d'avoir un téléphone.",
 empathie="Je comprends que ça étonne de voir des personnes qui fuient la guerre avec un téléphone à la main. Mais réfléchis : si tu devais fuir avec un seul objet, ce serait sans doute ton téléphone, pour te repérer et donner des nouvelles à tes proches.",
 legitimes=["Environ la moitié des demandeurs d'asile ne sont pas reconnus comme ayant besoin d'une protection.", "Les décisions d'éloignement des déboutés sont rarement exécutées (5,5 % en moyenne sur 2019-2025 selon le Sénat)."],
 contre=[
  ("Un vrai réfugié n'a pas les moyens de s'acheter un iPhone.", "Selon le HCR, les réfugiés consacrent jusqu'à un tiers de leurs revenus à rester connectés : c'est une priorité vitale, pas un signe d'aisance."),
  ("Ce sont des migrants économiques.", "Pour la moitié d'entre eux, la protection est reconnue après examen individuel ; pour les autres, la décision ne dépend pas du téléphone."),
 ],
 questions=["Si tu devais fuir ton pays avec un seul objet, lequel prendrais-tu ?", "Sais-tu quelle part des demandeurs d'asile obtient une protection en France ?"],
 limites=["L'étude du HCR date de 2016 ; aucune étude plus récente sur l'équipement des réfugiés n'a été lue.", "Le rapport d'activité 2025 de l'OFPRA est connu par l'Agence de l'UE pour l'asile, pas par le document lui-même."],
 publics={'convaincus': "Si tu devais fuir avec un seul objet, tu prendrais ton téléphone : c'est ton GPS, ton traducteur et ton seul lien avec ta famille. Selon le HCR, près d'un ménage réfugié sur trois n'en a même pas. Et en France, plus d'un demandeur sur deux est reconnu en danger après examen : le téléphone n'y change rien.",
  'indecis': "C'est vrai que l'image surprend. Mais pour un exilé, le téléphone est un outil de survie, pas un luxe. Le droit d'asile est examiné au cas par cas : en 2025, plus de la moitié des demandeurs ont obtenu une protection, et les autres doivent en principe quitter la France."},
 a_actualiser='2027-07-31',
))

if __name__ == '__main__':
    for f in FICHES:
        with open(os.path.join(OUT, f['id'] + '.json'), 'w', encoding='utf-8') as fh:
            json.dump(f, fh, ensure_ascii=False, indent=2); fh.write('\n')
    print(f"{len(FICHES)} fiches écrites")
