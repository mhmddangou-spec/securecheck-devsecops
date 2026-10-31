import unittest
from securecheck_core import calculer_score, evaluer_score


class TestSecureCheck(unittest.TestCase):

    def test_mot_de_passe_complet(self):
        self.assertEqual(calculer_score("Bonjour123!Ab"), 5)

    def test_mot_de_passe_vide(self):
        self.assertEqual(calculer_score(""), 0)

    def test_mot_de_passe_trop_court(self):
        self.assertEqual(calculer_score("Abc123!"), 4)

    def test_evaluation_faible(self):
        self.assertEqual(evaluer_score(2), "A RENFORCER")

    def test_evaluation_moyenne(self):
        self.assertEqual(evaluer_score(4), "MOYEN")

    def test_evaluation_complete(self):
        self.assertEqual(evaluer_score(5), "CRITERES SATISFAITS")


if __name__ == "__main__":
    unittest.main()
