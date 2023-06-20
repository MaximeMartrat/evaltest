from flask import request
from connectionbdd import connection_params
import mysql.connector
import queries_admin
import queries_formateur
import queries_apprenant
import queries_salarie

def insertAdmin():
    if request.method == 'POST':
        prenom = request.form['firstName']
        nom = request.form['lastName']
        pseudo = request.form['pseudo']
        email = request.form['emailAddress']
        telephone = request.form['telephone']
        section = request.form['section']

        with mysql.connector.connect(**connection_params) as db:
            with db.cursor() as c:
                params = (nom, prenom, pseudo, email, telephone, section)
                if request.form['formateur'] == 'y': 
                    try:
                        c.execute(queries_formateur.insert_formateur, params)
                        db.commit()
                        params = (nom, prenom)
                        c.execute(queries_formateur.get_formateur_id, params)
                        result = c.fetchone()
                        id_formateur = result[0]             
                        params = (nom, prenom, pseudo, email, telephone, id_formateur, section)
                        c.execute(queries_admin.insert_admin_formateur_true, params)
                        db.commit()
                        return 'insertion réussie'
                    except mysql.connector.Error as error:
                        print("Failed to execute query: {}".format(error))
                else:
                    try:
                        c.execute(queries_admin.insert_admin_formateur_false, params)
                        db.commit()
                        return 'insertion réussie'
                    except mysql.connector.Error as error:
                        print("Failed to execute query: {}".format(error))

def insertFormateur():
    if request.method == 'POST':
        prenom = request.form['firstName']
        nom = request.form['lastName']
        pseudo = request.form['pseudo']
        email = request.form['emailAddress']
        telephone = request.form['telephone']
        section = request.form['section']

        with mysql.connector.connect(**connection_params) as db:
            with db.cursor() as c:
                params = (nom, prenom, pseudo, email, telephone, section)
                try:
                    c.execute(queries_formateur.insert_formateur, params)
                    db.commit()
                    return 'insertion réussie'
                except mysql.connector.Error as error:
                    print("Failed to execute query: {}".format(error))

def insertApprenant():
    if request.method == 'POST':
        prenom = request.form['firstName']
        nom = request.form['lastName']
        pseudo = request.form['pseudo']
        adresse = request.form['adresse']
        rib = request.form['rib']
        secu = request.form['secu']
        email = request.form['emailAddress']
        telephone = request.form['telephone']
        formation = request.form['formation']
        section = request.form['section']

        with mysql.connector.connect(**connection_params) as db:
            with db.cursor() as c:
                params = (nom, prenom, pseudo, adresse, rib, secu, email, telephone, formation, section)
                try:
                    c.execute(queries_apprenant.insert_apprenant, params)
                    db.commit()
                    return 'insertion réussie'
                except mysql.connector.Error as error:
                    print("Failed to execute query: {}".format(error))

def insertSalarie():
     if request.method == 'POST':
        prenom = request.form['firstName']
        nom = request.form['lastName']
        pseudo = request.form['pseudo']
        email = request.form['emailAddress']
        telephone = request.form['telephone']
        section = request.form['section']

        with mysql.connector.connect(**connection_params) as db:
            with db.cursor() as c:
                params = (nom, prenom, pseudo, email, telephone, section)
                try:
                    c.execute(queries_salarie.insert_salarie, params)
                    db.commit()
                    return 'insertion réussie'
                except mysql.connector.Error as error:
                    print("Failed to execute query: {}".format(error))