import unittest
from flask import current_app
from app import create_app
import os

from app.models.materia import Materia
from app.models.nota import Nota

class AppTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()
        
    def test_materia_creation(self):
        materia = self.__nuevamateria()
        self.assertIsNotNone(materia)
        self.assertEqual(materia.nombre, "Matematicas")
        self.assertEqual(materia.codigo, "MAT-101")
        self.assertEqual(materia.observacion, "Esta es una materia de matematicas")
        self.assertIsNotNone(materia.nota)

    def __nuevamateria(self):
        materia = Materia()
        nota = Nota()
        materia.nombre = "Matematicas"
        materia.codigo = "MAT-101"
        materia.observacion = "Esta es una materia de matematicas"
        materia.nota = nota
        return materia