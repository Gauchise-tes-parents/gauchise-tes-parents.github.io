"""Migration des 6 fiches v2 vers le schéma v3 (idempotent).

Ajoute : type, rubriques, mots_cles, fiabilite, stabilite, contexte, explication,
argumentaires {court, moyen, detaille, empathie}, contre_arguments, fiabilite par fait.
Les contenus factuels (faits, sources, limites) ne sont pas modifiés.
"""
import json, os

LIB = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'library')

AJOUTS = {
 'immigres-aides': dict(
  mots_cles=['immigrés', 'aides sociales', 'allocations', 'rsa', 'étrangers', 'ocde', 'contribution nette', 'finances publiques'],
  fiabilite='etabli', stabilite='evolutive',
  contexte="L'idée que les immigrés seraient favorisés dans l'accès aux aides est très répandue. Elle mélange les règles d'accès aux prestations (identiques ou plus restrictives pour les étrangers) et le bilan budgétaire global de l'immigration.",
  explication="Les prestations sociales obéissent aux mêmes barèmes pour tous ; les étrangers non européens doivent en plus remplir des conditions de durée de séjour. Le bilan budgétaire dépend surtout du taux d'emploi.",
  moyen="Il faut séparer deux questions. Les règles d'abord : les aides ont les mêmes barèmes pour tout le monde, et pour le RSA un étranger hors Union européenne doit en général avoir un titre de séjour depuis au moins cinq ans. Le bilan ensuite : l'OCDE a calculé en 2021 que, dans presque tous les pays étudiés, on dépense moins par immigré que par natif. S'ils contribuent parfois un peu moins, c'est surtout parce qu'ils ont moins accès à l'emploi. Si on veut améliorer le bilan, la piste, c'est l'emploi, pas la suppression des aides.",
  empathie="Je comprends que ça puisse sembler injuste quand on a l'impression que d'autres reçoivent plus. Mais les règles sont en fait plus strictes pour les étrangers, et l'OCDE montre qu'on dépense en moyenne moins pour eux. Le vrai problème, c'est l'accès au travail.",
  contre=[
   ("Ils ont plus d'enfants, donc plus d'allocations familiales.", "Les allocations dépendent du nombre d'enfants, pas de la nationalité : une famille française de même taille touche la même chose."),
   ("Les immigrés coûtent plus qu'ils ne rapportent.", "Selon l'OCDE, la contribution nette reste comprise entre −1 % et +1 % du PIB dans la plupart des pays ; elle dépend surtout du taux d'emploi."),
  ]),
 'rsa-smic': dict(
  mots_cles=['rsa', 'smic', 'travail', 'assistanat', 'prime d activité', 'revenu', 'minimum social'],
  fiabilite='etabli', stabilite='evolutive',
  contexte="L'idée qu'on gagnerait autant au RSA qu'en travaillant nourrit le sentiment que le travail ne paie plus. Elle s'appuie souvent sur des cas particuliers (temps partiel, familles nombreuses).",
  explication="Le RSA est un revenu minimum pour les personnes sans ressources suffisantes ; son montant forfaitaire diminue quand d'autres revenus arrivent. La prime d'activité complète les revenus des salariés modestes.",
  moyen="Pour une personne seule, le RSA, c'est au maximum 651,69 € par mois depuis avril 2026. Un SMIC à temps plein, c'est environ 1 443 € net. Le travail rapporte donc plus du double, et un salarié au SMIC peut en plus toucher la prime d'activité. L'idée reçue vient de cas particuliers, comme un temps partiel très court ou des familles avec enfants, où d'autres aides jouent des deux côtés. Si on veut que le travail paie mieux, la vraie question, c'est le niveau des bas salaires.",
  empathie="Je comprends que ça énerve quand on travaille dur pour pas grand-chose. Mais le RSA, c'est 651 € par mois : personne ne vit bien avec ça. Le problème, c'est plutôt que les salaires les plus bas sont trop faibles.",
  contre=[
   ("Avec les APL et les autres aides, un allocataire gagne presque un SMIC.", "Les salariés modestes ont aussi droit aux aides au logement et à la prime d'activité : il faut comparer des foyers identiques, aides comprises des deux côtés."),
   ("Les gens au RSA travaillent au noir.", "Certains le font sans doute, mais aucune donnée ne permet de généraliser ; c'est l'affaire des contrôles, pas une raison de supprimer un minimum vital."),
  ]),
 'chomeurs-travailler': dict(
  mots_cles=['chômeurs', 'chômage', 'france travail', 'contrôles', 'paresse', 'assistés', 'recherche d emploi'],
  fiabilite='etabli', stabilite='evolutive',
  contexte="Le soupçon de paresse des chômeurs revient à chaque réforme de l'assurance chômage. Les contrôles de la recherche d'emploi, renforcés depuis plusieurs années, permettent de le confronter aux faits.",
  explication="Un contrôle vérifie les démarches de recherche d'emploi d'un inscrit. Les contrôles ciblés visent des profils jugés à risque ; les contrôles aléatoires donnent une image plus représentative.",
  moyen="France Travail contrôle des centaines de milliers de demandeurs d'emploi chaque année. En 2023, sur 523 400 contrôles, 83 % ont montré une recherche active ou ont remobilisé la personne, et même environ 91 % pour les contrôles tirés au sort. Il y a des abus, 17 % de sanctions, mais c'est une minorité. Le chômage s'explique surtout par d'autres raisons : qualifications, transport, garde d'enfants, santé, nombre d'offres.",
  empathie="Je comprends qu'on connaisse tous quelqu'un qui profite. Mais quand on contrôle au hasard, neuf chômeurs sur dix cherchent vraiment. Ceux qui galèrent ont souvent d'autres problèmes : pas de voiture, pas de garde pour les enfants, une santé fragile.",
  contre=[
   ("Il y a plein d'offres non pourvues.", "Des métiers ont du mal à recruter, c'est vrai ; mais les offres ne correspondent pas toujours aux compétences, aux lieux ou aux horaires des chômeurs. Ce point n'est pas chiffré dans cette fiche."),
   ("17 % de sanctions, c'est beaucoup.", "C'est sur des contrôles en partie ciblés vers les situations à risque ; sur les contrôles aléatoires, la proportion de recherche active est d'environ 91 %."),
  ]),
 'delinquance-partout': dict(
  mots_cles=['délinquance', 'insécurité', 'violences', 'cambriolages', 'homicides', 'stupéfiants', 'ssmsi', 'plaintes', 'chiffres'],
  fiabilite='etabli', stabilite='evolutive',
  contexte="Le sentiment d'insécurité est alimenté par des faits divers très médiatisés. Les statistiques officielles distinguent pourtant des évolutions très différentes selon les types d'infractions.",
  explication="La délinquance « enregistrée » compte les faits connus des forces de l'ordre ; elle dépend du nombre de plaintes et de l'activité des services. Les enquêtes de victimation interrogent directement la population pour mesurer aussi les faits non déclarés.",
  moyen="Ça dépend vraiment des infractions. Selon le bilan 2025 du service statistique du ministère de l'Intérieur, les cambriolages, les vols avec armes et les vols de véhicules baissent, et les homicides sont stables. Ce qui augmente, ce sont surtout les violences sexuelles, en partie parce que les victimes portent davantage plainte, les escroqueries et les affaires de stupéfiants. Et la délinquance enregistrée est très concentrée dans les grandes villes. Parler de « la délinquance » en bloc empêche de voir où il faut agir.",
  empathie="Je comprends que tu te sentes moins en sécurité ; ce sentiment est réel et il compte. Mais les chiffres montrent que tout n'augmente pas. Ça aide à cibler les vrais problèmes, comme les violences sexuelles ou le trafic de drogue.",
  contre=[
   ("Les gens ne portent plus plainte, donc les chiffres sont faux.", "C'est pour ça qu'il existe des enquêtes de victimation ; pour certaines infractions, comme les violences sexuelles, c'est même l'inverse : davantage de plaintes font monter les chiffres."),
   ("Les médias cachent la réalité.", "Les chiffres cités viennent du ministère de l'Intérieur lui-même, publiés chaque année."),
  ]),
 'impots-assistanat': dict(
  mots_cles=['impôts', 'assistanat', 'dépenses publiques', 'rsa', 'minima sociaux', 'retraites', 'santé', 'école', 'dette'],
  fiabilite='etabli', stabilite='evolutive',
  contexte="L'idée que l'argent public financerait surtout « l'assistanat » est très répandue. La comptabilité nationale permet de voir précisément où va la dépense publique.",
  explication="Les dépenses publiques regroupent celles de l'État, des collectivités et de la Sécurité sociale. Elles sont financées par les impôts, les cotisations sociales et l'emprunt.",
  moyen="En 2024, l'État, les collectivités et la Sécurité sociale ont dépensé 1 672 milliards d'euros. La première dépense, ce sont les retraites, dans la protection sociale ; puis la santé, l'école, la défense, la sécurité, et même les intérêts de la dette, qui coûtent 60 milliards. L'ensemble des minima sociaux, RSA compris, représente environ 2 % des dépenses publiques, et le RSA seul 12 milliards. On peut discuter du RSA, mais il ne pèse qu'une petite partie de nos impôts.",
  empathie="Je comprends qu'on ait envie de savoir où va son argent ; c'est normal quand on paie beaucoup. Mais quand on regarde, la plus grande part va aux retraites, à la santé et à l'école. Le RSA, c'est moins que les intérêts de la dette.",
  contre=[
   ("Les retraites, c'est aussi de l'assistanat.", "Les retraites sont financées par les cotisations versées pendant la vie active : c'est une assurance, pas une aide sous condition de ressources."),
   ("Il faut ajouter les aides au logement et les allocations familiales.", "On peut les ajouter, mais elles bénéficient aussi à des millions de salariés et de familles : ce n'est pas de « l'assistanat » au sens où l'entend l'affirmation."),
  ]),
 'rsa-profiteurs': dict(
  mots_cles=['rsa', 'non-recours', 'fraude', 'profiteurs', 'drees', 'allocataires', 'aides sociales'],
  fiabilite='estimation', stabilite='evolutive',
  contexte="Le soupçon de profiteurs du RSA est fréquent. Les études de la DREES sur le non-recours montrent un phénomène inverse et massif.",
  explication="Le non-recours désigne le fait de ne pas percevoir une prestation à laquelle on a droit. Il est estimé par simulation statistique, d'où une fourchette.",
  moyen="C'est plutôt l'inverse : d'après la DREES, environ un tiers des foyers qui ont droit au RSA ne le demandent pas, soit à peu près 561 000 foyers fin 2021. Si tous le demandaient, la dépense augmenterait d'environ 2,5 milliards d'euros par an. Les raisons sont connues : méconnaissance, démarches compliquées, peur d'être stigmatisé. La fraude existe, mais l'image d'une ruée sur le RSA ne correspond pas aux données.",
  empathie="Je comprends que les histoires de fraude choquent ; la fraude existe et doit être combattue. Mais beaucoup de gens qui auraient droit au RSA ne le demandent même pas, souvent par fierté ou parce que c'est trop compliqué.",
  contre=[
   ("La fraude au RSA coûte des milliards.", "La fraude existe et fait l'objet d'estimations par les organismes sociaux ; elle n'est pas chiffrée dans cette fiche. Le non-recours représente, lui, environ 2,5 Md€ non versés par an."),
   ("S'ils ne le demandent pas, c'est qu'ils n'en ont pas besoin.", "Pour environ trois quarts des foyers concernés, le non-recours ne dure qu'un trimestre ; il touche des personnes en situation précaire, souvent mal informées."),
  ]),
}

