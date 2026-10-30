// Suggestions d'affirmations à examiner, par volet et par sous-thème (utilisables hors ligne).
// Ce sont des phrases fréquemment entendues dans les discussions politiques, reformulées de façon
// générique : elles ne sont attribuées à personne et ne sont pas des citations.
//
// Format compact : "drapeaux|texte"
//   c = formulation tranchée, typique d'un débat ou d'une riposte (favorisée en mode « gagner »)
//   i = inquiétude ou question sincère (favorisée en mode « convaincre »)
//   # = argument chiffré ou statistique ; ~ = argument fondé sur le vécu
// NB : noms préfixés SG_ / sg… (l'aperçu concatène les modules).
import { VOLETS } from './taxonomy.js';
import { kbTokens } from './kbsearch.js';

export const SG_BIBLIOTHEQUE = {
  immigration: {
    'Immigration et démographie': [
      'c#|Les immigrés, c’est déjà un tiers de la population.',
      'c|On assiste à un grand remplacement de la population française.',
      'c#|Ce sont les immigrées qui font toute la natalité française.',
      'i|Sans les immigrés, la France vieillirait-elle encore plus vite ?',
      'i#|J’ai l’impression que la population immigrée augmente très vite ces dernières années.',
      'i|A-t-on vraiment besoin d’immigration pour payer nos retraites ?',
    ],
    'Immigration et travail': [
      'c|Les immigrés font baisser les salaires des Français.',
      'c|Les immigrés prennent le travail des Français.',
      'c#|La plupart des immigrés ne travaillent pas.',
      'i~|Sans les travailleurs immigrés, qui ferait le ménage, le bâtiment ou la cueillette ?',
      'i#|Les immigrés cotisent-ils vraiment autant que les autres salariés ?',
      'i|Les métiers en tension, c’est une vraie pénurie ou une excuse pour payer moins ?',
    ],
    'Immigration et aides sociales': [
      'c|Les immigrés touchent plus d’aides que les Français.',
      'c|Un étranger qui arrive en France touche le RSA tout de suite.',
      'c|Les immigrés viennent en France pour les allocations.',
      'i|Les sans-papiers ont-ils droit à la Sécu gratuitement ?',
      'i|Combien d’années de séjour faut-il pour toucher le RSA quand on est étranger ?',
      'i|Les allocations familiales attirent-elles des familles étrangères ?',
    ],
    'Immigration et asile': [
      'c|La France accueille toute la misère du monde.',
      'c|Les demandeurs d’asile sont presque tous des migrants économiques.',
      'c|Une fois débouté de l’asile, personne ne repart jamais.',
      'i|Combien de temps faut-il pour traiter une demande d’asile en France ?',
      'i|La France est-elle obligée d’accueillir les demandeurs d’asile ?',
      'i#|La France reçoit-elle plus de demandes d’asile que ses voisins ?',
    ],
    'Réfugiés et statuts administratifs': [
      'c|Réfugié, sans-papiers, migrant : c’est la même chose.',
      'c|Les réfugiés ont plus de droits que les Français.',
      'c|Les sans-papiers sont tous des délinquants puisqu’ils sont en situation illégale.',
      'i|Quelle différence entre un réfugié et un demandeur d’asile ?',
      'i|Un réfugié reconnu a-t-il le droit de travailler en France ?',
      'i|Les mineurs isolés sont-ils vraiment des mineurs ?',
    ],
    'Nationalité et accès aux droits': [
      'c|On donne la nationalité française à n’importe qui.',
      'c|Il suffit de naître en France pour être français.',
      'c|Les binationaux ne sont pas de vrais Français.',
      'i|Combien de temps faut-il pour devenir français ?',
      'i|Faut-il parler français pour obtenir la nationalité ?',
      'i|Un étranger en situation régulière a-t-il les mêmes droits sociaux qu’un Français ?',
    ],
    'Intégration': [
      'c|Les immigrés ne veulent pas s’intégrer.',
      'c|Les immigrés refusent d’apprendre le français.',
      'c|L’intégration est un échec total en France.',
      'i~|Les enfants d’immigrés réussissent-ils moins bien à l’école ?',
      'i|Le travail est-il le meilleur moyen de s’intégrer ?',
      'i|L’intégration marchait-elle mieux avant ?',
    ],
    'Économie et immigration': [
      'c|L’immigration ruine l’économie française.',
      'c|Les immigrés n’apportent rien à la croissance.',
      'c|Les pays sans immigration s’en sortent mieux économiquement.',
      'i|Les immigrés créent-ils des entreprises ?',
      'i|L’argent envoyé au pays par les immigrés est-il perdu pour la France ?',
      'i|Les étudiants étrangers coûtent-ils ou rapportent-ils à la France ?',
    ],
    'Immigration et finances publiques': [
      'c#|L’immigration coûte des dizaines de milliards par an à la France.',
      'c|L’aide médicale d’État coûte une fortune.',
      'c|Les immigrés coûtent plus cher qu’ils ne rapportent.',
      'i|Quand on compte les retraites et la santé, qui finance qui ?',
      'i#|Les études sur le coût de l’immigration sont-elles fiables ?',
      'i|Les jeunes immigrés qui travaillent financent-ils nos retraites ?',
    ],
    'Immigration et délinquance': [
      'c#|Les étrangers commettent la majorité des vols.',
      'c|Plus d’immigration, c’est forcément plus d’insécurité.',
      'c|Les mineurs isolés sont responsables de l’explosion des vols.',
      'i#|Est-ce vrai que les étrangers sont plus souvent mis en cause par la police ?',
      'i|La délinquance des étrangers vient-elle de la nationalité ou de la pauvreté ?',
      'i|Pourquoi les médias ne donnent-ils pas la nationalité des délinquants ?',
    ],
    'Immigration, délinquance et prisons': [
      'c#|Les immigrés remplissent les prisons françaises.',
      'c#|Les étrangers remplissent les prisons françaises.',
      'c|La délinquance est principalement liée à l’immigration.',
      'c|La France serait plus sûre si elle accueillait moins d’immigrés.',
      'c#|Les statistiques de délinquance démontrent que l’immigration augmente l’insécurité.',
      'i#|Les immigrés représentent une part disproportionnée de la population carcérale.',
      'i|Pourquoi y a-t-il autant d’étrangers en détention provisoire ?',
    ],
    'Expulsion des étrangers condamnés': [
      'c|Tous les étrangers condamnés devraient être expulsés.',
      'c|Un étranger qui commet un crime n’a plus sa place en France.',
      'c|Il suffit d’expulser les délinquants étrangers pour réduire la criminalité.',
      'c|Les criminels étrangers sont protégés par la justice française.',
      'i|Il faut renvoyer tous les étrangers qui ont déjà été condamnés.',
      'i|Une personne étrangère condamnée devrait automatiquement perdre son droit de séjour.',
      'i#|Pourquoi les OQTF ne sont-elles presque jamais exécutées ?',
    ],
    'Logement': [
      'c|Les logements sociaux sont donnés en priorité aux immigrés.',
      'c|Les migrants sont logés à l’hôtel pendant que des Français dorment dehors.',
      'c|Les étrangers font monter les loyers.',
      'i|Comment sont attribués les logements sociaux ?',
      'i~|Les étrangers sont-ils discriminés quand ils cherchent un appartement ?',
      'i|Pourquoi certaines familles étrangères sont-elles concentrées dans les mêmes quartiers ?',
    ],
    'Discriminations': [
      'c|Si les enfants d’immigrés ne trouvent pas de travail, c’est de leur faute.',
      'c|Les contrôles au faciès sont un mythe.',
      'c|Avec un nom à consonance arabe, on a autant de chances qu’un autre d’être embauché.',
      'i#|Les testings sur les CV prouvent-ils vraiment une discrimination ?',
      'i~|Pourquoi certains jeunes nés ici se sentent-ils rejetés ?',
      'i|La discrimination positive serait-elle une solution ?',
    ],
    'Racisme': [
      'c|Le racisme anti-blanc est le plus répandu aujourd’hui.',
      'c|Dire qu’il y a trop d’immigrés, ce n’est pas raciste.',
      'c|Le racisme en France, c’est fini depuis longtemps.',
      'i#|Les actes racistes augmentent-ils en France ?',
      'i|Où passe la frontière entre critiquer l’immigration et être raciste ?',
      'i~|Pourquoi certaines blagues racistes passent-elles pour de l’humour ?',
    ],
    'Comparaisons européennes': [
      'c|La France est le pays le plus généreux d’Europe avec les migrants.',
      'c|Le Danemark a réglé le problème de l’immigration, il faut faire pareil.',
      'c#|La France accueille plus d’immigrés que tous ses voisins.',
      'i|Les règles d’asile sont-elles les mêmes partout en Europe ?',
      'i|Le pacte européen sur la migration change-t-il quelque chose ?',
      'i|Pourquoi tant de migrants veulent-ils rejoindre le Royaume-Uni ?',
    ],
    'Histoire des migrations': [
      'c|Avant, les immigrés s’intégraient ; aujourd’hui, ce n’est plus le cas.',
      'c|La France n’a jamais été un pays d’immigration.',
      'c|Les Italiens et les Polonais, eux, étaient bien accueillis.',
      'i|D’où venaient les immigrés en France il y a cent ans ?',
      'i|Les travailleurs immigrés ont-ils reconstruit la France après la guerre ?',
      'i|Les rapatriés d’Algérie et les harkis, est-ce aussi de l’immigration ?',
    ],
  },

  securite: {
    'Délinquance': [
      'c#|La délinquance augmente partout.',
      'c|On n’est plus en sécurité nulle part en France.',
      'c|C’était beaucoup plus sûr il y a trente ans.',
      'i~|Pourquoi ai-je l’impression que mon quartier est moins sûr qu’avant ?',
      'i#|Les chiffres de la délinquance sont-ils fiables ?',
      'i|La délinquance augmente-t-elle vraiment ou en parle-t-on juste plus ?',
    ],
    'Violences': [
      'c|La violence gratuite explose en France.',
      'c|On peut se faire poignarder pour un regard.',
      'c|Les jeunes sont de plus en plus violents.',
      'i#|Les coups et blessures augmentent-ils vraiment ?',
      'i~|Pourquoi les faits divers violents semblent-ils plus nombreux ?',
      'i|Les réseaux sociaux rendent-ils les jeunes plus violents ?',
    ],
    'Homicides': [
      'c#|Il n’y a jamais eu autant de meurtres en France.',
      'c|Le narcotrafic transforme nos villes en zones de guerre.',
      'c|Les meurtres sont de plus en plus commis par des mineurs.',
      'i#|Le nombre d’homicides a-t-il augmenté depuis les années 1990 ?',
      'i|Les règlements de comptes liés à la drogue sont-ils en hausse ?',
      'i|La France est-elle plus violente que ses voisins ?',
    ],
    'Violences sexuelles': [
      'c|Les violences sexuelles sont surtout commises par des inconnus dans la rue.',
      'c|Avec MeToo, n’importe qui peut accuser n’importe qui.',
      'c#|Les fausses accusations de viol sont très fréquentes.',
      'i#|Les violences sexuelles augmentent-elles ou sont-elles mieux déclarées ?',
      'i|Pourquoi si peu de plaintes pour viol aboutissent-elles à une condamnation ?',
      'i~|Comment aider une proche qui n’ose pas porter plainte ?',
    ],
    'Violences intrafamiliales': [
      'c|Les violences conjugales, c’est une affaire privée.',
      'c|Les hommes sont autant victimes de violences conjugales que les femmes.',
      'c|Les bracelets anti-rapprochement ne servent à rien.',
      'i#|Combien de femmes sont tuées chaque année par leur conjoint ?',
      'i|Pourquoi les victimes restent-elles souvent avec leur agresseur ?',
      'i|Les plaintes pour violences conjugales sont-elles bien traitées ?',
    ],
    'Police et gendarmerie': [
      'c|La police est raciste.',
      'c|Les policiers ne peuvent plus rien faire, ils sont menottés par la loi.',
      'c|Critiquer la police, c’est être contre l’ordre.',
      'i#|Y a-t-il moins de policiers sur le terrain qu’avant ?',
      'i|Comment sont contrôlées les violences policières ?',
      'i~|Pourquoi la confiance entre jeunes et police est-elle si faible ?',
    ],
    'Justice pénale': [
      'c|La justice est laxiste, personne ne va en prison.',
      'c|Les juges sont politisés et protègent les délinquants.',
      'c|Les peines ne sont jamais exécutées.',
      'i|Pourquoi la justice met-elle autant de temps à juger ?',
      'i#|Les peines prononcées sont-elles plus faibles qu’avant ?',
      'i|À quoi servent les peines alternatives à la prison ?',
    ],
    'Prisons': [
      'c|Les prisons françaises sont des hôtels quatre étoiles.',
      'c|Il faut construire beaucoup plus de prisons.',
      'c|La prison, c’est l’école du crime, ça ne sert à rien.',
      'i#|Pourquoi les prisons françaises sont-elles surpeuplées ?',
      'i|La prison prépare-t-elle à la sortie ?',
      'i|Combien coûte un détenu par jour ?',
    ],
    'Récidive': [
      'c|Les délinquants récidivent tous.',
      'c|Les peines plancher étaient efficaces contre la récidive.',
      'c|Les remises de peine automatiques encouragent la récidive.',
      'i#|Quel est vraiment le taux de récidive en France ?',
      'i|Qu’est-ce qui marche le mieux pour éviter la récidive ?',
      'i|Le suivi après la prison existe-t-il vraiment ?',
    ],
    'Sécurité du quotidien': [
      'c|Les incivilités sont partout et personne ne fait rien.',
      'c|Il faut des caméras dans toutes les rues.',
      'c|Les rodéos urbains sont tolérés par l’État.',
      'i~|Pourquoi je me sens en insécurité dans les transports le soir ?',
      'i|La vidéosurveillance fait-elle vraiment baisser la délinquance ?',
      'i|La police municipale est-elle utile ?',
    ],
    'Criminalité organisée': [
      'c|La France est devenue un narco-État.',
      'c|Il suffit d’arrêter les consommateurs pour tuer le trafic.',
      'c|Légaliser le cannabis ferait exploser la consommation.',
      'i#|Le trafic de drogue a-t-il vraiment explosé ?',
      'i|Comment les réseaux recrutent-ils des mineurs ?',
      'i|Les saisies de drogue font-elles reculer le trafic ?',
    ],
    'Comparaisons statistiques': [
      'c|La France est le pays le plus dangereux d’Europe.',
      'c|Les États-Unis sont plus sûrs grâce à leur fermeté.',
      'c|À Singapour, il n’y a pas de délinquance grâce aux peines lourdes.',
      'i#|Peut-on comparer la délinquance entre pays ?',
      'i|Les enquêtes de victimation disent-elles la même chose que les plaintes ?',
      'i#|Le taux d’incarcération est-il plus élevé en France qu’ailleurs ?',
    ],
    'Prévention et politiques publiques': [
      'c|La prévention, c’est de l’argent jeté par les fenêtres.',
      'c|La seule solution, c’est la tolérance zéro.',
      'c|Les éducateurs de rue ne servent à rien.',
      'i|Quelles politiques ont réellement fait baisser la délinquance ailleurs ?',
      'i|Le sport et la culture peuvent-ils éviter la délinquance des jeunes ?',
      'i|Faut-il plus de police ou plus de prévention ?',
    ],
  },

  social: {
    'RSA': [
      'c|Avec le RSA, on gagne autant qu’au SMIC.',
      'c|Les gens au RSA ne font rien de leurs journées.',
      'c|Le RSA encourage à ne pas travailler.',
      'i#|Combien touche-t-on vraiment au RSA ?',
      'i|Les heures d’activité obligatoires pour le RSA sont-elles une bonne idée ?',
      'i#|Combien de personnes qui y ont droit ne demandent pas le RSA ?',
    ],
    'Allocations familiales': [
      'c|Certains font des enfants pour toucher les allocations.',
      'c|Les allocations familiales devraient être réservées aux Français.',
      'c|Les allocations sont versées même aux riches, c’est absurde.',
      'i#|Combien rapportent les allocations pour deux enfants ?',
      'i|Les allocations familiales font-elles vraiment monter la natalité ?',
      'i|Pourquoi n’y a-t-il pas d’allocations pour le premier enfant ?',
    ],
    'Aides au logement': [
      'c|Les APL font monter les loyers.',
      'c|Les APL profitent surtout aux propriétaires.',
      'c|Les étudiants touchent des APL alors que leurs parents sont riches.',
      'i#|Combien de foyers touchent une aide au logement ?',
      'i|Pourquoi les APL ont-elles baissé ces dernières années ?',
      'i~|Sans les APL, pourrais-je encore payer mon loyer ?',
    ],
    'Chômage': [
      'c|Les chômeurs ne veulent pas travailler.',
      'c|Il suffit de traverser la rue pour trouver un emploi.',
      'c|Les allocations chômage sont trop généreuses.',
      'i#|Y a-t-il vraiment plus d’offres d’emploi que de chômeurs ?',
      'i|Réduire les allocations fait-il retrouver un emploi plus vite ?',
      'i~|Pourquoi est-ce si difficile de retrouver du travail après cinquante ans ?',
    ],
    'Fraude sociale': [
      'c#|La fraude sociale coûte plus cher que la fraude fiscale.',
      'c|Les fraudeurs aux allocations ne sont jamais punis.',
      'c|Il y a des millions de cartes Vitale en trop.',
      'i#|Combien coûte vraiment la fraude aux prestations sociales ?',
      'i|Qui fraude le plus : les assurés, les entreprises ou les professionnels de santé ?',
      'i|Les contrôles de la CAF sont-ils efficaces ?',
    ],
    'Fraude fiscale': [
      'c|La fraude fiscale, ce sont surtout les petits artisans.',
      'c|L’optimisation fiscale est parfaitement légale, donc normale.',
      'c|On ne pourra jamais récupérer l’argent de l’évasion fiscale.',
      'i#|Combien d’argent la fraude fiscale fait-elle perdre chaque année ?',
      'i|Pourquoi les contrôles fiscaux ont-ils diminué ?',
      'i|Quelle différence entre fraude, évasion et optimisation fiscale ?',
    ],
    'Conditions d’accès aux prestations': [
      'c|On touche des aides sans rien faire pour les obtenir.',
      'c|Les aides sont automatiques, personne ne vérifie.',
      'c|Il suffit de demander pour tout obtenir.',
      'i|Quelles conditions faut-il remplir pour toucher la prime d’activité ?',
      'i~|Pourquoi les démarches pour obtenir une aide sont-elles si compliquées ?',
      'i#|Combien d’aides ne sont pas réclamées par ceux qui y ont droit ?',
    ],
    'Emploi et salaires': [
      'c|Le travail ne paie plus en France.',
      'c|Augmenter le SMIC détruirait des emplois.',
      'c|Les Français ne travaillent pas assez.',
      'i#|Le SMIC a-t-il suivi l’inflation ?',
      'i|Pourquoi tant de salariés restent-ils au SMIC toute leur carrière ?',
      'i#|Les Français travaillent-ils moins que leurs voisins ?',
    ],
    'Précarité': [
      'c|Les précaires n’ont qu’à se former.',
      'c|L’intérim et les CDD, c’est un choix de vie.',
      'c|Les travailleurs pauvres, ça n’existe pas en France.',
      'i#|Combien de personnes vivent avec des contrats précaires ?',
      'i~|Pourquoi est-il si dur de louer un logement sans CDI ?',
      'i|L’ubérisation améliore-t-elle ou dégrade-t-elle les conditions de travail ?',
    ],
    'Pauvreté': [
      'c|Avec toutes nos aides, il n’y a plus vraiment de pauvres en France.',
      'c|Les pauvres sont pauvres parce qu’ils ne font pas d’efforts.',
      'c|Être pauvre en France, c’est être riche ailleurs.',
      'i#|Combien de personnes vivent sous le seuil de pauvreté ?',
      'i|Comment définit-on la pauvreté ?',
      'i~|Pourquoi de plus en plus de gens vont-ils aux Restos du cœur ?',
    ],
    'Minimum social et niveau de vie': [
      'c|On vit très bien avec les minima sociaux.',
      'c|L’AAH est versée à n’importe qui.',
      'c|Le minimum vieillesse rapporte plus qu’une petite retraite de travailleur.',
      'i#|Avec quel revenu une personne seule vit-elle au RSA ?',
      'i|Les minima sociaux suivent-ils la hausse des prix ?',
      'i|Faut-il un revenu universel ?',
    ],
    'Coût et efficacité des aides': [
      'c|Les impôts ne servent qu’à payer l’assistanat.',
      'c|Les aides sociales coûtent une fortune et ne servent à rien.',
      'c|La France dépense plus que tout le monde en social pour aucun résultat.',
      'i#|Quelle part des dépenses publiques va aux minima sociaux ?',
      'i|Les aides sociales réduisent-elles vraiment la pauvreté ?',
      'i|Les retraites font-elles partie des dépenses sociales ?',
    ],
    'Revenus du travail et du patrimoine': [
      'c|Les riches ont gagné leur argent par leur travail.',
      'c|L’héritage, c’est le fruit du travail des parents, il ne faut pas le taxer.',
      'c|Les revenus du capital sont plus taxés que ceux du travail.',
      'i#|Le patrimoine est-il plus concentré que les revenus ?',
      'i|Pourquoi les loyers et les dividendes progressent-ils plus vite que les salaires ?',
      'i|Peut-on encore devenir propriétaire avec un salaire moyen ?',
    ],
  },

  economie: {
    'Inflation': [
      'c|L’inflation, c’est la faute des salaires trop élevés.',
      'c|L’inflation est finie, les prix ont baissé.',
      'c|L’euro a fait exploser les prix.',
      'i#|Pourquoi les prix restent-ils hauts alors que l’inflation ralentit ?',
      'i~|Pourquoi mes courses me coûtent-elles toujours plus cher ?',
      'i|Indexer les salaires sur les prix créerait-il plus d’inflation ?',
    ],
    'Salaires': [
      'c|Augmenter les salaires ferait fermer les entreprises.',
      'c|Les patrons ne peuvent pas payer plus.',
      'c|Les fonctionnaires sont mieux payés que le privé.',
      'i#|Les salaires ont-ils augmenté moins vite que les prix ?',
      'i|Pourquoi les salaires des femmes restent-ils plus bas ?',
      'i|Baisser les cotisations augmenterait-il vraiment le salaire net ?',
    ],
    'Prix alimentaires': [
      'c|Si l’alimentation est chère, c’est à cause des normes écologiques.',
      'c|Les supermarchés ne font presque pas de marge.',
      'c|Bien manger, c’est trop cher pour les pauvres.',
      'i#|Qui empoche la hausse des prix alimentaires ?',
      'i|Les lois EGalim protègent-elles vraiment les agriculteurs ?',
      'i~|Pourquoi le bio reste-t-il si cher ?',
    ],
    'Loyers': [
      'c|L’encadrement des loyers fait fuir les propriétaires.',
      'c|Les loyers sont chers parce qu’on ne construit pas assez.',
      'c|Airbnb n’a aucun effet sur les loyers.',
      'i#|De combien les loyers ont-ils augmenté en dix ans ?',
      'i|Pourquoi est-il si difficile de se loger dans les grandes villes ?',
      'i|Les logements vides pourraient-ils résoudre la crise ?',
    ],
    'Marges et profits': [
      'c|Les entreprises ont profité de la crise pour gonfler leurs marges.',
      'c|Les profits d’aujourd’hui sont les investissements de demain.',
      'c|Les superprofits n’existent pas.',
      'i#|Les marges des entreprises ont-elles augmenté pendant l’inflation ?',
      'i|Faut-il taxer les superprofits ?',
      'i|Les profits sont-ils réinvestis ou distribués ?',
    ],
    'Grandes entreprises': [
      'c|Les grandes entreprises paient moins d’impôts que les PME.',
      'c|Sans les grands groupes, il n’y aurait pas d’emplois en France.',
      'c|Les aides publiques aux entreprises créent des emplois.',
      'i#|Combien coûtent les aides publiques aux entreprises ?',
      'i|Les multinationales délocalisent-elles leurs profits ?',
      'i|Faut-il conditionner les aides aux entreprises ?',
    ],
    'PME et artisans': [
      'c|La gauche veut tuer les petits patrons.',
      'c|Les artisans sont écrasés de charges.',
      'c|Les PME paient pour les cadeaux faits aux multinationales.',
      'i~|Pourquoi tant d’artisans ont-ils du mal à recruter ?',
      'i|Les PME profitent-elles des baisses d’impôts ?',
      'i#|Combien de petites entreprises font faillite chaque année ?',
    ],
    'Fiscalité': [
      'c|La France est le pays le plus taxé du monde.',
      'c|Taxer les riches les fera tous partir.',
      'c|La moitié des Français ne paient pas d’impôts.',
      'i#|Qui paie vraiment le plus d’impôts en proportion de ses revenus ?',
      'i|La TVA est-elle un impôt injuste ?',
      'i|Supprimer l’ISF a-t-il fait revenir des capitaux ?',
    ],
    'Patrimoine': [
      'c|Le patrimoine des Français est bien réparti.',
      'c|Les droits de succession sont du vol.',
      'c|On ne peut plus rien transmettre à ses enfants.',
      'i#|Quelle part du patrimoine les 10 % les plus riches possèdent-ils ?',
      'i|Les droits de succession concernent-ils la plupart des familles ?',
      'i|L’immobilier est-il devenu un privilège ?',
    ],
    'Dividendes': [
      'c|Les dividendes battent des records pendant que les salaires stagnent.',
      'c|Les dividendes récompensent le risque pris par les actionnaires.',
      'c|Les entreprises distribuent plus aux actionnaires qu’aux salariés.',
      'i#|Les dividendes versés en France ont-ils augmenté plus vite que les salaires ?',
      'i|Faut-il partager davantage les profits avec les salariés ?',
      'i|La participation et l’intéressement compensent-ils les dividendes ?',
    ],
    'Dette publique': [
      'c|La dette va mettre la France en faillite.',
      'c|On laisse une dette énorme à nos enfants à cause des dépenses sociales.',
      'c|Un État, c’est comme un ménage : on ne dépense pas plus qu’on gagne.',
      'i#|À qui la France doit-elle sa dette ?',
      'i|La dette est-elle due aux dépenses ou aux baisses d’impôts ?',
      'i|Peut-on investir dans l’avenir en s’endettant ?',
    ],
    'Déficit public': [
      'c|Le déficit vient des fonctionnaires trop nombreux.',
      'c|Il faut couper dans les dépenses sociales pour réduire le déficit.',
      'c|Les règles européennes interdisent tout déficit.',
      'i#|Pourquoi le déficit s’est-il creusé ces dernières années ?',
      'i|Les baisses d’impôts ont-elles creusé le déficit ?',
      'i|L’austérité réduit-elle vraiment les déficits ?',
    ],
    'Services publics': [
      'c|Les services publics coûtent trop cher pour ce qu’ils rendent.',
      'c|Le privé ferait mieux et moins cher que l’État.',
      'c|On paie des impôts et on n’a plus aucun service.',
      'i#|Combien coûtent vraiment les services publics par habitant ?',
      'i|Les privatisations ont-elles fait baisser les prix ?',
      'i~|Pourquoi la poste et les gares ferment-elles près de chez moi ?',
    ],
    'Répartition des richesses': [
      'c|Les riches créent la richesse, il faut les laisser faire.',
      'c|La théorie du ruissellement fonctionne.',
      'c|Les inégalités sont le prix de la croissance.',
      'i#|Les plus riches ont-ils profité plus que les autres de la croissance ?',
      'i|Une meilleure répartition des richesses freinerait-elle l’économie ?',
      'i|Combien gagne un patron du CAC 40 par rapport à ses salariés ?',
    ],
    'Inégalités économiques': [
      'c|Les inégalités ont baissé en France.',
      'c|Les inégalités, c’est naturel.',
      'c|La France est le pays le plus égalitaire du monde.',
      'i#|Les inégalités augmentent-elles en France ?',
      'i|Les inégalités de patrimoine sont-elles plus fortes que celles de revenus ?',
      'i~|Pourquoi l’ascenseur social semble-t-il en panne ?',
    ],
    'Comparaisons internationales': [
      'c|Les Allemands travaillent plus et réussissent mieux.',
      'c|Le modèle américain crée plus de richesse pour tous.',
      'c|Tous nos voisins font des réformes, sauf nous.',
      'i#|Le pouvoir d’achat est-il plus élevé en Allemagne ?',
      'i|Les pays nordiques sont-ils riches malgré ou grâce à leurs impôts ?',
      'i|Peut-on comparer les taux de prélèvements obligatoires entre pays ?',
    ],
  },

  ecologie: {
    'Changement climatique': [
      'c|Le climat a toujours changé, l’homme n’y est pour rien.',
      'c|Le réchauffement climatique est exagéré par les écolos.',
      'c|Il a fait froid cet hiver, donc le réchauffement est une arnaque.',
      'i#|De combien la France s’est-elle déjà réchauffée ?',
      'i|Les canicules et les sécheresses sont-elles liées au climat ?',
      'i|Est-il trop tard pour agir ?',
    ],
    'Émissions de gaz à effet de serre': [
      'c|La France ne pollue presque pas, ça ne sert à rien de faire des efforts.',
      'c|C’est la Chine qui pollue, pas nous.',
      'c|Les avions privés, c’est symbolique, ça ne pèse rien.',
      'i#|Les émissions importées comptent-elles dans le bilan de la France ?',
      'i|Quels secteurs émettent le plus en France ?',
      'i#|Les plus riches émettent-ils beaucoup plus que les autres ?',
    ],
    'Nucléaire': [
      'c|Le nucléaire est une énergie dangereuse et dépassée.',
      'c|Sans nucléaire, on retournerait à la bougie.',
      'c|Les déchets nucléaires sont un problème insoluble.',
      'i#|Quelle part de notre électricité vient du nucléaire ?',
      'i|Les nouveaux réacteurs EPR valent-ils leur coût ?',
      'i|Le nucléaire est-il compatible avec le climat ?',
    ],
    'Énergies renouvelables': [
      'c|Les éoliennes ne servent à rien.',
      'c|Le solaire et l’éolien sont trop intermittents pour compter.',
      'c|Les renouvelables font exploser les factures.',
      'i#|Quelle part de l’électricité vient des renouvelables en France ?',
      'i|Les éoliennes abîment-elles les paysages et la biodiversité ?',
      'i|Peut-on se passer du nucléaire avec les renouvelables ?',
    ],
    'Prix de l’énergie': [
      'c|L’électricité est chère à cause du marché européen.',
      'c|Les taxes représentent la moitié du prix de l’essence.',
      'c|Le chèque énergie, c’est une aumône.',
      'i#|Pourquoi ma facture d’électricité a-t-elle autant augmenté ?',
      'i|Faut-il sortir du marché européen de l’électricité ?',
      'i~|Comment se chauffer quand on n’a pas les moyens ?',
    ],
    'Transports': [
      'c|La voiture électrique est plus polluante que l’essence.',
      'c|Les écolos veulent interdire la voiture.',
      'c|Le train est trop cher, c’est normal que les gens prennent l’avion.',
      'i#|La voiture électrique pollue-t-elle moins sur toute sa vie ?',
      'i~|Comment faire sans voiture à la campagne ?',
      'i|Les zones à faibles émissions pénalisent-elles les plus modestes ?',
    ],
    'Agriculture': [
      'c|Les normes écologiques tuent les agriculteurs.',
      'c|Les agriculteurs gagnent bien leur vie grâce aux subventions.',
      'c|Le bio ne pourrait pas nourrir le monde.',
      'i#|Combien gagne vraiment un agriculteur ?',
      'i|Les accords de libre-échange menacent-ils nos paysans ?',
      'i|À qui profitent les aides de la PAC ?',
    ],
    'Pesticides': [
      'c|Sans pesticides, l’agriculture française s’effondrerait.',
      'c|Le glyphosate est sans danger.',
      'c|Les pesticides, c’est le problème des agriculteurs, pas le nôtre.',
      'i|Les pesticides ont-ils un effet sur la santé des agriculteurs ?',
      'i#|La France utilise-t-elle plus de pesticides que ses voisins ?',
      'i|Existe-t-il des alternatives réalistes aux pesticides ?',
    ],
    'Biodiversité': [
      'c|La biodiversité, c’est un sujet de bobos.',
      'c|Les espèces disparaissent depuis toujours, c’est la nature.',
      'c|Protéger le loup coûte plus cher que ça ne rapporte.',
      'i#|Les insectes et les oiseaux disparaissent-ils vraiment ?',
      'i|Pourquoi la biodiversité est-elle utile à l’agriculture ?',
      'i|L’artificialisation des sols est-elle un problème en France ?',
    ],
    'Rénovation thermique': [
      'c|L’interdiction de louer les passoires thermiques va vider le marché locatif.',
      'c|MaPrimeRénov’ est une usine à fraudes.',
      'c|Isoler les maisons ne rapporte rien.',
      'i#|Combien de logements sont des passoires thermiques ?',
      'i~|Comment financer l’isolation quand on a des petits revenus ?',
      'i|Le diagnostic de performance énergétique est-il fiable ?',
    ],
    'Industrie': [
      'c|L’écologie détruit l’industrie française.',
      'c|On a délocalisé notre pollution en Chine.',
      'c|Réindustrialiser, c’est forcément polluer plus.',
      'i#|L’industrie française pèse-t-elle encore lourd ?',
      'i|Peut-on relocaliser des usines tout en réduisant les émissions ?',
      'i|L’acier et le ciment peuvent-ils être décarbonés ?',
    ],
    'Justice climatique': [
      'c|L’écologie punitive pèse sur les classes populaires.',
      'c|Les écolos sont des bobos qui donnent des leçons.',
      'c|Ce sont les pays pauvres qui polluent le plus.',
      'i#|Les plus riches polluent-ils plus que les plus pauvres ?',
      'i|Comment faire une transition juste pour tous ?',
      'i|Les taxes carbone sont-elles forcément injustes ?',
    ],
    'Transition énergétique et emploi': [
      'c|La transition écologique va détruire des emplois.',
      'c|Les emplois verts sont des emplois au rabais.',
      'c|L’écologie, c’est la décroissance et le chômage.',
      'i#|Combien d’emplois la rénovation et les renouvelables créent-ils ?',
      'i~|Que vont devenir les salariés de l’automobile ?',
      'i|La transition peut-elle créer des emplois dans les territoires ?',
    ],
  },

  services: {
    'Hôpital public': [
      'c|L’hôpital a plein d’argent, il est juste mal géré.',
      'c|Il y a trop d’administratifs à l’hôpital.',
      'c|Les urgences sont saturées à cause des gens qui y vont pour rien.',
      'i#|Combien de lits d’hôpital ont été fermés ces dernières années ?',
      'i~|Pourquoi attend-on autant aux urgences ?',
      'i|Pourquoi les soignants quittent-ils l’hôpital ?',
    ],
    'Médecins et déserts médicaux': [
      'c|Il suffit d’obliger les jeunes médecins à s’installer à la campagne.',
      'c|Les médecins ne veulent plus travailler autant qu’avant.',
      'c|Il y a assez de médecins, ils sont juste mal répartis.',
      'i#|Combien de Français n’ont pas de médecin traitant ?',
      'i|Le numerus clausus explique-t-il la pénurie ?',
      'i~|Pourquoi faut-il des mois pour voir un spécialiste ?',
    ],
    'Assurance maladie': [
      'c|La Sécu est en faillite.',
      'c|Les Français abusent des médicaments et des arrêts maladie.',
      'c|Les mutuelles privées géreraient mieux la santé.',
      'i#|Le déficit de la Sécu est-il vraiment hors de contrôle ?',
      'i|Les franchises médicales sont-elles justes ?',
      'i|Pourquoi les mutuelles augmentent-elles chaque année ?',
    ],
    'École publique': [
      'c|Le niveau scolaire s’effondre.',
      'c|Les profs sont toujours en vacances.',
      'c|L’école privée fait mieux que le public.',
      'i#|Les élèves français sont-ils moins bons qu’avant ?',
      'i|Pourquoi manque-t-il autant de professeurs ?',
      'i~|Pourquoi des familles quittent-elles le public pour le privé ?',
    ],
    'Inégalités scolaires': [
      'c|La réussite scolaire, c’est une question de mérite.',
      'c|L’école donne sa chance à tout le monde.',
      'c|Les enfants des quartiers ne veulent pas réussir.',
      'i#|L’origine sociale pèse-t-elle plus en France qu’ailleurs ?',
      'i|Les classes de niveau aideraient-elles les élèves en difficulté ?',
      'i|Pourquoi si peu d’enfants d’ouvriers font-ils de grandes écoles ?',
    ],
    'Université': [
      'c|L’université est une fabrique de chômeurs.',
      'c|Les études gratuites, ça n’incite pas à travailler.',
      'c|Parcoursup est plus juste que l’ancien système.',
      'i~|Pourquoi tant d’étudiants vivent-ils dans la précarité ?',
      'i#|Combien d’étudiants abandonnent en première année ?',
      'i|Faut-il augmenter les frais d’inscription ?',
    ],
    'Éducation prioritaire': [
      'c|On donne tout aux écoles de banlieue et rien aux campagnes.',
      'c|L’éducation prioritaire est un échec coûteux.',
      'c|Dédoubler les classes ne sert à rien.',
      'i#|Les élèves en éducation prioritaire progressent-ils ?',
      'i|Les écoles rurales sont-elles oubliées ?',
      'i|Pourquoi les profs débutants sont-ils envoyés dans les zones difficiles ?',
    ],
    'Services publics locaux': [
      'c|Les mairies gaspillent l’argent des contribuables.',
      'c|Les services publics ne ferment pas, ils se modernisent.',
      'c|Les maisons France Services remplacent bien les guichets.',
      'i~|Pourquoi faut-il faire 30 kilomètres pour une démarche administrative ?',
      'i|La dématérialisation laisse-t-elle des gens de côté ?',
      'i#|Combien de bureaux de poste ont fermé ?',
    ],
    'Transports collectifs': [
      'c|La SNCF est toujours en grève.',
      'c|Ouvrir le train à la concurrence fera baisser les prix.',
      'c|Les transports gratuits, c’est une utopie.',
      'i#|Pourquoi le train coûte-t-il plus cher que l’avion ?',
      'i|Les petites lignes ferroviaires peuvent-elles être sauvées ?',
      'i|La gratuité des transports a-t-elle marché quelque part ?',
    ],
    'Accès aux soins': [
      'c|En France, tout le monde est soigné gratuitement.',
      'c|Les dépassements d’honoraires sont normaux.',
      'c|La téléconsultation résout le problème des déserts médicaux.',
      'i~|Pourquoi certaines personnes renoncent-elles à se soigner ?',
      'i#|Combien coûte un passage aux urgences ?',
      'i|Les soins dentaires et optiques sont-ils vraiment remboursés ?',
    ],
    'Fonction publique': [
      'c|Il y a trop de fonctionnaires en France.',
      'c|Les fonctionnaires sont des privilégiés.',
      'c|Il faut supprimer le statut de fonctionnaire.',
      'i#|La France a-t-elle plus de fonctionnaires que ses voisins ?',
      'i|Où manque-t-il des agents publics ?',
      'i|Les fonctionnaires ont-ils vraiment la sécurité de l’emploi ?',
    ],
    'Financement des services essentiels': [
      'c|On n’a plus les moyens de financer les services publics.',
      'c|Il faut faire payer les usagers pour sauver les services publics.',
      'c|Chaque euro de service public est un euro de dette.',
      'i#|Comment sont financés l’hôpital et l’école ?',
      'i|Les partenariats public-privé coûtent-ils plus cher ?',
      'i|Peut-on financer les services publics sans augmenter les impôts ?',
    ],
  },

  droits: {
    'Féminisme': [
      'c|Le féminisme est allé trop loin.',
      'c|Les femmes ont déjà tous les droits en France.',
      'c|Les féministes détestent les hommes.',
      'i|À quoi sert encore le féminisme aujourd’hui ?',
      'i~|Pourquoi certaines femmes ont-elles peur de rentrer seules le soir ?',
      'i|La parité en politique a-t-elle changé quelque chose ?',
    ],
    'Égalité salariale': [
      'c|L’égalité salariale hommes-femmes, c’est réglé.',
      'c|Si les femmes gagnent moins, c’est qu’elles choisissent des métiers moins payés.',
      'c|L’écart de salaire est un mythe statistique.',
      'i#|À poste égal, les femmes sont-elles moins payées ?',
      'i|Les temps partiels expliquent-ils l’écart de salaires ?',
      'i~|Pourquoi la carrière des femmes ralentit-elle après un enfant ?',
    ],
    'Violences faites aux femmes': [
      'c|On exagère l’ampleur des violences faites aux femmes.',
      'c|Les féminicides baissent, il n’y a plus de problème.',
      'c|Les femmes mentent souvent pour se venger.',
      'i#|Combien de femmes subissent des violences chaque année ?',
      'i|Les moyens contre les violences sont-ils suffisants ?',
      'i|Le harcèlement de rue est-il vraiment puni ?',
    ],
    'Droits des personnes LGBT': [
      'c|Les LGBT ont déjà tous les droits.',
      'c|On fait de la propagande LGBT à l’école.',
      'c|L’homophobie n’existe presque plus en France.',
      'i#|Les actes anti-LGBT augmentent-ils ?',
      'i|Que change le mariage pour tous dans la vie des couples ?',
      'i~|Pourquoi tant de jeunes LGBT sont-ils harcelés ?',
    ],
    'Laïcité': [
      'c|La laïcité interdit les signes religieux dans la rue.',
      'c|La gauche a abandonné la laïcité.',
      'c|La laïcité est utilisée contre les musulmans.',
      'i|Que dit exactement la loi de 1905 ?',
      'i|Une accompagnatrice voilée peut-elle encadrer une sortie scolaire ?',
      'i|La laïcité protège-t-elle les croyants ou les en éloigne-t-elle ?',
    ],
    'Libertés publiques': [
      'c|On ne peut plus rien dire en France.',
      'c|La surveillance de masse protège les honnêtes gens.',
      'c|L’état d’urgence est devenu permanent.',
      'i|Le droit de manifester est-il menacé ?',
      'i|La reconnaissance faciale est-elle autorisée en France ?',
      'i|Où s’arrête la liberté d’expression ?',
    ],
    'Discriminations': [
      'c|Les discriminations à l’embauche, ça n’existe plus.',
      'c|Parler de discriminations, c’est se victimiser.',
      'c|Les quotas sont une discrimination à l’envers.',
      'i#|Les personnes handicapées ou âgées sont-elles discriminées à l’embauche ?',
      'i|Comment prouver une discrimination ?',
      'i~|Pourquoi certaines personnes changent-elles de prénom sur leur CV ?',
    ],
    'Handicap et accessibilité': [
      'c|L’AAH, c’est assez pour vivre.',
      'c|Les bâtiments sont tous accessibles maintenant.',
      'c|Le handicap, c’est l’affaire des familles.',
      'i#|Combien de personnes handicapées sont au chômage ?',
      'i~|Pourquoi est-ce si compliqué de scolariser un enfant handicapé ?',
      'i|La déconjugalisation de l’AAH a-t-elle changé quelque chose ?',
    ],
    'Droits des travailleurs': [
      'c|Le Code du travail est trop épais et empêche d’embaucher.',
      'c|Les syndicats bloquent le pays.',
      'c|Le droit de grève prend les usagers en otage.',
      'i|Les ordonnances travail ont-elles créé des emplois ?',
      'i~|Que faire face à un licenciement abusif ?',
      'i#|Les accidents du travail sont-ils en baisse ?',
    ],
    'Égalité des chances': [
      'c|En France, quand on veut, on peut.',
      'c|L’égalité des chances existe déjà grâce à l’école gratuite.',
      'c|La méritocratie est juste.',
      'i|Les bourses suffisent-elles à réduire les inégalités ?',
      'i~|Pourquoi le réseau compte-t-il autant pour trouver un stage ?',
      'i#|Un enfant de cadre a-t-il plus de chances de devenir cadre ?',
    ],
    'Émancipation': [
      'c|L’émancipation, c’est un concept de gauchiste.',
      'c|Chacun est responsable de sa réussite, l’État n’a pas à s’en mêler.',
      'c|La culture, c’est pour les élites.',
      'i|L’éducation populaire sert-elle encore à quelque chose ?',
      'i|Le temps libre est-il une conquête sociale ?',
      'i~|Comment se former quand on travaille déjà beaucoup ?',
    ],
    'Histoire des conquêtes sociales': [
      'c|Les congés payés, c’est le patronat qui les a offerts.',
      'c|Les acquis sociaux sont tombés du ciel.',
      'c|La Sécurité sociale a été créée par de Gaulle tout seul.',
      'i|Qui a obtenu la semaine de 40 heures ?',
      'i|Comment les grèves de 1936 ont-elles changé la vie des ouvriers ?',
      'i|D’où vient la retraite par répartition ?',
    ],
  },

  politique: {
    'France insoumise': [
      'c|Mélenchon crie tout le temps.',
      'c|LFI est antisémite.',
      'c|Mélenchon est dangereux pour la démocratie.',
      'i|Que propose vraiment La France insoumise ?',
      'i|Le programme de LFI est-il réaliste ?',
      'i|Pourquoi LFI est-elle aussi critiquée dans les médias ?',
    ],
    'Rassemblement national': [
      'c|Le RN défend les travailleurs.',
      'c|Le RN a changé, ce n’est plus l’extrême droite.',
      'c|Le RN n’a jamais gouverné, donc il mérite sa chance.',
      'i|Comment le RN vote-t-il sur les salaires à l’Assemblée ?',
      'i|D’où vient le Front national ?',
      'i|Que propose le RN pour les retraites ?',
    ],
    'Droite et extrême droite': [
      'c|La droite et l’extrême droite, c’est pareil.',
      'c|L’extrême droite, ça n’existe plus en France.',
      'c|Être de droite, c’est défendre la France.',
      'i|Où passe la frontière entre droite et extrême droite ?',
      'i|Pourquoi une partie de la droite s’allie-t-elle avec l’extrême droite ?',
      'i|Qu’est-ce qui distingue le conservatisme du nationalisme ?',
    ],
    'Gauche et pluralisme politique': [
      'c|La gauche ne s’occupe plus des ouvriers.',
      'c|La gauche est toujours divisée, elle ne gagnera jamais.',
      'c|La gauche, c’est le parti des assistés.',
      'i|Pourquoi la gauche a-t-elle perdu une partie des classes populaires ?',
      'i|Une union de la gauche est-elle possible durablement ?',
      'i|Qu’est-ce qui sépare les différentes gauches ?',
    ],
    'Programmes électoraux': [
      'c|Les programmes de gauche sont irréalisables.',
      'c|Les politiques ne tiennent jamais leurs promesses.',
      'c|Un programme chiffré, c’est forcément sérieux.',
      'i|Comment vérifier le coût d’un programme ?',
      'i|Les promesses électorales sont-elles souvent tenues ?',
      'i|Qui chiffre les programmes, et avec quelles hypothèses ?',
    ],
    'Institutions françaises': [
      'c|Le Parlement ne sert à rien.',
      'c|Le 49.3 est un déni de démocratie.',
      'c|Le président a tous les pouvoirs.',
      'i|À quoi sert le Sénat ?',
      'i|Comment fonctionne une motion de censure ?',
      'i|La proportionnelle rendrait-elle le pays ingouvernable ?',
    ],
    'Constitution': [
      'c|La Ve République est à bout de souffle.',
      'c|Il faut changer de Constitution pour sauver la démocratie.',
      'c|Le Conseil constitutionnel bloque la volonté du peuple.',
      'i|Qui peut réviser la Constitution ?',
      'i|Une VIe République changerait-elle vraiment les choses ?',
      'i|Le Conseil constitutionnel est-il indépendant ?',
    ],
    'Médias': [
      'c|Les médias cachent volontairement la vérité.',
      'c|Tous les médias sont de gauche.',
      'c|Quelques milliardaires possèdent toute la presse.',
      'i|Qui possède les principaux médias français ?',
      'i|L’audiovisuel public est-il neutre ?',
      'i|Comment savoir si un média est fiable ?',
    ],
    'Désinformation': [
      'c|Les fact-checkeurs sont des censeurs.',
      'c|On ne peut plus croire personne, tout le monde ment.',
      'c|Sur les réseaux, on trouve enfin la vraie information.',
      'i|Comment reconnaître une fausse information ?',
      'i|Les ingérences étrangères influencent-elles nos élections ?',
      'i~|Pourquoi partage-t-on parfois des fausses nouvelles sans le vouloir ?',
    ],
    'Sondages': [
      'c|Les sondages sont truqués.',
      'c|Les sondages font l’élection.',
      'c|Un sondage sur mille personnes ne veut rien dire.',
      'i#|Quelle est la marge d’erreur d’un sondage ?',
      'i|Comment est choisi l’échantillon d’un sondage ?',
      'i|Les sondages se sont-ils souvent trompés ?',
    ],
    'Abstention': [
      'c|Voter ne sert à rien, ils sont tous pareils.',
      'c|Les abstentionnistes n’ont pas le droit de se plaindre.',
      'c|L’abstention montre que les gens sont satisfaits.',
      'i#|Qui s’abstient le plus ?',
      'i|Le vote blanc devrait-il être reconnu ?',
      'i~|Pourquoi les jeunes votent-ils moins ?',
    ],
    'Financement politique': [
      'c|Les partis vivent de l’argent public sans rien faire.',
      'c|Tous les partis ont des affaires de financement.',
      'c|Les milliardaires achètent les élections.',
      'i|Comment les partis politiques sont-ils financés ?',
      'i|Les dons aux partis sont-ils plafonnés ?',
      'i|Les campagnes électorales coûtent-elles cher ?',
    ],
    'Union européenne': [
      'c|L’Union européenne nous impose tout.',
      'c|Sans l’Europe, on vivrait mieux.',
      'c|Bruxelles est dirigée par des technocrates non élus.',
      'i|Qui décide vraiment à Bruxelles ?',
      'i|La France paie-t-elle plus à l’UE qu’elle ne reçoit ?',
      'i|Pourrait-on changer les traités européens ?',
    ],
    'Souveraineté': [
      'c|Seul le peuple est souverain, et on ne lui demande jamais son avis.',
      'c|La souveraineté nationale, c’est une idée d’extrême droite.',
      'c|La France a perdu toute souveraineté.',
      'i|Que veut dire « souveraineté populaire » ?',
      'i|Peut-on être souverainiste et de gauche ?',
      'i|La souveraineté industrielle est-elle possible ?',
    ],
    'Démocratie directe': [
      'c|Le référendum d’initiative citoyenne, c’est la démocratie.',
      'c|Le RIC mènerait au chaos.',
      'c|On ne consulte jamais le peuple en France.',
      'i|Comment fonctionne le référendum d’initiative partagée ?',
      'i|La Suisse est-elle un modèle de démocratie directe ?',
      'i|Les conventions citoyennes servent-elles à quelque chose ?',
    ],
    'Comparaisons internationales': [
      'c|Les démocraties autoritaires sont plus efficaces.',
      'c|La démocratie française est la meilleure du monde.',
      'c|Les autres pays votent mieux que nous.',
      'i|Quels pays ont la plus forte participation électorale ?',
      'i|Le vote obligatoire marche-t-il ailleurs ?',
      'i|Comment les autres démocraties forment-elles leurs gouvernements ?',
    ],
    'Histoire politique contemporaine': [
      'c|Mai 68 a détruit l’autorité.',
      'c|Mitterrand a ruiné la France.',
      'c|La gauche n’a jamais rien fait de bien au pouvoir.',
      'i|Qu’a changé le tournant de la rigueur en 1983 ?',
      'i|Quelles réformes sociales datent des gouvernements de gauche ?',
      'i|Comment la cohabitation a-t-elle fonctionné ?',
    ],
  },

  international: {
    'Histoire sociale': [
      'c|Les ouvriers vivaient bien au XIXe siècle.',
      'c|Le progrès social vient du progrès technique, pas des luttes.',
      'c|La Commune de Paris n’était qu’une émeute.',
      'i|Comment vivaient les ouvriers avant les lois sociales ?',
      'i|Quand le travail des enfants a-t-il été interdit ?',
      'i|Que s’est-il passé pendant la Commune de Paris ?',
    ],
    'Histoire économique': [
      'c|Les Trente Glorieuses, c’était grâce au libéralisme.',
      'c|Le protectionnisme a toujours appauvri les pays.',
      'c|Les nationalisations ont été des échecs.',
      'i|Comment la France s’est-elle reconstruite après 1945 ?',
      'i|Pourquoi la croissance a-t-elle ralenti après 1973 ?',
      'i|Le plan Marshall a-t-il tout fait ?',
    ],
    'Histoire du mouvement ouvrier': [
      'c|Les syndicats n’ont jamais servi qu’à faire grève.',
      'c|Le Front populaire a ruiné l’économie.',
      'c|Les communistes ont collaboré pendant la guerre.',
      'i|Qu’a obtenu le Front populaire en 1936 ?',
      'i|Quel rôle ont joué les ouvriers dans la Résistance ?',
      'i|D’où vient le 1er mai ?',
    ],
    'Colonisation et décolonisation': [
      'c|La colonisation a apporté la civilisation.',
      'c|La France n’a pas à s’excuser pour son passé colonial.',
      'c|La colonisation a rapporté énormément d’argent à la France.',
      'i|Que s’est-il passé pendant la guerre d’Algérie ?',
      'i|La colonisation a-t-elle enrichi la France ou coûté cher ?',
      'i|Faut-il reconnaître les crimes coloniaux ?',
    ],
    'Guerres et conflits': [
      'c|La guerre en Ukraine, c’est la faute de l’OTAN.',
      'c|Il faut négocier avec Poutine à tout prix.',
      'c|Livrer des armes, c’est prolonger la guerre.',
      'i|Pourquoi la Russie a-t-elle envahi l’Ukraine ?',
      'i|Comment se terminent les guerres ?',
      'i|La France doit-elle augmenter ses dépenses militaires ?',
    ],
    'Palestine et Israël': [
      'c|Critiquer Israël, c’est être antisémite.',
      'c|Soutenir la Palestine, c’est soutenir le terrorisme.',
      'c|Le conflit est trop compliqué pour avoir un avis.',
      'i|Que dit le droit international sur la colonisation en Cisjordanie ?',
      'i|Quelle différence entre antisionisme et antisémitisme ?',
      'i|La solution à deux États est-elle encore possible ?',
    ],
    'Relations internationales': [
      'c|La France ne compte plus dans le monde.',
      'c|L’ONU ne sert à rien.',
      'c|L’aide au développement est de l’argent gaspillé.',
      'i|Quel rôle joue la France au Conseil de sécurité ?',
      'i|L’aide au développement réduit-elle les migrations ?',
      'i|Le droit international est-il encore respecté ?',
    ],
    'États-Unis': [
      'c|Le modèle américain prouve que le libéralisme marche.',
      'c|Aux États-Unis, tout le monde peut réussir.',
      'c|Les Américains nous protègent, on leur doit tout.',
      'i#|Les inégalités sont-elles plus fortes aux États-Unis ?',
      'i|Comment fonctionne la santé aux États-Unis ?',
      'i|L’Europe doit-elle être indépendante des États-Unis ?',
    ],
    'Europe': [
      'c|L’Allemagne domine l’Europe.',
      'c|L’euro a appauvri les Français.',
      'c|L’élargissement de l’UE a fait venir des travailleurs low cost.',
      'i|Les travailleurs détachés font-ils du dumping social ?',
      'i|Une Europe sociale est-elle possible ?',
      'i|Comment l’UE a-t-elle réagi à la crise du Covid ?',
    ],
    'Chine': [
      'c|La Chine prouve qu’une dictature est plus efficace.',
      'c|La Chine va dominer le monde, c’est inévitable.',
      'c|Tout ce qui est chinois est de la mauvaise qualité.',
      'i|Pourquoi l’Europe dépend-elle autant de la Chine ?',
      'i|La Chine respecte-t-elle les règles du commerce mondial ?',
      'i|Que se passe-t-il au Xinjiang ?',
    ],
    'Russie': [
      'c|Poutine défend les valeurs traditionnelles contre l’Occident.',
      'c|Les sanctions contre la Russie ne font souffrir que nous.',
      'c|La Russie a toujours été humiliée par l’Occident.',
      'i|Les sanctions ont-elles affaibli l’économie russe ?',
      'i|Comment la Russie influence-t-elle l’opinion en Europe ?',
      'i|Quelle est la situation des opposants en Russie ?',
    ],
    'Amérique latine': [
      'c|Le socialisme a ruiné le Venezuela.',
      'c|Cuba prouve que le communisme ne marche pas.',
      'c|Lula est un corrompu.',
      'i|Qu’ont changé les politiques sociales au Brésil ?',
      'i|Pourquoi le Venezuela est-il en crise ?',
      'i|L’Amérique latine a-t-elle réduit la pauvreté ?',
    ],
    'Institutions internationales': [
      'c|Le FMI et la Banque mondiale imposent l’austérité.',
      'c|L’OMC ne profite qu’aux multinationales.',
      'c|La Cour pénale internationale ne juge que les Africains.',
      'i|À quoi sert l’Organisation mondiale du commerce ?',
      'i|Comment fonctionne la Cour pénale internationale ?',
      'i|L’OMS a-t-elle bien géré la pandémie ?',
    ],
    'Comparaisons entre modèles économiques et sociaux': [
      'c|Le modèle social français est le pire d’Europe.',
      'c|Le modèle scandinave n’est possible que dans les petits pays.',
      'c|Le modèle anglo-saxon crée plus d’emplois.',
      'i#|La France redistribue-t-elle plus que ses voisins ?',
      'i|Qu’est-ce que la flexisécurité danoise ?',
      'i|Les pays les plus égalitaires sont-ils les plus heureux ?',
    ],
  },
};

