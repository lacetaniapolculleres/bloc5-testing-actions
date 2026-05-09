"""
T02-Bloc3-0487-ENTORNS - Bateria de proves Unittest
====================================================
Importa les solucions de les dues proves escrites i implementa
dues classes TestCase, una per a cada prova.
"""

import unittest
import prova_escrita_01 as p01
import prova_escrita_02 as p02


# ===========================================================================
# CLASSE DE TEST PER A LA PROVA ESCRITA 01 (Paper-01)
# Exercicis testejats: 2 (buscar_per_titol), 3 (afegir_a_biblioteca),
#                      4 (joc_mes_car)
# ===========================================================================

class TestProvaEscrita01(unittest.TestCase):
    """Bateria de proves per a les funcions de la Prova Escrita 01."""

    def setUp(self):
        self.videojocs = [
            {
                "titol": "The Legend of Zelda",
                "any_llancament": 2017,
                "genere": "Aventura",
                "plataforma": "Nintendo Switch",
                "puntuacio": 9.7,
                "desenvolupador": {"nom": "Nintendo", "pais": "Japó"},
                "dlcs": ["Master Trials", "Champions' Ballad"],
                "preu": 59.99
            },
            {
                "titol": "Cyberpunk 2077",
                "any_llancament": 2020,
                "genere": "RPG",
                "plataforma": "PC",
                "puntuacio": 7.8,
                "desenvolupador": {"nom": "CD Projekt Red", "pais": "Polònia"},
                "dlcs": ["Phantom Liberty"],
                "preu": 29.99
            },
            {
                "titol": "FIFA 24",
                "any_llancament": 2023,
                "genere": "Esports",
                "plataforma": "PlayStation",
                "puntuacio": 8.2,
                "desenvolupador": {"nom": "EA Sports", "pais": "Estats Units"},
                "dlcs": [],
                "preu": 69.99
            }
        ]
        self.biblioteca = []

    def test_buscar_titol_existent(self):
        resultat = p01.buscar_per_titol("FIFA 24", self.videojocs)
        self.assertIsNotNone(resultat)
        self.assertEqual(resultat["titol"], "FIFA 24")

    def test_buscar_titol_insensible_majuscules(self):
        resultat = p01.buscar_per_titol("cyberpunk 2077", self.videojocs)
        self.assertIsNotNone(resultat)
        self.assertEqual(resultat["titol"], "Cyberpunk 2077")

    def test_buscar_titol_no_existent(self):
        resultat = p01.buscar_per_titol("Mario Bros", self.videojocs)
        self.assertIsNone(resultat)

    def test_buscar_titol_llista_buida(self):
        resultat = p01.buscar_per_titol("FIFA 24", [])
        self.assertIsNone(resultat)

    def test_buscar_titol_retorna_diccionari_complet(self):
        resultat = p01.buscar_per_titol("The Legend of Zelda", self.videojocs)
        self.assertIn("preu", resultat)
        self.assertEqual(resultat["preu"], 59.99)

    def test_afegir_joc_correctament(self):
        resultat = p01.afegir_a_biblioteca("FIFA 24", self.videojocs, self.biblioteca)
        self.assertEqual(resultat, "✅ Joc afegit!")
        self.assertEqual(len(self.biblioteca), 1)

    def test_afegir_joc_no_trobat(self):
        resultat = p01.afegir_a_biblioteca("GTA VI", self.videojocs, self.biblioteca)
        self.assertEqual(resultat, "❌ Joc no trobat")
        self.assertEqual(len(self.biblioteca), 0)

    def test_afegir_joc_duplicat(self):
        p01.afegir_a_biblioteca("FIFA 24", self.videojocs, self.biblioteca)
        resultat = p01.afegir_a_biblioteca("FIFA 24", self.videojocs, self.biblioteca)
        self.assertEqual(resultat, "⚠️ Ja està a la biblioteca")
        self.assertEqual(len(self.biblioteca), 1)

    def test_afegir_diversos_jocs(self):
        p01.afegir_a_biblioteca("FIFA 24", self.videojocs, self.biblioteca)
        p01.afegir_a_biblioteca("Cyberpunk 2077", self.videojocs, self.biblioteca)
        self.assertEqual(len(self.biblioteca), 2)

    def test_joc_mes_car_correcte(self):
        resultat = p01.joc_mes_car(self.videojocs)
        self.assertEqual(resultat["titol"], "FIFA 24")
        self.assertEqual(resultat["preu"], 69.99)

    def test_joc_mes_car_un_element(self):
        un_joc = [self.videojocs[0]]
        resultat = p01.joc_mes_car(un_joc)
        self.assertEqual(resultat["titol"], "The Legend of Zelda")

    def test_joc_mes_car_llista_buida(self):
        resultat = p01.joc_mes_car([])
        self.assertIsNone(resultat)

    def test_joc_mes_car_retorna_diccionari(self):
        resultat = p01.joc_mes_car(self.videojocs)
        self.assertIsInstance(resultat, dict)

    # --- TEST INTENCIONADAMENT ERRONI (per demostrar CI en vermell) ---
    def test_ERROR_demostratiu(self):
        """Aquest test falla intencionadament per demostrar el CI en vermell."""
        resultat = p01.joc_mes_car(self.videojocs)
        self.assertEqual(resultat["preu"], 999.99)  # ERROR: el preu real és 69.99


