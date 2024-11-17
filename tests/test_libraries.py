import unittest
from converter.libraries.main import *
from dataTypes.whithin_function_block import Whithin_function_block
import re

class TestLibraries(unittest.TestCase):
    def test_on_press(self):
        whithin_function_block = Whithin_function_block("test", 2, '    кажи "Здравей"', "клавиатура:")
        
        result = ON_PRESS(whithin_function_block)
        expect = """
def <FUNC_NAME>(data):
    кажи "Здравей"
keyboard.on_press(<FUNC_NAME>)"""
        
        result_pattern = re.sub(r'def \S+\(data\):', 'def <FUNC_NAME>(data):', result.strip())
        result_pattern = re.sub(r'keyboard.on_press\(\S+\)', 'keyboard.on_press(<FUNC_NAME>)', result_pattern)

        expected_pattern = re.sub(r'def \S+\(data\):', 'def <FUNC_NAME>(data):', expect.strip())
        expected_pattern = re.sub(r'keyboard.on_press\(\S+\)', 'keyboard.on_press(<FUNC_NAME>)', expected_pattern)

        self.assertEqual(result_pattern, expected_pattern)
    def test_time_sleep(self):
        result = TIME_SLEEP("изчакай 1 секунда")
        self.assertEqual(result, "time.sleep(1)")

if __name__ == "__main__":
    unittest.main()