import unittest
from app import app

class TestBook(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_book_route(self):
        competition = "Spring Festival"  # Exemple de compétition
        club = "Simply Lift"  # Exemple de club
        response = self.app.get(f'/book/{competition}/{club}')
        self.assertEqual(response.status_code, 200)  # Vérifie que la route renvoie un code 200 (OK)

    # Vous pouvez ajouter d'autres tests pour vérifier le contenu de la réponse, par exemple :
    def test_book_content(self):
        competition = "Spring Festival"  # Exemple de compétition
        club = "Simply Lift"  # Exemple de club
        response = self.app.get(f'/book/{competition}/{club}')
        self.assertIn(b'Spring Festival', response.data)  # Vérifie la présence de la compétition dans le contenu de la réponse
        self.assertIn(b'Simply Lift', response.data)  # Vérifie la présence du club dans le contenu de la réponse

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_some_other_route_valid(self):
        # Cas où l'e-mail du club existe dans le système
        club_email = "john@simplylift.co"  # Remplacez par un e-mail existant dans votre système
        response = self.app.get(f'/some_other_route/{club_email}', follow_redirects=True)
        self.assertEqual(response.status_code, 200)  # Assurez-vous que la redirection fonctionne correctement
        # Assurez-vous que le contenu du club est présent dans la page rendue
        # Ajoutez d'autres assertions si nécessaire

    def test_some_other_route_invalid_email(self):
        # Cas où l'e-mail du club n'existe pas dans le système
        club_email = "nonexistent@example.com"  # Remplacez par un e-mail non existant dans votre système
        response = self.app.get(f'/some_other_route/{club_email}', follow_redirects=True)
        self.assertEqual(response.status_code, 200)  # Assurez-vous que la redirection fonctionne correctement
        # Assurez-vous que la redirection vers l'index est effectuée
if __name__ == '__main__':
    unittest.main()

if __name__ == '__main__':
    unittest.main()