/** Suggestions pour « Autre sujet » ou quand aucun volet n'est choisi. */
export const SG_GENERALES = [
  'c|C’était mieux avant.',
  'c|Ils sont tous pourris.',
  'c|On paie trop d’impôts pour rien.',
  'c|On ne peut plus rien dire.',
  'i|Comment savoir si une information est vraie ?',
  'i|Pourquoi les débats politiques finissent-ils toujours en dispute ?',
  'i|Comment parler politique en famille sans se fâcher ?',
];

const sgParse = (s) => { const k = s.indexOf('|'); const f = s.slice(0, k); return { texte: s.slice(k + 1), choc: f.includes('c'), chiffre: f.includes('#'), vecu: f.includes('~') }; };

/** Toutes les suggestions d'un sous-thème (ou d'un volet entier), annotées. */
export function sgPool(volet, sousTheme) {
  const v = SG_BIBLIOTHEQUE[volet];
  if (!v) return SG_GENERALES.map((s) => ({ ...sgParse(s), sousTheme: null }));
  if (sousTheme && v[sousTheme]) return v[sousTheme].map((s) => ({ ...sgParse(s), sousTheme }));
  // volet sans sous-thème : on alterne les sous-thèmes pour varier les arguments
  const listes = Object.entries(v).map(([st, arr]) => arr.map((s) => ({ ...sgParse(s), sousTheme: st })));
  const out = [];
  for (let k = 0; out.length < listes.reduce((a, l) => a + l.length, 0); k += 1) for (const l of listes) if (l[k]) out.push(l[k]);
  return out;
}

