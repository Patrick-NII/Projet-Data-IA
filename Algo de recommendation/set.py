# Librairies
import pandas as pd
import numpy as np

def load_clean_movie_data(movie_file):
    data = pd.read_csv(movie_file)
    data.dropna(inplace=True)
    data[['date_of_release', 'country_of_release']] = data['released'].str.extract(r'(\w+ \d+, \d+) \(([^)]+)\)')
    data.drop(['released', 'date_of_release'], axis=1, inplace=True)
    data.dropna(inplace=True)
    data = data[[
        'name',
        'genre',
        'year',
        'director',
        'writer',
        'star',
        'company',
        'country_of_release',
    ]]
    data['year'] = data['year'].astype('str')
    data['cat_features'] = data[data.columns].apply(lambda x: ' '.join(x), axis=1)

    return data

def get_recommendations(title, df, sim, count=10):
    # Obtenir l'indice de ligne du titre spécifié dans le DataFrame
    index = df.index[df['name'].str.lower() == title.lower()]
    
    # Retourner une liste vide s'il n'y a aucune entrée pour le titre spécifié
    if len(index) == 0:
        return []

    # Vérifier si l'indice est dans les limites de la matrice de similarité
    if index[0] >= len(sim):
        return []

    # Obtenir la ligne correspondante dans la matrice de similarité
    similarities = list(enumerate(sim[index[0]]))
    
    # Trier les scores de similarité dans cette ligne par ordre décroissant
    recommendations = sorted(similarities, key=lambda x: x[1], reverse=True)
    
    # Obtenir les n meilleures recommandations, en ignorant la première entrée de la liste car
    # elle correspond au titre lui-même (et a donc une similarité de 1.0)
    top_recs = recommendations[1:count + 1]

    # Générer une liste de titres à partir des indices dans top_recs
    titles = []

    for i in range(len(top_recs)):
        # Vérifier si l'indice est dans les limites du DataFrame
        if top_recs[i][0] < len(df):
            title = df.iloc[top_recs[i][0]]['name']
            titles.append(title)

    return titles