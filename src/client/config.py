import os
from pathlib import Path

HERE = os.path.dirname(os.path.abspath(__file__))
DATA_FOLDER = Path(HERE).parent.parent.parent / "data"
CO2_BODER = 1000

DYNAMODB_TABLE = "kashiwa-co2"