/**
 * Choisit `n` suggestions adaptées au contexte, sans répéter celles déjà vues tant qu'il en reste.
 * ctx : { volet, sousTheme, mode ('gagner'|'convaincre'), interlocuteur (profil), vues: [textes] }
 */
export function suggestionsPour(ctx = {}, n = 3) {
  const pool = sgPool(ctx.volet, ctx.sousTheme);
  const p = ctx.interlocuteur || {};
  const vues = new Set(ctx.vues || []);
  const cadre = p.cadre;
  const faits = p.faits;
  const securite = (p.valeurs || []).some((x) => x === 'securite' || x === 'ordre');
  const score = (s, i) => {
    let x = 0;
    if (ctx.mode === 'convaincre') x += s.choc ? 0 : 3; else x += s.choc ? 3 : 0;
    if (cadre === 'reseaux' || cadre === 'plusieurs' || p.lien === 'public') x += s.choc ? 1 : 0;
    if (cadre === 'repas' || cadre === 'prive' || p.lien === 'parent' || p.lien === 'conjoint') x += s.choc ? 0 : 1;
    if ((faits === 'chiffres' || faits === 'logique') && s.chiffre) x += 1.5;
    if ((faits === 'experience' || faits === 'temoignages' || faits === 'exemples') && s.vecu) x += 1.5;
    if (securite && !ctx.sousTheme && /(sécurit|délinqu|police|prison|violence|crime|expuls)/i.test(s.texte)) x += 1;
    // une affirmation proposée doit mener à une réponse : celles qui ont une fiche vérifiée passent devant
    if (ctx.estCouverte) x += ctx.estCouverte(s.texte) ? 10 : 0;
    return x - i * 0.01; // à score égal, l'ordre éditorial
  };
  const classees = pool.map((s, i) => ({ s, k: score(s, i) })).sort((a, b) => b.k - a.k).map((x) => x.s);
  let libres = classees.filter((s) => !vues.has(s.texte));
  let cycle = false;
  if (libres.length < n) { cycle = true; libres = [...libres, ...classees.filter((s) => vues.has(s.texte))]; }
  return { suggestions: libres.slice(0, n), total: pool.length, restantes: Math.max(0, classees.filter((s) => !vues.has(s.texte)).length - n), cycle };
}

