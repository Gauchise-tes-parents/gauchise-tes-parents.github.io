"""Fiches quotidiennes du 7 novembre 2026, passage de 20 h 15 (UTC) — phase alpha.

26 questions qui circulent (extrême droite, clichés sur la gauche, programmes) et qui n'avaient pas de fiche
qui leur réponde vraiment. Toutes les sources ont été ouvertes et lues le 7 novembre 2026 (consultee=True) ;
les chiffres viennent uniquement des passages cités. Données anciennes signalées dans les limites.
Chaque fiche contient les réponses selon le public (« publics » : électeur d'extrême droite convaincu / indécis).
Usage : python3 scripts/fiches/quotidien_20261107_2015.py  (puis node scripts/corrections-v10.js et node scripts/enrichir-fiches.js)
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from reponses_directes import src, fait, fiche as _fiche, OUT

TODAY = '2026-11-07'

def fiche(**k):
    d = _fiche(**k)
    d['derniere_verification'] = TODAY
    return d

# ── Sources : RN, programmes, institutions ─────────────────────────────────
IM_AUTO = ('im_auto', src("Renationaliser les concessions d'autoroutes (Marine Le Pen, présidentielle 2022)", "Institut Montaigne (chiffrage des programmes)", "14 février 2022",
  "https://www.institutmontaigne.org/presidentielle-2022/marine-le-pen/renationaliser-les-concessions-dautoroutes/",
  "Le programme 2022 de Marine Le Pen prévoit de « Renationaliser les autoroutes pour baisser de 15 % les péages ». L'Institut Montaigne évalue la compensation due aux concessionnaires entre 39,5 et 42,1 Md€, à quoi s'ajoute la reprise de la dette des sociétés (31,6 Md€ fin 2020) ; la dette publique augmenterait de 30 à plus de 70 Md€ selon l'hypothèse. Le gain annuel serait d'environ 4,5 Md€ à tarifs inchangés et d'environ 3,5 Md€ avec une baisse de 15 % ; impact jugé « neutre si maintien des tarifs, potentiellement négatif si baisse des tarifs ».",
  "Chiffrage d'un think tank libéral (2022).", 'etude'))
SENAT_AUTO20 = ('senat_auto20', src("Synthèse du rapport n° 709 (2019-2020) de la commission d'enquête sur les concessions autoroutières", "Sénat (rapporteur Vincent Delahaye)", "18 septembre 2020",
  "https://www.senat.fr/rap/r19-709-1/r19-709-1-syn.pdf",
  "Pour Vinci et Eiffage, la rentabilité attendue par les actionnaires serait atteinte « autour de 2022 » ; les dividendes versés de 2006 à 2019 totalisent environ 24,3 Md€, et « au-delà de 2022, les dividendes versés atteindraient environ 40 milliards d'euros ». Le ministère de l'Économie estime un rachat anticipé « entre 45 et 50 milliards d'euros » ; le Sénat juge « raisonnable d'aller au terme des concessions ».",
  "Rapport d'une commission d'enquête parlementaire."))
SENAT_AUTO24 = ('senat_auto24', src("Préparation de l'échéance des contrats de concessions autoroutières (rapport d'information n° 65, 2024-2025)", "Sénat, commission des finances (Hervé Maurey)", "23 octobre 2024",
  "https://www.senat.fr/rap/r24-065/r24-065_mono.html",
  "Les concessions historiques prennent fin entre 2031 (SANEF) et 2036 (ASF, AREA) ; conclus pour 35 ans, les contrats ont été prolongés à 64 à 75 ans. En 2023, Vinci Autoroutes représentait 9 % du chiffre d'affaires du groupe Vinci mais 43 % de son résultat net. Une résiliation anticipée pourrait coûter 40 à 50 Md€ ; la gratuité est qualifiée de « piège démagogique ».",
  "Rapport parlementaire."))
AN_AUTO = ('an_auto', src("Questions au gouvernement n° 525 et n° 678 (Pierre Meurin, RN) sur les autoroutes", "Assemblée nationale", "1er février et 22 mars 2023",
  "https://questions.assemblee-nationale.fr/dyn/16/questions/QANR5L16QG678.pdf",
  "Le député RN rappelle que Marine Le Pen réclame de longue date la nationalisation. Bruno Le Maire répond : « Vous avez proposé, madame Le Pen, la nationalisation des autoroutes françaises », pour un coût de « bien 40 à 50 milliards d'euros ».",
  "Compte rendu officiel des questions au gouvernement."))
LFI_AUTO = ('lfi_auto', src("Proposition de loi n° 1203 relative à la nationalisation des sociétés concessionnaires d'autoroutes", "Assemblée nationale (Christophe Bex, Mathilde Panot et al., LFI)", "1er avril 2025",
  "https://www.assemblee-nationale.fr/dyn/17/textes/l17b1203_proposition-loi.pdf",
  "« Les sociétés suivantes sont nationalisées » (seize sociétés concessionnaires) ; l'exposé des motifs évoque une hausse des péages d'environ 20 % en dix ans.",
  "Texte parlementaire."))
GOUV_1986 = ('gouv_1986', src("Jacques Chirac (1986-1988)", "info.gouv.fr (Gouvernement)", "non daté",
  "https://www.info.gouv.fr/les-anciens-premiers-et-premieres-ministres-de-la-ve-republique/jacques-chirac-1986-1988",
  "Le résultat des législatives est acquis au soir du 16 mars 1986 : « la droite obtient la majorité absolue ». C'est la première cohabitation ; l'Assemblée adopte ensuite « le retour au scrutin majoritaire pour les prochaines législatives ».",
  "Site du gouvernement."))
LAR_1986 = ('lar_1986', src("Les élections 1986 : les résultats, conséquences et perspectives", "Larousse, Journal de l'année (édition 1987)", "1987",
  "https://www.larousse.fr/archives/journaux_annee/1987/24/les_elections_1986",
  "Les vainqueurs disposent de « deux voix de majorité grâce à l'apport des divers droite » ; les listes FN totalisent 9,85 % des suffrages exprimés.",
  "Ouvrage de référence (1987).", 'secondaire'))
VDI_PROP = ('vdi_prop', src("La proportionnelle : une urgence démocratique", "La Vie des idées (Emiliano Grossman, Isabelle Guinaudeau)", "16 décembre 2025",
  "https://laviedesidees.fr/IMG/pdf/20251216_proportionnelle.pdf",
  "La durée moyenne des gouvernements est d'« environ douze mois sous la IVe République » contre « près de vingt sous la Ve ». La France a « l'écart moyen le plus élevé d'Europe entre part de voix et part de sièges ». « Les partis français n'ont jamais vraiment appris à gouverner ensemble. »",
  "Analyse de politistes, favorable à la proportionnelle.", 'etude'))
GC_LECORNU = ('gc_lecornu', src("Le gouvernement Lecornu est-il le plus court de l'histoire européenne ?", "Le Grand Continent (Marin Saillofest)", "7 octobre 2025",
  "https://legrandcontinent.eu/fr/2025/10/07/le-gouvernement-lecornu-est-il-le-le-plus-court-de-lhistoire-europeenne/",
  "Les gouvernements ont duré en moyenne 609 jours pendant le premier mandat d'Emmanuel Macron, contre 303 jours depuis le début du second. D'après le Pew Research Center (2023), les gouvernements des régimes parlementaires de l'UE durent environ deux ans en moyenne ; la durée médiane est de quatre ans et demi au Luxembourg et de moins d'un an en Belgique, en Finlande et en Italie.",
  "Revue d'analyse géopolitique.", 'media'))
LCP_PROP = ('lcp_prop', src("Proportionnelle aux législatives : François Bayrou consulte, les avis divergent", "LCP (Anne-Charlotte Dusseaulx)", "30 avril 2025",
  "https://lcp.fr/actualites/proportionnelle-aux-legislatives-francois-bayrou-consulte-les-avis-divergent-sur-le",
  "Marine Le Pen juge le scrutin de 1986 « un moindre mal » ; Manuel Bompard (LFI) se dit favorable à « un scrutin réellement proportionnel ». Laurent Wauquiez prévient que « la proportionnelle aboutira à ce qu'on institutionnalise le chaos politique ». MoDem et écologistes sont favorables, le PS divisé, Horizons opposé.",
  "Média parlementaire.", 'media'))
LCP_IVG_C = ('lcp_ivg_c', src("Après le vote du Congrès, la France devient le premier pays au monde à inscrire l'IVG dans sa Constitution", "LCP (Maxence Kagni)", "4 mars 2024",
  "https://lcp.fr/actualites/apres-le-vote-du-congres-la-france-devient-le-premier-pays-au-monde-a-inscrire-l-ivg",
  "Le Congrès adopte la révision par 780 voix pour et 72 contre (majorité requise : 512). Les députés du groupe RN ont voté 46 pour, 11 contre et 20 abstentions ; Marine Le Pen a voté pour.",
  "Média parlementaire.", 'media'))
LCP_IVG_AN = ('lcp_ivg_an', src("Inscription de l'IVG dans la Constitution : l'Assemblée adopte le projet de loi par 493 voix contre 30", "LCP (Soizic Bonvarlet)", "30 janvier 2024",
  "https://lcp.fr/actualites/inscription-de-l-ivg-dans-la-constitution-l-assemblee-adopte-le-projet-de-loi-par-493",
  "Le groupe RN a voté 46 pour (dont Marine Le Pen), 12 contre et 14 abstentions. La députée RN Pascale Bordes : « personne, absolument personne, ne souhaite dans la société française contemporaine remettre en cause l'IVG ».",
  "Média parlementaire.", 'media'))
PS_IVG16 = ('ps_ivg16', src("IVG : des cadres FN soutiennent Maréchal-Le Pen face à Philippot", "Public Sénat (avec AFP)", "7 décembre 2016",
  "https://www.publicsenat.fr/actualites/politique/ivg-des-cadres-fn-soutiennent-marechal-le-pen-face-a-philippot-51113",
  "En 2012, Marine Le Pen avait parlé d'« avortements de confort » et se disait prête à dérembourser l'avortement en cas de besoins budgétaires. En 2016, Marion Maréchal-Le Pen voulait « revenir sur le remboursement intégral et illimité de l'avortement ». Marine Le Pen disait alors ne pas remettre en cause l'accès à l'IVG.",
  "Média parlementaire (2016).", 'media'))
PS_IVG16B = ('ps_ivg16b', src("Marine Le Pen rejette les « chicayas » au FN sur le sujet « lunaire » de l'IVG", "Public Sénat", "11 décembre 2016",
  "https://www.publicsenat.fr/actualites/politique/marine-le-pen-rejette-les-chicayas-au-fn-sur-le-sujet-lunaire-de-l-ivg-51212",
  "En 2011, Marine Le Pen disait qu'il fallait « cesser de rembourser l'avortement ». En 2016 : « Aujourd'hui, ce débat est tranché, je n'ai pas de concession à faire, enfin plus (...) ».",
  "Média parlementaire (2016).", 'media'))
IM_OTAN = ('im_otan', src("Sortir la France du commandement intégré de l'OTAN (Marine Le Pen, présidentielle 2022)", "Institut Montaigne", "14 février 2022",
  "https://www.institutmontaigne.org/presidentielle-2022/marine-le-pen/sortir-la-france-du-commandement-integre-de-lotan",
  "« Marine Le Pen propose de : Sortir la France du commandement intégré de l'OTAN. » L'économie annuelle est estimée à 0,3 Md€.",
  "Chiffrage d'un think tank (2022).", 'etude'))
PS_OTAN = ('ps_otan', src("Otan : les propositions des candidats à la présidentielle", "Public Sénat (Pierre-Louis Boucé)", "25 mars 2022",
  "https://www.publicsenat.fr/actualites/politique/otan-les-propositions-des-candidats-a-la-presidentielle-200136",
  "Marine Le Pen : « On ne va pas le faire alors qu'il y a une guerre dans un pays européen », puis « il faudra le faire » une fois le conflit terminé. Jean-Luc Mélenchon veut quitter immédiatement le commandement intégré, puis, étape par étape, l'organisation dans son ensemble, qu'il qualifie d'« organisation inutile qui provoque des tensions ».",
  "Média parlementaire (2022).", 'media'))
E1_OTAN = ('e1_otan', src("Otan : Jordan Bardella contre une sortie du commandement intégré « en période de guerre »", "Europe 1 avec AFP", "28 mars 2024",
  "https://www.europe1.fr/politique/otan-jordan-bardella-contre-une-sortie-du-commandement-integre-en-periode-de-guerre-4238510",
  "Jordan Bardella : « Si la guerre est toujours en cours, non » et « On ne change pas les traités en période de guerre ». En avril 2022, Marine Le Pen avait promis de « quitter le commandement intégré de l'Otan ».",
  "Dépêche reprise par un média.", 'media'))
LNC_OTAN = ('lnc_otan', src("Législatives : Bardella lisse son programme, Macron déclenche une nouvelle polémique", "Les Nouvelles Calédoniennes / AFP", "20 juin 2024",
  "https://www.lnc.nc/article/france/politique/legislatives-bardella-lisse-son-programme-macron-declenche-une-nouvelle-polemique",
  "Jordan Bardella ne veut pas « remettre en cause les engagements pris par la France sur la scène internationale », invoquant « un enjeu de crédibilité à l'égard de nos partenaires européens et de nos alliés de l'Otan » : il exclut de quitter le commandement intégré.",
  "Dépêche AFP reprise par un quotidien.", 'media'))
ELY_OTAN = ('ely_otan', src("Déclaration de Nicolas Sarkozy sur le retour de la France dans le commandement intégré de l'OTAN", "Présidence de la République", "11 mars 2009",
  "https://www.elysee.fr/nicolas-sarkozy/2009/03/11/declaration-de-m-nicolas-sarkozy-president-de-la-republique-sur-le-retour-de-la-france-dans-le-commandement-integre-de-lotan-et-la-defense-europeenne-a-paris-le-11-mars-2009",
  "« nos forces armées sont et resteront nationales » ; « Nous ne placerons pas de contingent en permanence sous commandement allié en temps de paix. » Le discours rappelle la décision du général de Gaulle en 1966.",
  "Discours officiel."))
PS_LEG24 = ('ps_leg24', src("Législatives 2024 : le RN enregistre son plus fort total de voix au premier tour d'une élection", "Public Sénat (Henri Clavier)", "1er juillet 2024",
  "https://www.publicsenat.fr/actualites/politique/legislatives-2024-le-rn-enregistre-son-plus-fort-total-de-voix-au-premier-tour-dune-election",
  "Au premier tour, le RN et ses alliés obtiennent 10 628 330 voix, contre 4 248 537 en 2022. La participation atteint 66,71 %. Aux européennes de 2024, la liste Bardella avait obtenu 7 765 936 voix.",
  "Média parlementaire (chiffres du ministère de l'Intérieur).", 'media'))
MI_LEG24 = ('mi_leg24', src("Second tour des législatives : un résultat en trompe-l'œil ?", "Maire-info (Franck Lemarc)", "8 juillet 2024",
  "https://www.maire-info.com/second-tour-des-legislatives-un-resultat-en-trompe-loeil-article2-28795",
  "Au second tour, le RN et ses alliés obtiennent environ 10 millions de voix, soit 37 %, et 143 sièges (88 pour le RN seul) ; le NFP environ 7 millions (25,7 %) et 182 sièges ; Ensemble environ 6,3 millions (23,4 %). Le corps électoral du second tour est de 43,3 millions d'inscrits, contre 49 millions au premier.",
  "Quotidien des élus locaux.", 'media'))
LCP_EURO24 = ('lcp_euro24', src("Carte des résultats des européennes : le Rassemblement national en tête dans plus de 90 % des communes", "LCP (Raphaël Marchal)", "10 juin 2024",
  "https://lcp.fr/actualites/carte-des-resultats-des-europeennes-le-rassemblement-national-en-tete-dans-plus-de-90",
  "Le RN arrive en tête dans 32 613 communes sur 35 015, avec un peu plus de 31 % des suffrages exprimés (chiffres du ministère de l'Intérieur). L'abstention est de 48,17 %.",
  "Média parlementaire.", 'media'))
# ── Sources : vote des jeunes, députés, syndicats, laïcité, médias ─────────
IPSOS_EU24 = ('ipsos_eu24', src("Européennes 2024 : sociologie des électorats et profil des abstentionnistes", "Ipsos (pour France Télévisions, Radio France, Public Sénat/LCP)", "9 juin 2024",
  "https://www.ipsos.com/sites/default/files/ct/news/documents/2024-06/Ipsos-Sociologie-des-e%CC%81lectorats-10-juin-15h.pdf",
  "Enquête auprès de 8 923 inscrits. Chez les 18-24 ans qui ont voté, la liste LFI obtient 33 % et la liste RN 25 % ; le RN fait 30 % chez les 25-34 ans et atteint son maximum chez les 50-59 ans (40 %). L'abstention est de 60 % chez les 18-24 ans, de 65 % chez les 25-34 ans et de 29 % chez les 70 ans et plus.",
  "Enquête d'un institut de sondage.", 'etude'))
IPSOS_LEG24 = ('ipsos_leg24', src("Sociologie des électorats — Législatives 2024", "Ipsos Talan (pour France Télévisions, Radio France, Public Sénat)", "30 juin 2024",
  "https://www.ipsos.com/fr-fr/legislatives-2024/node/1025896",
  "Enquête auprès de 10 286 inscrits. « L'alliance de gauche a ainsi été choisie par la moitié des votants de moins de 25 ans » ; le NFP fait 40 % chez les 25-34 ans. Le RN et ses alliés font 32 % chez les moins de 35 ans, contre 18 % en 2022.",
  "Enquête d'un institut de sondage.", 'etude'))
FJJ_JEUNES = ('fjj_jeunes', src("Les jeunes « emmerdent »-ils le Rassemblement national ?", "Fondation Jean-Jaurès (Christelle Craplet, Adélaïde Zulfikarpasic, BVA Xsight)", "19 juin 2024",
  "https://www.jean-jaures.org/publication/les-jeunes-emmerdent-ils-le-rassemblement-national/",
  "25 % des 18-24 ans ont voté pour la liste Bardella aux européennes de 2024, contre 15 % en 2019 ; LFI reste le premier parti chez les jeunes votants (33 %). Chez les 18-24 ans, « seuls 40% se sont déplacés ».",
  "Analyse d'un think tank proche du Parti socialiste.", 'etude'))
AN_INDEM = ('an_indem', src("Fiche n° 7 : Situation matérielle du député (actualisée en janvier 2026)", "Assemblée nationale", "janvier 2026",
  "https://www.assemblee-nationale.fr/dyn/contenu/telechargement/631144/file/Fiche%207%20corrig%C3%A9e%20-%20Situation%20mat%C3%A9rielle%20du%20d%C3%A9put%C3%A9_actualis%C3%A9e%20080126.pdf",
  "L'indemnité parlementaire comprend une base de 5 931,95 €, une indemnité de résidence de 177,96 € et une indemnité de fonction de 1 527,48 €, « soit brut mensuel : 7 637,39 € » et « un montant net mensuel de 5 953,34 € ». Depuis le 1er janvier 2026, la dotation de fonctionnement parlementaire (fusion de l'avance de frais de mandat et de la dotation matérielle) est de 7 238,04 € par mois pour un député de métropole ; le crédit collaborateurs est de 11 463 € par mois, pour jusqu'à cinq collaborateurs.",
  "Document officiel de l'Assemblée."))
IPP_INDEM = ('ipp_indem', src("L'indemnité parlementaire et les revenus des Français depuis 1914 (note n° 91)", "Institut des politiques publiques (Éric Buge, Étienne Ollion)", "avril 2023",
  "https://www.ipp.eu/wp-content/uploads/2023/04/Note_IPP_Buge_Ollion-91_compressed.pdf",
  "En 2020, le revenu tiré de l'indemnité représente 3,2 fois le salaire ouvrier moyen ; les députés se situent autour du 97e percentile des revenus, alors qu'ils étaient au seuil du 1 % le plus élevé de 1945 à la fin des années 1990.",
  "Étude d'un institut de recherche.", 'etude'))
PS_AFM = ('ps_afm', src("Affaire Dubost : quelles sont les indemnités des parlementaires ?", "Public Sénat (Juliette Bezat)", "3 mai 2022",
  "https://www.publicsenat.fr/actualites/non-classe/affaire-dubost-quelles-sont-les-indemnites-des-parlementaires-205253",
  "L'avance de frais de mandat a remplacé l'IRFM avec les lois « confiance » de 2017. Les dépenses sont contrôlées par échantillon, chaque parlementaire au moins une fois par mandat, et les sommes « indûment prises en charge » doivent être remboursées.",
  "Média parlementaire (2022).", 'media'))
CC_SYND = ('cc_synd', src("Une réforme inaboutie du dialogue social dans la fonction publique (rapport public thématique)", "Cour des comptes (hébergé par Vie publique)", "octobre 2024",
  "https://www.vie-publique.fr/files/rapport/pdf/295923.pdf",
  "Le fonds paritaire institué par la loi du 5 mars 2014 est alimenté par une contribution des employeurs de 0,016 % des rémunérations (environ 100 M€) et par une subvention de l'État de 32,6 M€ ; ses ressources atteignent 144 M€ en 2022. Le taux de syndicalisation est de 18,7 % chez les agents publics et de 8,1 % dans le privé (2019). Le coût total du dialogue social dans les trois fonctions publiques est estimé à plus de 874 M€ en 2022.",
  "Rapport de la juridiction financière."))
JDN_SYND = ('jdn_synd', src("Dialogue social : patronat et syndicats ont touché près de 157 millions d'euros en 2025", "Journal du Net (Adrien Bar Hiyé)", "29 octobre 2026",
  "https://www.journaldunet.com/business/1557335-le-patronat-et-les-syndicats-ont-touche-pres-de-157-millions-d-euros-en-2025/",
  "En 2025, le fonds paritaire (AGFPN) a versé un peu plus de 103 M€ aux syndicats de salariés et 53,6 M€ aux organisations patronales ; environ 122,5 M€ proviennent de la contribution de 0,016 % versée par les entreprises et 34,7 M€ de subventions de l'État. CFDT 23,7 M€, CGT 22 M€, FO 18,4 M€ ; Medef 15,7 M€.",
  "Média économique.", 'media'))
CFDT_RES = ('cfdt_res', src("Quels moyens financiers pour une organisation syndicale ?", "CFDT", "non daté",
  "https://www.cfdt.fr/portail/nous-connaitre/nos-comptes/quels-moyens-financiers-pour-les-organisations-syndicales-/quels-moyens-financiers-pour-une-organisation-syndicale-rec_67020",
  "La CFDT déclare « 76 % de ressources internes contre 24 % de ressources externes » ; la cotisation représente « au minimum 0,75% » de la rémunération nette et ouvre droit à « un crédit d'impôts de 66% » ; les comptes sont « certifiés sans réserve par les commissaires aux comptes ».",
  "Déclaration d'une organisation partie prenante (année non précisée).", 'secondaire'))
AN_PERRUCHOT = ('an_perruchot', src("Question écrite n° 125621 (Christian Vanneste) sur le rapport Perruchot", "Assemblée nationale", "27 décembre 2011",
  "https://www.assemblee-nationale.fr/dyn/13/questions/QANR5L13QE125621.pdf",
  "La question cite le rapport Perruchot, non publié après le rejet de ses conclusions par la commission d'enquête : selon ce rapport, les cotisations ne représenteraient que 4 % des budgets syndicaux et la collectivité verserait environ 4 milliards d'euros par an pour l'activité syndicale. La question a été retirée en juin 2012 sans réponse.",
  "Document parlementaire rapportant les affirmations d'un député."))
CE_CRECHE = ('ce_creche', src("Analyse de la décision n° 395122 (crèche de Noël, Melun)", "Conseil d'État", "9 novembre 2016",
  "https://www.conseil-etat.fr/fr/arianeweb/CE/analyse/2016-11-09/395122",
  "L'installation temporaire d'une crèche « n'est légalement possible que lorsqu'elle présente un caractère culturel, artistique ou festif », sans exprimer la reconnaissance d'un culte. Dans un bâtiment public siège d'une collectivité, elle ne le peut pas « en l'absence de circonstances particulières » ; à Melun, faute d'usage local et d'élément festif, la crèche « méconnaît l'article 28 de la loi du 9 décembre 1905 ».",
  "Analyse officielle d'une décision de la plus haute juridiction administrative."))
CE_CRECHE18 = ('ce_creche18', src("Installation d'une crèche de Noël", "Conseil d'État", "14 février 2018",
  "https://conseil-etat.fr/actualites/installation-d-une-creche-de-noel",
  "Pour la crèche installée par le conseil général de Vendée, la cour administrative d'appel de Nantes a rejeté la demande d'annulation et le Conseil d'État n'a pas admis le pourvoi. Les critères sont le contexte (sans prosélytisme), les conditions de l'installation, les usages locaux et le lieu ; sur les autres emplacements publics, l'installation est possible si elle ne constitue pas un acte de prosélytisme ou de revendication religieuse.",
  "Communiqué de la plus haute juridiction administrative."))
BDT_CRECHE = ('bdt_creche', src("Le Conseil d'État autorise, sous condition, les crèches de Noël en mairie", "Banque des Territoires (Localtis, avec AFP)", "10 novembre 2016",
  "https://www.banquedesterritoires.fr/le-conseil-detat-autorise-sous-condition-les-creches-de-noel-en-mairie",
  "Pour Melun, le Conseil d'État juge que la cour de Paris a interprété la neutralité de façon excessive, mais confirme l'interdiction faute d'« usage local » et d'« environnement artistique, culturel ou festif ». Sur les autres emplacements, comme les marchés de Noël, l'installation de santons est a priori licite.",
  "Média des collectivités (Caisse des dépôts).", 'secondaire'))
PS_C8 = ('ps_c8', src("Fin de C8 : pourquoi la décision de l'Arcom n'est pas de la censure ?", "Public Sénat (Simon Barbarit)", "28 février 2025",
  "https://www.publicsenat.fr/actualites/societe/fin-de-c8-pourquoi-la-decision-de-larcom-nest-pas-de-la-censure",
  "Par sa délibération du 17 juillet 2024, l'Arcom retient 15 projets sur 25 ; C8 et NRJ12 ne sont pas retenues. La loi de 1986 limite une autorisation à 10 ans, renouvelable une fois. C8 a fait l'objet de 36 alertes et sanctions selon un décompte de Libération et de plus de 7,6 M€ d'amendes liées à TPMP selon le HuffPost ; elle cesse d'émettre dans la nuit du 28 février 2025. Roch-Olivier Maistre : « Les fréquences sont un bien public, elles ont la particularité d'être attribuées gratuitement ».",
  "Média parlementaire.", 'media'))
LANDOT_C8 = ('landot_c8', src("Arcom / C8 : voici l'arrêt (Conseil d'État, 19 février 2025, n° 499823 et 500009)", "Blog Landot & associés (Éric Landot, avocat)", "20 février 2025",
  "https://blog.landot-avocats.net/2025/02/20/arcom-c8-c-voici-larret/",
  "Le Conseil d'État rappelle que l'Arcom procède à une « appréciation des mérites comparés des candidatures reçues », selon des critères dont la « contribution au pluralisme et à la diversité des opérateurs » et la « capacité à respecter les obligations légales ». Pour C8, il relève des programmes « peu diversifiés », de « nombreuses sanctions financières, mises en demeure et mises en garde » et « un déficit chronique et significatif » ; les recours sont rejetés.",
  "Commentaire d'avocat reproduisant l'arrêt.", 'secondaire'))
CE_CNEWS = ('ce_cnews', src("Pluralisme et indépendance de l'information : l'Arcom devra se prononcer à nouveau sur le respect par CNews de ses obligations", "Conseil d'État", "13 février 2024",
  "https://conseil-etat.fr/actualites/pluralisme-et-independance-de-l-information-l-arcom-devra-se-prononcer-a-nouveau-sur-le-respect-par-cnews-de-ses-obligations",
  "L'Arcom « ne doit pas se limiter au décompte des temps de parole des personnalités politiques » et doit considérer l'ensemble des intervenants, « y compris les chroniqueurs, animateurs et invités ». Le Conseil d'État « ne se prononce pas sur le respect par les programmes de la chaîne CNews » de ses obligations.",
  "Communiqué de la plus haute juridiction administrative."))
OZAP_C8 = ('ozap_c8', src("« Un montant excessif » : le Conseil d'État contredit l'Arcom et réduit de moitié une amende infligée à C8", "Puremédias (Benjamin Rabier)", "7 mai 2025",
  "https://www.ozap.com/actu/un-montant-excessif-le-conseil-detat-contredit-larcom-et-reduit-de-moitie-une-amende-infligee-a-c8-a-cause-de-cyril-hanouna-et-de-tpmp/649824",
  "Le 6 mai 2025, le Conseil d'État a réduit de 300 000 € à 150 000 € une amende infligée à C8 pour des propos tenus dans TPMP en octobre 2022, jugeant le premier montant « excessif ».",
  "Média spécialisé.", 'media'))
# ── Sources : justice et sécurité ──────────────────────────────────────────
AN_LD557 = ('an_ld557', src("Proposition de loi n° 557 visant à instituer une présomption de légitime défense pour les membres des forces de l'ordre (exposé des motifs)", "Assemblée nationale", "29 novembre 2022",
  "https://www.assemblee-nationale.fr/dyn/16/textes/l16b0557_proposition-loi.pdf",
  "L'exposé des motifs recopie l'article 122-5 du code pénal : « N'est pas pénalement responsable la personne qui, devant une atteinte injustifiée envers elle-même ou autrui, accomplit, dans le même temps, un acte commandé par la nécessité de la légitime défense […] sauf s'il y a disproportion entre les moyens de défense employés et la gravité de l'atteinte. » Pour défendre un bien, l'acte doit être « autre qu'un homicide volontaire » et « strictement nécessaire ». L'article 122-6 présume la légitime défense « pour repousser, de nuit, l'entrée par effraction, violence ou ruse dans un lieu habité ».",
  "Texte parlementaire reproduisant le code pénal."))
AN_LD2016 = ('an_ld2016', src("Question écrite n° 74957 « légitime défense » (Hervé Féron) et réponse du ministère de la Justice", "Assemblée nationale", "5 avril 2016",
  "https://questions.assemblee-nationale.fr/dyn/14/questions/QANR5L14QE74957.pdf",
  "« La légitime défense est une cause d'irresponsabilité pénale. » En principe, il incombe à la personne poursuivie de démontrer qu'elle a agi en état de légitime défense ; l'article 122-6 crée une présomption « ne cédant que face à la preuve contraire ».",
  "Réponse ministérielle publiée au Journal officiel (2016)."))
AN_LD691 = ('an_ld691', src("Document d'étape sur la proposition de loi n° 691 (présomption de légitime défense des forces de l'ordre)", "Assemblée nationale (Ian Boucard, rapporteur)", "14 janvier 2026",
  "https://www.assemblee-nationale.fr/dyn/dyn/contenu/visualisation/1099899/file/EAT%20-%20PPL%20n%C2%B0%20691%20pr%C3%A9somption%20l%C3%A9gitime%20d%C3%A9fense.pdf",
  "Le document recopie l'article 122-6 et rappelle que la présomption est « simple » ; il cite une jurisprudence où elle a été écartée (Cass. crim., 11 mai 1995) et un refus de la légitime défense pour riposte non proportionnée (Cass. crim., 26 juin 2012). Il ne recense pas de statistique nationale sur ces affaires.",
  "Document parlementaire."))
CDJ_LD = ('cdj_ld', src("Présomption de légitime défense des forces de l'ordre : l'Assemblée nationale adopte le texte", "Le Club des juristes", "8 juillet 2026",
  "https://www.leclubdesjuristes.com/?p=16847",
  "Le texte, adopté le 7 juillet 2026, « doit maintenant être examiné par le Sénat » ; une pétition contre lui a recueilli plus de 370 000 signatures. Le ministre de l'Intérieur affirme qu'il « ne crée aucune irresponsabilité pénale ».",
  "Revue juridique.", 'secondaire'))
MJ_PDM07 = ('mj_pdm07', src("[Archives] Interdiction de la peine de mort (discours au Sénat)", "Ministère de la Justice", "7 février 2007",
  "https://www.justice.gouv.fr/node/1920",
  "La loi du 9 octobre 1981 a permis à la France de ratifier en 1986 le protocole n° 6, qui « permet néanmoins le rétablissement de la peine de mort pour des actes commis en temps de guerre ». Selon le Conseil constitutionnel (13 octobre 2005), le deuxième protocole facultatif au Pacte international relatif aux droits civils et politiques « ne comporte pas de clause de dénonciation » et « prescrit une abolition définitive ».",
  "Discours officiel archivé."))
MJ_PDM_SCEL = ('mj_pdm_scel', src("[Archives] Scellement de la loi constitutionnelle du 23 février 2007", "Ministère de la Justice", "28 mars 2007",
  "https://www.justice.gouv.fr/node/1952",
  "L'article 66-1 de la Constitution dispose : « Nul ne peut être condamné à la peine de mort ». La France « peut désormais ratifier » le protocole n° 13 (abolition en toutes circonstances) et le deuxième protocole facultatif.",
  "Communiqué officiel archivé."))
NRC_PDM = ('nrc_pdm', src("Deterrence and the Death Penalty (notice NCJ 238584)", "National Research Council, États-Unis (dir. Daniel Nagin, John Pepper) — notice du National Institute of Justice", "2012",
  "https://nij.ojp.gov/library/publications/deterrence-and-death-penalty",
  "« the research to date is not useful in determining the deterrent effect of the death penalty on homicide rates » : les études existantes ne permettent pas d'établir un effet dissuasif sur les homicides, notamment parce qu'elles « have not accounted for the possible effect of noncapital punishments ».",
  "Rapport de l'Académie des sciences américaine.", 'etude'))
DPIC = ('dpic', src("Murder Rate of Death Penalty States Compared to Non-Death Penalty States", "Death Penalty Information Center", "mis à jour le 14 mars 2025",
  "https://deathpenaltyinfo.org/facts-and-research/murder-rates/murder-rate-of-death-penalty-states-compared-to-non-death-penalty-states",
  "D'après les données du FBI, en 1999, le taux d'homicide était de 5,5 pour 100 000 habitants dans les États pratiquant la peine de mort, contre 3,6 dans les autres ; le taux des États sans peine de mort reste « consistently lower ».",
  "Organisation spécialisée, critique de la peine de mort.", 'secondaire'))
IM_FRACT = ('im_fract', src("Fractures françaises 2025 : d'une crise à l'autre", "Institut Montaigne (enquête Ipsos BVA / Sopra Steria pour Le Monde, Cevipof, Fondation Jean-Jaurès)", "octobre 2025",
  "https://institutmontaigne.org/publications/fractures-francaises-2025-la-societe-face-la-crise",
  "« 52 % (54 % des 18-24 ans) des personnes interrogées estiment qu'il faudrait rétablir la peine de mort en France », soit une progression d'un point sur un an.",
  "Enquête d'opinion annuelle.", 'etude'))
MJ_PP = ('mj_pp', src("Peines planchers : application et impact de la loi du 10 août 2007 (Infostat Justice n° 118)", "Ministère de la Justice (F. Leturcq)", "octobre 2012",
  "https://www.justice.gouv.fr/sites/default/files/migrations/portail/art_pix/stat_infostat_118_20121017.pdf",
  "En 2010, 10 122 peines planchers ont été prononcées sur 26 335 condamnations éligibles, soit 38 %. Pour les délits commis par des majeurs récidivistes, la part des peines au moins égales au minimum passe de 8,4 % (2004-2006) à 40,7 % (2008-2010) ; la durée moyenne d'emprisonnement passe de 9 à 15,6 mois.",
  "Statistique publique (données 2004-2010)."))
IPP_PP = ('ipp_pp', src("Les peines planchers sont-elles un outil efficace pour éviter la récidive ? (note n° 105)", "Institut des politiques publiques (Aurélie Ouss, Arnaud Philippe)", "mars 2024",
  "https://www.ipp.eu/wp-content/uploads/2024/03/Note_IPP_105_peines_planchers.pdf",
  "« À court terme, on n'observe pas de diminution de la récidive. » À moyen terme, la probabilité de commettre une infraction relevant du même régime baisse d'environ 10 %, sans changement pour les autres infractions ; les auteurs concluent à un « faible effet dissuasif global ». Le ministère estimait l'effet de la loi à environ 4 000 détenus de plus, pour un coût d'environ 146 M€ par an.",
  "Étude universitaire.", 'etude'))
AN_PP25 = ('an_pp25', src("Compte rendu n° 80 de la commission des lois (proposition de loi n° 1410 sur les peines planchers)", "Assemblée nationale", "16 juin 2025",
  "https://questions.assemblee-nationale.fr/dyn/17/comptes-rendus/cion_lois/l17cion_lois2425080_compte-rendu.pdf",
  "La commission adopte la proposition de loi instaurant des peines planchers pour les crimes et délits contre les forces de l'ordre et les pompiers ; la rapporteure cite l'étude de l'IPP (« les personnes plus sévèrement condamnées en application d'une peine plancher avaient moins récidivé »), d'autres députés le « faible effet dissuasif » relevé par la même étude.",
  "Compte rendu parlementaire."))
GEND_RO = ('gend_ro', src("Légère baisse des refus d'obtempérer routiers enregistrés entre 2016 et 2023", "Gendarmerie nationale (Gendinfo, d'après le SSMSI)", "19 avril 2024",
  "https://www.gendarmerie.interieur.gouv.fr/gendinfo/actualites/2024/legere-baisse-des-refus-d-obtemperer-routiers-enregistres-entre-2016-et-2023",
  "En moyenne 25 700 refus d'obtempérer routiers sont constatés chaque année entre 2016 et 2023, en baisse de 5 % sur la période (hausse jusqu'en 2021, puis baisse). La part des refus aggravés passe de 16 % en 2016 à 21 % en 2023 ; dans neuf cas sur dix, ils mettent en danger d'autres usagers.",
  "Publication officielle reprenant le service statistique du ministère de l'Intérieur."))
AN_RO = ('an_ro', src("Rapport d'information n° 2692 sur les refus d'obtempérer et dossier de presse", "Assemblée nationale, commission des lois (Thomas Rudigoz, Roger Vicot)", "29 mai 2024",
  "https://www.assemblee-nationale.fr/dyn/16/rapports/cion_lois/l16b2692_rapport-information.pdf",
  "La loi du 24 janvier 2022 a porté la peine du refus simple d'« un an d'emprisonnement et 7 500 euros » à « deux ans d'emprisonnement et 15 000 euros » ; le refus aggravé est puni jusqu'à sept ans et 100 000 € quand des forces de l'ordre sont exposées. 18 092 affaires ont été poursuivies en 2022, dont plus de 62 % en procédure accélérée. Entre 2012 et 2022, refus simples +33,7 % et refus aggravés +94,6 % ; la mission écarte le laxisme judiciaire comme cause.",
  "Rapport parlementaire transpartisan."))
LCP_RO = ('lcp_ro', src("Tirs lors de refus d'obtempérer : la mission d'information ne se prononce pas sur les effets de la loi de 2017", "LCP (Maxence Kagni)", "29 mai 2024",
  "https://lcp.fr/actualites/tirs-lors-de-refus-d-obtemperer-la-mission-d-information-ne-se-prononce-pas-sur-les",
  "Les refus simples passent de 19 174 à 25 641 et les refus aggravés de 2 520 à 4 905 entre 2012 et 2022. Les tirs sur des véhicules passent « de 116 tirs à 205 tirs » de 2012 à 2017, puis « de 205 tirs à 140 tirs » en 2022.",
  "Média parlementaire.", 'media'))
PS_RO = ('ps_ro', src("Nanterre : que dit la loi sur le refus d'obtempérer ?", "Public Sénat (Simon Barbarit)", "28 juin 2023",
  "https://www.publicsenat.fr/actualites/politique/nanterre-que-dit-la-loi-sur-le-refus-dobtemperer",
  "En 2022, « 13 personnes ont été tuées par la police » lors de refus d'obtempérer. L'article L435-1 du code de la sécurité intérieure autorise le tir sur un véhicule dont le conducteur « n'obtempère pas », sous condition d'absolue nécessité et de proportionnalité.",
  "Média parlementaire.", 'media'))
IGPN24 = ('igpn24', src("Rapport annuel 2024 de l'Inspection générale de la police nationale", "IGPN (hébergé par Vie publique)", "2025",
  "https://www.vie-publique.fr/files/rapport/pdf/300479.pdf",
  "« L'IGPN a été saisie de 914 enquêtes judiciaires en 2024 » (943 en 2023), dont 428 portent sur l'usage de la force (45 %). Le manquement d'« usage disproportionné de la force » a été retenu contre 37 agents dans 21 enquêtes administratives. Dans 12 procédures relatives à des tirs, la justice a conclu à la légitimité de l'usage de l'arme.",
  "Rapport d'une inspection officielle."))
MI_QE8872 = ('mi_qe8872', src("Question écrite n° 8872 et réponse du ministère de l'Intérieur", "Assemblée nationale", "16 décembre 2025",
  "https://www.assemblee-nationale.fr/dyn/17/questions/QANR5L17QE8872.pdf",
  "En 2024, 115 décès ou blessures graves ont été déclarés lors de missions de police ou de gendarmerie, dont 47 personnes décédées (36 en 2023) et 68 gravement blessées ; 1 063 signalements à l'IGPN portent sur des violences. La même année, 5 463 gendarmes ont subi des agressions physiques, « dont 2428 avec arme ».",
  "Réponse ministérielle publiée au Journal officiel."))
DDD_CTRL = ('ddd_ctrl', src("Relations police/population : contrôles d'identité et dépôts de plainte (enquête Accès aux droits 2024)", "Défenseur des droits", "juin 2025",
  "https://www.defenseurdesdroits.fr/sites/default/files/2025-06/DDD-EAD-2024_volume1_DP.pdf",
  "26 % des personnes ont été contrôlées au moins une fois en cinq ans (16 % en 2016). Les jeunes hommes perçus comme noirs, arabes ou maghrébins ont « 4 fois plus de risque » d'être contrôlés et 12 fois plus de subir un contrôle poussé. « Près d'1 personne contrôlée sur 5 déclare avoir été tutoyée, provoquée, insultée ou brutalisée. » Échantillon : 5 030 personnes.",
  "Enquête d'une autorité administrative indépendante."))
CDJ_FRAISSE = ('cdj_fraisse', src("Mort de Rémi Fraisse : la CEDH condamne la France pour violation du droit à la vie", "Le Club des juristes", "27 février 2025",
  "https://www.leclubdesjuristes.com/en-bref/mort-de-remi-fraisse-la-cedh-condamne-la-france-pour-violation-du-droit-a-la-vie-9512/",
  "Dans l'arrêt Fraisse et autres c. France du 27 février 2025, la Cour européenne des droits de l'homme constate une violation du droit à la vie dans son volet matériel : Rémi Fraisse est décédé de l'explosion d'une grenade OF-F1, une arme de dispersion à effet de souffle utilisée lors d'une opération de maintien de l'ordre, et la Cour juge que le cadre réglementaire de son usage n'était ni complet ni suffisamment précis. Pas de violation du volet procédural ; 37 600 € sont alloués à la famille.",
  "Revue juridique commentant un arrêt de la CEDH.", 'secondaire'))
# ── Sources : économie, travail, énergie ───────────────────────────────────
COR_CAPI = ('cor_capi', src("Répartition, réserves et capitalisation : quels enjeux pour les retraites ? (dossier « en bref », séance du 18 décembre 2025)", "Conseil d'orientation des retraites", "18 décembre 2025",
  "https://www.cor-retraites.fr/sites/default/files/2025-12/Dossier%20en%20bref_18.12.2025.pdf",
  "La répartition offre « un rendement en moyenne égal à la croissance de l'économie ». La capitalisation dépend des marchés : le rendement du capital dépasse souvent la croissance à long terme, mais l'assuré reste exposé aux fluctuations et aux frais, avec un « risque de fortes pertes en cas de crise ». Une transition suppose une double cotisation des actifs, une mise à contribution des retraités ou une prise en charge par l'État.",
  "Organisme public d'expertise sur les retraites."))
COR_LAVIGNE = ('cor_lavigne', src("Financer les retraites par capitalisation : pourquoi pas, mais avec quel capital ?", "Anne Lavigne (université d'Orléans), groupe de travail du COR", "11 décembre 2025",
  "https://www.cor-retraites.fr/sites/default/files/2026-01/1.2025_12_11_GT_COR_Lavigne.pdf",
  "Sur 1950-2015, dans 16 pays, l'écart moyen entre rendement financier et croissance est de 2,68 %. « La mutualisation des risques financiers dans la capitalisation individuelle n'existe pas. » « La question de la transition ne peut être résolue sans un fonds d'amorçage. » « La capitalisation n'est pas la réponse à court terme, mais une réponse possible à long terme. »",
  "Contribution universitaire présentée au COR.", 'etude'))
COR_OCDE = ('cor_ocde', src("Montée en charge de la retraite par capitalisation : expérience de certains pays de l'OCDE", "Stéphanie Payet, Hervé Boulhol (OCDE), présentation au COR", "12 novembre 2025",
  "https://www.cor-retraites.fr/sites/default/files/2025-11/COR_Transition%20capitalisation_12-11-2025.pdf",
  "Au Chili (réforme de 1981), l'État a financé le déficit lié à la transition à hauteur d'environ « 3,25 % du PIB / an en moyenne » ; le système a dû être complété par une pension solidaire (2008) puis une pension universelle garantie (2022). La Hongrie a fait marche arrière en 2011. En France en 2023, 28 % des 15-64 ans participent à un plan d'épargne retraite collectif et 15 % à un plan individuel.",
  "Présentation d'experts de l'OCDE au COR.", 'etude'))
DF_OCDE08 = ('df_ocde08', src("OCDE: fondos de pensiones cayeron 23% en 2008 por crisis", "Diario Financiero (Chili), d'après un rapport de l'OCDE", "23 juin 2009",
  "https://www.df.cl/internacional/ocde-fondos-de-pensiones-cayeron-23-en-2008-por-crisis",
  "Les fonds de pension privés des pays de l'OCDE ont perdu en moyenne 23 % de leur valeur en 2008 (−37,5 % en Irlande, −26,2 % aux États-Unis). Une responsable de l'OCDE déclare qu'il faut « des systèmes publics qui offrent un revenu de base » (« Hacen falta sistemas públicos que ofrezcan un ingreso de base »).",
  "Média économique (2009) reprenant l'OCDE.", 'media'))
CDE_CARB = ('cde_carb', src("Carburants : prix de l'essence et du gazole en France", "Connaissance des Énergies (d'après la DGEC et l'UFIP Énergies & Mobilités)", "3 novembre 2026",
  "https://www.connaissancedesenergies.org/fiche-pedagogique/structuration-des-prix-de-l-essence-et-du-gazole-france",
  "Semaine du 30 octobre 2026 : gazole à 2,371 €/L, dont accise 0,608 €, TVA 0,395 € et cotation Rotterdam 1,126 € (47,5 %) ; SP95-E10 à 2,095 €/L, dont accise 0,670 €, TVA 0,349 € et cotation 0,795 € (37,9 %). Les taxes pèsent 42,3 % du prix du gazole et environ 48,6 % de celui du SP95-E10 ; la marge nette du distributeur est estimée à 1 ou 2 centimes par litre.",
  "Site de vulgarisation reprenant les données officielles.", 'secondaire'))
AN_CARB = ('an_carb', src("Question écrite n° 5303 et réponse du ministère chargé de l'Énergie", "Assemblée nationale", "20 mai 2025",
  "https://www.assemblee-nationale.fr/dyn/17/questions/QANR5L17QE5303.pdf",
  "« Ces deux taxes ont représenté en moyenne 54 % du prix TTC du gazole et du sp95-e10 en France en 2024. » Le raffinage représente environ 7 % du prix et le transport-distribution 14 % en moyenne ; l'accise est « gelée depuis le 1er janvier 2019 ».",
  "Réponse ministérielle publiée au Journal officiel."))
CDE_UE = ('cde_ue', src("Carburants : quel prix sur la route des vacances dans les 27 pays de l'UE ?", "Connaissance des Énergies (Maël Dancette, d'après le Weekly Oil Bulletin de la Commission européenne)", "28 juillet 2026",
  "https://www.connaissancedesenergies.org/carburants-quel-prix-route-des-vacances-pays-ue",
  "Au 20 juillet 2026, la France est la 5e plus chère de l'UE pour l'essence (2,010 €/L, 51 % de taxes) et le gazole (2,066 €/L, 46 % de taxes). Part des taxes sur l'essence : Allemagne 53 %, Italie 53 %, Pays-Bas 54 %, Espagne 38 %.",
  "Site de vulgarisation reprenant les données de la Commission.", 'secondaire'))
BDF_CARB = ('bdf_carb', src("Quelle transmission des prix du pétrole aux prix des carburants ? (bloc-notes éco n° 233)", "Banque de France (Erwan Gautier, Magali Marx, Paul Vertier)", "14 octobre 2021",
  "https://www.banque-france.fr/fr/publications-et-statistiques/publications/quelle-transmission-des-prix-du-petrole-aux-prix-des-carburants",
  "En septembre 2021, le gazole valait 1,45 € TTC, dont 0,61 € de TICPE et 0,24 € de TVA. Une hausse de 1 % du prix du gazole raffiné importé fait monter à long terme le prix TTC de 0,3 % : comme la taxe est fixe par litre, la part des taxes baisse quand le pétrole monte.",
  "Publication de la banque centrale (2021)."))
AN_35H = ('an_35h', src("Rapport de la commission d'enquête sur l'impact de la réduction progressive du temps de travail (n° 2436)", "Assemblée nationale (Thierry Benoit, président ; Barbara Romagnan, rapporteure)", "9 décembre 2014",
  "https://www.assemblee-nationale.fr/14/pdf/rap-enq/r2436.pdf",
  "Sur les emplois créés : « Le chiffre de 350 000 est le plus communément admis. » Le coût net ex post pour les finances publiques est d'environ 2,5 Md€ par an ; « Les 35 heures ont amélioré la productivité horaire industrielle ». Le rapport relève « les fortes tensions dans la fonction publique hospitalière ». Le président de la commission indique : « je ne partage pas les conclusions de son rapport ».",
  "Rapport parlementaire (2014)."))
IRES_35H = ('ires_35h', src("Effets des 35 heures sur l'emploi — retour sur les évaluations", "Frédéric Lerais (Ires), audition à l'Assemblée nationale", "2 octobre 2014",
  "https://ires.fr/wp-content/uploads/2023/02/Effets_des_35_heures_octobre_2014_final.pdf",
  "Effet estimé à « 350 000 emplois à court terme » sur 1996-2002, « très inférieur aux estimations ex-ante » ; pour les entreprises, le coût est jugé « à peu près neutre » grâce à la modération salariale et aux gains de productivité.",
  "Institut de recherche lié aux syndicats.", 'etude'))
IM_35H = ('im_35h', src("Les 35 heures : efficaces et peu coûteuses ? Notre réaction en quatre points", "Institut Montaigne", "17 décembre 2014",
  "https://institutmontaigne.org/expressions/les-35-heures-efficaces-et-peu-couteuses-notre-reaction-en-quatre-points",
  "Selon le Conseil d'analyse économique, « le coût total de l'application des 35 heures dans le secteur privé est estimé à 12 Mds€ par an », surtout en allègements de cotisations ; le CAE (2007) juge l'effet de la baisse de la durée légale « au mieux très marginal ».",
  "Réaction d'un think tank libéral.", 'secondaire'))
INSEE_DUREE = ('insee_duree', src("Durée du travail (Emploi, chômage, revenus du travail, édition 2026)", "Insee (Insee Références)", "2 juillet 2026",
  "https://www.insee.fr/fr/statistiques/8733071",
  "En 2025, « la durée habituelle hebdomadaire du travail des salariés à temps complet est de 38,9 heures » ; la durée annuelle effective de travail des salariés à temps complet est de 1 656 heures en moyenne.",
  "Statistique publique."))
SENAT_ELEC = ('senat_elec', src("Avis politique sur la réforme du marché de l'électricité de l'Union", "Sénat, commission des affaires européennes", "1er juin 2023",
  "https://www.senat.fr/fileadmin/Commissions/Affaires_europeennes/Fichiers/Avis_politiques/Avis_politique_reforme_du_marche_de_l_electricite.pdf",
  "« les prix sur le marché de gros de l'électricité sont déterminés par le coût de production de la dernière centrale appelée », souvent au gaz ou au charbon. La crise « a révélé les faiblesses du fonctionnement actuel du marché européen » ; le Sénat regrette que la réforme conserve le prix marginal et défend les contrats de long terme et les tarifs réglementés.",
  "Avis d'une commission parlementaire."))
SDES_ELEC22 = ('sdes_elec22', src("Prix de l'électricité en France et dans l'Union européenne en 2022", "SDES (ministère de la Transition écologique)", "août 2023",
  "https://www.ecologie.gouv.fr/sites/default/files/DE_4p_prixelectricite_aout2023_V5.pdf",
  "Le prix spot moyen atteint 279 €/MWh en 2022, multiplié par 2,6 en un an. L'ARENH permettait d'acheter du nucléaire « au prix de 42 €/MWh » ; le bouclier a limité la hausse du tarif réglementé « à 4 % en moyenne au 1er février 2022 ». Les ménages français ont payé des prix « inférieurs de 22 % à ceux pratiqués dans l'UE ».",
  "Statistique publique (2022)."))
SDES_ELEC25 = ('sdes_elec25', src("Prix de l'électricité en France et dans l'Union européenne en 2025", "SDES (ministère de la Transition écologique)", "23 juillet 2026",
  "https://www.statistiques.developpement-durable.gouv.fr/prix-de-lelectricite-en-france-et-dans-lunion-europeenne-en-2025",
  "Le prix moyen pour les ménages est de 254,6 €/MWh TTC en 2025 (−9,0 % sur un an), 13 % sous la moyenne européenne ; les taxes augmentent de 16,5 % « avec la fin du bouclier tarifaire ». Pour les entreprises : 148,8 €/MWh hors TVA, 16 % sous la moyenne de l'UE.",
  "Statistique publique."))
CRE_2026 = ('cre_2026', src("Communiqués sur les tarifs réglementés (20 janvier 2026) et sur la surveillance des marchés de gros (25 juin 2026)", "Commission de régulation de l'énergie", "20 janvier et 25 juin 2026",
  "https://www.cre.fr/fileadmin/Documents/Communiques_de_presse/2026/260625_CP_Rapport_surveillance_marches_de_gros.pdf",
  "Les tarifs réglementés sont restés « stables, au 1er février 2026 (-0,83% TTC) », l'approvisionnement étant calculé « à 100% à un coût représentatif des prix de marchés de gros » en raison de la fin de l'ARENH le 31 décembre 2025. Le prix spot français est de 61 €/MWh en 2025 (97 en 2023), avec des exportations nettes record de 92,3 TWh ; la France est « parmi les marchés de gros d'électricité avec les prix les moins chers ».",
  "Régulateur public de l'énergie."))
OI_QPV = ('oi_qpv', src("Le sur-chômage des quartiers prioritaires", "Observatoire des inégalités (d'après l'ONPV)", "21 mai 2025",
  "https://inegalites.fr/Chomage-QPV",
  "En 2022, le taux de chômage est de 18,3 % dans les quartiers prioritaires contre 7,5 % dans les autres quartiers des mêmes villes. Pour les actifs de moins de 30 ans : 25,6 % contre 13,5 % ; à bac+2 et plus : 11,1 % contre 5 %. Le chômage en QPV est passé de 25 % en 2014 à 18,3 % en 2022.",
  "Association d'information reprenant les données publiques.", 'secondaire'))
BDT_QPV = ('bdt_qpv', src("Dans les quartiers prioritaires, seule une personne sur deux en âge de travailler est en emploi", "Banque des Territoires (Localtis, Catherine Abou El Khair), d'après l'ONPV", "21 juillet 2026",
  "https://www.banquedesterritoires.fr/dans-les-quartiers-prioritaires-seule-une-personne-sur-deux-en-age-de-travailler-est-en-emploi",
  "En 2024, « 49,8% des 15-64 ans sont en emploi » en QPV, contre 70 % dans les unités urbaines englobantes ; 40,2 % sont inactifs contre 24,3 %. « 18,3% des personnes en QPV souhaitent pourtant travailler. » « 21,8% des jeunes résidant en QPV sont ni en études, ni en emploi, ni en formation », contre 11,2 % ailleurs ; l'inactivité touche d'abord les femmes.",
  "Média des collectivités reprenant l'Observatoire national de la politique de la ville.", 'secondaire'))
INSEE_TESTING = ('insee_testing', src("Discriminations dans l'accès à l'emploi : les effets croisés du genre, de l'origine et de l'adresse (Économie et Statistique n° 541)", "Insee (Sylvain Chareyron, Yannick L'Horty, Pascale Petit)", "2023",
  "https://www.insee.fr/fr/statistiques/fichier/7677719/01_ES541_Chareyron-et-al_FR.pdf",
  "Testing auprès de 3 000 entreprises de la métropole lilloise (fin 2021) : le candidat d'origine maghrébine reçoit 27 % de réponses positives en moins. Les hommes ne sont discriminés selon leur origine que lorsqu'ils résident en quartier prioritaire (2,60 % de réponses positives contre 4,80 %) ; pour les candidats d'origine française, résider en QPV n'est pas pénalisant.",
  "Revue scientifique de la statistique publique.", 'etude'))
# ── Sources : logement, migrations, climat, religion, histoire, retraités ──
INSEE_SDF = ('insee_sdf', src("L'hébergement des sans-domicile en 2012 (Insee Première n° 1455)", "Insee-Ined", "juillet 2013",
  "https://insee.fr/fr/statistiques/fichier/version-html/1281324/ip1455.pdf",
  "« 141 500 personnes étaient sans domicile en France métropolitaine début 2012 », « soit une progression de près de 50 % depuis 2001 ». « La part des étrangers parmi les sans-domicile est ainsi passée de 38 % en 2001 à 53 % en 2012. » « 12 % des sans-domicile sont hébergés en hôtel. »",
  "Statistique publique (enquête de 2012)."))
PS_MALLOG = ('ps_mallog', src("Le mal-logement : l'alerte des associations", "Public Sénat (Emma Bador-Fritche)", "3 février 2026",
  "https://www.publicsenat.fr/actualites/societe/le-mal-logement-lalerte-relancee-a-la-veille-des-elections-municipales",
  "Le 31e rapport annuel de la Fondation pour le logement des défavorisés compte « environ 350 000 » personnes sans domicile ou hébergées en structures d'urgence, dont « 40 000 » à la rue, et « 4,2 millions de personnes » sans logement ou mal logées ; il signale « plus de 900 » décès de personnes sans abri en 2025.",
  "Média parlementaire.", 'media'))
FAS_ENFANTS = ('fas_enfants', src("Baromètre « Enfants à la rue » 2025 (synthèse)", "Unicef France et Fédération des acteurs de la solidarité", "août 2025",
  "https://www.federationsolidarite.org/wp-content/uploads/2025/08/Barometre-enfants-a-la-rue-2025-Synthese.pdf",
  "La nuit du 18 août 2025, « au moins 2 159 enfants » sont restés sans solution après un appel au 115, dont 503 de moins de trois ans, soit « + 6 % par rapport à l'année dernière et + 30 % par rapport à 2022 ».",
  "Enquête associative.", 'etude'))
CE_HEBERG = ('ce_heberg', src("Hébergement d'urgence des personnes sans-abri (ordonnance n° 356456)", "Conseil d'État", "10 février 2012",
  "https://www.conseil-etat.fr/site/actualites/hebergement-d-urgence-des-personnes-sans-abri",
  "L'article L. 345-2-2 du code de l'action sociale et des familles dispose : « Toute personne sans abri en situation de détresse médicale, psychique et sociale a accès, à tout moment, à un dispositif d'hébergement d'urgence » ; le droit à l'hébergement d'urgence est une liberté fondamentale. Le requérant était un ressortissant ivoirien, et la décision ne pose aucune condition de nationalité.",
  "Communiqué de la plus haute juridiction administrative (2012)."))
SENAT_P177 = ('senat_p177', src("Avis sur le projet de loi de finances 2025, programme 177 « Hébergement, parcours vers le logement et insertion des personnes vulnérables »", "Sénat (Nadia Sollogoub, rapporteure)", "4 décembre 2024",
  "https://conferenceconsensuslogement.senat.fr/rap/a24-147-2/a24-147-2-syn.pdf",
  "« 203 000 places ouvertes » d'hébergement généraliste en moyenne annuelle et 2,93 Md€ de crédits ; les crédits de l'hébergement d'urgence baissent de 25 % ; l'avis relève une sous-budgétisation chronique d'environ 250 M€.",
  "Avis budgétaire parlementaire."))
BM_GROUND = ('bm_ground', src("D'ici à 2050, le changement climatique risque de contraindre 216 millions de personnes à migrer à l'intérieur de leur pays (rapport Groundswell)", "Banque mondiale", "13 septembre 2021",
  "https://www.banquemondiale.org/fr/news/press-release/2021/09/13/climate-change-could-force-216-million-people-to-migrate-within-their-own-countries-by-2050",
  "Le changement climatique pourrait contraindre « quelque 216 millions de personnes dans le monde en développement à migrer à l'intérieur de leur pays » d'ici 2050 : jusqu'à 86 millions en Afrique subsaharienne, 49 en Asie de l'Est-Pacifique, 40 en Asie du Sud, 19 en Afrique du Nord, 17 en Amérique latine, 5 en Europe de l'Est-Asie centrale. Une réduction allant jusqu'à 80 % est possible avec une action rapide de réduction des émissions.",
  "Institution internationale."))
IDMC26 = ('idmc26', src("Rapport mondial sur le déplacement interne 2026 (synthèse)", "Observatoire des situations de déplacement interne (IDMC)", "2026",
  "https://api.internal-displacement.org/sites/default/files/publications/documents/2026-idmc-grid-2026-global-report-on-internal-displacement-summary-report-french.pdf",
  "82,2 millions de déplacés internes fin 2025, « première baisse enregistrée en dix ans » ; 29,9 millions de déplacements liés aux catastrophes en 2025 (−35 % sur un an) ; 13,6 millions de personnes vivaient en déplacement lié à une catastrophe fin 2025.",
  "Organisme de référence sur les déplacements."))
HCR_FIG = ('hcr_fig', src("Figures at a glance", "Haut-Commissariat des Nations unies pour les réfugiés (HCR)", "mis à jour le 4 novembre 2025",
  "https://www.unhcr.org/about-unhcr/who-we-are/figures-glance",
  "Mi-2025, « 117.3 million people had been forced to flee », dont 67,8 millions à l'intérieur de leur pays ; « 66 per cent » des réfugiés sont accueillis dans des pays voisins et les pays à revenu faible ou intermédiaire accueillent 71 % des réfugiés du monde.",
  "Agence des Nations unies."))
EN_IDMC25 = ('en_idmc25', src("'Where conflict, poverty and climate collide': Number of internally displaced people tops 80 million", "Euronews (Lottie Limb)", "15 mai 2025",
  "https://www.euronews.com/2025/05/15/where-conflict-poverty-and-climate-collide-number-of-internally-displaced-people-tops-80-m",
  "Selon l'IDMC, 45,8 millions de déplacements liés aux catastrophes ont été enregistrés en 2024, un record ; ces chiffres comptent des mouvements, dont des évacuations, et non des personnes. Les États-Unis en comptent 11 millions.",
  "Média européen.", 'media'))
GCP25 = ('gcp25', src("Global carbon dioxide emissions from fossil fuels rise in 2025", "CSIRO / Global Carbon Project", "13 novembre 2025",
  "https://www.csiro.au/en/news/All/News/2025/November/Global-Carbon-Budget-2025",
  "Les émissions fossiles sont « projected to rise by 1.1 per cent in 2025, reaching 42.2 billion tonnes » ; la Chine représente 32 % des émissions mondiales, les États-Unis 13 %, l'Inde 8 % et l'Union européenne 6 %.",
  "Consortium scientifique de référence."))
GCP_KEY = ('gcp_key', src("Key Targets 2025", "Global Carbon Budget", "janvier 2026",
  "https://globalcarbonbudget.org/key-targets-2025",
  "« China's emissions in 2025 are projected to increase by 0.4% ». Au cours de la dernière décennie, 35 pays ont nettement réduit leurs émissions fossiles tout en faisant croître leur économie ; ils représentent environ 27 % des émissions mondiales.",
  "Consortium scientifique de référence."))
SDES_EMP = ('sdes_emp', src("Empreinte carbone et émissions territoriales (Chiffres clés du climat, édition 2026)", "SDES (ministère de la Transition écologique)", "2026",
  "https://www.statistiques.developpement-durable.gouv.fr/edition-numerique/chiffres-cles-du-climat/fr/18-empreinte-carbone-et-emissions-territoriales",
  "L'empreinte carbone d'un Français est estimée à 8,3 t CO2 éq en 2025 (provisoire), en baisse de 32 % depuis 1990 ; elle est supérieure à la moyenne mondiale (6,4 t), légèrement inférieure à celle de l'UE (9,0 t) et à celle de la Chine. 52 % de l'empreinte provient d'émissions importées.",
  "Statistique publique."))
CB_CUMUL = ('cb_cumul', src("Analysis: China's emissions have now caused more global warming than EU", "Carbon Brief (Simon Evans, Verner Viisainen)", "19 novembre 2024",
  "https://www.carbonbrief.org/analysis-chinas-emissions-have-now-caused-more-global-warming-than-eu",
  "« China's historical emissions reached 312GtCO2 in 2023, overtaking the EU's 303GtCO2 », loin derrière les 532 Gt des États-Unis. Par habitant, le cumul est de 227 t de CO2 en Chine, 682 t dans l'UE à 27 et 1 570 t aux États-Unis.",
  "Média scientifique spécialisé.", 'etude'))
OWID_FR = ('owid_fr', src("France: CO₂ and Greenhouse Gas Emissions Country Profile", "Our World in Data (Hannah Ritchie, Pablo Rosado)", "19 décembre 2025",
  "https://ourworldindata.org/profile/co2/france",
  "« France emitted 0.68% of the world's CO2 emissions in 2024 », soit 3,97 t de CO2 par habitant ; la France représente 2,17 % des émissions cumulées depuis 1751.",
  "Base de données universitaire (Oxford).", 'etude'))
PEW_MUS = ('pew_mus', src("Europe's Muslim population will continue to grow – but how much depends on migration", "Pew Research Center (Michael Lipka)", "4 décembre 2017",
  "https://www.pewresearch.org/short-reads/2017/12/04/europes-muslim-population-will-continue-to-grow-but-how-much-depends-on-migration/",
  "En 2016, les musulmans représentaient 4,9 % de la population européenne ; la France comptait 5,7 millions de musulmans, soit 8,8 % de sa population. Sans aucune immigration, la France atteindrait 12,7 % en 2050. Les musulmanes ont en moyenne 2,6 enfants par femme, contre 1,6 pour les non-musulmanes.",
  "Centre de recherche américain (2017).", 'etude'))
INSEE_RELIG = ('insee_relig', src("La diversité religieuse en France : transmissions intergénérationnelles et pratiques selon les origines", "Insee (Insee Références ; Louis Drouhot, Patrick Simon, Vincent Tiberj — enquête TeO2)", "30 mars 2023",
  "https://www.insee.fr/fr/statistiques/6793308",
  "En 2019-2020, parmi les 18-59 ans de France métropolitaine, 51 % se déclarent sans religion, 29 % catholiques et 10 % musulmans ; les musulmans représentent 44 % des immigrés et 1 % de la population sans ascendance migratoire.",
  "Statistique publique."))
INSEE_FECOND = ('insee_fecond', src("Fécondité (Immigrés et descendants d'immigrés en France, édition 2023)", "Insee (Insee Références)", "30 mars 2023",
  "https://www.insee.fr/fr/statistiques/6793238",
  "La fécondité des femmes nées à l'étranger « s'établit à 2,3 enfants par femme en moyenne, contre 1,7 pour celles nées en France » (2021) ; pour les descendantes de deux parents immigrés, la descendance finale est de 2,0 enfants (générations 1960-1974).",
  "Statistique publique."))
MALDITA = ('maldita', src("Es falso que a partir de 2050 en Francia « el 50% de la población va a ser musulmana »", "Maldita.es (fact-checker espagnol)", "12 avril 2019",
  "https://maldita.es/malditodato/es-falso-que-a-partir-de-2050-en-francia-el-50-de-la-poblacion-va-a-ser-musulmana-como-dice-santiago-abascal/",
  "D'après Pew (2017), la France atteindrait en 2050 12,7 % de musulmans (sans immigration), 17,4 % (immigration moyenne) ou 18 % (immigration forte) ; la Suède, pays le plus haut, atteindrait 30,6 % dans le scénario fort. Verdict : « FALSO ».",
  "Fact-checker reconnu.", 'media'))
ELY_1961 = ('ely_1961', src("Cérémonie de commémoration des 60 ans du 17 octobre 1961", "Présidence de la République", "16 octobre 2021",
  "https://www.elysee.fr/emmanuel-macron/2021/10/16/ceremonie-de-commemoration-des-60-ans-du-17-octobre-1961",
  "« plus de 25.000 hommes, femmes et enfants » ont manifesté ; « près de 12.000 Algériens furent arrêtés » ; « plusieurs dizaines furent tués, leurs corps jetés dans la Seine ». Les « crimes commis cette nuit-là sous l'autorité de Maurice Papon sont inexcusables pour la République ». La tragédie fut longtemps « tue, déniée ou occultée ».",
  "Communiqué officiel."))
LCP_1961 = ('lcp_1961', src("L'Assemblée nationale reconnaît et condamne le « massacre des Algériens du 17 octobre 1961 à Paris »", "LCP (Raphaël Marchal)", "28 mars 2024",
  "https://lcp.fr/actualites/l-assemblee-nationale-reconnait-et-condamne-le-massacre-des-algeriens-du-17-octobre-1961",
  "La résolution, portée par une députée écologiste et cosignée par un député Renaissance, est adoptée par 67 voix contre 11 ; elle demande une journée de commémoration et n'est pas contraignante. Un député RN a dénoncé une « repentance à outrance ». Selon des travaux récents, il y aurait eu jusqu'à 200 morts.",
  "Média parlementaire.", 'media'))
VDI_1961 = ('vdi_1961', src("17 octobre 1961 : terreur d'État et violence « coloniale »", "La Vie des idées (Sylvie Thénault, historienne)", "7 février 2008",
  "https://laviedesidees.fr/17-octobre-1961-terreur-d-Etat-et",
  "Recension de Paris 1961 (Jim House et Neil MacMaster) : selon eux, « bien plus de 120 Algériens furent assassinés par la police en région parisienne » en septembre-octobre 1961 ; ils parlent de « terreur d'État ». Sur le bilan, la recension présente le désaccord entre Jean-Luc Einaudi et Jean-Paul Brunet.",
  "Revue universitaire.", 'etude'))
BRUNET_1961 = ('brunet_1961', src("Police Violence in Paris, October 1961: Historical Sources, Methods, and Conclusions (The Historical Journal, vol. 51-1)", "Jean-Paul Brunet (Cambridge University Press)", "mars 2008",
  "https://www.cambridge.org/core/services/aop-cambridge-core/content/view/2272247F83664961C082DB97EDD6B17F/S0018246X07006632a.pdf/police_violence_in_paris_october_1961_historical_sources_methods_and_conclusions.pdf",
  "L'article étudie « the repression of the Algerian Front de Libération Nationale (FLN) by the Paris police on 17 October 1961 », avec « more than 14,000 people arrested in two days » ; « there remains disagreement over the emotive question of the number of people killed ».",
  "Article universitaire de l'historien qui retient le bilan le plus bas.", 'etude'))
AN_1961 = ('an_1961', src("Question écrite n° 5123 (Noël Mamère) sur le 17 octobre 1961 et réponse du ministère de l'Intérieur", "Assemblée nationale", "20 octobre et 8 décembre 1997",
  "https://questions.assemblee-nationale.fr/dyn/11/questions/QANR5L11QE5123.pdf",
  "Le bilan officiel de l'époque faisait état de « deux morts et une dizaine de blessés ». Le 18 octobre 1997, une mission a été confiée à Dieudonné Mandelkern pour inventorier les archives de la préfecture de police.",
  "Document parlementaire officiel (1997)."))
COR_NV = ('cor_nv', src("Rapport annuel du COR, juin 2026 — partie 3, chapitre 2 (niveau de vie des retraités)", "Conseil d'orientation des retraites", "juin 2026",
  "https://www.cor-retraites.fr/sites/default/files/2026-06/RA_Part3_Chap2.pdf",
  "En 2023, le niveau de vie des retraités atteint 100,2 % de celui de l'ensemble de la population : 2 473 € par mois et par unité de consommation, contre 2 468 € pour l'ensemble et 2 693 € pour les actifs. En tenant compte des loyers imputés aux propriétaires, il dépasse de 6,5 % celui de l'ensemble, à un niveau très proche de celui des actifs. Il est projeté à 96,3 % en 2045 et 90,3 % en 2070 dans le scénario de référence.",
  "Organisme public d'expertise sur les retraites."))
DREES_NV = ('drees_nv', src("Le niveau de vie des retraités (fiche 9, Les retraités et les retraites, édition 2025)", "DREES", "juillet 2025",
  "https://drees.solidarites-sante.gouv.fr/sites/default/files/2025-07/Fiche%2009%20-%20Le%20niveau%20de%20vie%20des%20retrait%C3%A9s.pdf",
  "« Le niveau de vie médian des retraités est équivalent à celui de l'ensemble de la population » (2 030 € par mois en 2022). Leur taux de pauvreté est de « 10,0 % contre 14,4 % » pour l'ensemble en 2022 ; « 70 % des ménages dont la personne de référence est retraitée sont propriétaires de leur résidence principale », contre 57 % pour l'ensemble.",
  "Statistique publique."))

FICHES = []

# 1 ── RN et autoroutes ────────────────────────────────────────────────────────
FICHES.append(fiche(
 id='rn-nationaliser-autoroutes', affirmation="Le RN veut nationaliser les autoroutes pour baisser les péages.", volet='politique', sous_theme='Rassemblement national',
 mots_cles=['nationaliser les autoroutes', 'renationaliser les autoroutes', 'nationalisation des autoroutes', 'peages autoroute', 'baisser les peages', 'societes d autoroutes', 'concessions autoroutieres', 'vinci autoroutes'],
 verdict='plutot_exact', fiabilite='etabli',
 resume="C'était bien une promesse du programme présidentiel 2022 de Marine Le Pen : renationaliser les autoroutes pour baisser les péages de 15 %. La mesure coûterait 40 à 50 milliards d'euros selon le ministère de l'Économie et le Sénat, alors que les concessions expirent de toute façon entre 2031 et 2036. Elle n'est pas propre au RN : LFI a déposé en 2025 une proposition de loi de nationalisation.",
 contexte="La colère contre les péages est forte et la rentabilité des sociétés d'autoroutes est documentée par le Sénat ; le RN s'en sert pour se présenter comme défenseur du pouvoir d'achat.",
 explication="Les autoroutes ont été concédées à des sociétés privées (Vinci, Eiffage, Abertis) qui encaissent les péages jusqu'à la fin de leurs contrats. Les racheter avant le terme oblige l'État à indemniser les actionnaires ; attendre la fin des contrats permet de les reprendre sans indemnité.",
 sources=[IM_AUTO, SENAT_AUTO20, SENAT_AUTO24, AN_AUTO, LFI_AUTO],
 faits=[
  fait("Le programme présidentiel 2022 de Marine Le Pen promettait de « renationaliser les autoroutes pour baisser de 15 % les péages ».", 'im_auto', '2022', 'France', "La promesse existe bien.", 'etabli', '15 %'),
  fait("Le ministère de l'Économie estime le coût d'un rachat anticipé entre 45 et 50 milliards d'euros ; l'Institut Montaigne évalue l'indemnisation à environ 40 milliards, plus la reprise de 31,6 milliards de dette.", 'senat_auto20', '2020-2022', 'France', "Racheter avant l'échéance coûte très cher.", 'estimation', '45 à 50 Md€'),
  fait("Les concessions historiques prennent fin entre 2031 et 2036, après avoir été prolongées de 35 ans à 64 à 75 ans.", 'senat_auto24', '2024', 'France', "Attendre l'échéance permet de reprendre la main sans indemnité.", 'etabli', '2031-2036'),
  fait("Selon le Sénat, les sociétés d'autoroutes ont versé environ 24,3 milliards d'euros de dividendes de 2006 à 2019, et Vinci Autoroutes pesait en 2023 43 % du résultat net du groupe pour 9 % de son chiffre d'affaires.", 'senat_auto24', '2006-2023', 'France', "La rentabilité des concessions est très élevée.", 'etabli', '43 %'),
  fait("En 2025, des députés LFI ont déposé une proposition de loi visant à nationaliser seize sociétés concessionnaires d'autoroutes.", 'lfi_auto', '2025', 'France', "La mesure n'est pas propre au RN.", 'etabli'),
 ],
 court="Plutôt vrai pour 2022 : Marine Le Pen promettait de renationaliser les autoroutes pour baisser les péages de 15 %. Mais un rachat anticipé coûterait 40 à 50 milliards, alors que les concessions s'arrêtent entre 2031 et 2036. LFI propose aussi la nationalisation.",
 moyen="La promesse figurait dans le programme présidentiel 2022 de Marine Le Pen. Le constat de départ est juste : le Sénat a montré que les concessions ont été très rentables pour les actionnaires.\n\nMais racheter avant la fin des contrats obligerait l'État à verser 40 à 50 milliards d'euros d'indemnités. Les concessions expirent entre 2031 et 2036 : la vraie bataille est de préparer leur reprise publique à cette date, sans indemniser personne.",
 detaille="Le programme présidentiel 2022 de Marine Le Pen promettait de « renationaliser les autoroutes pour baisser de 15 % les péages ». En 2023, un député RN rappelait encore cette demande à l'Assemblée, et le ministre de l'Économie lui opposait un coût de « 40 à 50 milliards d'euros ». Les sources lues ne disent pas si la mesure figure toujours dans le programme de 2027.\n\nLe point de départ est fondé : selon le Sénat, les sociétés d'autoroutes ont versé environ 24,3 milliards d'euros de dividendes entre 2006 et 2019, et la rentabilité attendue par les actionnaires serait atteinte autour de 2022. Mais un rachat anticipé coûterait 45 à 50 milliards d'euros selon Bercy, et l'Institut Montaigne juge qu'une baisse de 15 % des péages réduirait le gain pour l'État.\n\nLes concessions historiques prennent fin entre 2031 et 2036. Les reprendre à l'échéance ne coûte pas d'indemnité : c'est là que se joue le choix entre une gestion publique et une nouvelle privatisation. La gauche (LFI) défend aussi la nationalisation, par une proposition de loi déposée en 2025.",
 empathie="Tu as raison d'être en colère contre les péages : le Sénat lui-même dit que les sociétés d'autoroutes ont fait des profits énormes. La question, c'est comment reprendre la main sans faire un chèque de 40 milliards aux actionnaires.",
 legitimes=["La rentabilité des concessions est jugée excessive par le Sénat lui-même.", "Les péages ont augmenté plus vite que l'inflation selon plusieurs parlementaires."],
 contre=[
  ("C'est la seule façon de baisser les péages.", "À l'échéance des contrats (2031-2036), l'État peut reprendre les autoroutes sans payer d'indemnité et fixer lui-même les tarifs."),
  ("La gauche a privatisé les autoroutes.", "La privatisation date de 2005-2006 ; aujourd'hui, LFI comme le RN défendent une reprise publique, avec des calendriers différents."),
 ],
 questions=["Sais-tu quand les contrats des sociétés d'autoroutes arrivent à échéance ?", "Qui paierait les 40 à 50 milliards d'indemnités d'un rachat anticipé ?"],
 limites=["La présence de la mesure dans les programmes RN de 2024 et de 2027 n'a pas été vérifiée.", "Les chiffrages datent de 2020-2022 ; la baisse de 15 % est une promesse, pas une évaluation indépendante."],
 publics={'convaincus': "La colère contre les péages est juste : le Sénat a montré des profits énormes. Mais racheter les autoroutes avant 2031-2036, c'est verser 40 à 50 milliards d'euros d'indemnités à ces mêmes actionnaires. Attendre la fin des contrats et les reprendre gratuitement, c'est bien plus efficace.",
  'indecis': "La promesse a bien existé en 2022, et l'idée de reprendre les autoroutes est défendue aussi à gauche. Le vrai sujet, c'est le moment : racheter maintenant coûte 40 à 50 milliards, alors que les contrats expirent entre 2031 et 2036. Regarde ce que chaque parti prévoit pour cette échéance."},
 a_actualiser='2027-06-30', raison="Programmes électoraux de 2027 et préparation de la fin des concessions.",
))

# 2 ── Proportionnelle ─────────────────────────────────────────────────────────
FICHES.append(fiche(
 id='proportionnelle-ingouvernable', affirmation="La proportionnelle rendrait la France ingouvernable.", volet='politique', sous_theme='Institutions françaises',
 mots_cles=['proportionnelle', 'scrutin proportionnel', 'mode de scrutin', 'ingouvernable', 'instabilite gouvernementale', 'quatrieme republique', 'legislatives 1986', 'coalition'],
 verdict='trompeur', fiabilite='interpretation',
 resume="En 1986, les législatives à la proportionnelle ont donné une majorité absolue, certes de deux voix, et un gouvernement qui a tenu jusqu'en 1988. Depuis 2022, c'est sous le scrutin majoritaire que la France a connu une forte instabilité. La crainte s'appuie sur l'histoire de la IVe République, mais la stabilité dépend surtout de la capacité des partis à gouverner ensemble.",
 contexte="Le débat est revenu après la dissolution de 2024 et les gouvernements successifs ; le RN, LFI, le MoDem et les écologistes sont favorables à la proportionnelle, LR et Horizons opposés.",
 explication="Avec la proportionnelle, chaque parti obtient un nombre de sièges proche de sa part de voix ; une majorité suppose alors souvent une coalition. Avec le scrutin majoritaire, le premier arrivé peut obtenir beaucoup plus de sièges que sa part de voix, mais ce n'est plus garanti quand trois blocs se partagent l'électorat.",
 sources=[GOUV_1986, LAR_1986, VDI_PROP, GC_LECORNU, LCP_PROP],
 faits=[
  fait("Aux législatives de 1986, élues à la proportionnelle, « la droite obtient la majorité absolue » et Jacques Chirac gouverne jusqu'en 1988.", 'gouv_1986', '1986-1988', 'France', "La proportionnelle n'a pas empêché une majorité.", 'etabli'),
  fait("Cette majorité ne tenait qu'à deux voix, grâce aux divers droite.", 'lar_1986', '1986', 'France', "La majorité était fragile.", 'etabli', '2 voix'),
  fait("Les gouvernements ont duré en moyenne 609 jours pendant le premier mandat d'Emmanuel Macron, contre 303 jours depuis le début du second, sous scrutin majoritaire.", 'gc_lecornu', '2017-2025', 'France', "Le scrutin majoritaire ne garantit plus la stabilité.", 'etabli', '303 jours'),
  fait("D'après le Pew Research Center, les gouvernements des régimes parlementaires de l'UE durent environ deux ans en moyenne, mais plus de quatre ans au Luxembourg et moins d'un an en Belgique, en Finlande ou en Italie.", 'gc_lecornu', '1945-2022', 'Union européenne', "Les situations sont très variables selon les pays.", 'estimation', '2 ans'),
  fait("Sous la IVe République, les gouvernements duraient en moyenne environ douze mois, contre près de vingt sous la Ve.", 'vdi_prop', '1946-2025', 'France', "L'instabilité de la IVe République est réelle.", 'etabli', '12 mois'),
 ],
 court="Trompeur : en 1986, la proportionnelle a donné une majorité absolue et un gouvernement qui a tenu deux ans. Et depuis 2022, c'est sous le scrutin majoritaire que les gouvernements tombent : 303 jours en moyenne. La stabilité dépend surtout de la capacité des partis à s'entendre.",
 moyen="La proportionnelle a déjà été utilisée en 1986 : la droite a obtenu une majorité absolue, étroite, et Jacques Chirac a gouverné jusqu'en 1988. Ce n'était donc pas le chaos.\n\nÀ l'inverse, le scrutin majoritaire actuel n'a pas empêché l'instabilité depuis 2022 : les gouvernements du second mandat d'Emmanuel Macron ont duré en moyenne 303 jours. En Europe, certains pays à la proportionnelle ont des gouvernements très stables, d'autres non : le mode de scrutin n'explique pas tout.",
 detaille="Le souvenir de la IVe République pèse : ses gouvernements duraient en moyenne une douzaine de mois. Mais l'expérience de 1986, seule élection de la Ve République à la proportionnelle, a donné une majorité absolue à la droite, avec deux voix d'avance, et un gouvernement qui a duré jusqu'en 1988.\n\nDepuis 2022, le scrutin majoritaire produit une Assemblée sans majorité : les gouvernements ont duré en moyenne 303 jours, contre 609 sous le premier mandat. Avec trois grands blocs, le scrutin majoritaire ne fabrique plus automatiquement de majorité, et il crée le plus grand écart d'Europe entre la part de voix et la part de sièges, selon deux politistes.\n\nEn Europe, la durée des gouvernements varie beaucoup : plus de quatre ans au Luxembourg, moins d'un an en Belgique ou en Italie. La différence tient aussi à la culture de coalition : les partis français, notent les chercheurs, « n'ont jamais vraiment appris à gouverner ensemble ».",
 empathie="Je comprends qu'après des mois de crises gouvernementales, on ait peur de compliquer encore les choses. Mais regarde : l'instabilité actuelle s'est produite avec le scrutin majoritaire, pas avec la proportionnelle.",
 legitimes=["La IVe République, élue à la proportionnelle, a été très instable.", "Plusieurs pays européens à la proportionnelle ont des gouvernements qui durent moins d'un an.", "La majorité de 1986 ne tenait qu'à deux voix."],
 contre=[
  ("La IVe République prouve que la proportionnelle mène au chaos.", "L'instabilité de la IVe République avait aussi d'autres causes (guerres coloniales, institutions) ; en 1986, la proportionnelle a donné une majorité."),
  ("Avec la proportionnelle, le RN aurait plus de sièges.", "C'est possible : la proportionnelle donne à chaque parti des sièges proches de ses voix, ce qui vaut pour tous les partis."),
 ],
 questions=["Sais-tu quel mode de scrutin était en vigueur pendant les crises gouvernementales de 2024-2025 ?", "Pourquoi certains pays à la proportionnelle sont-ils très stables et d'autres non ?"],
 limites=["Aucune source lue n'établit de lien statistique direct entre proportionnelle et durée des gouvernements en Europe.", "La source universitaire principale plaide pour la proportionnelle ; les débats postérieurs à avril 2025 n'ont pas été vérifiés."],
 publics={'convaincus': "Ton propre parti, le RN, défend la proportionnelle, et Marine Le Pen juge le scrutin de 1986 « un moindre mal ». En 1986, elle a d'ailleurs donné une majorité. Et l'instabilité de 2024-2025, c'est le scrutin majoritaire qui l'a produite.",
  'indecis': "La peur de l'instabilité est compréhensible, et la IVe République a été instable. Mais en 1986, la proportionnelle a produit une majorité, et depuis 2022 le scrutin majoritaire n'en produit plus. Tout dépend de la capacité des partis à négocier entre eux."},
 a_actualiser='2027-06-30', raison="Débats sur une réforme du mode de scrutin.",
))

# 3 ── RN et IVG ───────────────────────────────────────────────────────────────
FICHES.append(fiche(
 id='rn-ivg-toujours-defendu', affirmation="Le RN a toujours défendu le droit à l'avortement.", volet='politique', sous_theme='Rassemblement national',
 mots_cles=['rn avortement', 'rn ivg', 'le pen ivg', 'avortement de confort', 'ivg constitution', 'derembourser l ivg', 'remboursement avortement', 'rn droit des femmes'],
 verdict='contredit', fiabilite='etabli',
 resume="« Toujours » est faux : en 2011-2012, Marine Le Pen parlait d'« avortements de confort » et proposait de dérembourser l'IVG. En 2024, Marine Le Pen et 46 députés RN ont voté l'inscription de l'IVG dans la Constitution, mais 31 autres ont voté contre ou se sont abstenus au Congrès.",
 contexte="Le RN se présente désormais comme protecteur des droits des femmes ; l'argument sert à rassurer un électorat féminin et jeune.",
 explication="Le Front national a longtemps défendu une ligne hostile à l'avortement ; Marine Le Pen a changé de discours au milieu des années 2010, sans que tout le parti la suive.",
 sources=[LCP_IVG_C, LCP_IVG_AN, PS_IVG16, PS_IVG16B],
 faits=[
  fait("En 2011, Marine Le Pen disait qu'il fallait « cesser de rembourser l'avortement » ; en 2012, elle parlait d'« avortements de confort ».", 'ps_ivg16b', '2011-2012', 'France', "Le RN n'a pas « toujours » défendu l'IVG.", 'etabli'),
  fait("En 2016, Marion Maréchal-Le Pen voulait « revenir sur le remboursement intégral et illimité de l'avortement ».", 'ps_ivg16', '2016', 'France', "La question divisait encore le parti en 2016.", 'etabli'),
  fait("Au Congrès du 4 mars 2024, les députés du groupe RN ont voté 46 pour, 11 contre et 20 abstentions ; Marine Le Pen a voté pour.", 'lcp_ivg_c', '2024', 'France', "Une majorité du groupe a voté pour, mais pas tout le groupe.", 'etabli', '46 pour'),
  fait("En première lecture à l'Assemblée, le groupe RN a voté 46 pour, 12 contre et 14 abstentions.", 'lcp_ivg_an', '2024', 'France', "Le vote du groupe est resté partagé.", 'etabli'),
 ],
 court="Faux : en 2011-2012, Marine Le Pen voulait dérembourser l'IVG et parlait d'« avortements de confort ». En 2024, elle a voté l'IVG dans la Constitution avec 46 députés RN, mais 31 autres ont voté contre ou se sont abstenus.",
 moyen="Marine Le Pen a changé de position : en 2011, elle voulait « cesser de rembourser l'avortement » ; en 2016, elle disait que le débat était « tranché ». En 2024, elle a voté l'inscription de l'IVG dans la Constitution.\n\nMais tout le parti ne l'a pas suivie : au Congrès, 46 députés RN ont voté pour, 11 contre et 20 se sont abstenus. Dire que le RN a « toujours » défendu l'IVG, c'est effacer cette histoire.",
 detaille="Au début des années 2010, la ligne du Front national était hostile au remboursement de l'avortement : en 2011, Marine Le Pen disait qu'il fallait « cesser de rembourser l'avortement », et en 2012 elle parlait d'« avortements de confort » et d'« avortements de récidive ». En 2016, Marion Maréchal-Le Pen voulait encore revenir sur le remboursement « intégral et illimité », soutenue par plusieurs cadres ; Marine Le Pen répondait que le débat était « tranché ».\n\nEn 2024, lors de l'inscription de la liberté de recourir à l'IVG dans la Constitution, Marine Le Pen a voté pour. Au Congrès, les députés RN se sont partagés : 46 pour, 11 contre, 20 abstentions. Une députée RN déclarait que personne ne voulait remettre en cause l'IVG, quand une autre jugeait que « rien n'aura changé pour les femmes ».\n\nLe vote de 2024 est un fait, et il faut le reconnaître. Mais environ quatre députés RN sur dix n'ont pas voté pour, et les positions passées montrent que ce droit n'a pas toujours été défendu par ce parti.",
 empathie="C'est vrai que Marine Le Pen a voté pour l'IVG dans la Constitution, et c'est important. Mais son parti n'a pas toujours tenu ce discours, et une partie de ses députés n'a pas voté pour.",
 legitimes=["Marine Le Pen et une majorité du groupe RN ont voté la constitutionnalisation de l'IVG en 2024.", "Depuis 2016, Marine Le Pen dit ne pas remettre en cause l'accès à l'IVG."],
 contre=[
  ("Le RN a voté pour l'IVG dans la Constitution.", "Une majorité du groupe, oui ; mais 11 députés ont voté contre et 20 se sont abstenus au Congrès."),
  ("Ce sont de vieilles déclarations.", "Elles datent de 2011-2016 : c'est récent à l'échelle d'un droit fondamental, et le parti était divisé jusqu'en 2016."),
 ],
 questions=["Savais-tu qu'en 2011 Marine Le Pen voulait dérembourser l'IVG ?", "Pourquoi environ quatre députés RN sur dix n'ont-ils pas voté pour l'IVG dans la Constitution ?"],
 limites=["Le vote des sénateurs RN au Congrès et celui des eurodéputés RN n'ont pas été vérifiés.", "Les citations de 2011-2012 sont rapportées par la presse en 2016, pas lues dans leur source d'origine."],
 publics={'convaincus': "Marine Le Pen a voté pour l'IVG dans la Constitution, c'est vrai. Mais en 2011 elle voulait « cesser de rembourser l'avortement », et en 2024, 31 députés RN sur 77 n'ont pas voté pour. Si le droit à l'IVG compte pour toi, regarde les votes de chaque député, pas seulement le discours de la cheffe.",
  'indecis': "Le RN a évolué : sa présidente a voté l'IVG dans la Constitution en 2024. Mais il y a dix ans, elle parlait encore d'« avortements de confort », et une partie de ses députés reste opposée ou réservée. Ce droit dépend aussi des votes futurs, d'où l'importance de regarder l'ensemble des élus."},
 a_actualiser='2027-06-30', raison="Programmes 2027 et votes parlementaires sur l'IVG.",
))

# 4 ── RN et OTAN ──────────────────────────────────────────────────────────────
FICHES.append(fiche(
 id='rn-sortie-otan', affirmation="Le RN veut sortir la France de l'OTAN.", volet='politique', sous_theme='Rassemblement national',
 mots_cles=['sortir de l otan', 'sortie de l otan', 'commandement integre', 'rn otan', 'bardella otan', 'le pen otan', 'quitter l otan', 'alliance atlantique'],
 verdict='trompeur', fiabilite='etabli',
 resume="Le RN n'a jamais proposé de quitter l'OTAN, mais en 2022 Marine Le Pen voulait sortir de son commandement intégré, que la France a réintégré en 2009. En 2024, Jordan Bardella a renoncé à cette sortie « en période de guerre ». C'est LFI qui envisageait en 2022 de quitter, à terme, l'organisation elle-même.",
 contexte="La question revient avec la guerre en Ukraine et les liens du RN avec la Russie ; elle sert aussi à attaquer LFI.",
 explication="L'OTAN est une alliance militaire ; son commandement intégré est la structure militaire commune. La France en est sortie en 1966 sous de Gaulle et l'a réintégrée en 2009, sans quitter l'Alliance entre les deux.",
 sources=[IM_OTAN, PS_OTAN, E1_OTAN, LNC_OTAN, ELY_OTAN],
 faits=[
  fait("Le programme présidentiel 2022 de Marine Le Pen proposait de « sortir la France du commandement intégré de l'OTAN », pas de quitter l'Alliance.", 'im_otan', '2022', 'France', "La proposition portait sur le commandement militaire intégré.", 'etabli'),
  fait("En mars 2022, Marine Le Pen déclarait : « On ne va pas le faire alors qu'il y a une guerre dans un pays européen ».", 'ps_otan', '2022', 'France', "La mesure a été suspendue dès le début de la guerre en Ukraine.", 'etabli'),
  fait("En mars 2024, Jordan Bardella refusait cette sortie : « On ne change pas les traités en période de guerre » ; en juin 2024, il l'excluait au nom de la crédibilité de la France auprès de ses alliés.", 'lnc_otan', '2024', 'France', "Le RN a renoncé, au moins temporairement, à cette mesure.", 'etabli'),
  fait("En 2022, Jean-Luc Mélenchon voulait quitter immédiatement le commandement intégré puis, étape par étape, l'organisation dans son ensemble.", 'ps_otan', '2022', 'France', "C'est LFI qui envisageait une sortie complète.", 'etabli'),
  fait("La France a réintégré le commandement intégré en 2009, après en être sortie en 1966.", 'ely_otan', '1966-2009', 'France', "Sortir du commandement intégré n'est pas quitter l'Alliance.", 'etabli'),
 ],
 court="Trompeur : le RN n'a jamais proposé de quitter l'OTAN, seulement son commandement intégré (programme 2022), et Jordan Bardella y a renoncé en 2024. C'est LFI qui envisageait en 2022 de quitter l'organisation à terme.",
 moyen="En 2022, Marine Le Pen proposait de sortir du commandement militaire intégré de l'OTAN, comme de Gaulle en 1966, pas de quitter l'Alliance. Elle a suspendu ce projet dès le début de la guerre en Ukraine.\n\nEn 2024, Jordan Bardella a renoncé à cette sortie pour ne pas affaiblir la crédibilité de la France auprès de ses alliés. La proposition la plus radicale venait de LFI, qui envisageait de quitter l'organisation étape par étape.",
 detaille="L'OTAN est une alliance militaire dont la France est membre fondateur. En 1966, de Gaulle a fait sortir la France du commandement intégré, sans quitter l'Alliance ; Nicolas Sarkozy l'y a fait revenir en 2009. Le programme présidentiel 2022 de Marine Le Pen proposait de revenir à la situation de 1966.\n\nDès mars 2022, Marine Le Pen expliquait qu'elle ne le ferait pas pendant la guerre en Ukraine. En mars 2024, Jordan Bardella le confirmait (« On ne change pas les traités en période de guerre »), et en juin 2024 il excluait cette sortie pour ne pas « remettre en cause les engagements pris par la France ».\n\nEn 2022, LFI allait plus loin : quitter immédiatement le commandement intégré, puis l'organisation elle-même, qualifiée d'« organisation inutile qui provoque des tensions ». Les deux partis ont donc défendu une prise de distance avec l'OTAN, avec des formes différentes.",
 empathie="La question est légitime : l'indépendance militaire de la France compte pour beaucoup de gens. Mais il faut distinguer quitter l'OTAN et sortir de son commandement intégré.",
 legitimes=["Jusqu'en 2022, le RN voulait bien sortir du commandement intégré, et son recul est présenté comme lié à la guerre.", "Le programme initial de 2022 qualifiait l'OTAN d'« organisation belliciste »."],
 contre=[
  ("Le RN est pro-russe, donc anti-OTAN.", "Les liens du RN avec la Russie sont documentés ailleurs ; mais sur l'OTAN, son programme n'a jamais prévu de quitter l'Alliance."),
  ("LFI veut aussi sortir de l'OTAN.", "Oui, en 2022, LFI envisageait une sortie complète à terme : c'est un débat politique assumé, sur l'indépendance et la paix."),
 ],
 questions=["Sais-tu ce que la France a fait en 1966 et en 2009 avec l'OTAN ?", "Pourquoi le RN a-t-il changé d'avis en 2024 ?"],
 limites=["Les positions du RN et de LFI sur l'OTAN en 2025-2026 n'ont pas été vérifiées.", "La formule « sans délai » du programme RN initial est ambiguë sur son objet."],
 publics={'convaincus': "Le RN n'a jamais voulu quitter l'OTAN, seulement son commandement intégré, et Jordan Bardella y a renoncé en 2024 au nom de la crédibilité de la France. Si l'indépendance militaire compte pour toi, demande-toi pourquoi ce recul a été si rapide.",
  'indecis': "Il faut distinguer deux choses : quitter l'OTAN, et sortir de son commandement militaire intégré comme de Gaulle en 1966. Le RN proposait la seconde en 2022, puis y a renoncé ; LFI envisageait la première à terme. C'est un vrai débat sur la souveraineté, qui mérite des positions claires."},
 a_actualiser='2027-06-30', raison="Programmes 2027 sur la défense.",
))

# 5 ── RN premier parti ────────────────────────────────────────────────────────
FICHES.append(fiche(
 id='rn-premier-parti-majorite', affirmation="Le RN est le premier parti de France, il représente la majorité des Français.", volet='politique', sous_theme='Rassemblement national',
 mots_cles=['premier parti de france', 'rn majorite des francais', 'majorite des francais', 'rn premier parti', 'resultats legislatives 2024', 'resultats europeennes 2024', 'le peuple vote rn', '11 millions de voix'],
 verdict='trompeur', fiabilite='etabli',
 resume="Le RN est bien arrivé premier en voix aux européennes et aux législatives de 2024, avec un record de 10,6 millions de voix au premier tour des législatives. Mais il n'a jamais dépassé environ 37 % des suffrages exprimés, soit bien moins de la moitié des électeurs, et il n'a obtenu que 143 sièges sur 577 avec ses alliés.",
 contexte="Le slogan sert à dire que le RN serait illégitimement écarté du pouvoir.",
 explication="Être le premier parti en voix ne veut pas dire avoir la majorité : il faut plus de la moitié des suffrages, ou des sièges, pour gouverner seul. Les pourcentages sont calculés sur les suffrages exprimés ; rapportés aux inscrits, ils sont nettement plus faibles.",
 sources=[PS_LEG24, MI_LEG24, LCP_EURO24],
 faits=[
  fait("Au premier tour des législatives de 2024, le RN et ses alliés ont obtenu 10 628 330 voix, un record, contre 4 248 537 en 2022.", 'ps_leg24', '2024', 'France', "Le RN est bien le premier parti en voix.", 'etabli', '10,6 millions'),
  fait("Au second tour, le RN et ses alliés ont obtenu environ 37 % des voix et 143 sièges sur 577, dont 88 pour le RN seul.", 'mi_leg24', '2024', 'France', "Même au plus haut, ce n'est pas une majorité.", 'etabli', '143 sièges'),
  fait("Le corps électoral du premier tour comptait environ 49 millions d'inscrits : 10,6 millions de voix représentent environ 22 % des inscrits (calcul à partir des chiffres lus).", 'mi_leg24', '2024', 'France', "Près de quatre inscrits sur cinq n'ont pas voté pour le RN.", 'estimation', 'environ 22 %'),
  fait("Aux européennes de 2024, le RN est arrivé en tête dans 32 613 communes sur 35 015 avec un peu plus de 31 % des exprimés, pour 48,17 % d'abstention.", 'lcp_euro24', '2024', 'France', "Premier partout, mais avec moins d'un tiers des votants.", 'etabli', '31 %'),
 ],
 court="Trompeur : le RN est bien premier en voix en 2024 (10,6 millions au premier tour des législatives), mais avec au plus 37 % des exprimés, environ un inscrit sur cinq, et 143 sièges sur 577. Premier ne veut pas dire majoritaire.",
 moyen="Le RN a bien progressé de façon spectaculaire : 10,6 millions de voix au premier tour des législatives de 2024, un record, et premier dans 9 communes sur 10 aux européennes.\n\nMais il n'a jamais eu la majorité : au mieux 37 % des suffrages exprimés, et 143 sièges sur 577 avec ses alliés. Rapporté aux inscrits, c'est environ un électeur sur cinq. La majorité des Français a voté pour d'autres partis ou ne s'est pas exprimée.",
 detaille="Les résultats de 2024 sont nets : aux européennes, la liste de Jordan Bardella arrive en tête avec un peu plus de 31 % des exprimés et dans 32 613 communes sur 35 015 ; au premier tour des législatives, le RN et ses alliés rassemblent 10 628 330 voix, plus du double de 2022.\n\nMais aucune de ces élections ne lui donne une majorité. Au second tour des législatives, le RN et ses alliés obtiennent environ 37 % des voix et 143 sièges ; le Nouveau Front populaire, avec environ 25,7 % des voix, obtient 182 sièges. Les désistements entre partis ont pesé, ce qui fait partie des règles du scrutin majoritaire.\n\nRapporté aux quelque 49 millions d'inscrits du premier tour, le vote RN représente environ 22 % des électeurs. Être le premier parti donne un poids réel ; parler au nom de « la majorité des Français » est une autre affaire.",
 empathie="Je comprends que tu trouves injuste que le parti arrivé en tête ne gouverne pas. Mais arriver premier avec un tiers des voix, ce n'est pas avoir la majorité.",
 legitimes=["Le RN est le premier parti en voix en 2024 et, seul, le premier groupe face à chaque parti isolé.", "Les désistements du second tour ont réduit son nombre de sièges."],
 contre=[
  ("Le système électoral nous vole la victoire.", "Avec la proportionnelle, que le RN défend, il aurait environ un tiers des sièges : pas davantage de majorité."),
  ("Les abstentionnistes pensent comme nous.", "Rien ne permet de l'affirmer : on ne peut pas faire parler les abstentionnistes."),
 ],
 questions=["Quelle part des inscrits a voté RN au premier tour des législatives 2024 ?", "Combien de sièges faut-il pour avoir la majorité à l'Assemblée ?"],
 limites=["Le score exact du RN aux européennes 2024 diffère légèrement entre les sources lues (31,37 % ou 31,47 %) ; il faudrait le vérifier sur le site du ministère de l'Intérieur.", "La part des inscrits est un calcul approximatif ; les élections postérieures à juillet 2024 n'ont pas été examinées."],
 publics={'convaincus': "Le RN est bien premier en voix, et c'est un fait politique majeur. Mais 37 % des voix au mieux, c'est loin de la majorité, et rapporté aux inscrits c'est environ un électeur sur cinq. Parler au nom de tous les Français, c'est oublier les deux tiers qui ont voté autrement.",
  'indecis': "Le RN a beaucoup progressé et il est arrivé premier en 2024 : il faut le prendre au sérieux. Mais être premier n'est pas être majoritaire : 143 sièges sur 577 avec ses alliés. Les autres électeurs se sont répartis entre plusieurs partis, ou se sont abstenus."},
 a_actualiser='2027-07-31', raison="Élections présidentielle et législatives de 2027.",
))

# 6 ── Jeunes et RN ────────────────────────────────────────────────────────────
FICHES.append(fiche(
 id='jeunes-vote-rn', affirmation="Les jeunes votent massivement pour le RN.", volet='politique', sous_theme='Droite et extrême droite',
 mots_cles=['jeunes votent rn', 'vote des jeunes', 'jeunesse rn', 'jeunes bardella', '18-24 ans vote', 'jeunes extreme droite', 'vote jeune', 'generation bardella'],
 verdict='trompeur', fiabilite='estimation',
 resume="Le RN a fortement progressé chez les jeunes : 25 % des 18-24 ans qui ont voté aux européennes de 2024, contre 15 % en 2019. Mais LFI est arrivée devant chez les 18-24 ans (33 %), le Nouveau Front populaire a fait environ la moitié des voix des moins de 25 ans aux législatives, et 60 % des 18-24 ans se sont abstenus aux européennes.",
 contexte="L'image d'une jeunesse acquise à Jordan Bardella circule largement, notamment sur TikTok.",
 explication="Les votes par âge viennent de sondages réalisés le jour du vote, avec une marge d'erreur plus forte sur les petits groupes. Les pourcentages portent sur ceux qui ont voté ; chez les jeunes, l'abstention est très élevée.",
 sources=[IPSOS_EU24, IPSOS_LEG24, FJJ_JEUNES],
 faits=[
  fait("Aux européennes de 2024, chez les 18-24 ans qui ont voté, LFI obtient 33 % et le RN 25 %.", 'ipsos_eu24', '2024', 'France', "Chez les plus jeunes votants, la gauche radicale arrive devant.", 'estimation', '25 %'),
  fait("Le vote RN chez les 18-24 ans est passé de 15 % aux européennes de 2019 à 25 % en 2024.", 'fjj_jeunes', '2019-2024', 'France', "La progression du RN chez les jeunes est réelle.", 'estimation', '+10 points'),
  fait("60 % des 18-24 ans se sont abstenus aux européennes de 2024, contre 29 % des 70 ans et plus.", 'ipsos_eu24', '2024', 'France', "La majorité des jeunes ne vote pas du tout.", 'estimation', '60 %'),
  fait("Aux législatives de 2024, « l'alliance de gauche a ainsi été choisie par la moitié des votants de moins de 25 ans », tandis que le RN et ses alliés font 32 % chez les moins de 35 ans, contre 18 % en 2022.", 'ipsos_leg24', '2024', 'France', "La gauche reste en tête chez les plus jeunes, le RN progresse.", 'estimation', '32 %'),
 ],
 court="Trompeur : le RN progresse chez les jeunes (25 % des 18-24 ans votants aux européennes 2024, contre 15 % en 2019), mais LFI fait mieux (33 %), la gauche a eu la moitié des voix des moins de 25 ans aux législatives, et 60 % des 18-24 ans se sont abstenus.",
 moyen="La progression du RN chez les jeunes est réelle : un quart des 18-24 ans qui ont voté aux européennes de 2024 l'ont choisi, contre 15 % en 2019.\n\nMais chez les plus jeunes, la gauche reste devant : LFI fait 33 % aux européennes, et le Nouveau Front populaire environ la moitié des votants de moins de 25 ans aux législatives. Et surtout, six jeunes sur dix ne sont pas allés voter aux européennes.",
 detaille="Selon les sondages Ipsos réalisés lors des européennes de 2024, le RN obtient 25 % chez les 18-24 ans qui ont voté et 30 % chez les 25-34 ans. C'est une forte progression : 15 % chez les 18-24 ans en 2019.\n\nMais LFI arrive en tête chez les 18-24 ans votants, avec 33 %. Aux législatives qui suivent, la gauche réunie obtient environ la moitié des voix des moins de 25 ans, et 40 % chez les 25-34 ans ; le RN et ses alliés font 32 % chez les moins de 35 ans, contre 18 % en 2022.\n\nLe principal fait reste l'abstention : 60 % des 18-24 ans ne sont pas allés voter aux européennes, contre 29 % des plus de 70 ans. La jeunesse est divisée, et en grande partie silencieuse dans les urnes.",
 empathie="C'est vrai que le RN séduit de plus en plus de jeunes, et il faut comprendre pourquoi. Mais dire que la jeunesse vote massivement RN, c'est oublier qu'elle vote davantage à gauche, et surtout qu'elle s'abstient beaucoup.",
 legitimes=["Le RN a gagné environ dix points chez les 18-24 ans entre 2019 et 2024.", "Chez les 25-34 ans, le RN est arrivé en tête aux européennes de 2024."],
 contre=[
  ("Les jeunes regardent Bardella sur TikTok, ils votent pour lui.", "Une audience sur les réseaux n'est pas un vote : chez les 18-24 ans votants, LFI fait mieux que le RN."),
  ("La gauche a perdu la jeunesse.", "Aux législatives de 2024, la gauche a obtenu environ la moitié des voix des moins de 25 ans."),
 ],
 questions=["Sais-tu quel parti est arrivé en tête chez les 18-24 ans aux européennes de 2024 ?", "Pourquoi tant de jeunes ne votent-ils pas ?"],
 limites=["Les chiffres viennent de sondages, avec une marge d'erreur plus forte sur les sous-groupes d'âge.", "La participation des jeunes aux législatives de 2024 n'a pas été vérifiée ; la Fondation Jean-Jaurès est proche du PS."],
 publics={'convaincus': "Le RN progresse chez les jeunes, c'est vrai : un quart des 18-24 ans votants en 2024. Mais LFI a fait 33 % dans la même tranche d'âge, et la gauche a eu environ la moitié des voix des moins de 25 ans aux législatives. Et six jeunes sur dix ne votent pas : personne ne peut parler en leur nom.",
  'indecis': "La jeunesse est divisée : le RN gagne du terrain, mais la gauche reste en tête chez les plus jeunes qui votent. Le fait le plus frappant, c'est que la majorité des jeunes s'abstient. Si tu es jeune, ta voix pèse d'autant plus."},
 a_actualiser='2027-07-31', raison="Sondages des élections de 2027.",
))

# 7 ── Indemnité des députés ───────────────────────────────────────────────────
FICHES.append(fiche(
 id='deputes-salaire-15000', affirmation="Les députés touchent 15 000 euros par mois.", volet='politique', sous_theme='Institutions françaises',
 mots_cles=['salaire des deputes', 'indemnite parlementaire', 'deputes 15000 euros', 'deputes payes', 'elus se gavent', 'frais de mandat', 'remuneration des deputes', 'indemnite des deputes'],
 verdict='contredit', fiabilite='etabli',
 resume="L'indemnité d'un député est de 7 637,39 € brut, soit 5 953,34 € net par mois. Pour arriver à 15 000 €, il faut additionner des enveloppes qui ne sont pas un revenu : la dotation pour les frais du mandat (7 238 € par mois depuis 2026) et le crédit pour payer jusqu'à cinq collaborateurs (11 463 €). Un député reste parmi les 3 % de Français les mieux rémunérés.",
 contexte="Le chiffre circule pour dénoncer des élus déconnectés ; il nourrit l'idée que « tous les élus se gavent ».",
 explication="L'indemnité est la rémunération personnelle du député, imposable comme un salaire. La dotation de fonctionnement sert à payer les frais du mandat (permanence, déplacements) et fait l'objet de contrôles ; le crédit collaborateurs paie les salaires de ses assistants.",
 sources=[AN_INDEM, IPP_INDEM, PS_AFM],
 faits=[
  fait("L'indemnité parlementaire est de 7 637,39 € brut, soit 5 953,34 € net par mois.", 'an_indem', '2026', 'France', "La rémunération personnelle est bien inférieure à 15 000 €.", 'etabli', '5 953 € net'),
  fait("Depuis 2026, la dotation de fonctionnement parlementaire, de 7 238,04 € par mois, sert à payer les frais du mandat.", 'an_indem', '2026', 'France', "C'est une enveloppe de frais, pas un revenu.", 'etabli', '7 238 €'),
  fait("Le crédit collaborateurs, de 11 463 € par mois, paie jusqu'à cinq collaborateurs.", 'an_indem', '2026', 'France', "Cet argent rémunère des salariés, pas le député.", 'etabli', '11 463 €'),
  fait("Les frais de mandat sont contrôlés et les sommes « indûment prises en charge » doivent être remboursées.", 'ps_afm', '2018-2022', 'France', "L'utilisation des frais est encadrée.", 'etabli'),
  fait("En 2020, l'indemnité représentait 3,2 fois le salaire ouvrier moyen ; les députés se situent autour des 3 % de revenus les plus élevés.", 'ipp_indem', '2020', 'France', "Les députés restent nettement mieux payés que la moyenne.", 'etabli', '3,2 fois'),
 ],
 court="Faux : un député touche 5 953 € net par mois (7 637 € brut). Les 15 000 € additionnent des enveloppes pour les frais du mandat et les salaires des collaborateurs. Cela reste plus de trois fois le salaire ouvrier moyen.",
 moyen="La rémunération d'un député est de 7 637 € brut, soit environ 5 953 € net par mois. C'est beaucoup : plus de trois fois le salaire d'un ouvrier, parmi les 3 % de revenus les plus élevés.\n\nMais les 15 000 € additionnent d'autres enveloppes qui ne vont pas dans sa poche : environ 7 200 € pour les frais du mandat, contrôlés, et environ 11 500 € pour payer ses collaborateurs.",
 detaille="Selon l'Assemblée nationale, l'indemnité d'un député est de 7 637,39 € brut, soit 5 953,34 € net par mois, imposable comme un salaire. S'y ajoutent deux enveloppes qui ne sont pas un revenu : la dotation de fonctionnement parlementaire, de 7 238,04 € par mois depuis 2026, qui paie les frais du mandat, et le crédit collaborateurs, de 11 463 € par mois, qui paie jusqu'à cinq salariés.\n\nDepuis les lois de 2017, les frais de mandat sont contrôlés et les dépenses injustifiées doivent être remboursées. Les abus qui ont existé ont conduit à durcir ces règles.\n\nLa critique de fond reste légitime : selon l'Institut des politiques publiques, l'indemnité représentait en 2020 plus de trois fois le salaire ouvrier moyen, et les députés font partie des 3 % les mieux rémunérés. C'est un débat sur l'écart entre élus et citoyens, qui gagne à partir des vrais chiffres.",
 empathie="Je comprends qu'on trouve que les élus sont bien payés : avec près de 6 000 € net, ils gagnent plus de trois fois un salaire d'ouvrier. Mais 15 000 €, c'est en comptant l'argent qui paie leurs assistants.",
 legitimes=["Un député gagne plus de trois fois le salaire ouvrier moyen.", "Des abus sur les frais de mandat ont existé avant les réformes de 2017."],
 contre=[
  ("Les frais de mandat, ils les dépensent comme ils veulent.", "Depuis 2017, ils sont contrôlés, et les sommes indues doivent être remboursées."),
  ("Ils ont aussi plein d'avantages.", "Le débat sur les avantages est légitime ; mais il faut partir des montants réels, publiés par l'Assemblée."),
 ],
 questions=["Sais-tu à quoi sert le crédit collaborateurs d'un député ?", "Quel écart de rémunération te semblerait juste entre un élu et un ouvrier ?"],
 limites=["Le montant du crédit collaborateurs diffère selon les sources (11 463 € selon l'Assemblée en janvier 2026, 10 581 € selon un média en septembre 2026).", "Les règles de contrôle de la nouvelle dotation de 2026 n'ont pas été lues ; celles citées datent de 2022."],
 publics={'convaincus': "Un député touche 5 953 € net : c'est beaucoup, et tu as le droit de trouver ça trop. Mais les 15 000 € comptent l'argent qui paie ses assistants et ses frais, contrôlés. Si on veut réduire l'écart entre élus et citoyens, autant partir des vrais chiffres, publiés par l'Assemblée elle-même.",
  'indecis': "Les députés sont bien payés, environ 6 000 € net, plus de trois fois un salaire d'ouvrier. Le chiffre de 15 000 € ajoute des enveloppes pour les frais et les collaborateurs, qui ne vont pas dans leur poche. Le débat sur la rémunération des élus est légitime, à partir de ces montants."},
 a_actualiser='2027-06-30', raison="Revalorisations éventuelles de l'indemnité et des dotations.",
))

# 8 ── Syndicats et subventions ────────────────────────────────────────────────
FICHES.append(fiche(
 id='syndicats-subventions', affirmation="Les syndicats vivent des subventions de l'État.", volet='droits', sous_theme='Droits des travailleurs',
 mots_cles=['syndicats subventions', 'financement des syndicats', 'syndicats payes par l etat', 'argent des syndicats', 'rapport perruchot', 'fonds paritaire', 'cgt subventions', 'cotisations syndicales'],
 verdict='trompeur', fiabilite='etabli',
 resume="Le financement public des syndicats existe mais il est limité : en 2025, le fonds paritaire a versé un peu plus de 103 M€ aux syndicats de salariés et 53,6 M€ au patronat, dont seulement 34,7 M€ venaient de l'État, le reste d'une contribution des entreprises. La CFDT déclare 76 % de ressources propres. Le chiffre de « 4 % de cotisations » vient d'un rapport rejeté par l'Assemblée en 2011.",
 contexte="L'argument sert à présenter les syndicats comme des organisations vivant aux crochets de l'État, notamment pendant les grèves.",
 explication="Depuis 2014, un fonds paritaire finance le dialogue social, pour les syndicats de salariés comme pour le patronat, à partir d'une petite contribution des entreprises et d'une subvention publique. Dans la fonction publique, les décharges syndicales représentent un autre coût.",
 sources=[CC_SYND, JDN_SYND, CFDT_RES, AN_PERRUCHOT],
 faits=[
  fait("En 2025, le fonds paritaire a versé un peu plus de 103 M€ aux syndicats de salariés et 53,6 M€ aux organisations patronales ; environ 122,5 M€ provenaient de la contribution des entreprises et 34,7 M€ de l'État.", 'jdn_synd', '2025', 'France', "La part de l'État est minoritaire, et le patronat est aussi financé.", 'etabli', '34,7 M€'),
  fait("Le fonds paritaire, créé par la loi du 5 mars 2014, disposait de 144 M€ en 2022, dont 32,6 M€ de subvention de l'État.", 'cc_synd', '2022', 'France', "Les montants sont stables et encadrés par la loi.", 'etabli', '144 M€'),
  fait("La CFDT déclare « 76 % de ressources internes contre 24 % de ressources externes ».", 'cfdt_res', 'année non précisée', 'CFDT', "Pour ce syndicat, les cotisations et ressources propres dominent.", 'estimation', '76 %'),
  fait("Le chiffre de « 4 % de cotisations » vient du rapport Perruchot, dont l'Assemblée a rejeté les conclusions en 2011.", 'an_perruchot', '2011', 'France', "Le chiffre le plus cité n'a jamais été validé.", 'etabli', '4 %'),
  fait("Selon la Cour des comptes, le coût total du dialogue social dans les trois fonctions publiques dépasse 874 M€ en 2022.", 'cc_synd', '2022', 'Fonction publique', "Dans le public, les moyens syndicaux représentent un coût réel.", 'etabli', '874 M€'),
 ],
 court="Trompeur : en 2025, le fonds paritaire a versé environ 103 M€ aux syndicats et 54 M€ au patronat, dont seulement 34,7 M€ de l'État. La CFDT déclare 76 % de ressources propres. Le « 4 % de cotisations » vient d'un rapport rejeté en 2011.",
 moyen="Il existe bien un financement public du dialogue social : un fonds créé en 2014, alimenté surtout par une petite contribution des entreprises et, pour environ un cinquième, par l'État. En 2025, il a versé environ 103 M€ aux syndicats de salariés, et aussi 54 M€ aux organisations patronales comme le Medef.\n\nLes syndicats vivent d'abord des cotisations de leurs adhérents : la CFDT déclare 76 % de ressources propres. Le chiffre de 4 % de cotisations, souvent cité, vient d'un rapport rejeté par l'Assemblée en 2011.",
 detaille="Depuis la loi du 5 mars 2014, un fonds paritaire (AGFPN) finance les organisations syndicales et patronales pour leur rôle dans le dialogue social. Il est alimenté par une contribution des employeurs de 0,016 % des salaires et par une subvention de l'État. En 2025, il a versé un peu plus de 103 M€ aux syndicats de salariés et 53,6 M€ au patronat ; environ 34,7 M€ venaient de l'État.\n\nLa CFDT, qui publie des comptes certifiés, déclare 76 % de ressources internes. Le chiffre de « 4 % de cotisations », très repris, vient du rapport Perruchot de 2011, dont l'Assemblée a rejeté les conclusions et qui n'a jamais été publié officiellement.\n\nIl est vrai qu'une partie des moyens syndicaux est publique : crédit d'impôt sur les cotisations, et, dans la fonction publique, un coût du dialogue social estimé par la Cour des comptes à plus de 874 M€ en 2022 (décharges, mises à disposition). Avec 8,1 % de syndiqués dans le privé en 2019, les cotisations reposent sur une base étroite.",
 empathie="C'est une bonne question de savoir qui paie les syndicats. La réponse : surtout leurs adhérents, avec un financement public encadré, qui profite aussi au Medef.",
 legitimes=["Une partie des ressources syndicales est publique ou parapublique (subvention, crédit d'impôt, décharges dans la fonction publique).", "Le taux de syndicalisation est faible dans le privé (8,1 % en 2019)."],
 contre=[
  ("Le rapport Perruchot a prouvé le contraire.", "Ses conclusions ont été rejetées par la commission d'enquête elle-même en 2011, et le rapport n'a jamais été publié officiellement."),
  ("Les syndicats sont payés pour faire grève.", "Les grévistes perdent leur salaire ; le fonds paritaire finance le dialogue social, y compris côté patronal."),
 ],
 questions=["Savais-tu que le Medef reçoit aussi de l'argent du même fonds paritaire ?", "D'où vient, selon toi, le chiffre de 4 % de cotisations ?"],
 limites=["Les données de la Dares sur la syndicalisation n'ont pas pu être lues ; le taux de 2019 vient de la Cour des comptes.", "Il n'existe pas de chiffre consolidé de la part des cotisations pour toutes les confédérations ; la CFDT est documentée par elle-même."],
 publics={'convaincus': "Le financement public existe, mais il est limité : environ 35 M€ de l'État en 2025, et le même fonds finance aussi le Medef. Le chiffre de 4 % de cotisations vient d'un rapport rejeté en 2011. Si les syndicats étaient de simples relais de l'État, ils ne s'opposeraient pas aussi souvent aux gouvernements.",
  'indecis': "Les syndicats reçoivent bien de l'argent public pour le dialogue social, de façon encadrée et publique, comme les organisations patronales. Mais l'essentiel de leurs ressources vient de leurs adhérents. Si tu veux des syndicats plus indépendants, la meilleure garantie, c'est qu'ils aient plus d'adhérents."},
 a_actualiser='2027-10-31', raison="Rapport annuel du fonds paritaire.",
))

# 9 ── Crèches de Noël ─────────────────────────────────────────────────────────
FICHES.append(fiche(
 id='creches-noel-mairies', affirmation="Les crèches de Noël sont interdites dans les mairies.", volet='droits', sous_theme='Laïcité',
 mots_cles=['creche de noel', 'creches de noel', 'creche mairie', 'noel interdit', 'on interdit noel', 'creche laicite', 'tradition chretienne', 'santons'],
 verdict='trompeur', fiabilite='etabli',
 resume="Il n'existe pas d'interdiction générale. Depuis 2016, le Conseil d'État autorise une crèche installée par une collectivité si elle a un caractère culturel, artistique ou festif, sans prosélytisme. Dans le hall d'une mairie, la règle est plus stricte : il faut des circonstances particulières, comme un usage local. La crèche du département de Vendée a ainsi été validée, celle de la mairie de Melun refusée.",
 contexte="Chaque mois de décembre, l'idée qu'« on interdit Noël » circule pour opposer la laïcité aux traditions chrétiennes.",
 explication="L'article 28 de la loi de 1905 interdit d'apposer des signes religieux sur les monuments publics. Le juge distingue le signe religieux de la tradition festive : une crèche peut relever de l'une ou de l'autre selon le contexte.",
 sources=[CE_CRECHE, CE_CRECHE18, BDT_CRECHE],
 faits=[
  fait("Selon le Conseil d'État, l'installation temporaire d'une crèche par une personne publique est légale si elle présente « un caractère culturel, artistique ou festif ».", 'ce_creche', '2016', 'France', "Les crèches ne sont pas interdites par principe.", 'etabli'),
  fait("Dans un bâtiment public siège d'une collectivité, elle n'est pas possible « en l'absence de circonstances particulières » ; la crèche de la mairie de Melun a été jugée illégale.", 'ce_creche', '2016', 'France', "Dans une mairie, la règle est stricte.", 'etabli'),
  fait("La crèche installée à l'hôtel du département de Vendée a finalement été maintenue : la cour de Nantes a rejeté la demande d'annulation et le Conseil d'État n'a pas admis le pourvoi.", 'ce_creche18', '2018', 'France', "Une crèche peut être validée même dans un bâtiment public.", 'etabli'),
  fait("Sur les autres emplacements publics, comme les marchés de Noël, l'installation de santons est a priori licite.", 'bdt_creche', '2016', 'France', "Dans la rue, les crèches sont largement possibles.", 'etabli'),
 ],
 court="Trompeur : depuis 2016, le Conseil d'État autorise les crèches à caractère culturel ou festif. Dans une mairie, il faut un usage local ou un contexte festif : Melun a été refusée, la Vendée validée. Sur les marchés de Noël, c'est a priori licite.",
 moyen="Il n'y a pas d'interdiction générale des crèches. Le Conseil d'État les autorise quand elles ont un caractère culturel, artistique ou festif, sans prosélytisme.\n\nLa règle est plus stricte dans le hall d'une mairie : il faut des circonstances particulières, comme une tradition locale. La crèche de Melun a été refusée, celle du département de Vendée validée. Dans les rues et sur les marchés de Noël, elles sont a priori licites.",
 detaille="La loi de 1905, article 28, interdit d'apposer des signes religieux sur les monuments publics. En 2016, le Conseil d'État a fixé une règle d'équilibre : une crèche de Noël peut être installée temporairement par une collectivité si elle présente un caractère culturel, artistique ou festif et n'exprime pas la reconnaissance d'un culte.\n\nDans un bâtiment public qui sert de siège à une collectivité, comme une mairie, la crèche n'est possible qu'avec des circonstances particulières, notamment un usage local. À Melun, faute de tradition et de contexte festif, elle a été jugée illégale ; en Vendée, la justice a finalement maintenu celle de l'hôtel du département.\n\nSur la voie publique et dans les marchés de Noël, l'installation est possible si elle n'est pas un acte de prosélytisme. La laïcité ne vise pas Noël : elle demande aux pouvoirs publics de ne pas afficher de préférence religieuse.",
 empathie="Je comprends que tu tiennes aux traditions de Noël, et elles ne sont pas interdites. Le juge demande seulement qu'une mairie ne transforme pas son hall en lieu religieux sans tradition locale.",
 legitimes=["Dans une mairie, la règle est restrictive, et plusieurs crèches ont été censurées (Melun en 2016, Béziers en 2017 selon un commentaire d'avocat).", "L'appréciation au cas par cas peut sembler floue pour les élus."],
 contre=[
  ("On interdit Noël pour ne pas froisser les musulmans.", "La règle de l'article 28 date de 1905 et vaut pour tous les signes religieux, quelle que soit la religion."),
  ("C'est notre culture, pas de la religion.", "C'est exactement ce que dit le Conseil d'État : quand la crèche a un caractère culturel ou festif, elle est autorisée."),
 ],
 questions=["Sais-tu que le Conseil d'État autorise les crèches à caractère festif ?", "Où vois-tu des crèches chaque année dans ta ville ?"],
 limites=["La jurisprudence postérieure à 2018 n'a pas été recherchée.", "Le texte de l'article 28 n'a pas été lu sur Légifrance, mais dans les documents du Conseil d'État."],
 publics={'convaincus': "Noël n'est pas interdit : le Conseil d'État autorise les crèches qui ont un caractère culturel ou festif, et elles sont a priori licites sur les marchés de Noël. La règle de 1905 demande seulement que l'État ne fasse pas de religion officielle, et cette règle protège aussi les chrétiens.",
  'indecis': "La règle est plus nuancée qu'on ne le dit : dans la rue et sur les marchés, les crèches sont largement possibles ; dans une mairie, il faut une tradition locale ou un contexte festif. C'est un équilibre entre traditions et neutralité de l'État."},
 a_actualiser='2027-12-31', raison="Nouvelles décisions de justice chaque hiver.",
))

# 10 ── C8 et censure ──────────────────────────────────────────────────────────
FICHES.append(fiche(
 id='c8-fermeture-censure', affirmation="La fermeture de C8 est une censure politique.", volet='politique', sous_theme='Médias',
 mots_cles=['fermeture de c8', 'c8 censure', 'arcom censure', 'hanouna censure', 'tpmp', 'frequence tnt', 'c8 tnt', 'arcom c8'],
 verdict='trompeur', fiabilite='etabli',
 resume="C8 n'a pas été fermée par une décision politique : lors du renouvellement des fréquences de la TNT, l'Arcom a retenu 15 projets sur 25 et écarté C8 et NRJ12. Le Conseil d'État a jugé la décision légale en février 2025, en relevant des programmes peu diversifiés, de nombreuses sanctions et un déficit chronique. Le débat sur le pluralisme reste légitime, mais C8 continue d'exister hors TNT.",
 contexte="Les soutiens de Cyril Hanouna et une partie de la droite et de l'extrême droite ont dénoncé une atteinte à la liberté d'expression.",
 explication="Les fréquences de la TNT sont un bien public limité, attribué gratuitement pour 10 ans, renouvelable une fois. À l'échéance, l'Arcom compare les candidatures selon des critères fixés par la loi de 1986.",
 sources=[PS_C8, LANDOT_C8, CE_CNEWS, OZAP_C8],
 faits=[
  fait("Par sa délibération du 17 juillet 2024, l'Arcom a retenu 15 projets sur 25 ; C8 et NRJ12 n'ont pas été retenues.", 'ps_c8', '2024', 'France', "Une chaîne sans ligne politique a aussi été écartée.", 'etabli', '15 sur 25'),
  fait("Le Conseil d'État a rejeté les recours de C8 le 19 février 2025, en relevant des programmes « peu diversifiés », de « nombreuses sanctions financières, mises en demeure et mises en garde » et « un déficit chronique et significatif ».", 'landot_c8', '2025', 'France', "Le juge a validé des motifs prévus par la loi.", 'etabli'),
  fait("C8 a fait l'objet de 36 alertes et sanctions selon un décompte de Libération, et de plus de 7,6 M€ d'amendes liées à TPMP selon le HuffPost.", 'ps_c8', '2016-2024', 'France', "La chaîne avait un lourd passif de manquements.", 'estimation', '7,6 M€'),
  fait("En février 2024, le Conseil d'État a demandé à l'Arcom de contrôler le pluralisme en tenant compte de tous les intervenants, sans se prononcer sur le fond pour CNews.", 'ce_cnews', '2024', 'France', "Le contrôle du pluralisme s'est renforcé, pour toutes les chaînes.", 'etabli'),
 ],
 court="Trompeur : l'Arcom a retenu 15 projets sur 25 et écarté C8 et NRJ12, et le Conseil d'État a jugé la décision légale en 2025 (programmes peu diversifiés, nombreuses sanctions, déficit). Ce n'est pas une interdiction d'émettre : C8 a perdu une fréquence publique.",
 moyen="Les fréquences de la TNT sont un bien public limité, attribué gratuitement pour dix ans. En 2024, l'Arcom a choisi 15 projets parmi 25 candidats ; C8 et NRJ12 ont été écartées.\n\nLe Conseil d'État a confirmé la décision en 2025, pour des motifs prévus par la loi : grille peu diversifiée, nombreuses sanctions et déficit chronique. On peut discuter de ces critères, mais il ne s'agit pas d'interdire une opinion.",
 detaille="La TNT ne compte qu'un nombre limité de fréquences, attribuées gratuitement pour dix ans, renouvelables une fois. À l'échéance, l'Arcom lance un appel à candidatures et compare les projets. En juillet 2024, elle a retenu 15 projets sur 25 : C8, du groupe Canal+, et NRJ12, chaîne sans ligne politique, n'ont pas été retenues.\n\nLe Conseil d'État a jugé la décision légale le 19 février 2025. Il relève des programmes peu diversifiés, de nombreuses sanctions, mises en demeure et mises en garde, et un déficit chronique. Selon des décomptes de presse, C8 avait cumulé 36 alertes et sanctions et plus de 7,6 M€ d'amendes liées à TPMP. C8 a cessé d'émettre sur la TNT le 28 février 2025.\n\nLe débat sur le pluralisme est réel : le Conseil d'État a demandé en 2024 un contrôle élargi pour toutes les chaînes, et il a lui-même jugé « excessive » une amende infligée à C8 en 2025. Mais perdre une fréquence publique au profit d'autres candidats n'est pas une censure des idées.",
 empathie="Je comprends que les fans de l'émission aient vécu ça comme une injustice. Mais une fréquence TNT est un bien public prêté pour dix ans, et la chaîne avait accumulé les sanctions.",
 legitimes=["Le Conseil d'État a réduit de moitié une amende infligée à C8 en 2025, jugeant son montant « excessif ».", "Une partie des critères porte sur le contenu, ce qui alimente un débat légitime sur la liberté éditoriale."],
 contre=[
  ("On a fermé la chaîne de droite qui dérangeait.", "NRJ12, chaîne de divertissement sans ligne politique, a aussi été écartée, pour des motifs liés à sa grille et à ses finances."),
  ("C'est une décision politique de l'Arcom.", "Le Conseil d'État, juge indépendant, l'a confirmée au regard des critères de la loi de 1986."),
 ],
 questions=["Savais-tu que NRJ12 a aussi perdu sa fréquence ?", "Selon quels critères faudrait-il attribuer un nombre limité de fréquences publiques ?"],
 limites=["La décision motivée de l'Arcom et l'arrêt complet n'ont été lus qu'au travers d'extraits et d'articles.", "Les chiffres de 36 sanctions et de 7,6 M€ viennent de décomptes de presse, pas de l'Arcom."],
 publics={'convaincus': "Si c'était une censure politique, pourquoi NRJ12, chaîne de divertissement, a-t-elle été écartée aussi ? Le Conseil d'État a validé la décision pour des raisons prévues par la loi : sanctions à répétition et déficit. La liberté d'expression, c'est de pouvoir parler, pas d'avoir une fréquence gratuite à vie.",
  'indecis': "Le débat sur le pluralisme des médias est légitime. Mais la TNT n'a qu'un nombre limité de places, prêtées pour dix ans : en 2024, 15 projets ont été retenus sur 25. La justice a jugé la décision légale, en s'appuyant sur les sanctions et les difficultés financières de la chaîne."},
 a_actualiser='2027-06-30', raison="Évolutions du contrôle du pluralisme par l'Arcom.",
))

# 11 ── Légitime défense ───────────────────────────────────────────────────────
FICHES.append(fiche(
 id='legitime-defense-domicile', affirmation="En France, on n'a plus le droit de se défendre chez soi, c'est la victime qui finit en prison.", volet='securite', sous_theme='Justice pénale',
 mots_cles=['legitime defense', 'se defendre chez soi', 'droit de se defendre', 'cambrioleur', 'cambriolage', 'la victime en prison', 'defendre sa maison', 'presomption de legitime defense'],
 verdict='contredit', fiabilite='etabli',
 resume="La légitime défense est inscrite dans le code pénal : celui qui se défend contre une atteinte injustifiée n'est pas responsable pénalement, sauf riposte disproportionnée. La loi présume même la légitime défense pour celui qui repousse de nuit une entrée par effraction dans un lieu habité. Cette présomption peut être renversée, et une enquête a souvent lieu, ce qui nourrit l'inquiétude.",
 contexte="Des affaires médiatisées de commerçants ou de particuliers poursuivis après avoir blessé un cambrioleur alimentent ce sentiment.",
 explication="Quand quelqu'un est blessé ou tué, une enquête est ouverte pour vérifier les faits ; ce n'est pas une condamnation. Le juge vérifie que la défense était nécessaire, immédiate et proportionnée.",
 sources=[AN_LD557, AN_LD2016, AN_LD691, CDJ_LD],
 faits=[
  fait("Selon l'article 122-5 du code pénal, n'est pas pénalement responsable la personne qui se défend contre une atteinte injustifiée, « sauf s'il y a disproportion entre les moyens de défense employés et la gravité de l'atteinte ».", 'an_ld557', 'droit en vigueur', 'France', "Le droit de se défendre existe bien.", 'etabli'),
  fait("L'article 122-6 présume la légitime défense de celui qui agit « pour repousser, de nuit, l'entrée par effraction, violence ou ruse dans un lieu habité ».", 'an_ld557', 'droit en vigueur', 'France', "Chez soi, la nuit, la loi est du côté de celui qui se défend.", 'etabli'),
  fait("Pour défendre un bien, l'acte doit être « strictement nécessaire » et ne peut pas être un homicide volontaire.", 'an_ld557', 'droit en vigueur', 'France', "On ne peut pas tuer pour protéger un objet.", 'etabli'),
  fait("La présomption est « simple » : elle cède devant la preuve contraire, et la Cour de cassation a refusé la légitime défense pour une riposte non proportionnée (2012).", 'an_ld691', '1995-2026', 'France', "Le juge contrôle la proportionnalité au cas par cas.", 'etabli'),
  fait("En dehors de cette présomption, il revient en principe à la personne poursuivie de démontrer qu'elle était en légitime défense.", 'an_ld2016', '2016', 'France', "C'est ce qui explique le sentiment d'injustice dans certaines affaires.", 'etabli'),
 ],
 court="Faux : le code pénal protège celui qui se défend, sauf riposte disproportionnée, et présume même la légitime défense face à une effraction de nuit dans un logement. Une enquête n'est pas une condamnation ; ce qui est sanctionné, c'est la riposte disproportionnée.",
 moyen="La légitime défense existe bien : l'article 122-5 du code pénal protège celui qui se défend contre une agression, sauf si sa riposte est disproportionnée. Chez soi, la nuit, face à une effraction, la loi présume même qu'on était en légitime défense.\n\nQuand quelqu'un est blessé ou tué, une enquête est ouverte pour vérifier les faits : c'est normal, et ce n'est pas une condamnation. Le juge sanctionne seulement les ripostes disproportionnées, par exemple tirer sur quelqu'un qui s'enfuit.",
 detaille="Le code pénal pose le principe : n'est pas pénalement responsable la personne qui, face à une atteinte injustifiée envers elle-même ou autrui, accomplit dans le même temps un acte nécessaire à sa défense, sauf disproportion. Pour défendre un bien, l'acte doit être strictement nécessaire et ne peut pas être un homicide volontaire.\n\nL'article 122-6 va plus loin : il présume en légitime défense celui qui repousse, de nuit, une entrée par effraction, violence ou ruse dans un lieu habité. Cette présomption est « simple » : la preuve contraire reste possible, et la Cour de cassation a déjà refusé la légitime défense pour une riposte non proportionnée.\n\nLe sentiment d'injustice vient de là : quand il y a un blessé ou un mort, une enquête est ouverte, parfois une garde à vue ou une mise en examen. Aucune statistique nationale sur ces affaires n'a été trouvée. Les débats législatifs récents portent sur la présomption de légitime défense pour les forces de l'ordre, pas pour les particuliers.",
 empathie="L'idée d'être attaqué chez soi fait peur, et c'est normal de vouloir protéger sa famille. La bonne nouvelle, c'est que la loi te protège dans ce cas, surtout la nuit chez toi.",
 legitimes=["Une personne qui se défend peut être placée en garde à vue ou mise en examen pendant l'enquête.", "Hors présomption, c'est en principe à elle de prouver la légitime défense."],
 contre=[
  ("Untel a été condamné pour avoir tiré sur un cambrioleur.", "Dans ces affaires, le juge examine la proportionnalité : tirer sur quelqu'un qui fuit n'est plus se défendre."),
  ("Il faut une présomption totale de légitime défense.", "Une présomption irréfragable permettrait de tuer sans contrôle ; le juge doit pouvoir vérifier les faits."),
 ],
 questions=["Savais-tu que la loi présume la légitime défense pour une effraction de nuit chez soi ?", "Qu'est-ce qui distingue, pour toi, se défendre et se venger ?"],
 limites=["Aucune statistique nationale sur les poursuites ou condamnations pour légitime défense n'a été trouvée.", "Les articles du code pénal ont été lus dans des documents parlementaires qui les reproduisent, pas sur Légifrance ; la réponse ministérielle date de 2016."],
 publics={'convaincus': "La loi te protège : chez toi, la nuit, face à une effraction, tu es présumé en légitime défense. Ce que le juge sanctionne, c'est la riposte disproportionnée, comme tirer dans le dos de quelqu'un qui s'enfuit. Une enquête après un drame n'est pas une condamnation, c'est ce qui permet aussi de prouver qu'on était dans son droit.",
  'indecis': "Ta peur est compréhensible, et certaines affaires médiatisées choquent. Mais le code pénal protège celui qui se défend, et présume même la légitime défense face à une effraction de nuit. Le juge vérifie seulement que la riposte était proportionnée."},
 a_actualiser='2027-06-30', raison="Suite de la proposition de loi sur la présomption de légitime défense.",
))

# 12 ── Peine de mort ──────────────────────────────────────────────────────────
FICHES.append(fiche(
 id='peine-de-mort-dissuasion', affirmation="Il faut rétablir la peine de mort, ça dissuaderait les criminels.", volet='securite', sous_theme='Justice pénale',
 mots_cles=['peine de mort', 'retablir la peine de mort', 'peine capitale', 'abolition', 'dissuasion', 'effet dissuasif', 'badinter', 'executions'],
 verdict='contredit', fiabilite='etabli',
 resume="Aucun effet dissuasif n'est démontré : en 2012, l'Académie des sciences américaine a conclu que la recherche ne permet pas d'établir que la peine de mort réduit les homicides, et les États américains qui l'appliquent ont des taux d'homicide plus élevés. En France, le rétablissement est juridiquement verrouillé : la Constitution l'interdit depuis 2007 et un traité ratifié ne peut pas être dénoncé. 52 % des Français y étaient pourtant favorables en 2025.",
 contexte="Après chaque crime atroce, l'idée revient ; elle progresse dans les enquêtes d'opinion, y compris chez les jeunes.",
 explication="La dissuasion suppose que les criminels calculent le risque avant d'agir ; or beaucoup de crimes sont commis sous le coup de l'émotion, et la certitude d'être arrêté compte plus que la sévérité de la peine. Juridiquement, l'article 66-1 de la Constitution et les engagements internationaux de la France interdisent la peine de mort.",
 sources=[NRC_PDM, DPIC, MJ_PDM07, MJ_PDM_SCEL, IM_FRACT],
 faits=[
  fait("Selon le National Research Council américain, « the research to date is not useful in determining the deterrent effect of the death penalty on homicide rates ».", 'nrc_pdm', '2012', 'États-Unis', "Aucun effet dissuasif n'est démontré.", 'etabli'),
  fait("En 1999, le taux d'homicide était de 5,5 pour 100 000 dans les États américains pratiquant la peine de mort, contre 3,6 dans les autres.", 'dpic', '1999', 'États-Unis', "La peine de mort ne va pas de pair avec moins d'homicides.", 'etabli', '5,5 contre 3,6'),
  fait("Depuis 2007, l'article 66-1 de la Constitution dispose : « Nul ne peut être condamné à la peine de mort ».", 'mj_pdm_scel', '2007', 'France', "Le rétablissement exigerait une révision de la Constitution.", 'etabli'),
  fait("Selon le Conseil constitutionnel, le deuxième protocole facultatif au Pacte international relatif aux droits civils et politiques « ne comporte pas de clause de dénonciation » et « prescrit une abolition définitive ».", 'mj_pdm07', '2005', 'France', "La France s'est engagée de façon irréversible.", 'etabli'),
  fait("En octobre 2025, 52 % des personnes interrogées (54 % des 18-24 ans) estimaient qu'il faudrait rétablir la peine de mort.", 'im_fract', '2025', 'France', "L'opinion est partagée, avec une majorité favorable.", 'estimation', '52 %'),
 ],
 court="Faux sur la dissuasion : l'Académie des sciences américaine conclut qu'aucun effet n'est démontré, et les États américains avec peine de mort ont plus d'homicides. Et le rétablissement est interdit par la Constitution depuis 2007 et par un traité sans clause de sortie.",
 moyen="L'idée que la peine de mort dissuade n'est pas démontrée : en 2012, l'Académie des sciences américaine a conclu que les études ne permettent pas de l'établir. Aux États-Unis, les États qui exécutent ont même des taux d'homicide plus élevés que les autres.\n\nEn France, la peine de mort est abolie depuis 1981, interdite par la Constitution depuis 2007, et la France a signé un traité qui ne prévoit aucune possibilité de retour. La rétablir supposerait de rompre ces engagements.",
 detaille="La dissuasion suppose qu'un criminel pèse le risque avant d'agir. Les recherches ne le montrent pas : en 2012, le National Research Council américain a conclu que les études existantes ne permettent pas de déterminer l'effet de la peine de mort sur les homicides. Les États américains qui l'appliquent ont d'ailleurs des taux d'homicide plus élevés que ceux qui l'ont abolie (5,5 contre 3,6 pour 100 000 en 1999), ce qui ne prouve pas l'inverse mais contredit l'idée d'un effet évident.\n\nEn France, la loi du 9 octobre 1981 a aboli la peine de mort. La révision constitutionnelle de 2007 a inscrit à l'article 66-1 : « Nul ne peut être condamné à la peine de mort ». Le Conseil constitutionnel a relevé qu'un des traités signés « ne comporte pas de clause de dénonciation » et « prescrit une abolition définitive ».\n\nUne majorité de Français (52 % en 2025) se dit favorable au rétablissement : c'est une opinion respectable, souvent nourrie par la colère face aux crimes. Mais elle repose sur une efficacité qui n'est pas démontrée, et sur un risque irréparable en cas d'erreur judiciaire.",
 empathie="Face à certains crimes, la colère est naturelle, et vouloir que le pire soit puni l'est aussi. Mais si la peine de mort ne protège personne de plus, elle ne fait qu'ajouter une mort, avec le risque de tuer un innocent.",
 legitimes=["Une majorité de Français (52 % en 2025) est favorable au rétablissement.", "Le rapport américain ne prouve pas l'absence d'effet : il dit que les études ne permettent pas de trancher.", "La comparaison entre États américains est une corrélation, pas une preuve."],
 contre=[
  ("Au moins, un criminel exécuté ne récidive pas.", "La réclusion à perpétuité empêche aussi la récidive, sans le risque irréparable d'exécuter un innocent."),
  ("On pourrait faire un référendum.", "Il faudrait réviser la Constitution et sortir d'un traité qui ne prévoit aucune sortie : ce serait rompre la parole de la France."),
 ],
 questions=["Si la peine de mort dissuadait, pourquoi les États américains qui l'appliquent ont-ils plus d'homicides ?", "Que ferait-on en cas d'erreur judiciaire après une exécution ?"],
 limites=["Le chiffre comparatif américain date de 1999 ; les années récentes n'ont pas été lues.", "Le rapport du NRC a été lu sous forme de notice, pas en texte intégral ; la date de ratification des derniers protocoles par la France n'a pas été vérifiée."],
 publics={'convaincus': "Si la peine de mort dissuadait, les États américains qui l'appliquent auraient moins de meurtres : c'est l'inverse. Les scientifiques américains concluent qu'aucun effet n'est démontré. Et une erreur judiciaire, on ne peut plus la réparer.",
  'indecis': "La colère face aux crimes graves est légitime, et beaucoup de Français partagent ce souhait. Mais les recherches ne montrent pas d'effet dissuasif, et la Constitution l'interdit depuis 2007. La perpétuité protège la société sans risquer d'exécuter un innocent."},
 a_actualiser='2027-10-31', raison="Nouvelles enquêtes d'opinion annuelles.",
))

# 13 ── Peines planchers ───────────────────────────────────────────────────────
FICHES.append(fiche(
 id='peines-planchers-recidive', affirmation="Les peines planchers font baisser la récidive.", volet='securite', sous_theme='Récidive',
 mots_cles=['peines planchers', 'peine plancher', 'peines minimales', 'recidive', 'recidivistes', 'loi de 2007', 'peines automatiques', 'laxisme judiciaire'],
 verdict='trompeur', fiabilite='etabli',
 resume="L'évaluation de référence (Institut des politiques publiques, 2024) ne trouve aucune baisse de la récidive à court terme. À moyen terme, elle trouve une baisse d'environ 10 %, limitée aux infractions visées par la loi, et un « faible effet dissuasif global ». En contrepartie, la loi de 2007 a fortement allongé les peines de prison, avec environ 4 000 détenus de plus.",
 contexte="Le rétablissement des peines planchers, abrogées en 2014, revient dans des propositions de loi en 2025 et 2026.",
 explication="Une peine plancher impose au juge une peine minimale pour certains récidivistes, sauf décision motivée. Elle mise sur la dissuasion et sur la mise à l'écart ; son coût principal est l'augmentation de la population carcérale.",
 sources=[IPP_PP, MJ_PP, AN_PP25],
 faits=[
  fait("Selon l'IPP, « à court terme, on n'observe pas de diminution de la récidive » après les peines planchers.", 'ipp_pp', '2007-2014', 'France', "L'effet attendu n'apparaît pas immédiatement.", 'etabli'),
  fait("À moyen terme, la probabilité de commettre une infraction du même régime baisse d'environ 10 %, sans effet sur les autres infractions ; les auteurs concluent à un « faible effet dissuasif global ».", 'ipp_pp', '2007-2014', 'France', "L'effet est réel mais étroit.", 'estimation', '10 %'),
  fait("En 2010, les peines planchers ont été prononcées dans 38 % des cas éligibles, et la durée moyenne d'emprisonnement des récidivistes concernés est passée de 9 à 15,6 mois.", 'mj_pp', '2004-2010', 'France', "La loi a surtout allongé les peines.", 'etabli', '38 %'),
  fait("Le ministère estimait l'effet de la loi à environ 4 000 détenus de plus, pour un coût d'environ 146 M€ par an.", 'ipp_pp', '2007-2014', 'France', "L'efficacité limitée a un coût élevé.", 'estimation', '4 000 détenus'),
  fait("En juin 2025, la commission des lois de l'Assemblée a adopté une proposition de loi rétablissant des peines planchers pour les crimes et délits contre les forces de l'ordre.", 'an_pp25', '2025', 'France', "Le débat est d'actualité.", 'etabli'),
 ],
 court="Trompeur : selon l'évaluation de référence (IPP, 2024), aucune baisse de la récidive à court terme, et environ −10 % à moyen terme pour les seules infractions visées. En échange, environ 4 000 détenus de plus et 146 M€ par an.",
 moyen="Les peines planchers ont été appliquées de 2007 à 2014. Une étude de 2024 de l'Institut des politiques publiques montre qu'elles n'ont pas réduit la récidive à court terme ; à moyen terme, la récidive pour les mêmes infractions a baissé d'environ 10 %, sans effet sur les autres.\n\nEn revanche, elles ont fortement allongé les peines : environ 4 000 détenus de plus, dans des prisons déjà surpeuplées, pour un coût d'environ 146 M€ par an.",
 detaille="La loi du 10 août 2007 imposait des peines minimales aux récidivistes, sauf décision motivée du juge. En 2010, elles ont été prononcées dans 38 % des cas éligibles, et la durée moyenne d'emprisonnement des récidivistes concernés est passée de 9 à 15,6 mois.\n\nL'évaluation la plus solide, publiée par l'IPP en 2024, compare des personnes jugées juste avant et juste après la loi. Elle ne trouve pas de baisse de la récidive à court terme. À moyen terme, la probabilité de récidiver pour une infraction du même régime baisse d'environ 10 %, sans effet sur les autres infractions : les auteurs parlent d'un « faible effet dissuasif global ».\n\nCet effet limité a un prix : environ 4 000 détenus de plus et 146 M€ par an selon le ministère. Le débat revient au Parlement en 2025-2026 : il gagne à partir de ce bilan nuancé, plutôt que d'une promesse d'efficacité.",
 empathie="Je comprends l'envie que les récidivistes soient punis plus sévèrement, c'est un sentiment de justice légitime. Mais l'expérience de 2007-2014 montre que cela a surtout rempli les prisons, pour un effet faible sur la récidive.",
 legitimes=["L'étude IPP trouve une baisse d'environ 10 % de la récidive ciblée à moyen terme.", "Le juge pouvait déroger à la peine plancher par une décision motivée."],
 contre=[
  ("Un délinquant en prison ne récidive pas.", "C'est l'effet de neutralisation, mais l'étude ne trouve pas de baisse à court terme, et la prison peut aussi favoriser la récidive à la sortie."),
  ("Les juges sont trop laxistes, il faut les obliger.", "Même avec la loi, ils ont prononcé la peine minimale dans 38 % des cas éligibles, en motivant leurs décisions au cas par cas."),
 ],
 questions=["Savais-tu que les peines planchers ont existé de 2007 à 2014 ?", "Qu'est-ce qui réduit le plus la récidive selon toi : la durée de la peine ou ce qui se passe pendant et après ?"],
 limites=["Les données d'application s'arrêtent en 2010 ; l'abrogation de 2014 n'a pas été lue dans une source ouverte.", "La suite donnée en séance à la proposition de loi de 2025 n'a pas été vérifiée."],
 publics={'convaincus': "On a déjà essayé : de 2007 à 2014. L'étude la plus sérieuse ne trouve aucune baisse de la récidive à court terme, et seulement environ 10 % de baisse à moyen terme pour les mêmes infractions. Pendant ce temps, 4 000 personnes de plus en prison : est-ce vraiment là qu'on veut mettre l'argent de la sécurité ?",
  'indecis': "L'idée paraît logique, et l'expérience a eu un petit effet à moyen terme. Mais l'évaluation de 2024 montre un faible effet global, pour un coût élevé et des prisons plus pleines. La question est de savoir ce qui réduit vraiment la récidive : la durée de la peine, ou l'accompagnement à la sortie."},
 a_actualiser='2027-06-30', raison="Suite des propositions de loi sur les peines planchers.",
))

# 14 ── Refus d'obtempérer ────────────────────────────────────────────────────
FICHES.append(fiche(
 id='refus-obtemperer-hausse', affirmation="Les refus d'obtempérer explosent à cause du laxisme.", volet='securite', sous_theme='Police et gendarmerie',
 mots_cles=['refus d obtemperer', 'refus d obtempérer', 'delit de fuite', 'controle routier', 'fuite controle', 'tir sur vehicule', 'refus aggrave', 'conducteur en fuite'],
 verdict='trompeur', fiabilite='etabli',
 resume="Le nombre total de refus d'obtempérer n'a pas explosé : environ 25 700 par an entre 2016 et 2023, en légère baisse de 5 %. En revanche, les refus aggravés, qui mettent des vies en danger, ont presque doublé entre 2012 et 2022. La mission parlementaire transpartisane a écarté le « laxisme judiciaire » comme cause, et les peines ont été doublées en 2022.",
 contexte="Le sujet est devenu explosif après la mort d'un adolescent tué lors d'un refus d'obtempérer à Nanterre en 2023 ; l'argument sert à réclamer plus de fermeté et plus de liberté de tir pour les policiers.",
 explication="Un refus d'obtempérer est le fait de ne pas s'arrêter à un contrôle ; il est « aggravé » quand il met en danger d'autres personnes. Depuis 2017, l'article L435-1 du code de la sécurité intérieure encadre les tirs des forces de l'ordre sur des véhicules.",
 sources=[GEND_RO, AN_RO, LCP_RO, PS_RO],
 faits=[
  fait("Entre 2016 et 2023, environ 25 700 refus d'obtempérer routiers ont été constatés chaque année, en baisse de 5 % sur la période.", 'gend_ro', '2016-2023', 'France', "Le nombre total n'explose pas.", 'etabli', '25 700 par an'),
  fait("La part des refus aggravés est passée de 16 % en 2016 à 21 % en 2023 ; entre 2012 et 2022, ils ont augmenté de 94,6 %.", 'an_ro', '2012-2023', 'France', "Les refus les plus dangereux augmentent nettement.", 'etabli', '+94,6 %'),
  fait("La loi du 24 janvier 2022 a doublé la peine du refus simple, portée à deux ans d'emprisonnement et 15 000 € d'amende.", 'an_ro', '2022', 'France', "La réponse pénale a été durcie.", 'etabli', '2 ans'),
  fait("En 2022, 18 092 affaires ont été poursuivies, dont plus de 62 % en procédure accélérée ; la mission écarte le laxisme judiciaire comme cause.", 'an_ro', '2022', 'France', "Les poursuites sont nombreuses et rapides.", 'etabli', '18 092'),
  fait("En 2022, « 13 personnes ont été tuées par la police » lors de refus d'obtempérer ; les tirs sur véhicules ont culminé en 2017 (205), avant de redescendre à 140 en 2022.", 'ps_ro', '2012-2022', 'France', "Les refus d'obtempérer sont aussi un enjeu de vies humaines du côté des conducteurs.", 'etabli', '13 morts'),
 ],
 court="Trompeur : le nombre total de refus d'obtempérer est stable (environ 25 700 par an, −5 % entre 2016 et 2023), mais les refus dangereux ont presque doublé en dix ans. La mission parlementaire écarte le laxisme : les peines ont été doublées en 2022 et 18 092 affaires poursuivies.",
 moyen="Le nombre de refus d'obtempérer n'explose pas : environ 25 700 par an entre 2016 et 2023, en légère baisse. Ce qui augmente, ce sont les refus aggravés, qui mettent en danger les autres usagers et les forces de l'ordre : ils ont presque doublé entre 2012 et 2022.\n\nLa justice n'est pas laxiste sur ce point : la peine a été doublée en 2022, et 18 092 affaires ont été poursuivies cette année-là, souvent en procédure rapide. La mission de l'Assemblée a écarté le laxisme comme explication.",
 detaille="Les chiffres officiels montrent une stabilité d'ensemble : environ 25 700 refus d'obtempérer routiers par an entre 2016 et 2023, avec une hausse jusqu'en 2021 puis une baisse, soit −5 % sur la période. Un média automobile citant le service statistique du ministère fait état d'une hausse de 11 % en 2025, qui reste à vérifier à la source.\n\nLa vraie inquiétude porte sur la gravité : les refus aggravés sont passés de 16 % à 21 % du total entre 2016 et 2023, et ils ont augmenté de 94,6 % entre 2012 et 2022. Dans neuf cas sur dix, ils mettent en danger d'autres usagers.\n\nLa réponse pénale s'est durcie : la loi de janvier 2022 a doublé la peine du refus simple, et en 2022, 18 092 affaires ont été poursuivies. La mission parlementaire, menée par un député Renaissance et un député socialiste, écarte le laxisme judiciaire. Elle relève aussi que les tirs sur véhicules ont culminé en 2017, année de la loi qui les encadre, et qu'en 2022, 13 personnes ont été tuées par la police lors de refus d'obtempérer.",
 empathie="Un conducteur qui fonce sur un policier ou dans la foule, c'est terrifiant, et la hausse des refus dangereux est réelle. Mais la justice n'a pas fermé les yeux : les peines ont été doublées en 2022.",
 legitimes=["Les refus aggravés ont presque doublé en dix ans.", "Une hausse de 11 % en 2025 est signalée par un média citant le ministère.", "Des policiers et des gendarmes sont morts en lien avec des refus d'obtempérer."],
 contre=[
  ("Il faut laisser les policiers tirer.", "La loi de 2017 l'autorise déjà sous conditions ; les tirs ont culminé cette année-là, et 13 personnes ont été tuées en 2022."),
  ("Les juges relâchent les chauffards.", "Plus de 18 000 affaires poursuivies en 2022, majoritairement en procédure rapide, et des peines doublées."),
 ],
 questions=["Savais-tu que le nombre total de refus d'obtempérer est à peu près stable depuis 2016 ?", "Qu'est-ce qui pourrait expliquer la hausse des refus les plus dangereux ?"],
 limites=["La note du service statistique du ministère de l'Intérieur n'a pas pu être lue directement ; deux sources donnent des moyennes un peu différentes pour 2016-2023.", "Le chiffre de 2025 vient d'un média ; aucune série officielle des décès après 2022 n'a été lue."],
 publics={'convaincus': "Les refus les plus dangereux ont bien presque doublé en dix ans, tu as raison de t'inquiéter. Mais la justice a réagi : peines doublées en 2022, plus de 18 000 affaires poursuivies. La mission de l'Assemblée, à laquelle ont participé des élus de la majorité, écarte le laxisme : il faut chercher ailleurs les causes.",
  'indecis': "Le nombre total est à peu près stable, mais les refus qui mettent des vies en danger augmentent nettement. La réponse pénale s'est durcie. Le débat porte sur la prévention et sur l'encadrement des tirs, qui ont aussi fait des morts."},
 a_actualiser='2027-04-30', raison="Nouvelles données annuelles du ministère de l'Intérieur.",
))

# 15 ── Violences policières ──────────────────────────────────────────────────
FICHES.append(fiche(
 id='violences-policieres-existent', affirmation="Les violences policières n'existent pas.", volet='securite', sous_theme='Police et gendarmerie',
 mots_cles=['violences policieres', 'violence policiere', 'igpn', 'bavure', 'police violente', 'controle au facies', 'usage de la force', 'police tue'],
 verdict='contredit', fiabilite='etabli',
 resume="Les données officielles établissent des cas d'usage illégitime ou disproportionné de la force : en 2024, l'IGPN a retenu un « usage disproportionné de la force » contre 37 policiers, et 47 personnes sont mortes lors de missions de police ou de gendarmerie (toutes causes). La CEDH a condamné la France en 2025 pour violation du droit à la vie (arrêt Fraisse et autres c. France). Les forces de l'ordre subissent aussi beaucoup de violences.",
 contexte="Le terme est contesté par des responsables politiques et des syndicats de police, qui y voient une mise en cause de toute la profession.",
 explication="Parler de violences policières ne revient pas à accuser tous les policiers : cela désigne les cas où l'usage de la force n'est pas nécessaire ou proportionné. L'IGPN, le Défenseur des droits et la justice sont chargés de les examiner.",
 sources=[IGPN24, MI_QE8872, DDD_CTRL, CDJ_FRAISSE],
 faits=[
  fait("L'IGPN a été saisie de 914 enquêtes judiciaires en 2024, dont 428 (45 %) portent sur l'usage de la force.", 'igpn24', '2024', 'Police nationale', "Les plaintes pour violences sont nombreuses.", 'etabli', '914'),
  fait("En 2024, le manquement d'« usage disproportionné de la force » a été retenu contre 37 agents.", 'igpn24', '2024', 'Police nationale', "L'institution elle-même reconnaît des violences illégitimes.", 'etabli', '37 agents'),
  fait("En 2024, 47 personnes sont décédées et 68 ont été gravement blessées lors de missions de police ou de gendarmerie, toutes causes confondues.", 'mi_qe8872', '2024', 'France', "Les interventions ont des conséquences graves, à examiner au cas par cas.", 'etabli', '47 décès'),
  fait("Selon le Défenseur des droits, les jeunes hommes perçus comme noirs, arabes ou maghrébins ont « 4 fois plus de risque » d'être contrôlés, et près d'une personne contrôlée sur cinq déclare avoir été tutoyée, provoquée, insultée ou brutalisée.", 'ddd_ctrl', '2024', 'France', "Les abus touchent plus certaines populations.", 'estimation', '4 fois plus'),
  fait("En 2025, la Cour européenne des droits de l'homme a condamné la France pour violation du droit à la vie, après la mort d'un manifestant tué par une grenade (arrêt Fraisse et autres c. France).", 'cdj_fraisse', '2025', 'France', "Une juridiction internationale a reconnu une faute de l'État.", 'etabli'),
 ],
 court="Faux : en 2024, l'IGPN a retenu un usage disproportionné de la force contre 37 policiers, 47 personnes sont mortes lors d'interventions (toutes causes), et la CEDH a condamné la France en 2025 pour violation du droit à la vie. Les policiers subissent aussi des violences.",
 moyen="Les institutions elles-mêmes reconnaissent des violences illégitimes : en 2024, l'IGPN a retenu un usage disproportionné de la force contre 37 agents. La même année, 47 personnes sont mortes lors d'interventions de police ou de gendarmerie, et la France a été condamnée par la Cour européenne des droits de l'homme pour violation du droit à la vie.\n\nCela ne veut pas dire que tous les policiers sont violents, et les forces de l'ordre subissent elles-mêmes de nombreuses agressions. Mais nier les abus empêche de les corriger.",
 detaille="Selon son rapport annuel, l'IGPN a été saisie de 914 enquêtes judiciaires en 2024, dont 45 % portent sur l'usage de la force, et elle a retenu un « usage disproportionné de la force » contre 37 agents. Selon le ministère de l'Intérieur, 47 personnes sont décédées et 68 ont été gravement blessées lors de missions de police ou de gendarmerie en 2024, toutes causes confondues : ces chiffres ne sont pas tous des violences, mais ils justifient un contrôle.\n\nLe Défenseur des droits documente aussi des abus lors des contrôles : près d'une personne contrôlée sur cinq déclare avoir été tutoyée, provoquée, insultée ou brutalisée, et les jeunes hommes perçus comme noirs ou arabes sont quatre fois plus contrôlés. En 2025, la CEDH a jugé que la France avait violé le droit à la vie après la mort d'un manifestant tué par une grenade, faute d'un cadre suffisamment précis pour son usage.\n\nLes forces de l'ordre sont elles aussi exposées : 5 463 gendarmes ont subi des agressions physiques en 2024. Reconnaître les violences policières, c'est défendre une police respectée, pas l'attaquer.",
 empathie="Je comprends que tu veuilles défendre les policiers, qui font un métier dur et sont souvent agressés. Mais reconnaître qu'il y a des abus, c'est aussi protéger les policiers qui font bien leur travail.",
 legitimes=["Les forces de l'ordre subissent beaucoup de violences : 5 463 gendarmes agressés physiquement en 2024.", "Dans 12 procédures relatives à des tirs en 2024, la justice a conclu à la légitimité de l'usage de l'arme.", "Les 47 décès comptent toutes les causes et ne sont pas tous imputables à des violences."],
 contre=[
  ("Ce sont des cas isolés.", "37 agents sanctionnés pour usage disproportionné en une seule année, et une condamnation par la CEDH : ce sont des faits reconnus par les institutions."),
  ("Parler de violences policières, c'est être contre la police.", "Les chiffres viennent de l'IGPN et du ministère de l'Intérieur eux-mêmes."),
 ],
 questions=["Savais-tu que l'IGPN elle-même a retenu un usage disproportionné de la force contre 37 policiers en 2024 ?", "Comment une police peut-elle garder la confiance si les abus ne sont pas reconnus ?"],
 limites=["Aucune donnée sur les condamnations pénales de policiers pour violences n'a été trouvée.", "Les 47 décès comptent toutes les causes ; aucune statistique officielle sur les policiers blessés en 2024 n'a été lue."],
 publics={'convaincus': "Ce n'est pas la gauche qui le dit, c'est l'IGPN elle-même : usage disproportionné de la force retenu contre 37 policiers en 2024. Et la Cour européenne a condamné la France pour violation du droit à la vie après la mort d'un manifestant. Reconnaître les abus, c'est protéger la majorité des policiers qui font bien leur travail.",
  'indecis': "Les policiers font un métier difficile et sont eux-mêmes souvent agressés. Mais les institutions reconnaissent des abus : sanctions de l'IGPN, contrôles discriminatoires documentés par le Défenseur des droits, condamnation de la CEDH. Les deux réalités existent."},
 a_actualiser='2027-10-31', raison="Rapport annuel 2025 de l'IGPN.",
))

# 16 ── Retraite par capitalisation ───────────────────────────────────────────
FICHES.append(fiche(
 id='retraite-capitalisation-rendement', affirmation="Une retraite par capitalisation rapporterait plus que la répartition.", volet='droits', sous_theme='Droits des travailleurs',
 mots_cles=['capitalisation', 'retraite par capitalisation', 'fonds de pension', 'repartition', 'retraite par repartition', 'epargne retraite', 'modele chilien', 'rendement retraite'],
 verdict='trompeur', fiabilite='interpretation',
 resume="Sur longue période, le rendement des placements dépasse souvent la croissance, donc le rendement de la répartition : le COR le reconnaît. Mais ce supplément s'accompagne d'un risque de fortes pertes, non mutualisé (−23 % en moyenne pour les fonds de pension de l'OCDE en 2008), de frais, et surtout d'une transition très coûteuse : il faudrait payer les pensions actuelles tout en épargnant pour les futures. Au Chili, l'État a dû compléter le système.",
 contexte="La capitalisation est mise en avant par des think tanks libéraux et une partie de la droite comme solution au financement des retraites.",
 explication="En répartition, les cotisations des actifs paient les pensions des retraités ; le rendement suit la croissance des salaires. En capitalisation, chacun épargne pour sa propre retraite, placée sur les marchés ; le rendement dépend de la Bourse au moment du départ.",
 sources=[COR_CAPI, COR_LAVIGNE, COR_OCDE, DF_OCDE08],
 faits=[
  fait("Selon le COR, la répartition offre « un rendement en moyenne égal à la croissance de l'économie », et le rendement du capital dépasse souvent la croissance à long terme, avec un « risque de fortes pertes en cas de crise ».", 'cor_capi', '2025', 'France', "La capitalisation rapporte plus en moyenne, mais avec un risque.", 'etabli'),
  fait("Sur 1950-2015, dans 16 pays, l'écart moyen entre rendement financier et croissance est de 2,68 %, mais « la mutualisation des risques financiers dans la capitalisation individuelle n'existe pas ».", 'cor_lavigne', '1950-2015', '16 pays', "Le gain moyen cache des pertes individuelles possibles.", 'estimation', '2,68 %'),
  fait("En 2008, les fonds de pension privés des pays de l'OCDE ont perdu en moyenne 23 % de leur valeur.", 'df_ocde08', '2008', 'OCDE', "Un krach au mauvais moment ampute la retraite.", 'etabli', '−23 %'),
  fait("Au Chili, l'État a financé la transition à hauteur d'environ 3,25 % du PIB par an, puis a dû créer une pension solidaire (2008) et une pension universelle garantie (2022).", 'cor_ocde', '1981-2022', 'Chili', "La capitalisation pure n'a pas suffi à garantir des pensions décentes.", 'estimation', '3,25 % du PIB'),
  fait("Une transition suppose une double cotisation des actifs, une mise à contribution des retraités ou une prise en charge par l'État.", 'cor_capi', '2025', 'France', "Une génération paierait deux fois.", 'etabli'),
 ],
 court="Trompeur : en moyenne, la Bourse rapporte plus que la croissance, mais sans protection collective (−23 % pour les fonds de pension en 2008), et passer à la capitalisation obligerait une génération à payer deux fois. Au Chili, l'État a dû compléter le système.",
 moyen="Le COR le reconnaît : sur longue période, les placements rapportent souvent plus que la croissance, qui fait le rendement de la répartition. Mais ce gain moyen cache un risque : en 2008, les fonds de pension ont perdu 23 % en moyenne, et celui qui part à la retraite après un krach n'a aucun filet.\n\nSurtout, il faudrait continuer à payer les retraites actuelles tout en épargnant pour les siennes : une double charge pendant des décennies. Au Chili, pionnier de la capitalisation, l'État a dû créer une pension publique pour compléter des retraites trop faibles.",
 detaille="En répartition, les cotisations d'aujourd'hui paient les pensions d'aujourd'hui, et le rendement suit, selon le COR, la croissance de l'économie. En capitalisation, chacun place son épargne ; sur 1950-2015, dans 16 pays, le rendement financier a dépassé la croissance de 2,68 points en moyenne.\n\nMais ce rendement n'est pas garanti pour chaque personne : en 2008, les fonds de pension privés de l'OCDE ont perdu 23 % en moyenne, et plus de 37 % en Irlande. Une économiste de l'université d'Orléans le résume pour le COR : « La mutualisation des risques financiers dans la capitalisation individuelle n'existe pas. »\n\nLe principal obstacle est la transition. Les retraités actuels doivent continuer à être payés : les actifs devraient cotiser deux fois, ou l'État s'endetter. Le Chili, qui a basculé en 1981, a financé ce déficit à hauteur d'environ 3,25 % du PIB par an, puis a dû créer une pension solidaire en 2008 et une pension universelle en 2022. En France, l'épargne retraite existe déjà en complément, pour ceux qui en ont les moyens.",
 empathie="Je comprends l'envie d'un système qui rapporte plus, surtout quand on doute de toucher une retraite correcte. Mais la Bourse peut aussi faire perdre beaucoup, et on ne choisit pas l'année de son départ.",
 legitimes=["Sur longue période, le rendement du capital dépasse souvent la croissance, ce que reconnaît le COR.", "La répartition comporte aussi un risque démographique et politique.", "Des fonds publics comme celui de la fonction publique ont obtenu de bons rendements selon une note versée au COR."],
 contre=[
  ("La Bourse finit toujours par remonter.", "Sur longue période en moyenne, oui ; mais celui qui part en retraite juste après un krach subit la perte, sans mutualisation."),
  ("Les autres pays l'ont fait.", "Le Chili a dû recréer une pension publique, et la Hongrie est revenue en arrière en 2011."),
 ],
 questions=["Qui paierait les retraites actuelles pendant que les actifs épargnent pour eux-mêmes ?", "Que se passe-t-il pour celui qui part à la retraite l'année d'un krach ?"],
 limites=["Les chiffres sur 2008 viennent d'un article de presse reprenant l'OCDE, la publication originale n'a pas été lue.", "Les pages chiffrées du Panorama des pensions 2025 de l'OCDE n'ont pas pu être lues."],
 publics={'convaincus': "En moyenne, la Bourse rapporte plus, c'est vrai. Mais en 2008, les fonds de pension ont perdu 23 % : si tu pars à la retraite cette année-là, tu perds une partie de ta pension, sans filet. Et pour changer de système, ta génération devrait payer deux fois : pour les retraités actuels et pour elle-même.",
  'indecis': "Ton inquiétude sur l'avenir des retraites est légitime. La capitalisation peut rapporter plus en moyenne, mais elle fait porter le risque à chacun, et la transition coûterait très cher. L'épargne retraite existe déjà en complément ; la question est de savoir si on veut remplacer la solidarité entre générations."},
 a_actualiser='2027-06-30', raison="Rapport annuel du COR.",
))

# 17 ── Essence et taxes ───────────────────────────────────────────────────────
FICHES.append(fiche(
 id='essence-prix-taxes', affirmation="Le prix de l'essence, ce sont surtout des taxes.", volet='economie', sous_theme='Fiscalité',
 mots_cles=['prix de l essence', 'taxes carburant', 'prix du carburant', 'ticpe', 'accise', 'taxes essence', 'prix du gazole', 'plein d essence'],
 verdict='plutot_exact', fiabilite='etabli',
 resume="Les taxes représentent environ la moitié du prix des carburants : 54 % en moyenne en 2024 pour le gazole et le SP95-E10, environ 49 % pour le SP95-E10 et 42 % pour le gazole fin octobre 2026. Leur part baisse quand le pétrole est cher, car l'accise est un montant fixe par litre. La France est dans la moyenne européenne, et le prix du pétrole raffiné pèse autant que les taxes.",
 contexte="L'argument revient à chaque hausse des prix à la pompe, contre l'État et contre la fiscalité écologique.",
 explication="Le prix à la pompe comprend le prix du produit raffiné (cotation de Rotterdam), les coûts de transport et de distribution, l'accise (ex-TICPE), fixe par litre et gelée depuis 2019, et la TVA à 20 %, qui s'applique aussi sur l'accise.",
 sources=[AN_CARB, CDE_CARB, CDE_UE, BDF_CARB],
 faits=[
  fait("L'accise et la TVA ont représenté en moyenne 54 % du prix TTC du gazole et du SP95-E10 en 2024.", 'an_carb', '2024', 'France', "Les taxes pèsent bien environ la moitié du prix.", 'etabli', '54 %'),
  fait("Fin octobre 2026, les taxes pèsent 42,3 % du prix du gazole et environ 48,6 % de celui du SP95-E10, tandis que la cotation du gazole raffiné représente 47,5 % de son prix.", 'cde_carb', 'octobre 2026', 'France', "Quand le pétrole est cher, il pèse autant que les taxes.", 'etabli', '42,3 %'),
  fait("L'accise est gelée depuis le 1er janvier 2019 ; comme elle est fixe par litre, la part des taxes baisse quand le pétrole monte.", 'an_carb', '2019-2025', 'France', "Les hausses récentes viennent du pétrole, pas des taxes.", 'etabli'),
  fait("En juillet 2026, la part des taxes sur l'essence était de 51 % en France, 53 % en Allemagne et en Italie, 54 % aux Pays-Bas et 38 % en Espagne.", 'cde_ue', 'juillet 2026', 'Union européenne', "La France est dans la moyenne de ses voisins.", 'etabli', '51 %'),
  fait("La marge nette des distributeurs est estimée à 1 ou 2 centimes par litre.", 'cde_carb', '2026', 'France', "Les stations-service gagnent peu sur le carburant.", 'estimation'),
 ],
 court="Plutôt vrai : les taxes font environ la moitié du prix (54 % en moyenne en 2024). Mais leur part baisse quand le pétrole flambe (42 % sur le gazole fin octobre 2026), l'accise est gelée depuis 2019, et la France est dans la moyenne européenne.",
 moyen="Les taxes représentent environ la moitié du prix des carburants : 54 % en moyenne en 2024 selon le gouvernement. C'est un poids réel pour les ménages qui dépendent de leur voiture.\n\nMais l'accise est gelée depuis 2019 et fixe par litre : quand les prix montent, c'est d'abord le pétrole qui augmente. Fin octobre 2026, le pétrole raffiné pesait 47,5 % du prix du gazole, plus que les taxes. Et la France taxe à peu près comme l'Allemagne ou l'Italie.",
 detaille="Selon une réponse ministérielle, l'accise sur les carburants et la TVA ont représenté en moyenne 54 % du prix du gazole et du SP95-E10 en 2024. La TVA s'applique aussi sur l'accise, ce qui alourdit la facture.\n\nMais cette part varie : l'accise est un montant fixe par litre, gelé depuis 2019. Quand le pétrole flambe, la part des taxes baisse : fin octobre 2026, elle était de 42,3 % pour le gazole, dont la cotation du produit raffiné représentait 47,5 % du prix. Les hausses récentes viennent donc surtout du pétrole.\n\nEn Europe, la France n'est pas une exception : en juillet 2026, la part des taxes sur l'essence était de 51 % en France, 53 % en Allemagne et en Italie, 54 % aux Pays-Bas, 38 % en Espagne. Le vrai débat porte sur la dépendance au pétrole et sur la répartition de l'effort : ceux qui n'ont pas d'autre choix que la voiture paient le plus.",
 empathie="Faire le plein est devenu un vrai poids pour beaucoup de gens, surtout à la campagne. Les taxes en sont une grosse part, c'est vrai ; mais ce sont surtout les prix du pétrole qui ont fait monter la facture ces dernières années.",
 legitimes=["Les taxes représentent environ la moitié du prix, et la TVA s'applique sur l'accise.", "L'État encaisse plus de TVA quand les prix montent.", "La France fait partie des cinq pays les plus chers de l'UE pour les carburants en juillet 2026."],
 contre=[
  ("Il suffit de baisser les taxes.", "C'est possible, mais l'accise rapporte des milliards à l'État ; une baisse générale profite aussi aux gros rouleurs aisés, une aide ciblée aux ménages modestes est plus juste."),
  ("Ce sont les écolos qui ont fait monter les prix.", "L'accise est gelée depuis 2019 : les hausses récentes viennent du pétrole."),
 ],
 questions=["Sais-tu que l'accise sur les carburants n'a pas augmenté depuis 2019 ?", "Pourquoi la part des taxes baisse-t-elle quand le pétrole devient plus cher ?"],
 limites=["Les données de 2026 viennent d'un site de vulgarisation reprenant les données officielles ; les pages du ministère et de l'UFIP n'ont pas été lues directement.", "Les parts varient chaque semaine avec le prix du pétrole."],
 publics={'convaincus': "Les taxes font bien environ la moitié du prix, tu as raison. Mais elles n'ont pas bougé depuis 2019 : quand le plein augmente, c'est le pétrole qui monte. Et les Allemands ou les Italiens paient autant de taxes que nous.",
  'indecis': "Les taxes représentent environ la moitié du prix des carburants, et c'est lourd pour ceux qui n'ont pas d'autre choix que la voiture. Mais les hausses récentes viennent surtout du pétrole. La vraie question est de réduire notre dépendance au pétrole et d'aider d'abord ceux qui en dépendent le plus."},
 a_actualiser='2027-03-31', raison="Prix des carburants très variables.",
))

# 18 ── 35 heures ──────────────────────────────────────────────────────────────
FICHES.append(fiche(
 id='trente-cinq-heures-ruine', affirmation="Les 35 heures ont ruiné la France.", volet='social', sous_theme='Emploi et salaires',
 mots_cles=['35 heures', 'trente-cinq heures', 'lois aubry', 'reduction du temps de travail', 'rtt', '35h', 'temps de travail', 'aubry 35 heures'],
 verdict='contredit', fiabilite='interpretation',
 resume="Les évaluations retiennent environ 350 000 emplois créés par les lois Aubry, pour un coût net pour les finances publiques d'environ 2,5 milliards d'euros par an selon le rapport parlementaire de 2014. Le bilan reste débattu : les allègements de cotisations coûtent environ 12 milliards par an en brut selon le Conseil d'analyse économique, et le passage aux 35 heures a été difficile à l'hôpital. Mais parler de ruine n'est pas fondé.",
 contexte="Les 35 heures sont souvent présentées comme la cause du déclin économique français et un symbole de la « paresse » de la gauche.",
 explication="Les lois Aubry (1998-2000) ont réduit la durée légale du travail de 39 à 35 heures, en échange d'allègements de cotisations et d'une plus grande flexibilité. La durée légale est le seuil de déclenchement des heures supplémentaires, pas un plafond.",
 sources=[AN_35H, IRES_35H, IM_35H, INSEE_DUREE],
 faits=[
  fait("Selon le rapport parlementaire de 2014, « le chiffre de 350 000 est le plus communément admis » pour les emplois créés par les 35 heures.", 'an_35h', '1998-2002', 'France', "Les 35 heures ont créé des emplois.", 'estimation', '350 000'),
  fait("Le coût net ex post pour les finances publiques est estimé à environ 2,5 milliards d'euros par an.", 'an_35h', 'ex post', 'France', "Le coût net est limité.", 'estimation', '2,5 Md€'),
  fait("Selon le Conseil d'analyse économique, cité par l'Institut Montaigne, le coût brut des 35 heures dans le privé est estimé à 12 milliards d'euros par an, surtout en allègements de cotisations.", 'im_35h', 'par an', 'Secteur privé', "Le coût brut est élevé.", 'estimation', '12 Md€'),
  fait("Pour les entreprises, le coût est jugé « à peu près neutre », grâce à la modération salariale et aux gains de productivité.", 'ires_35h', '1996-2002', 'France', "Les salariés ont payé une partie de la réforme par des salaires plus modérés.", 'estimation'),
  fait("En 2025, la durée habituelle hebdomadaire des salariés à temps complet est de 38,9 heures.", 'insee_duree', '2025', 'France', "Les salariés à temps plein travaillent bien plus que 35 heures.", 'etabli', '38,9 h'),
 ],
 court="Faux : les évaluations retiennent environ 350 000 emplois créés, pour un coût net de 2,5 milliards par an. Le coût brut des allègements (12 milliards) et les difficultés à l'hôpital sont de vrais débats, mais pas une ruine. Et les salariés à temps plein travaillent 38,9 heures en moyenne.",
 moyen="Les 35 heures ont créé environ 350 000 emplois selon le chiffre le plus admis, retenu par le rapport parlementaire de 2014. Leur coût net pour les finances publiques est estimé à 2,5 milliards par an, car les emplois créés rapportent des cotisations.\n\nLe bilan est discuté : le coût brut des allègements est élevé, et l'hôpital a mal vécu la réforme. Mais aujourd'hui, un salarié à temps plein travaille en moyenne 38,9 heures par semaine : les 35 heures sont un seuil pour les heures supplémentaires, pas un plafond.",
 detaille="Les lois Aubry ont abaissé la durée légale du travail à 35 heures entre 1998 et 2002. Les évaluations, reprises par la commission d'enquête de l'Assemblée en 2014, retiennent environ 350 000 emplois créés à court terme. Le coût net pour les finances publiques est estimé à environ 2,5 milliards d'euros par an, et le coût pour les entreprises jugé à peu près neutre, grâce à la modération salariale et aux gains de productivité.\n\nLe débat est réel. Le Conseil d'analyse économique estime le coût brut des allègements de cotisations à 12 milliards par an, et juge l'effet de la seule baisse de la durée légale « au mieux très marginal ». Dans la fonction publique hospitalière, le passage aux 35 heures a été un « facteur de crispation », avec des jours accumulés sur les comptes épargne-temps. Le président de la commission de 2014 ne partageait pas les conclusions du rapport.\n\nMais aucune de ces évaluations ne parle de ruine. En 2025, les salariés à temps complet travaillent en moyenne 38,9 heures par semaine, car les heures supplémentaires sont possibles au-delà de 35 heures.",
 empathie="Je comprends que les 35 heures soient devenues un symbole, en bien ou en mal. Les évaluations sérieuses donnent un bilan contrasté, mais aucune ne parle de ruine.",
 legitimes=["Le coût brut des allègements de cotisations est élevé (12 Md€ par an selon le CAE).", "Le passage aux 35 heures a été difficile à l'hôpital.", "Les évaluations sont discutées, y compris au sein de la commission d'enquête de 2014."],
 contre=[
  ("Les Français ne travaillent plus assez à cause des 35 heures.", "Les salariés à temps plein travaillent en moyenne 38,9 heures par semaine en 2025 selon l'Insee."),
  ("Les entreprises ont payé la facture.", "Selon les évaluations, le coût pour elles a été à peu près neutre, grâce aux allègements, à la flexibilité et à la modération des salaires."),
 ],
 questions=["Sais-tu combien d'heures travaille en moyenne un salarié à temps plein aujourd'hui ?", "Combien d'emplois les 35 heures ont-elles créé selon le rapport de 2014 ?"],
 limites=["Les évaluations datent de 2004 à 2014 ; aucune publication de la Dares n'a été lue directement.", "Le chiffre de 12 Md€ du CAE est cité de seconde main par l'Institut Montaigne."],
 publics={'convaincus': "Les 35 heures ont créé environ 350 000 emplois selon les évaluations retenues par l'Assemblée, pour un coût net de 2,5 milliards par an. Et un salarié à temps plein travaille en moyenne 38,9 heures aujourd'hui. On peut critiquer leur coût ou leur effet à l'hôpital, mais la France n'a pas été ruinée.",
  'indecis': "Le bilan des 35 heures est discuté : des emplois créés, un coût réel pour les finances publiques, des difficultés à l'hôpital. Mais aucune évaluation sérieuse ne parle de ruine. Les 35 heures sont un seuil pour les heures supplémentaires, pas un plafond."},
 a_actualiser='2027-07-31', raison="Nouvelles données de l'Insee sur la durée du travail.",
))

# 19 ── Électricité et marché européen ────────────────────────────────────────
FICHES.append(fiche(
 id='electricite-prix-marche-europeen', affirmation="On paie l'électricité plus cher à cause du marché européen.", volet='ecologie', sous_theme='Prix de l’énergie',
 mots_cles=['prix de l electricite', 'marche europeen de l electricite', 'facture d electricite', 'arenh', 'prix marginal', 'tarif reglemente', 'electricite trop chere', 'sortir du marche europeen'],
 verdict='trompeur', fiabilite='etabli',
 resume="Le mécanisme européen du prix marginal, qui aligne le prix de gros sur la dernière centrale appelée, souvent au gaz, a bien transmis la flambée du gaz en 2022. Mais les ménages français ont payé leur électricité 22 % moins cher que la moyenne de l'UE en 2022 et 13 % moins cher en 2025, grâce au bouclier tarifaire et à l'ARENH. En 2025, le prix de gros français est parmi les plus bas d'Europe et la France a exporté un record d'électricité.",
 contexte="Le RN et une partie de la gauche réclament de sortir du marché européen de l'électricité ; l'argument a pris de la force avec la crise de 2022.",
 explication="Sur le marché de gros européen, le prix est fixé par la centrale la plus chère nécessaire pour répondre à la demande. Les tarifs réglementés français sont calculés à partir de ces prix ; jusqu'à fin 2025, l'ARENH permettait d'acheter une partie du nucléaire d'EDF à 42 €/MWh.",
 sources=[SENAT_ELEC, SDES_ELEC22, SDES_ELEC25, CRE_2026],
 faits=[
  fait("Sur le marché de gros européen, « les prix sont déterminés par le coût de production de la dernière centrale appelée », souvent au gaz ou au charbon.", 'senat_elec', '2023', 'Union européenne', "La crise du gaz s'est transmise aux prix de l'électricité.", 'etabli'),
  fait("En 2022, le prix spot moyen a atteint 279 €/MWh, multiplié par 2,6 en un an.", 'sdes_elec22', '2022', 'France', "La flambée de 2022 a été très forte.", 'etabli', '279 €/MWh'),
  fait("Les ménages français ont payé des prix inférieurs de 22 % à la moyenne de l'UE en 2022, et de 13 % en 2025.", 'sdes_elec25', '2022-2025', 'France et UE', "Les Français paient moins que la moyenne européenne.", 'etabli', '−13 %'),
  fait("En 2025, le prix spot français est de 61 €/MWh et la France a exporté un record net de 92,3 TWh ; elle est « parmi les marchés de gros d'électricité avec les prix les moins chers ».", 'cre_2026', '2025', 'France', "Le marché profite aussi à la France, qui exporte.", 'etabli', '92,3 TWh'),
  fait("Depuis la fin de l'ARENH au 31 décembre 2025, les tarifs réglementés sont calculés à 100 % sur les prix de gros ; ils sont restés stables au 1er février 2026 (−0,83 %).", 'cre_2026', '2026', 'France', "La protection de l'ARENH a disparu, mais les prix de gros sont bas.", 'etabli'),
 ],
 court="Trompeur : le marché européen a bien transmis la flambée du gaz en 2022, mais les ménages français ont payé 22 % de moins que la moyenne de l'UE en 2022 et 13 % de moins en 2025. En 2025, la France est parmi les prix de gros les plus bas et exporte un record.",
 moyen="La règle européenne du prix marginal a bien fait flamber les prix de gros en 2022, quand le gaz est devenu très cher : c'est une critique sérieuse, partagée par le Sénat.\n\nMais les ménages français ont été protégés par le bouclier tarifaire et l'ARENH : ils ont payé 22 % moins cher que la moyenne européenne en 2022, et encore 13 % moins cher en 2025. Et en 2025, la France vend énormément d'électricité à ses voisins grâce au marché.",
 detaille="Sur le marché de gros européen, le prix est fixé par la dernière centrale appelée, souvent au gaz. En 2022, la flambée du gaz a donc fait exploser les prix de gros, jusqu'à 279 €/MWh en moyenne en France. Le Sénat a critiqué ce mécanisme et regretté que la réforme européenne le conserve.\n\nLes Français ont toutefois été protégés : le bouclier tarifaire a limité la hausse des tarifs réglementés, et l'ARENH permettait d'acheter une partie du nucléaire à 42 €/MWh. Résultat, selon le ministère : les ménages ont payé 22 % moins cher que la moyenne de l'UE en 2022, et 13 % moins cher en 2025.\n\nDepuis, le marché joue en faveur de la France : en 2025, son prix de gros (61 €/MWh) est parmi les plus bas d'Europe, et elle a exporté un record net de 92,3 TWh. La fin de l'ARENH au 31 décembre 2025 supprime une protection, et la question d'un prix de l'électricité qui reflète les coûts du parc français reste un vrai débat.",
 empathie="La facture d'électricité a beaucoup augmenté depuis 2021, et la colère est légitime. Le marché européen y a joué un rôle en 2022, mais les Français paient quand même moins que la moyenne des Européens.",
 legitimes=["Le prix marginal a propagé la flambée du gaz malgré un parc largement nucléaire.", "Les tarifs réglementés ont nettement augmenté entre 2021 et 2023.", "Depuis la fin de l'ARENH, le tarif réglementé suit entièrement les prix de gros."],
 contre=[
  ("Avec notre nucléaire, on devrait payer bien moins.", "C'est un vrai débat sur la façon de fixer les prix ; mais les ménages français paient déjà 13 % moins que la moyenne de l'UE."),
  ("Il faut sortir du marché européen.", "En 2025, la France y a exporté un record net de 92,3 TWh : le marché lui sert aussi à vendre son électricité."),
 ],
 questions=["Savais-tu que les ménages français paient leur électricité moins cher que la moyenne européenne ?", "Comment fixer un prix qui reflète les coûts du nucléaire tout en restant connecté aux voisins ?"],
 limites=["La base Eurostat n'a pas été lue directement : les comparaisons viennent du service statistique du ministère.", "Le rôle des arrêts de réacteurs en 2022 dans la flambée n'est pas documenté dans les sources lues."],
 publics={'convaincus': "En 2022, le marché européen a bien fait flamber les prix, tu as raison de le critiquer. Mais les ménages français paient 13 % de moins que la moyenne européenne en 2025, et la France vend un record d'électricité à ses voisins grâce à ce marché. Le vrai combat, c'est un prix qui reflète les coûts de notre parc, pas le repli.",
  'indecis': "Le marché européen a transmis la crise du gaz en 2022, mais les protections françaises ont limité la hausse : les ménages paient moins que la moyenne de l'UE. Le débat porte maintenant sur l'après-ARENH : comment garder des prix stables et justes."},
 a_actualiser='2027-02-28', raison="Évolution des tarifs réglementés après la fin de l'ARENH.",
))

# 20 ── Jeunes des quartiers et travail ───────────────────────────────────────
FICHES.append(fiche(
 id='banlieues-jeunes-travailler', affirmation="Dans les banlieues, les jeunes ne veulent pas travailler.", volet='social', sous_theme='Chômage',
 mots_cles=['banlieues travailler', 'jeunes de banlieue', 'quartiers prioritaires', 'jeunes des cites', 'qpv chomage', 'jeunes ne veulent pas travailler', 'cites emploi', 'chomage des quartiers'],
 verdict='contredit', fiabilite='etabli',
 resume="Le chômage des jeunes est deux fois plus élevé dans les quartiers prioritaires (25,6 % contre 13,5 % pour les moins de 30 ans en 2022), y compris à diplôme égal. Or être au chômage, c'est chercher un emploi. Un testing publié par l'Insee montre des discriminations à l'embauche pour les hommes d'origine maghrébine qui y résident. L'inactivité y est réellement plus forte, notamment chez les femmes.",
 contexte="Le cliché vise les jeunes des quartiers populaires, souvent issus de l'immigration, présentés comme vivant d'aides ou de trafics.",
 explication="Les quartiers prioritaires de la politique de la ville (QPV) concentrent pauvreté, faible niveau de diplôme et éloignement des emplois. Le chômage mesure ceux qui cherchent activement un emploi ; l'inactivité regroupe ceux qui n'en cherchent pas, pour des raisons diverses.",
 sources=[OI_QPV, BDT_QPV, INSEE_TESTING],
 faits=[
  fait("En 2022, le chômage des actifs de moins de 30 ans est de 25,6 % dans les quartiers prioritaires contre 13,5 % dans les autres quartiers des mêmes villes.", 'oi_qpv', '2022', 'QPV', "Beaucoup de jeunes des quartiers cherchent un emploi sans en trouver.", 'etabli', '25,6 %'),
  fait("À diplôme égal (bac+2 et plus), le chômage est de 11,1 % dans les quartiers prioritaires contre 5 % ailleurs.", 'oi_qpv', '2022', 'QPV', "Le diplôme ne suffit pas à effacer l'écart.", 'etabli', '11,1 %'),
  fait("Dans un testing auprès de 3 000 entreprises, les hommes d'origine maghrébine résidant en quartier prioritaire reçoivent 2,60 % de réponses positives contre 4,80 % pour un candidat d'origine française.", 'insee_testing', '2021', 'Métropole de Lille', "Les discriminations à l'embauche existent.", 'etabli', '2,60 % contre 4,80 %'),
  fait("En 2024, 18,3 % des habitants des quartiers prioritaires souhaitent travailler sans avoir d'emploi, et 21,8 % des jeunes n'y sont ni en emploi, ni en études, ni en formation, contre 11,2 % ailleurs.", 'bdt_qpv', '2024', 'QPV', "Le décrochage est réel, mais beaucoup veulent travailler.", 'etabli', '21,8 %'),
  fait("Le chômage dans les quartiers prioritaires est passé de 25 % en 2014 à 18,3 % en 2022.", 'oi_qpv', '2014-2022', 'QPV', "Quand l'emploi progresse, il progresse aussi dans les quartiers.", 'etabli'),
 ],
 court="Faux : le chômage des moins de 30 ans est deux fois plus élevé dans les quartiers prioritaires (25,6 % contre 13,5 %), y compris à diplôme égal, et un testing montre des discriminations à l'embauche. Un chômeur cherche du travail ; l'inactivité est plus forte, mais ne prouve pas un refus.",
 moyen="Dans les quartiers prioritaires, le chômage des jeunes est deux fois plus élevé qu'ailleurs, même à diplôme égal. Être au chômage, c'est chercher un emploi : le problème n'est pas l'envie de travailler, mais l'accès à l'emploi.\n\nUn testing publié par l'Insee le montre : à CV équivalent, un jeune homme d'origine maghrébine habitant un quartier prioritaire reçoit presque deux fois moins de réponses positives. Quand l'économie va mieux, le chômage y baisse : de 25 % en 2014 à 18,3 % en 2022.",
 detaille="Selon l'Observatoire national de la politique de la ville, le chômage des actifs de moins de 30 ans atteint 25,6 % dans les quartiers prioritaires en 2022, contre 13,5 % dans les autres quartiers des mêmes villes. L'écart persiste à diplôme égal : 11,1 % contre 5 % pour les diplômés du supérieur.\n\nLes discriminations y contribuent : dans un testing auprès de 3 000 entreprises de la métropole lilloise, publié par l'Insee, les hommes d'origine maghrébine résidant en quartier prioritaire obtiennent 2,60 % de réponses positives, contre 4,80 % pour un candidat d'origine française. Les auteurs notent que l'adresse seule n'est pas pénalisante pour un candidat d'origine française.\n\nL'inactivité est réellement plus forte dans ces quartiers : 40,2 % des 15-64 ans contre 24,3 % ailleurs, d'abord chez les femmes, et 21,8 % des jeunes n'y sont ni en emploi, ni en études, ni en formation. Mais 18,3 % des habitants souhaitent travailler sans avoir d'emploi, et le chômage y a nettement reculé depuis 2014 : les jeunes des quartiers saisissent les emplois quand ils existent.",
 empathie="Je comprends que certaines images de jeunes qui traînent en bas des immeubles marquent les esprits. Mais les chiffres montrent surtout des jeunes qui cherchent du travail et en trouvent moins, même avec des diplômes.",
 legitimes=["L'inactivité est beaucoup plus forte dans les quartiers prioritaires (40,2 % contre 24,3 %).", "La part des jeunes ni en emploi, ni en études, ni en formation y est près de deux fois plus élevée."],
 contre=[
  ("Ils préfèrent les trafics.", "Rien dans les données lues ne le montre ; le chômage des jeunes des quartiers mesure ceux qui cherchent activement un emploi."),
  ("Ils n'ont qu'à faire des études.", "À diplôme égal, le chômage reste deux fois plus élevé dans les quartiers prioritaires."),
 ],
 questions=["Savais-tu qu'à diplôme égal, le chômage est deux fois plus élevé dans les quartiers prioritaires ?", "Que ferais-tu si tu envoyais des dizaines de CV sans réponse ?"],
 limites=["Les chiffres de l'ONPV sont repris par l'Observatoire des inégalités et la presse, le rapport n'a pas été lu directement.", "Le testing porte sur une seule métropole et date de 2021."],
 publics={'convaincus': "Un chômeur, par définition, cherche du travail : et dans les quartiers, un jeune sur quatre cherche sans trouver, même avec un diplôme. Un testing de l'Insee montre qu'à CV équivalent, un jeune d'origine maghrébine qui y habite reçoit presque deux fois moins de réponses. Et quand l'emploi repart, le chômage y baisse aussi.",
  'indecis': "Il y a un vrai problème d'emploi dans les quartiers prioritaires, avec plus d'inactivité et de décrochage. Mais les données montrent surtout un chômage deux fois plus élevé à diplôme égal et des discriminations à l'embauche. La solution passe par l'accès à l'emploi, pas par le soupçon."},
 a_actualiser='2027-07-31', raison="Rapport annuel de l'Observatoire national de la politique de la ville.",
))

# 21 ── Migrants à l'hôtel, SDF dehors ────────────────────────────────────────
FICHES.append(fiche(
 id='migrants-hotel-sdf', affirmation="On loge les migrants à l'hôtel pendant que les SDF français dorment dehors.", volet='immigration', sous_theme='Logement',
 mots_cles=['sdf francais', 'sans abri francais', 'migrants a l hotel', 'migrants loges', 'sdf dehors', 'hebergement d urgence', '115', 'sans domicile'],
 verdict='trompeur', fiabilite='etabli',
 resume="L'hébergement d'urgence est ouvert à toute personne sans abri en détresse, sans condition de nationalité ; il n'existe pas de priorité pour les migrants. Le système est saturé pour tout le monde : selon la Fondation pour le logement des défavorisés, environ 350 000 personnes sont sans domicile, dont 40 000 à la rue, et au moins 2 159 enfants sont restés sans solution après un appel au 115 une nuit d'août 2025. Les étrangers sont majoritaires parmi les sans-domicile (53 % en 2012).",
 contexte="L'argument oppose les sans-abri français aux exilés, notamment lors de l'ouverture de centres d'accueil ou après des drames de la rue.",
 explication="L'hébergement d'urgence (le 115) relève de l'article L. 345-2-2 du code de l'action sociale et des familles, qui vise « toute personne sans abri ».",
 sources=[CE_HEBERG, INSEE_SDF, PS_MALLOG, FAS_ENFANTS, SENAT_P177],
 faits=[
  fait("Selon le code de l'action sociale, « toute personne sans abri en situation de détresse médicale, psychique et sociale a accès, à tout moment, à un dispositif d'hébergement d'urgence ».", 'ce_heberg', 'droit en vigueur', 'France', "Le droit à l'hébergement ne dépend pas de la nationalité.", 'etabli'),
  fait("En 2012, 53 % des sans-domicile étaient étrangers, contre 38 % en 2001 ; 12 % des sans-domicile étaient hébergés à l'hôtel.", 'insee_sdf', '2012', 'France métropolitaine', "Les étrangers sont eux-mêmes majoritaires parmi les sans-domicile.", 'etabli', '53 %'),
  fait("La Fondation pour le logement des défavorisés estime à environ 350 000 les personnes sans domicile, dont 40 000 à la rue, et signale plus de 900 décès de personnes sans abri en 2025.", 'ps_mallog', '2025-2026', 'France', "La pénurie touche tout le monde.", 'estimation', '350 000'),
  fait("La nuit du 18 août 2025, au moins 2 159 enfants sont restés sans solution après un appel au 115.", 'fas_enfants', '2025', 'France', "Le manque de places est massif, y compris pour les enfants.", 'estimation', '2 159 enfants'),
  fait("En 2025, le Parlement comptait 203 000 places d'hébergement généraliste, mais les crédits de l'hébergement d'urgence baissaient de 25 %.", 'senat_p177', '2025', 'France', "La pénurie est aussi un choix budgétaire.", 'etabli', '203 000 places'),
 ],
 court="Trompeur : l'hébergement d'urgence est ouvert à toute personne sans abri, sans condition de nationalité, et il manque de places pour tous : 2 159 enfants sans solution une nuit d'août 2025. Les étrangers sont d'ailleurs majoritaires parmi les sans-domicile (53 % en 2012).",
 moyen="Il n'y a pas de priorité pour les migrants : la loi garantit l'hébergement d'urgence à « toute personne sans abri » en détresse, français ou étranger. Le problème, c'est qu'il manque de places pour tout le monde.\n\nUne nuit d'août 2025, au moins 2 159 enfants n'ont pas trouvé de place après un appel au 115. Et parmi les sans-domicile, les étrangers sont majoritaires : 53 % en 2012. Opposer les uns aux autres cache le vrai sujet : le manque de moyens.",
 detaille="Le droit français ne fait pas de tri : selon l'article L. 345-2-2 du code de l'action sociale et des familles, toute personne sans abri en situation de détresse a accès à tout moment à un hébergement d'urgence. Le Conseil d'État en a fait une liberté fondamentale, dans une affaire concernant un ressortissant étranger.\n\nLa réalité, c'est la saturation. La Fondation pour le logement des défavorisés estime à environ 350 000 les personnes sans domicile ou en hébergement d'urgence, dont 40 000 à la rue, et signale plus de 900 décès de personnes sans abri en 2025. Une nuit d'août 2025, au moins 2 159 enfants sont restés sans solution après un appel au 115. Pendant ce temps, les crédits de l'hébergement d'urgence baissaient de 25 % en 2025.\n\nSelon la dernière grande enquête de l'Insee (2012), 53 % des sans-domicile étaient étrangers, et 12 % étaient hébergés à l'hôtel. Les sans-abri français et étrangers sont victimes de la même pénurie : c'est elle qu'il faut combattre.",
 empathie="Voir des gens dormir dehors dans le froid est insupportable, et c'est normal de se demander pourquoi on ne les aide pas. Mais les étrangers sont eux-mêmes nombreux à dormir dehors : la vraie cause, c'est le manque de places.",
 legitimes=["Les étrangers sont majoritaires parmi les sans-domicile, ce qui pèse sur un système saturé.", "Les nuitées d'hôtel sont très utilisées, surtout dans les métropoles."],
 contre=[
  ("Les migrants passent avant les Français au 115.", "La loi ne prévoit aucune priorité selon la nationalité, et des milliers d'enfants, de toutes origines, restent sans solution."),
  ("Si on arrêtait l'immigration, il y aurait de la place.", "Les crédits de l'hébergement d'urgence baissent de 25 % en 2025 : la pénurie est aussi un choix budgétaire."),
 ],
 questions=["Savais-tu que l'hébergement d'urgence est ouvert à toute personne sans abri, sans condition de nationalité ?", "Combien d'enfants dorment dehors faute de place, selon toi ?"],
 limites=["La dernière enquête nationale de l'Insee sur les sans-domicile date de 2012.", "Le dispositif propre aux demandeurs d'asile n'a pas pu être documenté (pages de la Cour des comptes et de la DREES inaccessibles) ; le rapport de la Fondation a été lu via Public Sénat."],
 publics={'convaincus': "Personne ne passe devant au 115 selon sa nationalité : la loi vise toute personne sans abri. Une nuit d'août 2025, plus de 2 000 enfants n'ont pas eu de place, et les étrangers sont eux-mêmes majoritaires parmi les sans-domicile. Ce qui manque, ce sont des places, et leur budget a baissé de 25 % en 2025.",
  'indecis': "La colère devant les sans-abri est juste. Mais il n'y a pas de priorité pour les migrants : l'hébergement d'urgence manque de places pour tout le monde, Français comme étrangers. La solution passe par plus de places et de logements, pas par une concurrence entre pauvres."},
 a_actualiser='2027-02-28', raison="Rapport annuel sur le mal-logement.",
))

# 22 ── Migrants climatiques ──────────────────────────────────────────────────
FICHES.append(fiche(
 id='migrants-climatiques-europe', affirmation="Des centaines de millions de migrants climatiques vont envahir l'Europe.", volet='ecologie', sous_theme='Justice climatique',
 mots_cles=['migrants climatiques', 'refugies climatiques', 'migration climatique', '216 millions', 'deplaces climatiques', 'rechauffement migrations', 'invasion climatique', 'deplaces internes'],
 verdict='contredit', fiabilite='etabli',
 resume="Le chiffre souvent cité, 216 millions de migrants climatiques d'ici 2050 (Banque mondiale), concerne des migrations à l'intérieur des pays en développement, pas vers l'Europe, et il pourrait être réduit de 80 % par une action rapide sur les émissions. Aujourd'hui, la plupart des personnes déplacées restent dans leur pays ou dans un pays voisin : 66 % des réfugiés sont accueillis par un pays voisin.",
 contexte="L'argument combine la peur de l'immigration et le changement climatique, parfois pour justifier une fermeture totale des frontières.",
 explication="Les catastrophes climatiques provoquent surtout des déplacements de courte distance, souvent temporaires, à l'intérieur des pays. Les migrations internationales lointaines demandent des ressources que les plus pauvres n'ont généralement pas.",
 sources=[BM_GROUND, IDMC26, HCR_FIG, EN_IDMC25],
 faits=[
  fait("Selon la Banque mondiale, le changement climatique pourrait contraindre 216 millions de personnes à migrer « à l'intérieur de leur pays » d'ici 2050, dans le monde en développement.", 'bm_ground', 'projection 2050', 'Pays en développement', "Le chiffre ne concerne pas des arrivées en Europe.", 'estimation', '216 millions'),
  fait("Cette projection pourrait être réduite jusqu'à 80 % avec une action rapide pour réduire les émissions mondiales.", 'bm_ground', 'projection 2050', 'Monde', "L'ampleur dépend de nos choix climatiques.", 'estimation', '80 %'),
  fait("En 2025, 29,9 millions de déplacements liés aux catastrophes ont été enregistrés, et 13,6 millions de personnes vivaient en déplacement lié à une catastrophe à la fin de l'année.", 'idmc26', '2025', 'Monde', "Les déplacements liés aux catastrophes sont surtout internes.", 'etabli', '29,9 millions'),
  fait("Mi-2025, 66 % des réfugiés étaient accueillis dans des pays voisins, et 71 % dans des pays à revenu faible ou intermédiaire.", 'hcr_fig', '2025', 'Monde', "Les personnes déplacées restent surtout près de chez elles.", 'etabli', '66 %'),
  fait("En 2024, les États-Unis ont enregistré 11 millions de déplacements liés aux catastrophes, le plus grand nombre au monde.", 'en_idmc25', '2024', 'Monde', "Les pays riches sont aussi touchés.", 'etabli', '11 millions'),
 ],
 court="Faux : les 216 millions de la Banque mondiale sont des migrations à l'intérieur des pays en développement d'ici 2050, réductibles de 80 % par l'action climatique. Les déplacés restent surtout chez eux ou dans un pays voisin (66 % des réfugiés).",
 moyen="Le chiffre de 216 millions vient de la Banque mondiale, mais il porte sur des migrations à l'intérieur des pays en développement d'ici 2050, pas sur des arrivées en Europe. Et il pourrait baisser de 80 % si le monde réduit vite ses émissions.\n\nAujourd'hui, les catastrophes déplacent surtout des gens à l'intérieur de leur pays, souvent pour peu de temps. Les réfugiés sont accueillis à 66 % par un pays voisin, et à 71 % par des pays pauvres ou intermédiaires.",
 detaille="En 2021, la Banque mondiale a estimé que le changement climatique pourrait contraindre jusqu'à 216 millions de personnes à migrer à l'intérieur de leur pays d'ici 2050 : jusqu'à 86 millions en Afrique subsaharienne, 49 en Asie de l'Est, 40 en Asie du Sud, 19 en Afrique du Nord. Ce sont des projections conditionnelles, réductibles jusqu'à 80 % par une action rapide sur les émissions.\n\nLes données actuelles confirment que les déplacements liés au climat sont surtout internes : 29,9 millions de déplacements liés aux catastrophes en 2025 selon l'IDMC, dont beaucoup d'évacuations temporaires. Les pays riches sont aussi touchés : les États-Unis ont enregistré 11 millions de déplacements de ce type en 2024.\n\nPour les migrations internationales, le HCR rappelle que 66 % des réfugiés vivent dans un pays voisin du leur. Le changement climatique est une menace sérieuse, aussi pour les migrations ; la meilleure façon de limiter les déplacements est de réduire les émissions et d'aider les régions les plus exposées à s'adapter.",
 empathie="L'inquiétude face au changement climatique et à ses conséquences est légitime. Mais les chiffres alarmants qu'on entend portent sur des migrations à l'intérieur des pays du Sud, pas sur une arrivée massive en Europe.",
 legitimes=["Les déplacements liés aux catastrophes ont atteint un record en 2024 (45,8 millions de mouvements).", "Une partie des migrations internes peut, à terme, devenir internationale."],
 contre=[
  ("216 millions, ce sont autant de gens qui vont venir.", "Le rapport parle de migrations « à l'intérieur de leur pays » ; seule une petite part des déplacés franchit une frontière, et surtout vers un pays voisin."),
  ("Ça ne sert à rien de lutter contre le climat.", "Selon la Banque mondiale, une action rapide pourrait réduire ces migrations jusqu'à 80 %."),
 ],
 questions=["Savais-tu que les 216 millions de la Banque mondiale sont des migrations internes ?", "Quelle est la meilleure façon de limiter les déplacements dus au climat ?"],
 limites=["Les projections Groundswell datent de 2021 et dépendent des scénarios retenus.", "Aucune source primaire du GIEC n'a été lue pour cette fiche."],
 publics={'convaincus': "Les 216 millions dont on parle, ce sont des gens qui migreraient à l'intérieur de leur propre pays, selon la Banque mondiale elle-même. Aujourd'hui, deux réfugiés sur trois restent dans un pays voisin. Et si tu veux vraiment limiter ces migrations, le moyen le plus efficace, c'est de réduire les émissions : jusqu'à 80 % de déplacements en moins.",
  'indecis': "Le changement climatique va pousser des millions de personnes à se déplacer, c'est une vraie inquiétude. Mais l'essentiel restera à l'intérieur des pays ou dans les régions voisines. Réduire les émissions et aider les pays exposés à s'adapter, c'est ce qui limite le plus ces déplacements."},
 a_actualiser='2027-06-30', raison="Rapport annuel de l'IDMC.",
))

# 23 ── La Chine pollue plus ──────────────────────────────────────────────────
FICHES.append(fiche(
 id='chine-pollue-efforts-inutiles', affirmation="La Chine pollue bien plus que nous, nos efforts pour le climat ne servent à rien.", volet='ecologie', sous_theme='Émissions de gaz à effet de serre',
 mots_cles=['la chine pollue', 'chine pollue plus', 'nos efforts ne servent a rien', 'chine co2', 'france 1 % des emissions', 'emissions chinoises', 'empreinte carbone', 'ca sert a rien l ecologie'],
 verdict='trompeur', fiabilite='etabli',
 resume="La Chine émet bien 32 % du CO2 fossile mondial, contre 6 % pour l'Union européenne. Mais l'empreinte carbone d'un Français (8,3 tonnes) est proche de celle d'un Chinois, et plus de la moitié vient de produits importés, souvent fabriqués en Chine. Les Européens ont émis par habitant trois fois plus que les Chinois depuis 1850, et 35 pays ont réduit leurs émissions tout en faisant croître leur économie.",
 contexte="L'argument sert à rejeter les politiques climatiques françaises et européennes comme inutiles et coûteuses.",
 explication="Les émissions « territoriales » comptent ce qui est émis sur le sol d'un pays ; l'« empreinte carbone » ajoute les émissions des produits importés et retire celles des exportations. Le climat dépend des émissions cumulées depuis le XIXe siècle.",
 sources=[GCP25, GCP_KEY, SDES_EMP, CB_CUMUL, OWID_FR],
 faits=[
  fait("En 2025, la Chine représente 32 % des émissions mondiales de CO2 fossile, les États-Unis 13 %, l'Inde 8 % et l'Union européenne 6 %.", 'gcp25', '2025', 'Monde', "La Chine est de loin le premier émetteur annuel.", 'etabli', '32 %'),
  fait("L'empreinte carbone d'un Français est estimée à 8,3 t CO2 éq en 2025, légèrement inférieure à celle d'un Européen (9,0 t) et d'un Chinois ; 52 % provient d'émissions importées.", 'sdes_emp', '2025', 'France', "Une partie des émissions chinoises sert à produire ce que nous consommons.", 'estimation', '8,3 t'),
  fait("Depuis 1850, les émissions cumulées par habitant sont de 227 t de CO2 en Chine, 682 t dans l'UE à 27 et 1 570 t aux États-Unis.", 'cb_cumul', '1850-2023', 'Monde', "La responsabilité historique de l'Europe est bien plus forte par habitant.", 'etabli', '682 t contre 227 t'),
  fait("La France a émis 0,68 % du CO2 mondial en 2024, mais représente 2,17 % des émissions cumulées depuis 1751.", 'owid_fr', '1751-2024', 'France', "Notre part historique est trois fois plus élevée que notre part actuelle.", 'etabli', '0,68 %'),
  fait("Au cours de la dernière décennie, 35 pays ont nettement réduit leurs émissions fossiles tout en faisant croître leur économie.", 'gcp_key', '2015-2025', 'Monde', "Réduire ses émissions est possible sans s'appauvrir.", 'etabli', '35 pays'),
 ],
 court="Trompeur : la Chine émet 32 % du CO2 mondial, mais l'empreinte d'un Français (8,3 t) est proche de celle d'un Chinois, et plus de la moitié vient de nos importations. Depuis 1850, un Européen a émis trois fois plus qu'un Chinois.",
 moyen="La Chine est bien le premier émetteur : 32 % du CO2 fossile mondial, contre 6 % pour l'Union européenne. Mais en comptant ce que nous importons, souvent fabriqué en Chine, l'empreinte d'un Français (8,3 tonnes) est proche de celle d'un Chinois.\n\nEt le climat dépend des émissions accumulées : depuis 1850, un Européen a émis en moyenne trois fois plus de CO2 qu'un Chinois. 35 pays ont réduit leurs émissions tout en continuant à s'enrichir : agir n'est pas inutile.",
 detaille="Selon le Global Carbon Project, la Chine représente 32 % des émissions fossiles mondiales en 2025, et ses émissions augmentent encore légèrement (+0,4 % projeté). La France, elle, pèse 0,68 % des émissions mondiales.\n\nMais cette comparaison est trompeuse. D'abord, selon le ministère de la Transition écologique, l'empreinte carbone d'un Français, qui compte les produits importés, est de 8,3 t en 2025, légèrement inférieure à celle d'un Chinois ; 52 % de cette empreinte vient de l'étranger. Ensuite, le réchauffement dépend des émissions cumulées : depuis 1850, un habitant de l'UE a émis 682 t de CO2, contre 227 t pour un Chinois, et la France pèse 2,17 % des émissions cumulées depuis 1751.\n\nEnfin, 35 pays ont réduit leurs émissions en faisant croître leur économie. L'effort de chaque pays compte, parce que le total est la somme de tous ces efforts, et parce que les pays riches, qui ont le plus émis, ont les moyens d'agir les premiers.",
 empathie="C'est vrai que nos efforts paraissent minuscules à côté des usines chinoises, et ça peut décourager. Mais une partie de ces usines fabrique ce que nous achetons, et nous avons émis bien plus qu'eux depuis 150 ans.",
 legitimes=["La Chine est de loin le premier émetteur annuel, et ses émissions augmentent encore légèrement.", "Depuis 2023, le cumul historique de la Chine dépasse celui de l'UE.", "Une baisse française isolée a un effet direct faible sur le climat mondial."],
 contre=[
  ("La France ne pèse que 1 %, ça ne change rien.", "Si chaque pays qui pèse 1 % ou moins renonçait, ce serait une grande partie des émissions mondiales ; et notre empreinte réelle inclut nos importations."),
  ("Les Chinois ne font rien, pourquoi nous ?", "Si chaque pays attend les autres, personne n'agit ; et 35 pays ont montré qu'on peut réduire ses émissions en faisant croître son économie."),
 ],
 questions=["Sais-tu quelle part de l'empreinte carbone d'un Français vient de produits importés ?", "Qui a émis le plus de CO2 par habitant depuis 1850 : un Européen ou un Chinois ?"],
 limites=["Les émissions annuelles par habitant de la Chine n'ont pas pu être lues ; la part des émissions importées par la France attribuable à la Chine n'est pas connue.", "Le rapport du Haut Conseil pour le climat n'a pas été lu."],
 publics={'convaincus': "La Chine émet beaucoup, c'est vrai. Mais plus de la moitié de notre empreinte carbone vient de ce que nous importons, souvent fabriqué là-bas, et un Européen a émis trois fois plus de CO2 qu'un Chinois depuis 1850. Dire « les autres d'abord », c'est ce que chaque pays pourrait dire, et personne n'agirait.",
  'indecis': "C'est décourageant de voir que la France pèse moins de 1 % des émissions. Mais notre empreinte réelle, avec les importations, est proche de celle d'un Chinois, et nous avons beaucoup plus émis dans l'histoire. Trente-cinq pays montrent qu'on peut réduire ses émissions sans s'appauvrir."},
 a_actualiser='2027-11-30', raison="Nouveau Global Carbon Budget annuel.",
))

# 24 ── Musulmans bientôt majoritaires ────────────────────────────────────────
FICHES.append(fiche(
 id='musulmans-majoritaires-france', affirmation="La France compte le plus de musulmans d'Europe, ils seront bientôt majoritaires.", volet='immigration', sous_theme='Immigration et démographie',
 mots_cles=['musulmans majoritaires', 'bientot majoritaires', 'nombre de musulmans', 'musulmans en france', 'islamisation', 'france musulmane', 'pew musulmans', 'part des musulmans'],
 verdict='contredit', fiabilite='etabli',
 resume="Aucune projection ne s'approche d'une majorité : le Pew Research Center prévoit entre 12,7 % et 18 % de musulmans en France en 2050 selon les scénarios d'immigration. Aujourd'hui, 10 % des 18-59 ans se déclarent musulmans selon l'Insee et l'Ined, contre 51 % sans religion et 29 % catholiques. La fécondité des descendantes d'immigrées se rapproche de la moyenne.",
 contexte="L'affirmation accompagne la théorie du « grand remplacement » et circule avec de faux chiffres, comme « 50 % de musulmans en 2050 ».",
 explication="Le recensement ne demande pas la religion : les chiffres viennent d'enquêtes déclaratives ou d'estimations. Les projections dépendent de l'immigration, de la fécondité et de la transmission religieuse.",
 sources=[PEW_MUS, INSEE_RELIG, INSEE_FECOND, MALDITA],
 faits=[
  fait("En 2016, la France comptait 5,7 millions de musulmans, soit 8,8 % de sa population, selon le Pew Research Center.", 'pew_mus', '2016', 'France', "Les musulmans sont une minorité.", 'estimation', '8,8 %'),
  fait("Selon Pew, la part des musulmans en France serait en 2050 de 12,7 % sans immigration, 17,4 % avec une immigration moyenne et 18 % avec une immigration forte.", 'maldita', 'projection 2050', 'France', "Même le scénario le plus haut est très loin d'une majorité.", 'estimation', '18 % au plus'),
  fait("En 2019-2020, parmi les 18-59 ans, 51 % se déclarent sans religion, 29 % catholiques et 10 % musulmans.", 'insee_relig', '2019-2020', 'France métropolitaine', "Les sans-religion sont majoritaires.", 'etabli', '10 %'),
  fait("La fécondité des femmes nées à l'étranger est de 2,3 enfants contre 1,7 pour les femmes nées en France (2021), et de 2,0 pour les descendantes de deux parents immigrés.", 'insee_fecond', '2021', 'France', "La fécondité se rapproche de la moyenne en une génération.", 'etabli', '2,3 contre 1,7'),
  fait("Même la Suède, pays le plus haut de l'étude Pew, atteindrait 30,6 % de musulmans en 2050 dans le scénario d'immigration forte.", 'maldita', 'projection 2050', 'Europe', "Aucun pays européen n'approche d'une majorité.", 'estimation', '30,6 %'),
 ],
 court="Faux : selon le Pew Research Center, la France compterait entre 12,7 % et 18 % de musulmans en 2050 selon l'immigration. Aujourd'hui, 10 % des 18-59 ans se disent musulmans, et 51 % sans religion. Aucune projection n'approche d'une majorité.",
 moyen="Les musulmans représentaient environ 8,8 % de la population française en 2016 selon le Pew Research Center. Même dans le scénario d'immigration la plus forte, ils seraient 18 % en 2050 : loin d'une majorité.\n\nSelon l'Insee et l'Ined, 10 % des 18-59 ans se déclarent musulmans, contre 51 % sans religion et 29 % catholiques. Et la fécondité des filles d'immigrées se rapproche de la moyenne française.",
 detaille="Le Pew Research Center estimait en 2016 que la France comptait 5,7 millions de musulmans, soit 8,8 % de la population. Ses projections pour 2050 vont de 12,7 % sans aucune immigration à 18 % avec une immigration forte. Le chiffre de 50 % de musulmans en 2050, qui a circulé en Europe, a été qualifié de faux par un fact-checker espagnol sur cette base. Même la Suède, pays le plus haut de l'étude, atteindrait 30,6 % dans le scénario maximal.\n\nL'enquête Trajectoires et Origines de l'Insee et de l'Ined donne une photographie : en 2019-2020, parmi les 18-59 ans, 10 % se déclarent musulmans, 29 % catholiques et 51 % sans religion.\n\nLa part des musulmans augmente, notamment parce que les musulmanes ont plus d'enfants en moyenne (2,6 contre 1,6 en Europe selon Pew) et que la population est plus jeune. Mais la fécondité converge : 2,3 enfants pour les femmes nées à l'étranger, 2,0 pour les descendantes d'immigrés, contre 1,7 pour les femmes nées en France.",
 empathie="Je comprends que les changements visibles dans certains quartiers puissent inquiéter. Mais les projections les plus hautes restent très loin d'une majorité : moins d'un Français sur cinq en 2050.",
 legitimes=["La part des musulmans augmente, même sans immigration, à cause de l'âge et de la fécondité.", "La transmission religieuse est forte dans les familles musulmanes selon l'Insee."],
 contre=[
  ("Les chiffres officiels sont truqués.", "Les projections viennent d'un centre de recherche américain indépendant et d'enquêtes de l'Insee et de l'Ined : elles concordent."),
  ("Ils font beaucoup plus d'enfants.", "L'écart existe, mais il se réduit en une génération : 2,0 enfants pour les descendantes d'immigrées."),
 ],
 questions=["Quelle part de musulmans prévoit le scénario le plus haut de Pew pour la France en 2050 ?", "Sais-tu quelle est la part des personnes sans religion en France ?"],
 limites=["Les données de Pew datent de 2016-2017 ; le rapport complet n'a pas pu être lu.", "L'affirmation selon laquelle la France compte le plus de musulmans d'Europe n'a pas été vérifiée dans les sources lues ; le recensement ne demande pas la religion."],
 publics={'convaincus': "Même dans le scénario le plus élevé du Pew Research Center, avec une immigration forte, les musulmans seraient 18 % en France en 2050. Ça laisse plus de quatre Français sur cinq qui ne le sont pas. Aujourd'hui, la majorité qui progresse, ce sont les sans-religion : 51 % des 18-59 ans.",
  'indecis': "La part des musulmans augmente, c'est vrai, mais lentement : de 8,8 % en 2016 à 12,7 % à 18 % en 2050 selon les scénarios. Les chiffres alarmistes qui circulent sont faux. Et la fécondité des filles d'immigrées rejoint vite la moyenne française."},
 a_actualiser='2028-06-30', raison="Nouvelles enquêtes sur la diversité religieuse.",
))

# 25 ── 17 octobre 1961 ───────────────────────────────────────────────────────
FICHES.append(fiche(
 id='massacre-17-octobre-1961', affirmation="Le massacre du 17 octobre 1961 est une invention de la gauche.", volet='international', sous_theme='Colonisation et décolonisation',
 mots_cles=['17 octobre 1961', 'massacre du 17 octobre', 'papon', 'algeriens jetes dans la seine', 'guerre d algerie', 'repentance', 'manifestation fln paris', 'massacre des algeriens'],
 verdict='contredit', fiabilite='etabli',
 resume="La répression du 17 octobre 1961 est un fait établi, reconnu par l'État : en 2021, la présidence de la République a qualifié d'« inexcusables pour la République » les crimes commis cette nuit-là sous l'autorité du préfet Maurice Papon, et l'Assemblée nationale les a condamnés en 2024. Les historiens débattent du nombre de morts (de plusieurs dizaines à plus de 120), pas de la réalité de la répression.",
 contexte="Le négationnisme sur ce massacre s'inscrit dans le refus de la « repentance » sur la guerre d'Algérie.",
 explication="Le 17 octobre 1961, en pleine guerre d'Algérie, le FLN appelle les Algériens de la région parisienne à manifester à Paris. La police, dirigée par le préfet Maurice Papon, réprime la manifestation ; le bilan officiel de l'époque est de deux morts.",
 sources=[ELY_1961, LCP_1961, VDI_1961, BRUNET_1961, AN_1961],
 faits=[
  fait("Selon l'Élysée, plus de 25 000 hommes, femmes et enfants ont manifesté, près de 12 000 Algériens ont été arrêtés et « plusieurs dizaines furent tués, leurs corps jetés dans la Seine ».", 'ely_1961', '1961', 'Paris', "L'État reconnaît des dizaines de morts.", 'etabli', 'plusieurs dizaines'),
  fait("En 2021, le président de la République a qualifié d'« inexcusables pour la République » les crimes commis cette nuit-là sous l'autorité de Maurice Papon.", 'ely_1961', '2021', 'France', "La reconnaissance vient du sommet de l'État, pas d'un parti.", 'etabli'),
  fait("Le 28 mars 2024, l'Assemblée nationale a adopté par 67 voix contre 11 une résolution condamnant le massacre, portée par une députée écologiste et cosignée par un député Renaissance.", 'lcp_1961', '2024', 'France', "La condamnation dépasse la gauche.", 'etabli', '67 contre 11'),
  fait("Pour les historiens Jim House et Neil MacMaster, « bien plus de 120 Algériens » ont été tués par la police en région parisienne en septembre-octobre 1961.", 'vdi_1961', '1961', 'Région parisienne', "Les estimations des historiens dépassent la centaine.", 'estimation', 'plus de 120'),
  fait("L'historien Jean-Paul Brunet, qui retient le bilan le plus bas, ne nie pas la répression : il évoque plus de 14 000 arrestations en deux jours et un désaccord sur le nombre de morts.", 'brunet_1961', '1961', 'Paris', "Le débat porte sur le bilan, pas sur les faits.", 'etabli', '14 000'),
 ],
 court="Faux : la présidence de la République a reconnu en 2021 des crimes « inexcusables pour la République », avec plusieurs dizaines de morts, et l'Assemblée a condamné le massacre en 2024. Les historiens débattent du bilan (des dizaines à plus de 120), pas des faits.",
 moyen="Le 17 octobre 1961, la police parisienne, dirigée par le préfet Maurice Papon, a violemment réprimé une manifestation d'Algériens : près de 12 000 arrestations et plusieurs dizaines de morts, dont des corps jetés dans la Seine, selon l'Élysée.\n\nCe n'est pas une invention de la gauche : c'est le président Emmanuel Macron qui a parlé en 2021 de crimes « inexcusables pour la République », et l'Assemblée a condamné le massacre en 2024 avec des voix de la majorité. Les historiens discutent du nombre de morts, pas de la réalité des faits.",
 detaille="Le 17 octobre 1961, en pleine guerre d'Algérie, plus de 25 000 hommes, femmes et enfants algériens manifestent à Paris à l'appel du FLN. La police, sous l'autorité du préfet Maurice Papon, réprime la manifestation : près de 12 000 personnes sont arrêtées, et, selon la présidence de la République, « plusieurs dizaines furent tués, leurs corps jetés dans la Seine ». Le bilan officiel de l'époque ne reconnaissait que deux morts.\n\nLongtemps « tue, déniée ou occultée », selon les mots de l'Élysée, cette tragédie a été documentée par les historiens. Jim House et Neil MacMaster estiment que bien plus de 120 Algériens ont été tués par la police en septembre-octobre 1961 ; Jean-Paul Brunet retient un bilan plus bas, mais décrit lui aussi une répression avec plus de 14 000 arrestations en deux jours.\n\nEn 2021, Emmanuel Macron a qualifié ces crimes d'« inexcusables pour la République ». En 2024, l'Assemblée nationale a adopté une résolution condamnant le massacre par 67 voix contre 11, un député RN dénonçant une « repentance à outrance ». Reconnaître un crime d'État n'est pas haïr la France : c'est ce qui permet de transmettre une histoire commune.",
 empathie="Je comprends que ces pages de l'histoire soient douloureuses et qu'on n'ait pas envie de se sentir accusé. Mais reconnaître ce qui s'est passé n'accuse pas les Français d'aujourd'hui ; c'est l'État lui-même qui l'a reconnu.",
 legitimes=["Le nombre exact de morts reste discuté entre historiens, qui s'opposent sur leurs méthodes.", "Les faits se sont produits en pleine guerre d'Algérie, dans un contexte de violence entre le FLN et la police."],
 contre=[
  ("C'est de la repentance.", "C'est la présidence de la République et une résolution votée au-delà de la gauche qui reconnaissent ces faits, documentés par des historiens de sensibilités différentes."),
  ("Le bilan officiel était de deux morts.", "C'était le bilan de 1961 ; les archives et les historiens ont établi depuis des dizaines de morts, ce que reconnaît l'Élysée."),
 ],
 questions=["Savais-tu que c'est Emmanuel Macron qui a qualifié ces crimes d'« inexcusables pour la République » ?", "Sur quoi les historiens sont-ils en désaccord : les faits ou le nombre de morts ?"],
 limites=["Le rapport Mandelkern de 1998 et le texte officiel de la résolution de 2024 n'ont pas été lus.", "Le bilan chiffré de Jean-Paul Brunet n'a pas été lu dans sa source ; l'estimation de 200 morts n'est rapportée que par la presse."],
 publics={'convaincus': "Ce n'est pas la gauche qui le dit : c'est Emmanuel Macron, en 2021, qui a parlé de crimes « inexcusables pour la République ». Même l'historien qui donne le bilan le plus bas reconnaît une répression massive. Aimer son pays, ce n'est pas nier ses crimes, c'est être capable de les regarder en face.",
  'indecis': "La répression du 17 octobre 1961 est un fait reconnu par l'État et documenté par les historiens : des milliers d'arrestations et des dizaines de morts au moins. Le débat porte sur le bilan exact. Connaître cette histoire aide à comprendre les blessures liées à la guerre d'Algérie."},
 a_actualiser='2028-10-31', raison="Travaux historiques et commémorations.",
))

# 26 ── Retraités et niveau de vie ────────────────────────────────────────────
FICHES.append(fiche(
 id='retraites-niveau-vie-actifs', affirmation="Les retraités ont un meilleur niveau de vie que les actifs.", volet='social', sous_theme='Minimum social et niveau de vie',
 mots_cles=['niveau de vie des retraites', 'retraites plus riches', 'retraites privilegies', 'boomers', 'retraites aises', 'pension et actifs', 'retraites vs actifs', 'generation sacrifiee'],
 verdict='trompeur', fiabilite='etabli',
 resume="Le niveau de vie moyen des retraités équivaut à celui de l'ensemble de la population (100,2 % en 2023), mais il reste inférieur à celui des actifs : 2 473 € contre 2 693 € par mois. En tenant compte du fait que 70 % des retraités sont propriétaires de leur logement, l'écart avec les actifs devient très faible. Leur taux de pauvreté est plus bas que la moyenne (10 % contre 14,4 %), et leur niveau de vie relatif est projeté en baisse.",
 contexte="L'argument oppose les générations et sert à justifier des économies sur les pensions, ou au contraire à présenter les jeunes comme une génération sacrifiée.",
 explication="Le niveau de vie se mesure par unité de consommation, en tenant compte de la taille du ménage. Les « loyers imputés » ajoutent au revenu des propriétaires le loyer qu'ils n'ont pas à payer.",
 sources=[COR_NV, DREES_NV],
 faits=[
  fait("En 2023, le niveau de vie des retraités atteint 100,2 % de celui de l'ensemble de la population : 2 473 € par mois, contre 2 468 € pour l'ensemble et 2 693 € pour les actifs.", 'cor_nv', '2023', 'France', "Les retraités sont dans la moyenne, mais en dessous des actifs.", 'etabli', '2 473 € contre 2 693 €'),
  fait("En tenant compte des loyers imputés, le niveau de vie des retraités dépasse de 6,5 % celui de l'ensemble, à un niveau très proche de celui des actifs.", 'cor_nv', '2023', 'France', "La propriété du logement réduit l'écart avec les actifs.", 'etabli', '+6,5 %'),
  fait("En 2022, le taux de pauvreté des retraités est de 10,0 %, contre 14,4 % pour l'ensemble de la population.", 'drees_nv', '2022', 'France', "Les retraités sont moins souvent pauvres.", 'etabli', '10,0 %'),
  fait("70 % des ménages retraités sont propriétaires de leur résidence principale, contre 57 % de l'ensemble.", 'drees_nv', '2023-2024', 'France', "Le patrimoine immobilier favorise les retraités.", 'etabli', '70 %'),
  fait("Le niveau de vie relatif des retraités est projeté à 96,3 % de celui de l'ensemble en 2045 et 90,3 % en 2070.", 'cor_nv', 'projection', 'France', "La situation relative des retraités devrait se dégrader.", 'estimation', '90,3 % en 2070'),
 ],
 court="Trompeur : le niveau de vie des retraités égale celui de l'ensemble de la population (100,2 % en 2023), mais reste inférieur à celui des actifs (2 473 € contre 2 693 € par mois). Ils sont moins souvent pauvres et plus souvent propriétaires, et leur situation relative devrait baisser.",
 moyen="Le niveau de vie moyen des retraités est égal à celui de l'ensemble des Français, mais il reste un peu inférieur à celui des actifs : 2 473 € contre 2 693 € par mois en 2023.\n\nLes retraités sont moins souvent pauvres que la moyenne et sont plus souvent propriétaires de leur logement, ce qui réduit l'écart. Mais derrière la moyenne, il y a de grandes inégalités entre retraités, et leur niveau de vie relatif devrait baisser dans les prochaines décennies.",
 detaille="Selon le Conseil d'orientation des retraites, le niveau de vie moyen des retraités atteint en 2023 100,2 % de celui de l'ensemble de la population : 2 473 € par mois et par unité de consommation, contre 2 693 € pour les actifs. L'affirmation est donc fausse au sens strict.\n\nElle contient une part de vérité : 70 % des ménages retraités sont propriétaires de leur logement, contre 57 % de l'ensemble, et en comptant le loyer qu'ils n'ont pas à payer, leur niveau de vie devient très proche de celui des actifs. Leur taux de pauvreté est aussi plus faible (10 % contre 14,4 % en 2022).\n\nCette situation est le fruit de carrières plus complètes et d'un système de retraite protecteur. Elle ne durera pas forcément : le COR projette un niveau de vie relatif des retraités de 96,3 % en 2045 et 90,3 % en 2070. Opposer jeunes et retraités détourne du vrai sujet : la répartition des richesses entre revenus du travail, pensions et patrimoine.",
 empathie="Je comprends que les jeunes actifs qui peinent à se loger aient l'impression que les retraités s'en sortent mieux. Les chiffres montrent une situation proche, avec de fortes inégalités entre retraités, et une dégradation prévue pour les suivants.",
 legitimes=["Les retraités sont moins souvent pauvres que la moyenne (10 % contre 14,4 %).", "En comptant les loyers imputés, leur niveau de vie est très proche de celui des actifs.", "Les revenus du patrimoine pèsent davantage dans leurs revenus."],
 contre=[
  ("Les boomers ont tout pris.", "Derrière la moyenne, les situations sont très inégales : 10 % des retraités vivent sous le seuil de pauvreté."),
  ("Il faut baisser les pensions.", "Le COR projette déjà une baisse du niveau de vie relatif des retraités ; la question est de financer les retraites sans appauvrir les futurs retraités."),
 ],
 questions=["Sais-tu que le niveau de vie moyen des retraités reste inférieur à celui des actifs ?", "Le vrai clivage est-il entre générations, ou entre ceux qui ont un patrimoine et ceux qui n'en ont pas ?"],
 limites=["Les données datent de 2022-2023 ; la publication de l'Insee sur la pauvreté 2023 n'a pas été lue."],
 publics={'convaincus': "Les retraités ne vivent pas mieux que les actifs en moyenne : 2 473 € contre 2 693 € par mois en 2023. Ils sont plus souvent propriétaires, ce qui réduit l'écart, mais beaucoup vivent avec de petites pensions. Opposer les générations arrange surtout ceux qui veulent couper dans les retraites.",
  'indecis': "Les retraités ont en moyenne le même niveau de vie que l'ensemble des Français, un peu moins que les actifs, et ils sont moins souvent pauvres. Leur situation relative devrait baisser dans les décennies à venir. Le vrai sujet, c'est la répartition des richesses, pas une guerre des générations."},
 a_actualiser='2027-06-30', raison="Rapport annuel du COR.",
))

if __name__ == '__main__':
    for f in FICHES:
        with open(os.path.join(OUT, f['id'] + '.json'), 'w', encoding='utf-8') as fh:
            json.dump(f, fh, ensure_ascii=False, indent=2); fh.write('\n')
    print(f"{len(FICHES)} fiches écrites")
