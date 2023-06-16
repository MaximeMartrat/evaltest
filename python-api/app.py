from flask import Flask, render_template, request
from DAO.adminDAO import insertAdmin

app = Flask(__name__)

@app.route('/')
def index():
     return render_template('accueil.html')

@app.route('/admin')
def post():
    return render_template('form.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        insertAdmin()
        return render_template('accueil.html', message='Admin créé !')
    
if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)


    


