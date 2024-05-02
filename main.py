from model import venta
from model.venta import Venta
from model.pantalon import Pantalon
from model.producto import Producto
from model.camisa import Camisa
from model.temporada_verano import Verano
from controller import producto_controller, venta_controller

from utils.validates import click, validar_codigo, validar_existencia

@click.group()
def main():
    pass


# listar productos
@main.command()
def productos():
    producto_controller.listar_productos()

# listar por categoria
@main.command()
@click.option('--categoria',
              prompt = 'Categoria',
              help = "Introducir una parte del nombre de la categoría para ver resultados de busqueda",
              type = str)
@click.pass_context
def p_p_categoria(context, categoria):
    if not categoria:
        context.fail("Debe ingresar almenos la inicial de la categoría a buscar")
    else:
        producto_controller.listar_productos_por_categoria(categoria)

# registrar productos
@main.command()
@click.option('--codigo',prompt = 'Código', help = "Introducir codigo del producto",type = click.UNPROCESSED,callback = validar_codigo)
@click.option('--nombre',prompt = 'Nombre',help = "Introducir nombre del producto",type = str)
@click.option('--categoria',prompt = 'Categoria',help = "Introducir categoría del producto",type = str)
@click.option('--precio',prompt = 'Precio unitario',help = "Introducir precio del producto",type = float)
@click.option('--color',prompt = 'Color de la prenda',help = "Introducir color del producto",type = str)
@click.option('--stock',prompt = 'Stock inicial',help = "Introducir stock actual del producto",type = int)
@click.pass_context
def nuevo_producto(context, codigo, nombre, categoria, precio, color, stock):
    producto1 = Producto(codigo, nombre, categoria, precio, color, stock)

    match producto1.categoria:
        case "camisa":
            producto1 = Camisa(
                codigo, nombre, categoria, precio, color, stock,
                float(input("Ingrese el descuento: ")),
                input("Ingrese el tipo de cuello: "),
                input("Ingrese el tipo de manga: ")
            )

        case "pantalon":
            producto1 = Pantalon(
                codigo, nombre, categoria, precio, color, stock,
                input("Ingresa el tipo : "),
                input("ingresar talla: "),
            )

    producto_controller.registrar_producto(producto1)

# Registrar Venta
@main.command()
@click.option('--codigo',prompt = 'Código del producto', help = "Introducir codigo del producto a comprar",type = click.UNPROCESSED,callback = validar_existencia)
@click.option('--cantidad',prompt = 'Cantidad de productos', help = "Introducir la cantidad del producto a comprar",type = int)
@click.pass_context
def nueva_venta(context, codigo, cantidad):
    prod = producto_controller.buscar_productos_por_codigo(codigo)

    v = Venta(prod, cantidad)
    venta_controller.registrar_venta(v)


main()
