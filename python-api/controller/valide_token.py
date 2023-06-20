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
            pass
        except jwt.InvalidTokenError:
            # Gérer les autres erreurs de token
            pass

    return False

def has_valid_token_administrateur():
    token = session.get('token')

    if token:
        secret_key = 'fondes2023'  # Remplacez par votre clé secrète

        try:
            payload = jwt.decode(token, secret_key, algorithms=['HS256'])
            if payload['user_type'] == 'administrateur':
                # Vérifiez les informations supplémentaires dans le payload si nécessaire
                return True
        except jwt.ExpiredSignatureError:
            # Gérer les erreurs d'expiration du token
            pass
        except jwt.InvalidTokenError:
            # Gérer les autres erreurs de token
            pass

    return False

def has_valid_token_formateur():
    token = session.get('token')

    if token:
        secret_key = 'fondes2023'  # Remplacez par votre clé secrète

        try:
            payload = jwt.decode(token, secret_key, algorithms=['HS256'])
            if payload['user_type'] == 'formateur':
                # Vérifiez les informations supplémentaires dans le payload si nécessaire
                return True
        except jwt.ExpiredSignatureError:
            # Gérer les erreurs d'expiration du token
            pass
        except jwt.InvalidTokenError:
            # Gérer les autres erreurs de token
            pass

    return False

def has_valid_token_apprenant():
    token = session.get('token')

    if token:
        secret_key = 'fondes2023'  # Remplacez par votre clé secrète

        try:
            payload = jwt.decode(token, secret_key, algorithms=['HS256'])
            if payload['user_type'] == 'apprenant':
                # Vérifiez les informations supplémentaires dans le payload si nécessaire
                return True
        except jwt.ExpiredSignatureError:
            # Gérer les erreurs d'expiration du token
            pass
        except jwt.InvalidTokenError:
            # Gérer les autres erreurs de token
            pass

    return False

def has_valid_token_salarie():
    token = session.get('token')

    if token:
        secret_key = 'fondes2023'  # Remplacez par votre clé secrète

        try:
            payload = jwt.decode(token, secret_key, algorithms=['HS256'])
            if payload['user_type'] == 'salarie':
                # Vérifiez les informations supplémentaires dans le payload si nécessaire
                return True
        except jwt.ExpiredSignatureError:
            # Gérer les erreurs d'expiration du token
            pass
        except jwt.InvalidTokenError:
            # Gérer les autres erreurs de token
            pass

    return False