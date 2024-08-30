# Ce script génère un fichier CSV de formulaires fictifs, on se base sur les proportions réelles des catégories professionnelles et sur des couples de demandes et raisons fictifs générés par Chat GPT.
import csv
import random

# Catégories socio-professionnelles et leurs proportions
categories = [
    ("Exploitants agricoles", 1),
    ("Artisans", 2),
    ("Commerçants et assimilés", 5),
    ("Chefs d'entreprise de 10 salariés ou plus", 1),
    ("Professions libérales et assimilées", 2),
    ("Cadres de la fonction publique", 10),
    ("Professeurs et professions scientifiques", 2),
    ("Professions de l'information, des arts et des spectacles", 1),
    ("Cadres administratifs et commerciaux d'entreprise", 2),
    ("Ingénieurs et cadres techniques d'entreprise", 2),
    ("Professions intermédiaires de l'enseignement, de la santé, de la fonction publique et assimilés", 2),
    ("Professions intermédiaires administratives et commerciales des entreprises", 2),
    ("Techniciens", 2),
    ("Contremaîtres, agents de maîtrise", 2),
    ("Employés civils et agents de service de la fonction publique", 5),
    ("Policiers et militaires", 2),
    ("Employés administratifs d'entreprise", 15),
    ("Employés de commerce", 5),
    ("Personnels des services directs aux particuliers", 2),
    ("Ouvriers qualifiés", 10),
    ("Ouvriers non qualifiés", 5),
    ("Conducteurs de véhicules et du personnel de transport", 2),
    ("Retraités", 20),
    ("Chômeurs", 5),
    ("Etudiants", 5),
    ("Autres personnes sans activité professionnelle", 2)
]

