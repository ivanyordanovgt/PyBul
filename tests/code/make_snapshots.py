import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from pybul_converter import custom_translate

custom_translate('./tests/code/simple', True)
custom_translate('./tests/code/medium', True)
