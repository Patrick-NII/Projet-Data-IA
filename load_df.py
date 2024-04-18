import os

def load_df(paths):
  """La fonction fait une boucle sur les différents chemins donnés et avec la bibliothèque "os" elle vérifie si le chemin existe dans ton ordi"""
  for path in paths:
    if os.path.exists(path):
      try:
        dataframe = pd.read_csv(path, sep='\t')
        print(f"Dataframe récupéré à partir de: {path}")
        return dataframe
      except Exception as e:
        print(f"Erreur pour charger le chemin: {path}")
        print(e)
  print("Aucun des chemins ont été rétrouvés")
  return None