class TestProvaEscrita02(unittest.TestCase):
    """Bateria de proves per a les funcions de la Prova Escrita 02."""

    def setUp(self):
        self.llista_prova = [3, -1, 7, 2, -1, 9, 4, 7]
        self.matriu_3x3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.matriu_no_quadrada = [[1, 2], [3, 4, 5]]

    def test_crear_sequencia_cas_valid(self):
        resultat = p02.crear_sequencia(5, 10)
        self.assertEqual(resultat, [5, 6, 7, 8, 9, 10])

    def test_crear_sequencia_inici_major_que_final(self):
        resultat = p02.crear_sequencia(10, 5)
        self.assertEqual(resultat, [])

    def test_crear_sequencia_valor_negatiu(self):
        resultat = p02.crear_sequencia(-2, 5)
        self.assertEqual(resultat, [])

    def test_crear_sequencia_valors_iguals(self):
        resultat = p02.crear_sequencia(5, 5)
        self.assertEqual(resultat, [])

    def test_crear_sequencia_no_enters(self):
        resultat = p02.crear_sequencia(1.5, 5)
        self.assertEqual(resultat, [])

    def test_senars_majors_cas_valid(self):
        resultat = p02.numeros_senars_majors(self.llista_prova, 3)
        self.assertEqual(resultat, [7, 9, 7])

    def test_senars_majors_llista_buida(self):
        resultat = p02.numeros_senars_majors([], 3)
        self.assertEqual(resultat, [])

    def test_senars_majors_limit_no_enter(self):
        resultat = p02.numeros_senars_majors([1, 3, 5], 2.5)
        self.assertEqual(resultat, [])

    def test_senars_majors_cap_compleix(self):
        resultat = p02.numeros_senars_majors([2, 4, 6, 8], 1)
        self.assertEqual(resultat, [])

    def test_primera_posicio_trobat(self):
        resultat = p02.primera_posicio(self.llista_prova, 7)
        self.assertEqual(resultat, 2)

    def test_primera_posicio_no_trobat(self):
        resultat = p02.primera_posicio(self.llista_prova, 15)
        self.assertEqual(resultat, -1)

    def test_primera_posicio_llista_buida(self):
        resultat = p02.primera_posicio([], 5)
        self.assertEqual(resultat, -1)

    def test_primera_posicio_element_al_principi(self):
        resultat = p02.primera_posicio([5, 3, 1], 5)
        self.assertEqual(resultat, 0)

    def test_primera_posicio_element_al_final(self):
        resultat = p02.primera_posicio([1, 2, 3, 99], 99)
        self.assertEqual(resultat, 3)

    def test_diagonal_principal_matriu_3x3(self):
        resultat = p02.diagonal_principal(self.matriu_3x3)
        self.assertEqual(resultat, [1, 5, 9])

    def test_diagonal_principal_matriu_no_quadrada(self):
        resultat = p02.diagonal_principal(self.matriu_no_quadrada)
        self.assertEqual(resultat, [])

    def test_diagonal_principal_matriu_buida(self):
        resultat = p02.diagonal_principal([])
        self.assertEqual(resultat, [])

    def test_diagonal_principal_matriu_1x1(self):
        resultat = p02.diagonal_principal([[42]])
        self.assertEqual(resultat, [42])

    def test_diagonal_principal_no_es_llista(self):
        resultat = p02.diagonal_principal("no és una matriu")
        self.assertEqual(resultat, [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
