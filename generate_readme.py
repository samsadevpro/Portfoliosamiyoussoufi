import os
from bs4 import BeautifulSoup

# Fonction pour extraire le titre du fichier HTML
def extract_html_title(file_path):
    """Extrait le titre du projet à partir du fichier HTML."""
    with open(file_path, 'r', encoding='utf-8') as file:
        # Utilisation de BeautifulSoup pour analyser le HTML
        soup = BeautifulSoup(file, 'html.parser')
        
        # Récupérer le titre dans la balise <title> (si elle existe)
        title = soup.title.string if soup.title else "Mon Portfolio"
    
    return title

# Fonction principale pour générer le README.md
def generate_readme(project_dir):
    """
    Génère un fichier README.md pour un portfolio en analysant les fichiers
    HTML, CSS et JS dans le répertoire du projet.
    """
    readme_content = "# Mon Portfolio Personnel\n\n"
    
    # Partie Description du projet
    html_file = os.path.join(project_dir, 'index.html')
    
    if os.path.exists(html_file):
        title = extract_html_title(html_file)
        # On ajoute le titre du projet dans la section description
        readme_content += f"## Description\n\nBienvenue sur mon portfolio ! C'est un site simple que j'ai créé pour présenter mes projets et compétences. Le titre de ce portfolio est : **{title}**.\n\n"
    else:
        readme_content += "## Description\n\nBienvenue sur mon portfolio ! C'est un site simple pour présenter mes projets et compétences.\n\n"
    
    # Partie Installation
    readme_content += "## Installation\n\nClonez le projet et ouvrez le fichier `index.html` dans un navigateur moderne pour voir le site.\n\n"
    
    # Partie Utilisation
    readme_content += "## Utilisation\n\n1. Clonez ce projet sur votre machine locale.\n2. Ouvrez `index.html` dans un navigateur pour voir le site.\n\n"
    
    # Partie Dépendances (CSS/JS)
    css_files = []
    js_files = []
    
    # Recherche de tous les fichiers CSS et JS dans le projet
    for root, dirs, files in os.walk(project_dir):
        for file in files:
            if file.endswith('.css'):
                css_files.append(file)
            elif file.endswith('.js'):
                js_files.append(file)
    
    if css_files:
        readme_content += "## Dépendances\n\nLe projet utilise les fichiers CSS suivants :\n"
        for css in css_files:
            readme_content += f"- `{css}`\n"
    if js_files:
        readme_content += "Le projet utilise les fichiers JavaScript suivants :\n"
        for js in js_files:
            readme_content += f"- `{js}`\n"
    
    # Partie Contribuer
    readme_content += "\n## Contribuer\n\nLes contributions ne sont pas nécessaires pour ce portfolio, mais n'hésitez pas à me contacter pour toute suggestion !\n\n"
    
    # Partie Licence
    readme_content += "## Licence\n\nCe projet est sous licence MIT.\n"

    # Sauvegarder le README.md
    with open('README.md', 'w', encoding='utf-8') as readme_file:
        readme_file.write(readme_content)
    print("README.md généré avec succès!")

# Exemple d'utilisation : remplacer le chemin par ton projet
generate_readme('/chemin/vers/votre/projet')
