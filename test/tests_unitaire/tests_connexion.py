import unittest
from flask import Flask, url_for
from app import app

class TestValidEmail(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_valid_email_returns_ok(self):
        response = self.app.post('/showSummary', data={'email': 'john@simplylift.co'})
        self.assertEqual(response.status_code, 200)  # Succès
        self.assertIn(b'Bienvenue', response.data)

class TestInvalidEmail(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_invalid_email_returns_404(self):
        response = self.app.post('/showSummary', data={'email': 'invalid@example.com'})
        self.assertEqual(response.status_code, 302)  # Erreur 404
        
class TestNoEmail(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_no_email_returns_redirect(self):
        response = self.app.post('/showSummary', data={})
        self.assertEqual(response.status_code, 302)  # Redirection

class TestLogoutFunction(unittest.TestCase):
    
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_logout_redirect(self):
        # Effectuer une requête GET vers la route /logout
        response = self.app.get('/logout', follow_redirects=True)
        
        # Vérifier si la redirection vers la page d'accueil a eu lieu
        self.assertEqual(response.status_code, 200)  # Code de statut 200 indique succès
        self.assertIn(b'index', response.data)  # Vérifie la présence du contenu de la page d'accueil




    

if __name__ == '__main__':
    unittest.main()