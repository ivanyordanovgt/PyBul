import unittest
from converter.vanilla.main import *

class TestVanilla(unittest.TestCase):
    def test_while(self):
        result = WHILE("докато var е 1")
        self.assertEqual(result, "while var == 1")
    def test_print(self):
        result = PRINT('кажи "Здрасти"')
        self.assertEqual(result, 'print( "Здрасти" )')
    def test_input(self):
        result = INPUT('попитай "Д/н"')
        self.assertEqual(result, 'str(input( "Д/н"))')
    def test_if(self):
        result = IF('ако потребител е 1 или потребител е 5:')
        self.assertEqual(result, "if потребител == 1 или потребител == 5:")
    def test_elif_or(self):
        result = ELIF("if потребител == 1 или потребител == 5:")
        self.assertEqual(result, "if потребител == 1 or потребител == 5:")
    def test_elif(self):
        result = ELIF("или ако потребител е 0 или потребител е 1")
        self.assertEqual(result, "elif потребител == 0 or потребител == 1")
    def test_else(self):
        result = ELSE("друго:")
        self.assertEqual(result, "else:")
    def test_break(self):
        result = BREAK('спри')
        self.assertEqual(result, 'break')
if __name__ == "__main__":
    unittest.main()