def migrer():
    n = 0
    for fid, a in AJOUTS.items():
        p = os.path.join(LIB, fid + '.json')
        d = json.load(open(p, encoding='utf-8'))
        out = {
            'id': d['id'], 'type': 'idee_recue', 'affirmation': d['affirmation'], 'volet': d['volet'], 'sous_theme': d['sous_theme'],
            'rubriques': d.get('rubriques', []), 'mots_cles': a['mots_cles'], 'verdict': d['verdict'],
            'fiabilite': a['fiabilite'], 'stabilite': a['stabilite'],
            'resume': d['resume'], 'contexte': a['contexte'], 'explication': a['explication'],
            'faits': [{**f, 'fiabilite': f.get('fiabilite', a['fiabilite'])} for f in d['faits']],
            'argumentaires': {
                'court': d.get('replique') or d['argumentaires']['court'],
                'moyen': a['moyen'],
                'detaille': d.get('detail') or d['argumentaires']['detaille'],
                'empathie': a['empathie'],
            },
            'contre_arguments': [{'objection': o, 'reponse': r} for o, r in a['contre']],
            'questions': d['questions'], 'limites': d['limites'], 'sources': d['sources'],
            'derniere_verification': d['derniere_verification'], 'a_actualiser_le': d['a_actualiser_le'],
            'raison_actualisation': d['raison_actualisation'],
        }
        with open(p, 'w', encoding='utf-8') as fh:
            json.dump(out, fh, ensure_ascii=False, indent=2)
            fh.write('\n')
        n += 1
    print(n, 'fiches migrées')

if __name__ == '__main__':
    migrer()
