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
        """
        Prepara les dades de prova abans de cada test.
        Es crea una còpia fresca de videojocs i biblioteca per evitar
        que un test afecti el resultat del següent.
        """
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
        self.biblioteca = []  # Biblioteca buida per a cada test

    # -----------------------------------------------------------------------
    # Exercici 2: buscar_per_titol
    # -----------------------------------------------------------------------

    def test_buscar_titol_existent(self):
        """Verifica que es troba un joc existent pel seu títol exacte."""
        resultat = p01.buscar_per_titol("FIFA 24", self.videojocs)
        self.assertIsNotNone(resultat)
        self.assertEqual(resultat["titol"], "FIFA 24")

    def test_buscar_titol_insensible_majuscules(self):
        """Verifica que la cerca no distingeix majúscules de minúscules."""
        resultat = p01.buscar_per_titol("cyberpunk 2077", self.videojocs)
        self.assertIsNotNone(resultat)
        self.assertEqual(resultat["titol"], "Cyberpunk 2077")

    def test_buscar_titol_no_existent(self):
        """Verifica que retorna None per un joc que no existeix al catàleg."""
        resultat = p01.buscar_per_titol("Mario Bros", self.videojocs)
        self.assertIsNone(resultat)

    def test_buscar_titol_llista_buida(self):
        """Verifica el comportament amb una llista de videojocs buida."""
        resultat = p01.buscar_per_titol("FIFA 24", [])
        self.assertIsNone(resultat)

    def test_buscar_titol_retorna_diccionari_complet(self):
        """Verifica que el diccionari retornat conté tots els camps."""
        resultat = p01.buscar_per_titol("The Legend of Zelda", self.videojocs)
        self.assertIn("preu", resultat)
        self.assertEqual(resultat["preu"], 59.99)

    # -----------------------------------------------------------------------
    # Exercici 3: afegir_a_biblioteca
    # -----------------------------------------------------------------------

    def test_afegir_joc_correctament(self):
        """Verifica que s'afegeix un joc nou i es rep el missatge d'èxit."""
        resultat = p01.afegir_a_biblioteca("FIFA 24", self.videojocs, self.biblioteca)
        self.assertEqual(resultat, "✅ Joc afegit!")
        self.assertEqual(len(self.biblioteca), 1)

    def test_afegir_joc_no_trobat(self):
        """Verifica el missatge d'error quan el joc no existeix al catàleg."""
        resultat = p01.afegir_a_biblioteca("GTA VI", self.videojocs, self.biblioteca)
        self.assertEqual(resultat, "❌ Joc no trobat")
        self.assertEqual(len(self.biblioteca), 0)

    def test_afegir_joc_duplicat(self):
        """Verifica que no s'afegeix un joc que ja és a la biblioteca."""
        p01.afegir_a_biblioteca("FIFA 24", self.videojocs, self.biblioteca)
        resultat = p01.afegir_a_biblioteca("FIFA 24", self.videojocs, self.biblioteca)
        self.assertEqual(resultat, "⚠️ Ja està a la biblioteca")
        self.assertEqual(len(self.biblioteca), 1)

    def test_afegir_diversos_jocs(self):
        """Verifica que es poden afegir múltiples jocs diferents."""
        p01.afegir_a_biblioteca("FIFA 24", self.videojocs, self.biblioteca)
        p01.afegir_a_biblioteca("Cyberpunk 2077", self.videojocs, self.biblioteca)
        self.assertEqual(len(self.biblioteca), 2)

    # -----------------------------------------------------------------------
    # Exercici 4: joc_mes_car
    # -----------------------------------------------------------------------

    def test_joc_mes_car_correcte(self):
        """Verifica que retorna el joc amb el preu més alt (FIFA 24 = 69.99€)."""
        resultat = p01.joc_mes_car(self.videojocs)
        self.assertEqual(resultat["titol"], "FIFA 24")
        self.assertEqual(resultat["preu"], 69.99)

    def test_joc_mes_car_un_element(self):
        """Verifica que amb un sol joc, el retorna directament."""
        un_joc = [self.videojocs[0]]
        resultat = p01.joc_mes_car(un_joc)
        self.assertEqual(resultat["titol"], "The Legend of Zelda")

    def test_joc_mes_car_llista_buida(self):
        """Verifica que retorna None amb una llista buida."""
        resultat = p01.joc_mes_car([])
        self.assertIsNone(resultat)

    def test_joc_mes_car_retorna_diccionari(self):
        """Verifica que el resultat és un diccionari (no un preu numèric)."""
        resultat = p01.joc_mes_car(self.videojocs)
        self.assertIsInstance(resultat, dict)


# ===========================================================================
# CLASSE DE TEST PER A LA PROVA ESCRITA 02 (Paper-02)
# Exercicis testejats: 1 (crear_sequencia), 2 (numeros_senars_majors),
#                      3 (primera_posicio), 4 (diagonal_principal)
# ===========================================================================

