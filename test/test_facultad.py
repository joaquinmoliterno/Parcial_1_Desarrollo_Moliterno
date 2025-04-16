import unittest
from flask import current_app
from app import create_app
from app.models import Facultad
import os


class FacultadTestCase(unittest.TestCase):
    
    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        
    def testDown(self):
        self.app_context.pop()
        
    def test_facultad_creation(self):
        facultad=Facultad()
        facultad.nombre = "fa"
        facultad.abreviatura = "gsd"
        facultad.directorio = "hfds"
        facultad.sigla = "hsd"
        facultad.codigoPostal = "sdfh"
        facultad.ciudad = "sdfh"
        facultad.domicilio = "sdfh"
        facultad.telefono = "sdfh"
        facultad.contacto = "sdfh"
        facultad.email = "sdfh"
        self.assertIsNotNone(facultad)
        self.assertEqual(facultad.nombre,"fa")
        self.assertEqual(facultad.abreviatura,"gsd")
        
if __name__ == '__main__':
    unittest.main()