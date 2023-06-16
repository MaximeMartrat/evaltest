from flask import Flask,  render_template, request
from DAO.adminDAO import insertAdmin

app = Flask(__name__)

@app.route('/')
def post():
    return render_template('form.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        insertAdmin()
        return 'insertion reussie'
if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)


    


