from .producto import Producto 

class Pantalon(Producto):
    def __init__(self, codigo, nombre, categoria, precio, color, talla, tipo, stock):
        super().__init__(codigo, nombre, categoria, precio, color, stock)
        self.__talla = talla
        self.__tipo = tipo

    @property
    def talla(self):
        return self.__talla
    
    @talla.setter
    def tipo(self, talla):
        self.__talla == talla 

    @property
    def tipo(self):
        return self.__tipo
    
    @tipo.setter
    def tipo(self, tipo):
        self.__tipo == tipo

    def mensaje(self):
        print("Nuevo modelo de pantlón agregado")