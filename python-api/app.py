from flask import Flask,  render_template, request
import mysql.connector
import bcrypt

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
sql_request = "INSERT INTO administrateur (nomAdmin, prenomAdmin, pseudoAdmin, emailAdmin, telephoneAdmin, passwordAdmin, id_section_FK) values (%s, %s, %s, %s, %s, %s, %s)"

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

        params = (nom, prenom, pseudo, email, telephone, hashed_password, section)
        if request.form['formateur'] == 'y':
             sql_request2 = "INSERT INTO formateur (nomFormateur, prenomFormateur, pseudoFormateur, emailFormateur, passwordFormateur, id_section_FK) values (%s, %s, %s, %s, %s, %s)"
             params2 = (nom, prenom, pseudo, email, hashed_password, section)
             with mysql.connector.connect(**connection_params) as db:
                with db.cursor() as c:
                    c.execute(sql_request2, params2)
                    db.commit()        
        
        with mysql.connector.connect(**connection_params) as db:
            with db.cursor() as c:
                c.execute(sql_request, params)
                db.commit()
                return 'insertion réussie'
    else:
        return 'insertion ratée'
        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