/** Audit : sous-thèmes sans suggestions suffisantes, doublons, sous-thèmes inconnus. */
export function auditSuggestions({ min = 3, minParMode = 2 } = {}) {
  const problemes = [];
  const vus = new Map();
  let nb = 0;
  for (const v of VOLETS) {
    const lib = SG_BIBLIOTHEQUE[v.id] || {};
    for (const st of v.sousThemes) {
      const arr = (lib[st] || []).map(sgParse);
      nb += 1;
      if (arr.length < min + 2) problemes.push(`${v.id} › ${st} : ${arr.length} suggestion(s), minimum ${min + 2}`);
      if (arr.filter((s) => s.choc).length < minParMode) problemes.push(`${v.id} › ${st} : pas assez de formulations « riposte »`);
      if (arr.filter((s) => !s.choc).length < minParMode) problemes.push(`${v.id} › ${st} : pas assez de formulations « dialogue »`);
      for (const s of arr) {
        const cle = s.texte.toLowerCase();
        if (vus.has(cle)) problemes.push(`doublon : « ${s.texte} » (${vus.get(cle)} et ${v.id} › ${st})`);
        vus.set(cle, `${v.id} › ${st}`);
      }
    }
    for (const st of Object.keys(lib)) if (!v.sousThemes.includes(st)) problemes.push(`${v.id} › ${st} : sous-thème inconnu de la taxonomie`);
  }
  // quasi-doublons (indice de Jaccard ≥ 0,7 sur les mots pleins) : reformulations recyclées
  const COMMUNS = new Set(['france', 'franca', 'pays', 'europe', 'monde', 'faut', 'vraiment', 'peut']);
  const toutes = [...vus.entries()].map(([t, ou]) => ({ t, ou, m: new Set(kbTokens(t).map((x) => x.slice(0, 6)).filter((x) => !COMMUNS.has(x))) }));
  for (let i = 0; i < toutes.length; i++) for (let j = i + 1; j < toutes.length; j++) {
    const a = toutes[i].m; const b = toutes[j].m;
    if (a.size < 3 || b.size < 3) continue;
    let c = 0; for (const x of a) if (b.has(x)) c += 1;
    if (c / (a.size + b.size - c) >= 0.7 && c >= 3) problemes.push(`quasi-doublon : « ${toutes[i].t} » (${toutes[i].ou}) / « ${toutes[j].t} » (${toutes[j].ou})`);
  }
  return { sousThemes: nb, suggestions: vus.size, problemes };
}
