#image de base Python
FROM python:3.11.4

WORKDIR /app

# Copier les dépendances Python et les installer
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
