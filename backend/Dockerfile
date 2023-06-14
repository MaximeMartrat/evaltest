# Utilisez une image de base Python
FROM python:3.11.4

# Clonez votre projet GitHub

RUN git clone https://github.com/MaximeMartrat/evaltest/tree/main/backend /app


# Accédez au répertoire du projet
WORKDIR /app

# Installez les dépendances du projet
RUN pip install -r requirements.txt

# Exécutez le script principal du backend
CMD ["python", "main.py"]

