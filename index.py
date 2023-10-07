from flask import Flask, render_template, request, redirect, url_for
from airtable import Airtable

app = Flask(__name__)

# Configuration Airtable
API_KEY = 'YOUR_AIRTABLE_API_KEY'
BASE_ID = 'YOUR_AIRTABLE_BASE_ID'
CLIENT_TABLE = 'Leads'
CORDAGE_TABLE = 'Products'

airtable_clients = Airtable(BASE_ID, CLIENT_TABLE, api_key=API_KEY)
airtable_cordages = Airtable(BASE_ID, CORDAGE_TABLE, api_key=API_KEY)

@app.route('/')
def index():
    cordages = airtable_cordages.get_all()
    return render_template('index.html', cordages=cordages)

@app.route('/add_client', methods=['POST'])
def add_client():
    data = {
        'Nom': request.form['nom'],
        'Email': request.form['email']
    }
    airtable_clients.insert(data)
    return redirect(url_for('index'))

@app.route('/choose_cordage', methods=['POST'])
def choose_cordage():
    cordage_id = request.form['cordage_id']
    date_recuperation = request.form['date_recuperation']
    # Ajoutez le code pour enregistrer le choix du client dans Airtable
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
