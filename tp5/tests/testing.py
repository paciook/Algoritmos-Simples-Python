import unittest
import sys
import os
from os import path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import src.agenda as agenda  # noqa
import src.capitalizada as capitalizada  # noqa
import src.contraseña as contrasena  # noqa
import src.devolucion_de_letras as devolucion_de_letras  # noqa
import src.punto_2 as punto_2  # noqa
import src.vocales as vocales  # noqa


class TestAgenda(unittest.TestCase):
    def test_agenda(self):
        pass


class TestCapitalizada(unittest.TestCase):
    def test_capitalizada(self):
        respuesta = ["USB", "Universal Serial Bus", ""]
        self.assertEqual(capitalizada.ejercicios("universal\
                                                  serial bus"), respuesta)
        self.assertEqual(capitalizada.ejercicios("UNIVERSAL\
                                                  SERIAL BUS"), respuesta)

        # bitguarden
        # syncthing


class TestContraseña(unittest.TestCase):
    def test_contrasena(self):
        self.assertTrue(contrasena.verificaContrasena("WindowsXP"))
        self.assertFalse(contrasena.verificaContrasena("MiContraseña"))
        self.assertFalse(contrasena.verificaContrasena("FefeMoon"))


class TestDevolucionDeLetras(unittest.TestCase):
    def test_devolucion_de_letras(self):
        self.assertEqual(devolucion_de_letras.consonantes("algoritmos"),
                         "lgrtms")
        self.assertEqual(devolucion_de_letras.vocales("algoritmos"), "aoio")


class TestPunto2(unittest.TestCase):
    def test_punto_2(self):
        self.assertEqual(punto_2.letras("Embajada"), "A")
        self.assertEqual(punto_2.letras("Venenosa"), "E")
        self.assertEqual(punto_2.letras("Venta"), 0)
        self.assertEqual(punto_2.letras("Ver3da"), -1)
        self.assertEqual(punto_2.letras("Hola como estas"), -1)
        self.assertEqual(punto_2.letras("paciook"), "Hermoso, A")


class TestVocales(unittest.TestCase):
    def test_vocales(self):
        cantVocales = [1, 2, 3, 4, 5]
        self.assertEqual(vocales.devuelveVocales("aeeIIiooooUuUuU"),
                         cantVocales)
        cantVocales = [2, 3, 1, 3, 1]
        self.assertEqual(vocales.devuelveVocales("aeaeieouoo"), cantVocales)
        pass


if __name__ == "__main__":
    unittest.main()
