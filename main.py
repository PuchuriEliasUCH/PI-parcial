from model.venta import Venta
from model.pantalon import Pantalon
from model.producto import Producto
from model.camisa import Camisa
from model.temporada_verano import Verano
from controller import producto_controller

# producto1 = Producto(
#     input("ingresar codigo: "),
#     input("ingresar nombre: "),
#     input("ingresar categoria: "),
#     float(input("ingresar precio: ")),
#     input("ingresar color: "),
#     int(input("ingresar stock: "))
# )
#
# match producto1.categoria:
#     case "camisa":
#         producto1 = Camisa(
#             producto1.codigo,
#             producto1.nombre,
#             producto1.categoria,
#             producto1.precio,
#             producto1.color,
#             producto1.stock,
#             float(input("ingresar descuento: ")),
#             input("ingresar cuello: "),
#             input("ingresar manga: ")
#         )
#
#     case "pantalon":
#         producto1 = Pantalon(
#             producto1.codigo,
#             producto1.nombre,
#             producto1.categoria,
#             producto1.precio,
#             producto1.color,
#             producto1.stock,
#             input("ingresar tipo: "),
#             input("ingresar talla: "),
#         )
#
#
# producto_controller.registrar_producto(producto1)
# producto_controller.listar_categoria(input("Ingresar categoria: "))
producto_controller.listar_productos()