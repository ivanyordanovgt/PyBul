import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from pybul_converter import custom_translate

SNAPSHOTS = [
    './tests/code/simple',
    './tests/code/medium'
]

for SNAPSHOT in SNAPSHOTS:
    custom_translate(SNAPSHOT, True, False)

