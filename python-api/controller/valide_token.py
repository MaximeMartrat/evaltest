from flask import session
import jwt

def has_valid_token():
    token = session.get('token')

    if token:
        secret_key = 'fondes2023'  # Remplacez par votre clé secrète

        try:
            payload = jwt.decode(token, secret_key, algorithms=['HS256'])
            # Vérifiez les informations supplémentaires dans le payload si nécessaire
            return True
        except jwt.ExpiredSignatureError:
            # Gérer les erreurs d'expiration du token
            return False
        except jwt.InvalidTokenError:
            # Gérer les autres erreurs de token
            return False

    return False
