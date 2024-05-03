import sys
from pathlib import Path
from tabulate import tabulate

sys.path.append(str(Path(__file__).resolve().parent.parent))
from utils.json_manager import read_data, write_json

lista_productos = read_data()['productos']


def listar_productos():
    print(tabulate(lista_productos, headers="keys", tablefmt='pretty'))


def buscar_productos_por_codigo(codigo):
    prod = []
    for i in lista_productos:
        if i['codigo'] != int(codigo):
            continue
        else:
            prod.append(i)
            break

    if len(prod) == 0:
        print("Este producto no está registrado")
    else:
        return prod


def listar_productos_por_categoria(cate):
    resultados = list(filter(lambda x: x['categoria'] == cate, read_data()['productos']))

    if resultados:
        print(tabulate(resultados, headers="keys", tablefmt='pretty'))
    else:
        print("No tenemos productos en esta categoría")


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
        prod['cuello'] = producto.cuello
        prod['manga'] = producto.manga
        prod['precio'] = producto.aplicar_descuento()
    elif producto.categoria == 'pantalon':
        prod['tipo'] = producto.tipo
        prod['talla'] = producto.talla

    data['productos'].append(prod)

    producto.mensaje()

    write_json(data)
