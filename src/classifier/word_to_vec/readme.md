Voici une première version du programme pour détecter les thèmes abordés par un texte.

Pour faire tourner les cellules, il vous faut:

- Télécharger le fichier .txt présent sur <a href="https://wikipedia2vec.github.io/wikipedia2vec/pretrained/">cette page</a>. <br>
  Il s'agit du modèle pré-entrainé qui implémente word2vec ie il convertit chaque mot qu'on lui donne en un vecteur de taille p.<br>
  La taille p du vecteur peut être choisie sur cette page de téléchargement (il y a, en français, le choix entre 100 et 300).<br>
  Pour le télécharger, cliquer sur le ".txt" n'a pas suffit pour moi, il glisser le lien dans un nouvel onglet. <br>
  Le chargement (sur mon ordinateur) de la version avec p=100 prend environ 5mins et celle avec p=300 prend bien 20 mins.<br>
  Il faut compter quelques Gb en RAM.

- Télécharger le spacy et gensim avec pip install

- Télécharger le module de gestion des tokens en français : python -m spacy download fr_core_news_sm²
