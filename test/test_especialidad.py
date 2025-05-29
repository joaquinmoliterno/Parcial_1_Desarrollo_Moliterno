import unittest
from flask import current_app
from app import create_app
import os

from app.models.especialidad import Especialidad
from app.models.tipo_especialidad import TipoEspecialidad

class AppTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()
        
    def test_especialidad_creation(self):
        especialidad = self.__nuevaespecialidad()
        self.assertIsNotNone(especialidad)
        self.assertEqual(especialidad.nombre, "Especialidad de prueba")
        self.assertEqual(especialidad.letra, "E")
        self.assertEqual(especialidad.observacion, "Especialidad de prueba")
        self.assertIsNotNone(especialidad.tipo_especialidad)

    def __nuevaespecialidad(self):
        especialidad = Especialidad()
        tipo_especialidad = TipoEspecialidad()
        especialidad.nombre = "Especialidad de prueba"
        especialidad.letra = "E"
        especialidad.observacion = "Especialidad de prueba"
        especialidad.tipo_especialidad = tipo_especialidad
        return especialidad
        