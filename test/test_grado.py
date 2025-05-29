import unittest
from flask import current_app
from app import create_app,db
from app.models.grado import Grado
import os


class GradoTestCase(unittest.TestCase):
    
    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        
    def tearDown(self):
        self.app_context.pop()
        
    def test_grado_creation(self):
        grado = self.__nuevogrado()
        self.assertIsNotNone(grado)
        self.assertEqual(grado.nombre,"3ro")

    def __nuevogrado(self):
        grado=Grado()
        grado.nombre = "3ro"
        return grado

    '''def test_crear_grado(self):
        grado= self.__nuevogrado()
        db.session.add(grado)
        db.session.commit()
        self.assertIsNotNone(grado.id)
        self.assertEqual(grado.nombre, "3ro")

    def test_actualizar_grado(self):
        grado= self.__nuevogrado()
        db.session.add(grado)
        db.session.commit()
        grado.nombre= "Grado Actualizado"
        db.session.commit()
        grado_actualizado= Grado.query.get(grado.id)
        self.assertEqual(grado_actualizado.nombre, "Grado Actualizado")

    def test_borrar_grado(self):
        grado = self.__nuevogrado()
        db.session.add(grado)
        db.session.commit()
        db.session.delete(grado)
        db.session.commit()
        resultado = Grado.query.get(grado.id)
        self.assertIsNone(resultado)'''


        
if __name__ == '__main__':
    unittest.main()