from flask import request, session
from DAO.connectionbdd import connection_params
import DAO.queries_general
import mysql.connector
import bcrypt
import jwt

def verifyLog():
    if request.method == 'GET':
        pseudo = request.args.get('pseudo')
        password = request.args.get('password')

        with mysql.connector.connect(**connection_params) as db:
            with db.cursor() as c:
                c.execute(DAO.queries_general.get_hashed_password, {'pseudo': pseudo})
                result = c.fetchone()

                if result is not None:
                    hashed_password = result[0]

                    if bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
                        c.execute(DAO.queries_general.get_user_firstname, {'pseudo': pseudo})
                        firstname_result = c.fetchone()

                        if firstname_result is not None:
                            firstname = firstname_result[0]

                             # Générer le token de connexion
                            c.execute(DAO.queries_general.select_table, {'pseudo': pseudo})
                            table_result = c.fetchone()  

                            if table_result:
                                table_name, pseudo = table_result
                                # Générer le token de connexion en utilisant le nom de la table
                                payload = {'pseudo': pseudo, 'user_type': table_name}
                                secret_key = 'fondes2023'  # Remplacez par votre clé secrète
                                token = jwt.encode(payload, secret_key, algorithm='HS256')
                                session['token'] = token

                            return f'Bienvenue, {firstname} !'
                        else:
                            return 'Prénom utilisateur non disponible.'
                    else:
                        return 'Mot de passe incorrect.'
                else:
                    return 'Utilisateur inconnu.'