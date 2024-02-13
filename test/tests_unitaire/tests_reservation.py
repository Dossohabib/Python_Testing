import unittest
from flask import Flask, request
from app import app  # Assurez-vous d'importer correctement votre application Flask et ses dépendances

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_purchase_places_valid(self):
        # Cas où le nombre de places est valide
        data = {
            'competition': "Spring Festival",
            'club': "Simply Lift",
            'places': '5'
        }
        response = self.app.post('/purchasePlaces', data=data)
        self.assertEqual(response.status_code, 302)  # Assurez-vous que la redirection fonctionne correctement

    def test_purchase_places_invalid(self):
        # Cas où le nombre de places est valide
        data = {
            'competition': "Spring Festival",
            'club': "Simply Lift",
            'places': '0'
        }
        response = self.app.post('/purchasePlaces', data=data)
        self.assertEqual(response.status_code, 302)  # Assurez-vous que la redirection fonctionne correctement

    def test_purchase_places_sup(self):
        # Cas où le nombre de places est valide
        data = {
            'competition': "Spring Festival",
            'club': "Simply Lift",
            'places': '50'
        }
        response = self.app.post('/purchasePlaces', data=data)
        self.assertEqual(response.status_code, 302)  # Assurez-vous que la redirection fonctionne correctement

    def test_purchase_places_sup_club(self):
        # Cas où le nombre de places est valide
        data = {
            'competition': "Spring Festival",
            'club': "Iron Temple",
            'places': '6'
        }
        response = self.app.post('/purchasePlaces', data=data)
        self.assertEqual(response.status_code, 302)  # Assurez-vous que la redirection fonctionne correctement
        # Ajoutez d'autres assertions si nécessaire

if __name__ == '__main__':
    unittest.main()
