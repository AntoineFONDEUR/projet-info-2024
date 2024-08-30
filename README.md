# projet-info-2024
## Nos motivations
Dans le cadre de la démocratie participative, qui vise à associer les citoyens au processus de décision politique, il est important de pouvoir entendre tous les citoyens et conserver leurs pensées, demandes et idées. Cette collecte doit se faire de manière simple pour les concitoyens, donc à travers quelque chose qu'ils ont l'habitude d'utiliser comme un site internet.

Il est donc nécessaire d'avoir un outil qui gère la collecte des demandes des citoyens pour alimenter le pipeline des outils numériques, qui puissent être utilisés pour la démocratie participative.

L'objectif avec notre projet est d'offrir un espace de recueil des doléances de nos concitoyens couplé à un outil de visualisation des données collectées avec analyse des thèmes prépondérants et des émotions.

Nous espérons construire un outil de communication entre les citoyens et les élus, qui permettra de mieux comprendre les attentes des citoyens et de mieux répondre à leurs besoins.  


## Notre démarche  

1. Collecte des données

Les données des concitoyens sont collectées à l'aide d'un formulaire qui récupère leur catégorie socio-professionnelle, une doléance et la raison de la demande. Ces données sont ensuite envoyées dans une base de données.
2. Traitement des données

Les données collectées sont ensuite traitées pour en extraire les thèmes prépondérants et les émotions. Les phrases vont être tokenisées afin de pouvoir les traiter avec un algorithme de type word2vec qui va nous donner pour chaque réponse un score par rapport à chacun des thèmes identifiés au préalable. En parallèle, une analyse de sentiments est réalisée sur la réponse et donne un score allant de -1 (pas content) à 1 (heureux).
3. Visualisation des données

Les données collectées sont dans un premier temps visualisées sous forme de nuages de mots avec un traitement très léger pour enlever les mots de liaison ou sans sens intrinsèque. Ensuite, les données traitées sont visualisées sous forme de graphiques pour montrer les thèmes prépondérants et les émotions selon différentes catégories recoupées.

## Protection des données

### Anonymat et Données Personnelles

**Données Personnelles :**

    Le RGPD s'applique aux données personnelles, c'est-à-dire toute information se rapportant à une personne physique identifiée ou identifiable.
    Si les données collectées ne permettent pas d'identifier une personne physique, directement ou indirectement, ces données ne sont pas considérées comme des données personnelles.

**Anonymisation vs Pseudonymisation :**

    Anonymisation : Les données anonymes sont des données qui ne peuvent en aucun cas être reliées à une personne identifiable, même avec des informations supplémentaires. Les données anonymes ne sont pas soumises au RGPD.
    Pseudonymisation : Les données pseudonymisées peuvent être reliées à une personne à l'aide d'informations supplémentaires. Ces données sont toujours considérées comme des données personnelles et sont soumises au RGPD.

Ici la seule donnée collectée est la catégorie socio-professionnelle et il n'y a aucun moyen de relier cette information à une personne identifiable donc le formulaire peut être considéré comme anonyme. Dans ce cas, le RGPD ne s'applique pas, car il ne traite pas de données personnelles.

Si notre formulaire est effectivement anonyme et ne collecte que des informations non identifiables, alors la plupart des obligations du RGPD ne s'appliquent pas. Cependant, il est important de vérifier que les données ne peuvent en aucun cas être utilisées pour identifier une personne, même indirectement. Si les données peuvent être combinées avec d'autres informations pour identifier quelqu'un, alors elles ne seraient pas considérées comme anonymes, et le RGPD s'appliquerait.

