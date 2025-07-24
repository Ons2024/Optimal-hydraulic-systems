# Image officielle Python slim (léger)
FROM python:3.9-slim

# Créer et se placer dans le dossier /app dans le container
WORKDIR /app

# Copier le fichier requirements.txt dans le container
COPY requirements.txt .

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le contenu du dossier local dans /app
COPY . .

# Exposer le port 5000 (Flask par défaut)
EXPOSE 5000

# Lancer l'application Flask
CMD ["python", "app.py"]
