#suíte de teste desenvolvida:
# A suite de teste foi baseada nos possiveis fluxos
# se o teste passa no primeiro if
# e quanado ela não passa qual o compotamento dela nos diferentes casos 

import main
from unittest.mock import MagicMock
from unittest.mock import patch

import unittest

class teste_mock(unittest.TestCase):
    def teste_normalize_menor_igual_menor(self):
        main.my_min = MagicMock(return_value=3)
        main.my_max = MagicMock(return_value=3)
        self.assertEqual([100],main.normalize([3]))
    
    def teste_normalize(self):
        main.my_min = MagicMock(return_value=3)
        main.my_max = MagicMock(return_value=4)
        self.assertEqual([0.0, 100.0],main.normalize([3,4]))
    
    def teste_normalize_maior_que_100(self):
        main.my_min = MagicMock(return_value=100)
        main.my_max = MagicMock(return_value=1000)
        self.assertEqual([0.0, 100.0],main.normalize([100,1000]))
    
    def teste_normalize_menor_que_1(self):
        main.my_min = MagicMock(return_value=0.4)
        main.my_max = MagicMock(return_value=10)
        self.assertEqual([0.0, 6.25, 100.0],main.normalize([0.4,1,10]))
    
    def teste_normalize_erro(self):
        main.my_min = MagicMock(return_value=20)
        main.my_max = MagicMock(return_value=10)
        self.assertEqual([196.00000000000003, 190.0, 100.0],main.normalize([0.4,1,10]))
    
    
if __name__ == '__main__':
    unittest.main()