from flask import request
import mysql.connector
import bcrypt
from connectionbdd import connection_params
from queries_admin import insert_admin_formateur_false, insert_admin_formateur_true
from queries_formateur import insert_formateur, get_formateur_id

def insertAdmin():
    if request.method == 'POST':
        nom = request.form['firstName']
        prenom = request.form['lastName']
        pseudo = request.form['pseudo']
        email = request.form['emailAddress']
        telephone = request.form['telephone']
        password = request.form['password']
        section = request.form['section']

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        with mysql.connector.connect(**connection_params) as db:
            with db.cursor() as c:
                params = (nom, prenom, pseudo, email, telephone, hashed_password, section)
                if request.form['formateur'] == 'y': 
                    try:
                        c.execute(insert_formateur, params)
                        db.commit()
                        params = (nom, prenom)
                        c.execute(get_formateur_id, params)
                        result = c.fetchone()
                        id_formateur = result[0]             
                        params = (nom, prenom, pseudo, email, telephone, hashed_password, id_formateur, section)
                        c.execute(insert_admin_formateur_true, params)
                        db.commit()
                        return 'insertion réussie'
                    except mysql.connector.Error as error:
                        print("Failed to execute query: {}".format(error))
                else:
                    try:
                        c.execute(insert_admin_formateur_false, params)
                        db.commit()
                        return 'insertion réussie'
                    except mysql.connector.Error as error:
                        print("Failed to execute query: {}".format(error))