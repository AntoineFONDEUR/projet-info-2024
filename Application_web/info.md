retouver le cours sur le site : https://network.slides.bmarchand.fr/cours3.html
un framework c'est une librairie qui va aider au dvlp d'un site web
Pour faire un site web il faut 2 aspects:
- interface graphique (cf cours de web)
- gestion des serveurs (ce cours)

dans l'url on peut ajouter des arguments (ex: name=Basile) on peut le récuperer dans la fonction associée à l'URL avec `name = request.args.get("name","No Name")` pour mettre plusieurs arguments on les sépare d'une &
 On peut demander d'envoyer directement un fichier HTML, pour cela:
 -on crée un dossier templates

On peut faire plusieurs requêtes: GET, POST, ...
Pour un même chemin on peut avoir plusieurs requêtes on écrit donc:
```py
@app.route("/chemin", methods=['GET','POST'])
def the_function():
    if request.method == "POST"
        return post_reponse
    elif request.method =="GET"
        return get_reponse

@app.get("/chemin")
def post_reponse():
    return #something
```

Si on veut des pages avec un contenu dynamique on  peut utiliser:
- CSR: l'affichage est géré coté navigateur
- SSR :l'affichage est géré coté serveur