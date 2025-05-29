import unittest
from flask import current_app
from app import create_app,db
import os

from app.models.area import Area
from app.models.grupo import Grupo


class GrupoTestCase(unittest.TestCase):
    
    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        
    def tearDown(self):
        self.app_context.pop()
        
    def test_area_creation(self):
        area = self.__nuevaarea()
        self.assertIsNotNone(area)
        self.assertEqual(area.nombre, "Basica")
        self.assertIsNotNone(area.grupo)

    def __nuevaarea(self):
        area = Area()
        grupo = Grupo()
        area.nombre = 'Basica'
        area.grupo = grupo
        return area