import json
from flask import Flask,render_template,request,redirect,flash,url_for
from datetime import datetime


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
    return render_template('index.html',clubs=clubs,competitions=competitions)

@app.route('/showSummary',methods=['POST'])
def showSummary():
    # Vérifiez si l'utilisateur a fourni un e-mail
    if 'email' not in request.form or not request.form['email']:
        flash("Veuillez entrer votre e-mail s'il vous plaît.", 'error')
        return redirect(url_for('index'))  # Redirigez vers la page où l'erreur doit être affichée

    comp = [competition for competition in competitions if datetime.strptime(competition['date'], "%Y-%m-%d %H:%M:%S") >= today]
    matching_clubs = [club for club in clubs if club['email'] == request.form['email']]
    if not matching_clubs:
        flash("L'e-mail fourni n'existe pas dans notre système.", 'error')
        return redirect(url_for('index'))  # Redirigez vers la page où l'erreur doit être affichée
    club = matching_clubs[0]
    return render_template('welcome.html', club=club, competitions=comp)


@app.route('/book/<competition>/<club>')
def book(competition,club):
    foundClub = [c for c in clubs if c['name'] == club][0]
    foundCompetition = [c for c in competitions if c['name'] == competition][0]
    if foundClub and foundCompetition:
        return render_template('booking.html',club=foundClub,competition=foundCompetition)
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/purchasePlaces',methods=['POST'])
def purchasePlaces():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    placesRequired = int(request.form['places'])
    if placesRequired <= 0:
        flash("le nombre fourni n'est pas valide.", 'error')
        return redirect(url_for('book',club=club['name'],competition=competition['name']))  # Redirigez vers la page où l'erreur doit être affichée
    if placesRequired <= int(club['points']) and placesRequired <= 12:
        competition['numberOfPlaces'] = int(competition['numberOfPlaces'])-placesRequired
        club['points'] = int(club['points']) - placesRequired
        flash('reservation Reussit!')
        return render_template('welcome.html', club=club, competitions=competitions)  # Redirigez vers la page où l'erreur doit être affichée
    if placesRequired >= int(competition['numberOfPlaces']):
        flash("le nombre fourni est superieur au nombre de place.", 'error')
        return redirect(url_for('book',club=club['name'],competition=competition['name']))  # Redirigez vers la page où l'erreur doit être affichée
    if placesRequired > int(club['points']):
        flash("le nombre fourni est superieur au nombre de points du club.", 'error')
        return redirect(url_for('book',club=club['name'],competition=competition['name']))  # Redirigez vers la page où l'erreur doit être affichée
     # Gérer les cas d'erreurs restants
    if placesRequired > 12:
        flash("Vous ne pouvez pas acheter plus de 12 places.", 'error')
    elif placesRequired > int(club['points']):
        flash("Le club n'a pas assez de points pour acheter autant de places.", 'error')
    return redirect(url_for('book', club=club['name'], competition=competition['name']))
# TODO: Add route for points display


@app.route('/logout')
def logout():
    return redirect(url_for('index'))