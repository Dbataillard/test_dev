from flask import Flask, render_template, request, redirect, url_for
from airtable import Airtable

app = Flask(__name__)

# Configuration Airtable
API_KEY = 'pat28jA9jpapynge9.d82b2274baf802746434350cb6b73d4fd2d29caaeeccd2ab68be5cb3f43405b6'
BASE_ID = 'appVGsF9U4djrIPsz'
CLIENT_TABLE = 'Leads'
CORDAGE_TABLE = 'Products'
RESERVATION_TABLE = 'Reservation'

airtable_clients = Airtable(BASE_ID,CLIENT_TABLE, API_KEY)
airtable_cordages = Airtable(BASE_ID,CORDAGE_TABLE, API_KEY)
airtable_reservation = Airtable(BASE_ID,RESERVATION_TABLE, API_KEY)

@app.route('/')
def index():
    cordages = airtable_cordages.get_all()
    return render_template('index.html', cordages=cordages)

@app.route('/add_client', methods=['POST'])
def add_client():

    email = request.form['email']
    
    # Vérifiez si l'utilisateur est déjà dans la base de données
    existing_client = airtable_clients.search('Email', email)
    
    if existing_client:
        # L'utilisateur est déjà dans la base de données
        # Vous pouvez rediriger l'utilisateur vers la page d'accueil avec un message d'erreur
        # ou gérer cela comme vous le souhaitez
        return "L'utilisateur existe déjà dans la base de données!", 400
    
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
    email = request.form['email']
    
    # Vérifiez si l'utilisateur est déjà dans la base de données
    existing_client = airtable_clients.search('Email', email)
    
    if not existing_client:
        # L'utilisateur n'est pas dans la base de données
        # Vous pouvez rediriger l'utilisateur vers la page d'inscription ou afficher un message d'erreur
        return "L'utilisateur n'existe pas dans la base de données. Veuillez vous inscrire d'abord.", 400
    
    size = request.form['taille_id']
    print(size)
    # Si l'utilisateur est dans la base de données, ajoutez sa réservation
    data = {
        'Email': email,
        'Marque': request.form['cordage_id'],
        'Modèle': request.form['modele_id'],  # Assurez-vous que le nom du champ correspond à celui de votre formulaire
        'Size': request.form['taille_id'],  # Assurez-vous que le nom du champ correspond à celui de votre formulaire
        'Date de récupération': request.form['date_recuperation']
    }
    
    # Insérez les données dans la table "reservation"
    airtable_reservation.insert(data)
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
