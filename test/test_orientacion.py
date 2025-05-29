import unittest
from flask import current_app
from app import create_app
import os
from app.models.especialidad import Especialidad
from app.models.materia import Materia
from app.models.orientacion import Orientacion

class AppTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()
        
    def test_documento_creation(self):
        orientacion = self.__nuevaorientacion()
        self.assertIsNotNone(orientacion)
        self.assertIsNotNone(orientacion.materia)
        self.assertIsNotNone(orientacion.especialidad)
        self.assertEqual(orientacion.nombre, "Orientacion 1")

    def __nuevaorientacion(self):
        orientacion= Orientacion()
        materia = Materia()
        especialidad = Especialidad()
        orientacion.materia = materia
        orientacion.especialidad = especialidad
        orientacion.nombre = 'Orientacion 1'
        return orientacion
        
if __name__ == '__main__':
    unittest.main()