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


if __name__ == '__main__':
    unittest.main()
