import unittest
from flask import current_app
from app import create_app,db
from app.models.grupo import Grupo
from app.models.grado import Grado
import os


class GrupoTestCase(unittest.TestCase):
    
    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        
    def tearDown(self):
        self.app_context.pop()
        
    def test_grupo_creation(self):
        grupo = self.__nuevogrupo()
        self.assertIsNotNone(grupo)
        self.assertEqual(grupo.nombre,"Grupo 1")
        self.assertIsNotNone(grupo.grado)

    def __nuevogrupo(self):
        grupo=Grupo()
        grado=Grado()
        grupo.nombre = "Grupo 1"
        grupo.grado= grado
        return grupo

    '''def test_crear_grupo(self):
        grupo= self.__nuevogrupo()
        db.session.add(grupo)
        db.session.commit()
        self.assertIsNotNone(grupo.id)
        self.assertEqual(grupo.nombre, "Grupo 1")

    def test_actualizar_grupo(self):
        grupo= self.__nuevogrupo()
        db.session.add(grupo)
        db.session.commit()
        grupo.nombre= "Grupo 1 actualizado"
        db.session.commit()
        grupo_actualizado= Grupo.query.get(grupo.id)
        self.assertEqual(grupo_actualizado.nombre, "Grupo 1 actualizado")

    def test_borrar_grupo(self):
        grupo = self.__nuevogrupo()
        db.session.add(grupo)
        db.session.commit()
        db.session.delete(grupo)
        db.session.commit()
        resultado = Grupo.query.get(grupo.id)
        self.assertIsNone(resultado)'''


        
if __name__ == '__main__':
    unittest.main()
    