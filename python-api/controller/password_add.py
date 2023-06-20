from flask import request
from DAO.connectionbdd import connection_params
import mysql.connector
import bcrypt
import DAO.queries_general
def updateThisPassword(method):
    if method == 'POST':
        try:
            pseudo = request.form['pseudo']
            password = request.form['password']

            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            params = {'pseudo': pseudo, 'hashed_password': hashed_password }

            with mysql.connector.connect(**connection_params) as db:
                with db.cursor() as c:
                    c.execute(DAO.queries_general.select_table, {'pseudo': pseudo})
                    result = c.fetchone()

                    if result:
                        table_name, pseudo = result
                        if table_name == 'administrateur':
                            update_password = DAO.queries_general.update_password_admin
                        elif table_name == 'formateur':
                            update_password = DAO.queries_general.update_password_formateur
                        elif table_name == 'salarie':
                            update_password = DAO.queries_general.update_password_salarie
                        elif table_name == 'apprenant':
                            update_password = DAO.queries_general.update_password_apprenant
                        else:
                            return 'table inconnue'
                        c.execute(update_password, params)
                        db.commit()
                        return 'Mot de passe mis à jour avec succès'
                    else:
                        return 'Pseudo introuvable dans toutes les tables.'

        except mysql.connector.Error as error:
            print("Failed to execute query: {}".format(error))

