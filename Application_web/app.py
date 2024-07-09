from flask import Flask, render_template, request, redirect, url_for
import csv
from wordcloud import WordCloud
import pandas as pd
import numpy as np
import io
import base64
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
import requests
import logging
import matplotlib.pyplot as plt

# Configurez ces variables avec vos informations Notion
NOTION_API_URL = "https://api.notion.com/v1/pages"
NOTION_API_KEY = "secret_3lW3pscXNMTLyVt8ucguorEg8Zrtld5rOo04jLOD43o"
DATABASE_ID = "d6e83d295d2c40548fdc0fa0241a24c4"
NOTION_QUERY_URL = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"

# Télécharger les ressources nltk
nltk.download('punkt')
nltk.download('stopwords')

# Charger les mots vides
stop_words = set(stopwords.words('french'))

# Charger la liste de verbes à enlever
with open('liste_verbes.txt', 'r', encoding='utf-8') as file:
    verb_list = [line.strip() for line in file]

app = Flask(__name__)

# Configurer le logging
logging.basicConfig(level=logging.DEBUG)

def add_to_notion(data):
    headers = {
        "Authorization": f"Bearer {NOTION_API_KEY}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }

    payload = {
        "parent": {"database_id": DATABASE_ID},
        "properties": {
            "Rep1": {"rich_text": [{"text": {"content": data['en_tant_que']}}]},
            "Rep2": {"rich_text": [{"text": {"content": data['jaimerais']}}]},
            "Rep3": {"rich_text": [{"text": {"content": data['afin_de_parce_que']}}]},
            "Index": {"rich_text": [{"text": {"content": data['Index']}}]}
        }
    }

    response = requests.post(NOTION_API_URL, json=payload, headers=headers)
    
    logging.debug(f"Request payload: {payload}")
    logging.debug(f"Response status code: {response.status_code}")
    logging.debug(f"Response content: {response.content}")
    
    return response.status_code

def fetch_data_from_notion():
    headers = {
        "Authorization": f"Bearer {NOTION_API_KEY}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }

    response = requests.post(NOTION_QUERY_URL, headers=headers)
    data = response.json()

    logging.debug(f"Response status code: {response.status_code}")
    logging.debug(f"Response content: {response.content}")

    rows = []
    for result in data['results']:
        properties = result['properties']
        en_tant_que = properties['Rep1']['rich_text'][0]['text']['content']
        jaimerais = properties['Rep2']['rich_text'][0]['text']['content']
        afin_de_parce_que = properties['Rep3']['rich_text'][0]['text']['content']
        Index = properties['Index']['rich_text'][0]['text']['content']
        rows.append([en_tant_que, jaimerais, afin_de_parce_que, Index])
    
    return rows

DATABASE_ID_analyse = "6fb0749269924363afa68bd3fab90fa2"
NOTION_QUERY_URL_analyse = f"https://api.notion.com/v1/databases/{DATABASE_ID_analyse}/query"

def fetch_data_from_notion_analyse():
    headers = {
        "Authorization": f"Bearer {NOTION_API_KEY}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }

    response = requests.post(NOTION_QUERY_URL_analyse, headers=headers)
    data = response.json()

    logging.debug(f"Response status code: {response.status_code}")
    logging.debug(f"Response content: {response.content}")

    rows = []
    for result in data['results']:
        properties = result['properties']
        environnement = properties['environnement']['rich_text'][0]['text']['content']
        politique = properties['politique']['rich_text'][0]['text']['content']
        agriculture = properties['agriculture']['rich_text'][0]['text']['content']
        economie = properties['économie']['rich_text'][0]['text']['content']
        education = properties['éducation']['rich_text'][0]['text']['content']
        transport = properties['transport']['rich_text'][0]['text']['content']
        religion = properties['religion']['rich_text'][0]['text']['content']
        sante = properties['santé']['rich_text'][0]['text']['content']
        travail = properties['travail']['rich_text'][0]['text']['content']
        sport = properties['sport']['rich_text'][0]['text']['content']
        justice = properties['justice']['rich_text'][0]['text']['content']
        loisir = properties['loisir']['rich_text'][0]['text']['content']
        social = properties['social']['rich_text'][0]['text']['content']
        technologie = properties['technologie']['rich_text'][0]['text']['content']
        art = properties['art']['rich_text'][0]['text']['content']
        emotion = properties['emotion']['rich_text'][0]['text']['content']
        num = properties['num']['rich_text'][0]['text']['content'] #Indexs

        rows.append([num,environnement, politique, agriculture, economie,education,transport,religion,sante,travail,sport,justice,loisir,social,technologie, art, emotion])
    
    return rows

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/resultats')
def graphs():
    import seaborn as sns
    # Récupérer les Réponses triatées depuis Notion
    reptraitees = fetch_data_from_notion_analyse()

    # Récupérer les Réponses triatées depuis Notion
    repbrutes = fetch_data_from_notion()

    # Convertir les données en DataFrame
    datat = pd.DataFrame(reptraitees, columns=['num','environnement', 'politique', 'agriculture', 'economie','education','transport','religion','sante','travail','sport','justice','loisir','social','technologie', 'art','emotion'])
    datatb = pd.DataFrame(repbrutes, columns=['en_tant_que', 'jaimerais', 'afin_de_parce_que', 'Index'])
    
    


    def find_major_themes(row):
        row = row.drop(labels=['num'])  # Ignorer la colonne 'num'
        row = row.drop(labels=['emotion'])  # Ignorer la colonne 'emotion'
        sorted_themes = row.sort_values(ascending=False).index.tolist()
        return sorted_themes[0], sorted_themes[1]

    datat[['theme_major1', 'theme_major2']] = datat.apply(find_major_themes, axis=1, result_type='expand')


    # Fusion en conservant tous les éléments du premier tableau
    row = pd.merge(datat, datatb, left_on='num', right_on='Index', how='left')
    row.drop(columns=['Index'], inplace=True)

    row.to_csv('merged_data.csv', index=False)
   


    # Crée des graphiques des thèmes les plus fréquents pour le premier et le deuxième thème majoritaire
    fig, axes = plt.subplots(nrows=4, ncols=1, figsize=(21, 28))

    # Graphique pour le premier thème majoritaire
    by_theme_major1 = datat.groupby(by='theme_major1').size()
    by_theme_major1.plot(kind='bar', ax=axes[0], color='blue')
    axes[0].set_title('Nombre de personnes par premier thème majoritaire')
    axes[0].set_xlabel('Thème')
    axes[0].set_ylabel('Nombre de personnes')

    # Graphique pour le deuxième thème majoritaire
    by_theme_major2 = datat.groupby(by='theme_major2').size()
    by_theme_major2.plot(kind='bar', ax=axes[1], color='green')
    axes[1].set_title('Nombre de personnes par deuxième thème majoritaire')
    axes[1].set_xlabel('Thème')
    axes[1].set_ylabel('Nombre de personnes')

    # Préparation des données pour le graphique à bulles
    theme_counts = row.groupby(['en_tant_que', 'theme_major1']).size().reset_index(name='count')

    # Définir une palette de couleurs pour les thèmes
    palette = sns.color_palette('tab10', n_colors=len(datat['theme_major1'].unique()))

    # Graphique à bulles pour la distribution des thèmes majoritaires par classe sociale
    bubble_plot = sns.scatterplot(data=theme_counts, x='en_tant_que', y='theme_major1', size='count', hue='theme_major1', legend='full', palette=palette, sizes=(100, 2000), ax=axes[2])
    axes[2].set_title('Distribution des Thèmes Majoritaires par Classe Sociale')
    axes[2].set_xlabel('Classe Sociale')
    axes[2].set_ylabel('Thème Majoritaire')
    axes[2].tick_params(axis='x', rotation=45)

    # Ajouter une légende pour la couleur des points à l'intérieur du graphique
    #handles, labels = bubble_plot.get_legend_handles_labels()
    #axes[2].legend(handles=handles, labels=labels, title='Thème Majoritaire', loc='center left', bbox_to_anchor=(1, 0.5), scatterpoints=1)

    handles, labels = bubble_plot.get_legend_handles_labels()
    axes[2].legend(handles=handles, labels=labels, title='Nombre de personnes', loc='center left', bbox_to_anchor=(1, 0.5), scatterpoints=1, fontsize='large')

    emotions = row['emotion']
    sorted_emotions = np.sort(emotions)
    axes[3].hist(sorted_emotions, bins=10, edgecolor='black')  # Tracer l'histogramme avec 50 bins
    axes[3].set_title('Histogramme des émotions')
    axes[3].set_xlabel('Valeur des émotions')
    axes[3].set_ylabel('Fréquence')
    axes[3].grid(True)

    plt.tight_layout()

    # Sauvegarder les graphiques en mémoire
    img = io.BytesIO()
    plt.savefig(img, format='PNG')
    img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode()

    # Rendre le template HTML avec les graphiques
    return render_template('resultats.html', graph_url=graph_url)

@app.route('/repondre')
def index():
    return render_template('form.html', options_en_tant_que=[
        "Exploitants agricoles",
        "Artisans",
        "Commerçants et assimilés",
        "Chefs d'entreprise de 10 salariés ou plus",
        "Professions libérales et assimilées",
        "Cadres de la fonction publique",
        "Professeurs et professions scientifiques",
        "Professions de l'information, des arts et des spectacles",
        "Cadres administratifs et commerciaux d'entreprise",
        "Ingénieurs et cadres techniques d'entreprise",
        "Professions intermédiaires de l'enseignement, de la santé, de la fonction publique et assimilés",
        "Professions intermédiaires administratives et commerciales des entreprises",
        "Techniciens",
        "Contremaîtres, agents de maîtrise",
        "Employés civils et agents de service de la fonction publique",
        "Policiers et militaires",
        "Employés administratifs d'entreprise",
        "Employés de commerce",
        "Personnels des services directs aux particuliers",
        "Ouvriers qualifiés",
        "Ouvriers non qualifiés",
        "Conducteurs de véhicules et du personnel de transport",
        "Retraités",
        "Chômeurs",
        "Etudiants",
        "Autres personnes sans activité professionnelle"
])

@app.route('/save', methods=['POST'])
def save():
    en_tant_que = request.form['en_tant_que']
    jaimerais = request.form['jaimerais']
    afin_de_parce_que = request.form['afin_de_parce_que']

    # Récupérer les données depuis Notion
    rows = fetch_data_from_notion()


    # Convertir les données en DataFrame avec toutes les colonnes nécessaires
    df = pd.DataFrame(rows, columns=['Rep1', 'Rep2', 'Rep3', 'Index'])
    if df['Index'].empty:
        NewIndex = 1
    else:
        # Trouver le numéro le plus grand dans la colonne 'Index'
        max_index = max(df['Index'].astype('int32'))
        print(df['Index'].unique(),max_index)
        # Convertir max_index en entier si ce n'est pas déjà le cas
        max_index = int(max_index) if pd.notnull(max_index) else 0
        # Générer un nouveau numéro qui sera +1 grand
        NewIndex = max_index + 1
    
    Index = str(NewIndex)  # Convertir en chaîne de caractères

    # Sauvegarder dans un fichier CSV
    with open('data.csv', 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([en_tant_que, jaimerais, afin_de_parce_que])

    # Envoyer les données à Notion
    notion_data = {
        'en_tant_que': en_tant_que,
        'jaimerais': jaimerais,
        'afin_de_parce_que': afin_de_parce_que,
        'Index': Index  # Assurez-vous que Index est une chaîne de caractères
    }
    status = add_to_notion(notion_data)

    if status == 200:
        return redirect(url_for('generate_wordcloud'))
    else:
        return 'Réponse enregistrée mais échec de l\'envoi à Notion.'
    
@app.route('/generate_wordcloud')
def generate_wordcloud():
    # Récupérer les données depuis Notion
    rows = fetch_data_from_notion()

    # Convertir les données en DataFrame
    df = pd.DataFrame(rows, columns=['en_tant_que', 'jaimerais', 'afin_de_parce_que', 'Index'])
    df = df.drop(columns=['Index'])

    # Fonction pour filtrer les mots vides et les verbes
    def filter_words(sentence):
        words = word_tokenize(sentence.lower())
        filtered_words = [word.strip(',.;:!?') for word in words if word.strip(',.;:!?') not in stop_words and word.strip(',.;:!?') not in verb_list]
        return filtered_words

    # Créer un nuage de mots pour chaque colonne
    wordclouds = []
    for column in df.columns:
        words_count = df[column].apply(lambda x: filter_words(str(x))).explode().value_counts()
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(words_count)
        wordclouds.append(wordcloud)

    # Convertir chaque nuage de mots en image
    images = []
    for wordcloud in wordclouds:
        img = io.BytesIO()
        wordcloud.to_image().save(img, format='PNG')
        img.seek(0)
        images.append(base64.b64encode(img.getvalue()).decode())

    # Rendre le template HTML avec les images des nuages de mots
    return render_template('wordcloud.html', images=images)

if __name__ == '__main__':
    app.run(debug=True)
