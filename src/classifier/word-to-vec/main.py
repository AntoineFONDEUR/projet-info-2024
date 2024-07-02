# %%
import string
import spacy
from gensim.models import keyedvectors
import json
import numpy as np

# %%
path_model=r".\models\frwiki_20180420_100d.txt.bz2"
trained=keyedvectors.load_word2vec_format(path_model, binary=False)
nlp = spacy.load("fr_core_news_sm")

# %%
path_categories = r"..\categories.json"
with open(path_categories, 'r') as file:
    categories_json = json.load(file)

categories = categories_json['categories']

# %%
def my_doc_2_vec(mots,trained):
    #Vecteur moyen d'un ensemble de mots
    p=trained.vectors.shape[1]
    vec=np.zeros(p)
    nb=0
    for tk in mots:
        try:
            values=trained[tk]
            vec=vec+values
            nb+=1
        except:
            pass
    if nb>0: vec=vec/nb
    return vec

# %%
def get_vect(texte):
    #Lemnisation du texte et retourne le vecteur moyen des mots
    doc = nlp(texte)
    lemmes = [token.lemma_ for token in doc]
    mots_filtrés = [lemme for lemme in lemmes if lemme not in nlp.Defaults.stop_words and lemme not in list(string.punctuation)]
    return my_doc_2_vec(mots_filtrés,trained)

# %%
def dist(word_vector1, word_vector2):
    #Retourne la distance entre deux vecteurs
    return np.dot(word_vector1, word_vector2) / (np.linalg.norm(word_vector1) * np.linalg.norm(word_vector2))

# %%
def get_sorted_cats(texte):
    #Retourne les catégories triées par ordre de ressemblance
    vec = get_vect(texte)
    cat_arr = np.array([trained[cat] for cat in categories])
    distances = [dist(cat_arr[i],vec) for i in range(len(categories))]
    d=[(categories[i],distances[i]) for i in range(len(categories))]
    d.sort(key=lambda x:-x[1])
    return d

# %%
