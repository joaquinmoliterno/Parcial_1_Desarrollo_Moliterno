import unittest
from flask import current_app
from app import create_app
from app.models.alumno import Alumno
import os
from app.models.documento import Documento

class AppTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()
        
        
    def test_alumno_creation(self):
        alumno = self.__nuevoalumno()
        self.assertIsNotNone(alumno)
        self.assertEqual(alumno.apellido, "Silva")
        self.assertEqual(alumno.nombre, "Abril")
        self.assertEqual(alumno.documento, "12345678")
        self.assertIsNotNone(alumno.tipo_documento)
        self.assertEqual(alumno.fecha_nacimiento, "1990-01-01")
        self.assertEqual(alumno.sexo, "F")
        self.assertEqual(alumno.legajo, 1234)
        self.assertEqual(alumno.fecha_ingreso, "2022-01-01")

    def __nuevoalumno(self):
        alumno = Alumno()
        tipo_documento=Documento()
        alumno.apellido = 'Silva'
        alumno.nombre = 'Abril'
        alumno.documento = '12345678'
        alumno.tipo_documento = tipo_documento
        alumno.fecha_nacimiento = '1990-01-01'
        alumno.sexo = 'F'
        alumno.legajo = 1234
        alumno.fecha_ingreso = '2022-01-01'
        return alumno
        


if __name__ == '__main__':
    unittest.main()