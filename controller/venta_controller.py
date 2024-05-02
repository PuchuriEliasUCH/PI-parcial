import sys
from pathlib import Path
from tabulate import tabulate
sys.path.append(str(Path(__file__).resolve().parent.parent))
from utils.json_manager import lista_productos
def seleccionar_producto():
    print(lista_productos())
