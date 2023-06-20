from flask import Flask, render_template, request, session, redirect, flash
from controller.login import verifyLog
import controller.user
import controller.password_add
import controller.valide_token

app = Flask(__name__)
app.secret_key = 'fondes2023'

@app.route('/')
def log():
     return render_template('login.html')

@app.route('/verifyLogin', methods=['GET'])
def login():
    if request.method == 'GET':
        message = verifyLog()
        flash(message)
        verifyLog()
        return redirect('/accueil')

@app.route('/accueil')
def index():
    token = session.get('token')
    if controller.valide_token.has_valid_token_administrateur(): 
        return render_template('accueil_admin.html')
    elif controller.valide_token.has_valid_token_formateur():
        return render_template('accueil_formateur.html')
    elif controller.valide_token.has_valid_token_apprenant():
        return render_template('accueil_apprenant.html')
    elif controller.valide_token.has_valid_token_salarie():
        return render_template('accueil_salarie.html')
    else:
        return render_template('login.html', message='veuillez vous connecter')
    
@app.route('/logout')
def logout():
    session.pop('token', None)
    flash('Vous êtes déconnecté !')
    return redirect('/') 

@app.route('/create')
def post():
    if controller.valide_token.has_valid_token_administrateur():
        # L'utilisateur est authentifié, permettre l'accès à la page
        return render_template('creation.html')
    else:
        # L'utilisateur n'est pas authentifié, rediriger vers la page de connexion
        return 'Veuillez vous connecter pour accéder à cette page'
    

@app.route('/creaAdmin', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        controller.user.insertAdmin()
        return render_template('accueil_admin.html', alerte='Admin créé !')

@app.route('/creaFormateur', methods=['POST'])
def form2():
    if request.method == 'POST':
        controller.user.insertFormateur()
        return render_template('accueil_admin.html', alerte='Formateur créé !')


@app.route('/creaApprenant', methods=['POST'])
def form3():
    if request.method == 'POST':
        controller.user.insertApprenant()
        return render_template('accueil_admin.html', alerte='Apprenant créé !')

@app.route('/creaSalarie', methods=['POST'])
def form4():
    if request.method == 'POST':
        controller.user.insertSalarie()
        return render_template('accueil_admin.html', alerte='Salarie créé !')


@app.route('/updatePass')
def updatePass():
     return render_template('update_pass.html')


@app.route('/updatePassword', methods=['POST'])
def updatePassword():
    if request.method == 'POST':
         message = controller.password_add.updateThisPassword(request.method)
         controller.password_add.updateThisPassword(request.method)
         flash(message)
         return redirect('/')

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)
