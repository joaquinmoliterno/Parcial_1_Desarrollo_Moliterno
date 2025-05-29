import unittest
from flask import current_app
from app import create_app
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
        
    def test_documento_creation(self):
        documento = Documento()
        documento.tipo_documento = 'DNI'
        self.assertIsNotNone(documento)
        self.assertEqual(documento.tipo_documento, "DNI")
        
if __name__ == '__main__':
    unittest.main()