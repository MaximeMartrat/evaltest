from flask import Flask,  render_template, request
import mysql.connector
import bcrypt
from queries_admin import insert_admin_formateur_false, insert_admin_formateur_true
from queries_formateur import insert_formateur, get_formateur_id

app = Flask(__name__)

@app.route('/')
def post():
    return render_template('form.html')

connection_params = {
    'host': "dbBB",
    'user': "user",
    'password': "password",
    'database': "db",
}

@app.route('/form', methods=['GET', 'POST'])
def form():
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


