import unittest
from app import loadClubs, loadCompetitions  # Assurez-vous d'importer correctement vos fonctions
import json

class TestLoadData(unittest.TestCase):

    def test_loadClubs(self):
        # Créez un fichier clubs.json factice pour le test
        clubs_data = {"clubs": [
            {"name": "Simply Lift", "email": "john@simplylift.co", "points": "13"},
            {"name": "Iron Temple", "email": "admin@irontemple.com", "points": "4"},
            {"name": "She Lifts", "email": "kate@shelifts.co.uk", "points": "12"}
        ]}
        with open('clubs.json', 'w') as f:
            json.dump(clubs_data, f)

        # Testez la fonction loadClubs
        clubs = loadClubs()
        self.assertEqual(len(clubs), 3)  # Vérifiez si trois clubs ont été chargés
        self.assertEqual(clubs[0]['name'], 'Simply Lift')  # Vérifiez le nom du premier club
        self.assertEqual(clubs[1]['email'], 'admin@irontemple.com')  # Vérifiez l'email du deuxième club

    def test_loadCompetitions(self):
        # Créez un fichier competitions.json factice pour le test
        competitions_data = {"competitions": [
            {"name": "Spring Festival", "date": "2020-03-27 10:00:00", "numberOfPlaces": "25"},
            {"name": "Fall Classic", "date": "2020-10-22 13:30:00", "numberOfPlaces": "13"}
        ]}
        with open('competitions.json', 'w') as f:
            json.dump(competitions_data, f)

        # Testez la fonction loadCompetitions
        competitions = loadCompetitions()
        self.assertEqual(len(competitions), 2)  # Vérifiez si deux compétitions ont été chargées
        self.assertEqual(competitions[0]['name'], 'Spring Festival')  # Vérifiez le nom de la première compétition
        self.assertEqual(competitions[1]['date'], '2020-10-22 13:30:00')  # Vérifiez la date de la deuxième compétition

if __name__ == '__main__':
    unittest.main()
