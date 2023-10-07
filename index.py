from flask import Flask, render_template, request, redirect, url_for
from airtable import Airtable

app = Flask(__name__)

# Configuration Airtable
API_KEY = 'pat28jA9jpapynge9.d82b2274baf802746434350cb6b73d4fd2d29caaeeccd2ab68be5cb3f43405b6'
BASE_ID = 'appVGsF9U4djrIPsz'
CLIENT_TABLE = 'Leads'
CORDAGE_TABLE = 'Products'

airtable_clients = Airtable(BASE_ID,CLIENT_TABLE, API_KEY)
airtable_cordages = Airtable(BASE_ID,CORDAGE_TABLE, API_KEY)

@app.route('/')
def index():
    cordages = airtable_cordages.get_all()
    return render_template('index.html', cordages=cordages)

@app.route('/add_client', methods=['POST'])
def add_client():
    data = {
        'Nom': request.form['nom'],
        'Prénom' : request.form['prenom'],
        'Email': request.form['email'],
        'Ville': request.form['ville'],
        'Code postal': request.form['codepostal'],
        'Genre': request.form['genre'],
        'Date de naissance': request.form['datedenaissance']
    }
    airtable_clients.insert(data)
    return redirect(url_for('index'))

@app.route('/choose_cordage', methods=['POST'])
def choose_cordage():
    cordage_id = request.form['Marque']
    date_recuperation = request.form['date_recuperation']
    # Ajoutez le code pour enregistrer le choix du client dans Airtable
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
