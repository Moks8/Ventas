from flask import Flask 
from flask_testing import TestCase
import run 

class TestFlaskBase(TestCase):
    def create_app(self):
        self.app = run.app
        return run.app
      

    def setUp(self): #se lanza cada vez antes de cada test y el teardown despues
        self.client = self.app.test_client()  #simulador de navegador
        self.client.testing = True #se le dice que va a ser de prueba

    def tearDown(self):
        pass