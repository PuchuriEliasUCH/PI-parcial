import sys
from pathlib import Path
from tabulate import tabulate

sys.path.append(str(Path(__file__).resolve().parent.parent))
from utils.json_manager import read_data, write_json


def listar_ventas():
    print(tabulate(read_data()['ventas'], headers='keys', tablefmt='pretty'))


def registrar_venta(venta):
    data = read_data()

    v = {
        'número de venta': len(data['ventas']) + 1,
        'codigo de producto': venta.producto[0]['codigo'],
        'nombre de producto': venta.producto[0]["nombre"],
        'precio unitario': venta.producto[0]["precio"],
        'cantidad': venta.cantidad,
        'subtotal': venta.subtotal(),
        'impuesto': venta.aplicar_impuesto(),
        'total': venta.total()
    }

    data['ventas'].append(v)

    write_json(data)
