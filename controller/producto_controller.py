import sys
from pathlib import Path
from tabulate import tabulate
sys.path.append(str(Path(__file__).resolve().parent.parent))
from utils.json_manager import read_data, write_json
from model.producto import Producto
from model.camisa import Camisa
from model.pantalon import Pantalon

def listar_productos():
    print(tabulate(read_data()['productos'], headers="keys", tablefmt='pretty'))

def listar_categoria(cate):
    print(tabulate(list(filter(lambda x: x['categoria'] == cate, read_data()['productos'])), headers="keys", tablefmt='pretty'))

def registrar_producto(producto):
    data = read_data()

    prod = {
        'codigo': producto.codigo,
        'nombre': producto.nombre,
        'categoria': producto.categoria,
        'precio': producto.precio,
        'color': producto.color,
        'stock': producto.stock
    }

    if producto.categoria == 'camisa':
        prod['descuento'] = producto.descuento
        prod['cuello'] = producto.cuello
        prod['manga'] = producto.manga
    elif producto.categoria == 'pantalon':
        prod['tipo'] = producto.tipo
        prod['talla'] = producto.talla


    data['productos'].append(prod)

    producto.mensaje()

    write_json(data)


