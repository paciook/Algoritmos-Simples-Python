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
        pass

        # bitguarden
        # syncthing



class TestContraseña(unittest.TestCase):
    def test_contraseña(self):
        self.assertTrue(contrasena.verificaContrasena("WindowsXP"))
        self.assertFalse(contrasena.verificaContrasena("MiContraseña"))



        pass


class TestDevolucionDeLetras(unittest.TestCase):
    def test_devolucion_de_letras(self):
        pass


class TestPunto2(unittest.TestCase):
    def test_punto_2(self):
        pass


class TestVocales(unittest.TestCase):
    def test_vocales(self):
        pass


if __name__ == "__main__":
    unittest.main()