# Exemples de demandes et raisons avec sentiments implicites
demandes_raisons = [
    ("Réduction des taxes agricoles", "Les coûts de production sont trop élevés et les marges trop faibles pour survivre."),
    ("Soutien à l'artisanat local", "Le commerce en ligne nous écrase et on perd notre clientèle fidèle."),
    ("Amélioration des infrastructures urbaines", "Les rues sont en mauvais état, cela dissuade les clients de venir."),
    ("Simplification des démarches administratives", "Les formalités sont trop complexes et nous font perdre un temps précieux."),
    ("Révision des honoraires des professions libérales", "Les tarifs actuels ne nous permettent plus de vivre correctement."),
    ("Augmentation des salaires des fonctionnaires", "Les salaires sont gelés depuis trop longtemps, c'est décourageant."),
    ("Augmentation des budgets pour la recherche", "Les financements sont insuffisants, nous ne pouvons pas avancer."),
    ("Soutien aux industries culturelles", "La pandémie a durement frappé ce secteur, nous sommes au bord du gouffre."),
    ("Réduction de la charge fiscale sur les entreprises", "Les impôts sont trop élevés, nous avons du mal à rester à flot."),
    ("Investissements dans l'innovation technologique", "Nous devons rester compétitifs au niveau mondial, sinon nous serons dépassés."),
    ("Amélioration des conditions de travail", "Les conditions actuelles sont épuisantes, nous ne pouvons pas continuer ainsi."),
    ("Stabilisation des contrats de travail", "Le précariat est trop répandu, nous avons besoin de sécurité."),
    ("Formation continue pour les techniciens", "Nous avons besoin de mise à jour régulière des compétences pour ne pas être dépassés."),
    ("Reconnaissance des compétences des contremaîtres", "Notre rôle est crucial mais souvent sous-estimé."),
    ("Amélioration des services publics", "Les ressources sont insuffisantes, nous ne pouvons pas bien faire notre travail."),
    ("Augmentation des effectifs de police", "Les équipes sont en sous-effectif, c'est stressant et dangereux."),
    ("Télétravail et flexibilité des horaires", "Nous avons besoin de plus de flexibilité pour mieux concilier vie professionnelle et personnelle."),
    ("Soutien aux petits commerces", "La concurrence des grandes surfaces est écrasante, nous ne survivrons pas longtemps."),
    ("Augmentation des salaires minimum", "Le coût de la vie augmente, nous ne pouvons plus joindre les deux bouts."),
    ("Soutien aux industries locales", "La délocalisation menace nos emplois, nous avons peur de perdre notre travail."),
    ("Programmes de reconversion professionnelle", "Les opportunités sont limitées, nous avons besoin de nouvelles compétences."),
    ("Amélioration des infrastructures routières", "Les routes sont dangereuses, c'est un risque quotidien pour nous."),
    ("Augmentation des pensions de retraite", "Le coût de la vie augmente, notre pension ne suffit plus."),
    ("Création d'emplois et formations", "Nous avons besoin d'opportunités pour sortir du chômage."),
    ("Réduction des frais de scolarité", "L'éducation doit être accessible à tous, c'est crucial pour l'avenir."),
    ("Soutien aux personnes sans emploi", "La précarité est difficile à vivre, nous avons besoin de soutien."),
    ("Réduction du temps de travail", "Les journées de travail sont trop longues et nuisent à notre santé."),
    ("Augmentation des allocations familiales", "Les coûts liés à l'éducation des enfants sont de plus en plus élevés."),
    ("Réduction des frais médicaux", "Les dépenses de santé sont difficiles à supporter pour les familles modestes."),
    ("Amélioration de la sécurité au travail", "Les accidents sont fréquents et les mesures de sécurité sont insuffisantes."),
    ("Soutien à l'innovation entrepreneuriale", "Les startups ont besoin de plus de financement pour se développer."),
    ("Création de logements sociaux", "Il y a une pénurie de logements abordables pour les familles à faible revenu."),
    ("Renforcement de la lutte contre la discrimination au travail", "Les inégalités de traitement persistent malgré les lois existantes."),
    ("Accès à l'éducation pour les adultes", "Beaucoup d'adultes n'ont pas les compétences nécessaires pour les emplois actuels."),
    ("Développement des transports publics", "Les transports en commun sont insuffisants et mal desservis dans les zones rurales."),
    ("Soutien psychologique pour les travailleurs", "Le stress au travail est un problème majeur qui affecte la productivité et le bien-être."),
    ("Réduction des délais d'attente pour les soins médicaux", "Les patients doivent attendre trop longtemps pour obtenir des soins de qualité."),
    ("Soutien aux familles monoparentales", "Les parents seuls ont du mal à concilier vie professionnelle et vie familiale."),
    ("Promotion de l'égalité salariale entre hommes et femmes", "Il existe encore un écart salarial important entre les sexes."),
    ("Soutien aux travailleurs indépendants", "Les charges sociales et fiscales sont trop lourdes pour les auto-entrepreneurs."),
    ("Protection de l'environnement", "Les politiques actuelles ne font pas assez pour lutter contre le changement climatique."),
    ("Augmentation des aides sociales", "Les aides actuelles ne suffisent pas à couvrir les besoins essentiels des plus démunis, ce qui complique énormément leur quotidien."),
    ("Promotion de la diversité culturelle", "Il est important de valoriser la richesse culturelle de notre pays pour éviter que certaines communautés ne se sentent exclues."),
    ("Amélioration des conditions de travail dans les hôpitaux", "Les personnels soignants sont épuisés et les conditions de travail se détériorent."),
    ("Soutien à l'agriculture biologique", "L'agriculture durable est cruciale pour la santé et l'environnement, et le manque de soutien actuel met les agriculteurs dans une position délicate."),
    ("Augmentation des pensions d'invalidité", "Les personnes handicapées ne reçoivent pas assez de soutien financier, ce qui les laisse souvent dans des situations très difficiles."),
    ("Meilleure accessibilité des bâtiments publics", "Les personnes à mobilité réduite rencontrent encore trop d'obstacles, ce qui limite leur autonomie."),
    ("Réduction des inégalités d'accès à la technologie", "Tout le monde doit pouvoir bénéficier des avancées technologiques pour ne pas être laissé de côté."),
    ("Soutien aux jeunes entrepreneurs", "Les jeunes ont des idées innovantes mais manquent de moyens pour les réaliser, ce qui freine leur potentiel."),
    ("Amélioration des services de garde d'enfants", "Les places en crèche sont insuffisantes, ce qui complique la vie des parents qui travaillent."),
    ("Lutte contre le harcèlement scolaire", "Les enfants doivent pouvoir aller à l'école sans crainte de subir des mauvais traitements."),
    ("Accès à des soins de santé mentale", "Les services de santé mentale sont débordés et beaucoup ne peuvent pas obtenir l'aide dont ils ont besoin."),
    ("Soutien à la transition énergétique", "Nous devons réduire notre dépendance aux énergies fossiles pour un avenir plus durable."),
    ("Amélioration des conditions de travail pour les enseignants", "Les enseignants sont surchargés et manquent de ressources, ce qui affecte la qualité de l'enseignement."),
    ("Soutien aux familles nombreuses", "Les familles nombreuses ont des besoins spécifiques qui ne sont pas toujours pris en compte, ce qui complique leur gestion quotidienne."),
    ("Promotion du télétravail", "Le télétravail permet de mieux concilier vie professionnelle et personnelle, et devrait être plus largement accessible.")
]


# Générer les données
data = []
total_population = 200  # Total de la population pour notre exemple
i=1
for categorie, proportion in categories:
    count = int((proportion / 100) * total_population)
    for _ in range(count):
        demande, raison = random.choice(demandes_raisons)
        data.append([categorie, demande, raison, i])
        i+=1

# Sauvegarder en CSV
file_path = 'formulaires.csv'
with open(file_path, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(["CategorieSocioPro", "Demande", "Raison", "Index"])
    writer.writerows(data)

file_path
