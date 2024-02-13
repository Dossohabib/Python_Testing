import json
from flask import Flask,render_template,request,redirect,flash,url_for
from datetime import datetime
from purchase import*

def loadClubs():
    with open('clubs.json') as c:
         listOfClubs = json.load(c)['clubs']
         return listOfClubs


def loadCompetitions():
    with open('competitions.json') as comps:
         listOfCompetitions = json.load(comps)['competitions']
         return listOfCompetitions


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()
today = datetime.now()

@app.route('/')
def index():
    clubs = loadClubs()  # Charger les données des clubs à chaque fois que la route est appelée
    return render_template('index.html', clubs=clubs, competitions=competitions)

@app.route('/showSummary', methods=['POST'])
def showSummary():
    # Vérifier si l'utilisateur a fourni un e-mail
    if 'email' not in request.form or not request.form['email']:
        flash("Veuillez entrer votre e-mail s'il vous plaît.", 'error')
        return redirect(url_for('index'))  # Redirigez vers la page où l'erreur doit être affichée

    # Récupérer les compétitions à venir
    upcoming_competitions = [c for c in competitions if datetime.strptime(c['date'], "%Y-%m-%d %H:%M:%S") >= today]

    # Rechercher le club correspondant à l'e-mail fourni
    matching_clubs = [club for club in clubs if club['email'] == request.form['email']]
    if not matching_clubs:
        flash("L'e-mail fourni n'existe pas dans notre système.", 'error')
        return redirect(url_for('index'))  # Redirigez vers la page où l'erreur doit être affichée

    # Sélectionner le premier club correspondant
    club = matching_clubs[0]

    return render_template('welcome.html', club=club, competitions=upcoming_competitions)


@app.route('/book/<competition>/<club>')
def book(competition,club):
    foundClub = [c for c in clubs if c['name'] == club][0]
    foundCompetition = [c for c in competitions if c['name'] == competition][0]
    if foundClub and foundCompetition:
        return render_template('booking.html',club=foundClub,competition=foundCompetition)
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club, competitions=competitions)

@app.route('/purchasePlaces', methods=['POST'])
def purchasePlaces():
    competition_name = request.form['competition']
    club_name = request.form['club']
    placesRequired = int(request.form['places'])

    # Rechercher la compétition et le club correspondants dans la liste des compétitions et des clubs
    competition = next((c for c in competitions if c['name'] == competition_name), None)
    club = next((c for c in clubs if c['name'] == club_name), None)

    # Vérifier si la compétition et le club existent
    if not competition or not club:
        flash("La compétition ou le club n'existe pas.", 'error')
        return redirect(url_for('index'))

    if placesRequired <= 0:
        flash("Le nombre de places fourni n'est pas valide.", 'error')
        return redirect(url_for('book', club=club_name, competition=competition_name))

    if placesRequired <= int(club['points']) and placesRequired <= 12:
        # Tente d'ajouter les tickets
        if ajouter_ticket(club['name'], competition['name'], placesRequired):
            # Si l'ajout est réussi, mettez à jour les autres informations et redirigez
            competition['numberOfPlaces'] = int(competition['numberOfPlaces']) - placesRequired
            club['points'] = int(club['points']) - placesRequired  # Mettre à jour les points du club
            flash('Réservation réussie !', "success")
            
            # Mettre à jour les points du club dans le HTML
            return redirect(url_for('book', club=club['name'], competition=competition['name']))
        else:
            flash("La limite de tickets pour cette compétition a été dépassée.", 'error')
    else:
        flash("Vous ne pouvez pas acheter plus de 12 places.", 'error')

    return redirect(url_for('book', club=club_name, competition=competition_name))




@app.route('/logout')
def logout():
    return redirect(url_for('index'))