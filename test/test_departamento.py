import unittest
from flask import current_app
from app import create_app
import os
from app.models.departamento import Departamento

class AppTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()
        
    def test_departamento_creation(self):
        departamento = Departamento()
        departamento.Nombre = 'Departamento 1'
        self.assertIsNotNone(departamento)
        self.assertEqual(departamento.Nombre, "Departamento 1")
        
if __name__ == '__main__':
    unittest.main()