from flask import Flask, render_template, request, session
from DAO.loginDAO import verifyLog
import DAO.userDAO
import DAO.generalDAO
import valide_token

app = Flask(__name__)
app.secret_key = 'fondes2023'


@app.route('/')
def index():
     return render_template('accueil.html')

@app.route('/logout')
def logout():
    session.pop('token', None)
    message = 'Vous êtes déconnecté.'
    return render_template('accueil.html', message=message) 

@app.route('/create')
def post():
    if valide_token.has_valid_token():
        # L'utilisateur est authentifié, permettre l'accès à la page
        return render_template('creation.html')
    else:
        # L'utilisateur n'est pas authentifié, rediriger vers la page de connexion
        return 'Veuillez vous connecter pour accéder à cette page'
    

@app.route('/creaAdmin', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        DAO.userDAO.insertAdmin()
        return render_template('accueil.html', message='Admin créé !')

@app.route('/creaFormateur', methods=['POST'])
def form2():
    if request.method == 'POST':
        DAO.userDAO.insertFormateur()
        return render_template('accueil.html', message='Formateur créé !')


@app.route('/creaApprenant', methods=['POST'])
def form3():
    if request.method == 'POST':
        DAO.userDAO.insertApprenant()
        return render_template('accueil.html', message='Apprenant créé !')

@app.route('/creaSalarie', methods=['POST'])
def form4():
    if request.method == 'POST':
        DAO.userDAO.insertSalarie()
        return render_template('accueil.html', message='Salarie créé !')

@app.route('/login')
def log():
     return render_template('login.html')

@app.route('/verifyLogin', methods=['GET'])
def login():
    if request.method == 'GET':
        message = verifyLog()
        verifyLog()
        return render_template('accueil.html', message=message)

@app.route('/updatePass')
def updatePass():
     return render_template('update_pass.html')


@app.route('/updatePassword', methods=['POST'])
def updatePassword():
    if request.method == 'POST':
         message = DAO.generalDAO.updateThisPassword(request.method)
         DAO.generalDAO.updateThisPassword(request.method)
         return render_template('accueil.html', message=message)

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)
