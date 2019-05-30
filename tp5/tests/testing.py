import unittest
import sys
import os
from os import path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import src.agenda as agenda  # noqa
import src.capitalizada as capitalizada  # noqa
import src.contraseña as contraseña  # noqa
import src.devolucion_de_letras as devolucion_de_letras  # noqa
import src.punto_2 as punto_2  # noqa
import src.vocales as vocales  # noqa

class TestAgenda(unittest.TestCase):
    def test_agenda(self):
        pass