class TestProvaEscrita02(unittest.TestCase):
    """Bateria de proves per a les funcions de la Prova Escrita 02."""

    def setUp(self):
        """Prepara dades de prova reutilitzables per als tests."""
        self.llista_prova = [3, -1, 7, 2, -1, 9, 4, 7]
        self.matriu_3x3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.matriu_no_quadrada = [[1, 2], [3, 4, 5]]

    # -----------------------------------------------------------------------
    # Exercici 1: crear_sequencia
    # -----------------------------------------------------------------------

    def test_crear_sequencia_cas_valid(self):
        """Verifica la generació correcta d'una seqüència (ambdós extrems inclosos)."""
        resultat = p02.crear_sequencia(5, 10)
        self.assertEqual(resultat, [5, 6, 7, 8, 9, 10])

    def test_crear_sequencia_inici_major_que_final(self):
        """Verifica que retorna llista buida si inici > final."""
        resultat = p02.crear_sequencia(10, 5)
        self.assertEqual(resultat, [])

    def test_crear_sequencia_valor_negatiu(self):
        """Verifica que retorna llista buida si algun valor és negatiu."""
        resultat = p02.crear_sequencia(-2, 5)
        self.assertEqual(resultat, [])

    def test_crear_sequencia_valors_iguals(self):
        """Verifica que retorna llista buida si inici == final."""
        resultat = p02.crear_sequencia(5, 5)
        self.assertEqual(resultat, [])

    def test_crear_sequencia_no_enters(self):
        """Verifica que retorna llista buida si els paràmetres no són enters."""
        resultat = p02.crear_sequencia(1.5, 5)
        self.assertEqual(resultat, [])

    # -----------------------------------------------------------------------
    # Exercici 2: numeros_senars_majors
    # -----------------------------------------------------------------------

    def test_senars_majors_cas_valid(self):
        """Verifica el filtratge correcte: senars de llista_prova majors que 3."""
        resultat = p02.numeros_senars_majors(self.llista_prova, 3)
        self.assertEqual(resultat, [7, 9, 7])

    def test_senars_majors_llista_buida(self):
        """Verifica que retorna llista buida si l'entrada és buida."""
        resultat = p02.numeros_senars_majors([], 3)
        self.assertEqual(resultat, [])

    def test_senars_majors_limit_no_enter(self):
        """Verifica que retorna llista buida si limit no és un enter."""
        resultat = p02.numeros_senars_majors([1, 3, 5], 2.5)
        self.assertEqual(resultat, [])

    def test_senars_majors_cap_compleix(self):
        """Verifica el cas on cap element és senar i major que el limit."""
        resultat = p02.numeros_senars_majors([2, 4, 6, 8], 1)
        self.assertEqual(resultat, [])

    # -----------------------------------------------------------------------
    # Exercici 3: primera_posicio
    # -----------------------------------------------------------------------

    def test_primera_posicio_trobat(self):
        """Verifica que retorna la posició correcta de la primera aparició."""
        resultat = p02.primera_posicio(self.llista_prova, 7)
        self.assertEqual(resultat, 2)

    def test_primera_posicio_no_trobat(self):
        """Verifica que retorna -1 si l'element no és a la llista."""
        resultat = p02.primera_posicio(self.llista_prova, 15)
        self.assertEqual(resultat, -1)

    def test_primera_posicio_llista_buida(self):
        """Verifica que retorna -1 amb una llista buida."""
        resultat = p02.primera_posicio([], 5)
        self.assertEqual(resultat, -1)

    def test_primera_posicio_element_al_principi(self):
        """Verifica que detecta correctament l'element a la posició 0."""
        resultat = p02.primera_posicio([5, 3, 1], 5)
        self.assertEqual(resultat, 0)

    def test_primera_posicio_element_al_final(self):
        """Verifica que detecta correctament l'element a l'última posició."""
        resultat = p02.primera_posicio([1, 2, 3, 99], 99)
        self.assertEqual(resultat, 3)

    # -----------------------------------------------------------------------
    # Exercici 4: diagonal_principal
    # -----------------------------------------------------------------------

    def test_diagonal_principal_matriu_3x3(self):
        """Verifica la diagonal principal d'una matriu quadrada 3x3."""
        resultat = p02.diagonal_principal(self.matriu_3x3)
        self.assertEqual(resultat, [1, 5, 9])

    def test_diagonal_principal_matriu_no_quadrada(self):
        """Verifica que retorna llista buida per una matriu no quadrada."""
        resultat = p02.diagonal_principal(self.matriu_no_quadrada)
        self.assertEqual(resultat, [])

    def test_diagonal_principal_matriu_buida(self):
        """Verifica que retorna llista buida per una matriu buida."""
        resultat = p02.diagonal_principal([])
        self.assertEqual(resultat, [])

    def test_diagonal_principal_matriu_1x1(self):
        """Verifica la diagonal d'una matriu 1x1 (un sol element)."""
        resultat = p02.diagonal_principal([[42]])
        self.assertEqual(resultat, [42])

    def test_diagonal_principal_no_es_llista(self):
        """Verifica que retorna llista buida si l'entrada no és una llista."""
        resultat = p02.diagonal_principal("no és una matriu")
        self.assertEqual(resultat, [])


# ===========================================================================
# Punt d'entrada
# ===========================================================================

if __name__ == "__main__":
    unittest.main(verbosity=2)
