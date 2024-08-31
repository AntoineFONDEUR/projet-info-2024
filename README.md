# Projet 31 : Collecte des demandes de concitoyens pour alimenter les systèmes de démocratie représentative
Vous trouverez sur ce repos GIT, le Projet 31 réalisé par Antoine FONDEUR, Camille PRIGENT et Noémie SAUVAGE, sous la supervision de Serge NEUMAN.  

Vous trouverez :  
1. Dans Application_web : tout le code relatif au site internet, ce dernier peut-être lancé en local avec le programme app.py  
2. Dans generation_donnees : un programme pour générer des données de test  
3. A compléter pour Antoine  
4. A compléter pour Noémie 


## Notre démarche  

1. Collecte des données (Dossiers 1 et 2)

Les données des concitoyens sont collectées à l'aide d'un formulaire qui récupère leur catégorie socio-professionnelle, une doléance et la raison de la demande. Ces données sont ensuite envoyées dans une base de données.  

2. Traitement des données (Dossier 3)

Les données collectées sont ensuite traitées pour en extraire les thèmes prépondérants et les émotions. Les phrases vont être tokenisées afin de pouvoir les traiter avec un algorithme de type word2vec qui va nous donner pour chaque réponse un score par rapport à chacun des thèmes identifiés au préalable. En parallèle, une analyse de sentiments est réalisée sur la réponse et donne un score allant de -1 (pas content) à 1 (heureux).  

3. Visualisation des données (Dossiers 1 et 4)

Les données collectées sont dans un premier temps visualisées sous forme de nuages de mots avec un traitement très léger pour enlever les mots de liaison ou sans sens intrinsèque. Ensuite, les données traitées sont visualisées sous forme de graphiques pour montrer les thèmes prépondérants et les émotions selon différentes catégories recoupées.


