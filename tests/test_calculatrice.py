import unittest
import sys
import os

# Permet d'importer depuis /src
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from calculatrice import division, puissance, moyenne


class TestCalculatrice(unittest.TestCase):

    # ------------------
    # Tests division
    # ------------------

    def test_division_simple(self):
        self.assertEqual(division(10, 2), 5.0)

    def test_division_decimale(self):
        self.assertEqual(division(5, 2), 2.5)

    def test_division_par_zero(self):
        with self.assertRaises(ZeroDivisionError):
            division(10, 0)

    # ------------------
    # Tests puissance
    # ------------------

    def test_puissance_classique(self):
        self.assertEqual(puissance(2, 3), 8.0)

    def test_puissance_exposant_zero(self):
        self.assertEqual(puissance(7, 0), 1.0)

    def test_puissance_exposant_negatif(self):
        with self.assertRaises(ValueError):
            puissance(2, -1)

    # ------------------
    # Tests moyenne
    # ------------------

    def test_moyenne_normale(self):
        self.assertEqual(moyenne([10, 20, 30]), 20.0)

    def test_moyenne_liste_vide(self):
        with self.assertRaises(ValueError):
            moyenne([])


if __name__ == "__main__":
    unittest.main()
