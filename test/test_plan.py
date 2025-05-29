import unittest
from flask import current_app
from app import create_app 
import os

from app.models.plan import Plan

class AppTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()
        
    def test_plan_creation(self):
        plan = self.__nuevoplan()
        self.assertIsNotNone (plan)
        self.assertEqual(plan.nombre, "Plan de prueba")
        self.assertEqual(plan.fecha_inicio, "2020-01-01")
        self.assertEqual(plan.fecha_fin, "2020-01-31")
        self.assertEqual(plan.observacion, "Plan de prueba")

    def __nuevoplan(self):
        plan = Plan()
        plan.nombre = "Plan de prueba"
        plan.fecha_inicio = "2020-01-01"
        plan.fecha_fin = "2020-01-31"
        plan.observacion = "Plan de prueba"
        return plan