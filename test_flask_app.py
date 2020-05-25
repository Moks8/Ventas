import unittest
from test_base import TestFlaskBase

class TestWeb(TestFlaskBase):
    def test_server_is_on(self):
        loquemedevuelve = self.client.get("/") #si el servidore sta levantado la peticion devolvera algo, al hacer GET. Para que me devuelva algo lo meto en variable
        self.assertEqual(loquemedevuelve.status_code,200)
        #self.assert200

    def test_route_index_is_lista_regiones(self):
        loquemedevuelve = self.client.get("/") 
        self.assertEqual(loquemedevuelve.data,b"Hola, Mundo")



if __name__== "__main__":
    unittest.main()

