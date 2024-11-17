import unittest
from converter.modded.main import *

class TestVanilla(unittest.TestCase):
    def test_show(self):
        result = SHOW("покажи променлива")
        self.assertEqual(result, "print( променлива.show() )")
    def test_random_number(self):
        result = RANDOM_NUMBER("случайно число от 1 до 10")
        self.assertEqual(result, "random.randint(1, 10)")
    def test_matrix_game_map(self):
        result = GAME_MAP('игралноПоле 2x2')
        self.assertEqual(result, "GameList([[' ', ' '], [' ', ' ']]) ")


if __name__ == "__main__":
    unittest.main()
