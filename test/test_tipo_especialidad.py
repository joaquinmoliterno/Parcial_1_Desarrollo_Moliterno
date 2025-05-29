import unittest
from flask import current_app
from app import create_app
import os

from app.models.tipo_especialidad import TipoEspecialidad

class AppTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()
        
    def test_tipoespecialidad_creation(self):
        tipo_especialidad = self.__nuevo_tipoespecialidad()
        self.assertIsNotNone(tipo_especialidad)
        self.assertEqual(tipo_especialidad.nombre, 'Prueba')
        self.assertEqual(tipo_especialidad.nivel, '1')

    def __nuevo_tipoespecialidad(self):
        tipo_especialidad = TipoEspecialidad()
        tipo_especialidad.nombre = 'Prueba'
        tipo_especialidad.nivel = '1'
        return tipo_especialidad
        