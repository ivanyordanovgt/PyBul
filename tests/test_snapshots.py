import unittest
from pybul_converter import custom_translate
from tests.utils.files import get_file_contents
import os

class TestSnapshots(unittest.TestCase):
    def test_demo_files(self):
        root_dir = "./codes"
        expected_value = "1"

        for dirpath, dirnames, filenames in os.walk(root_dir):
            if "demo.pybul" in filenames:
                file_path = os.path.join(dirpath, "demo.pybul")
                snapshot_path = os.path.join(dirpath, "snapshot.py")
                
                with open(file_path, 'r') as file:
                    content = file.read().strip()
                    converter_result = custom_translate(content)
                with open(snapshot_path, 'r') as file:
                    snapshot = file.read().strip()
                    self.assertEqual(converter_result, snapshot)
