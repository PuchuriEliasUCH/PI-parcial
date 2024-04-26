from .producto import Producto
from .temporada_verano import Verano


class Camisa(Producto, Verano):
    def __init__(self, codigo, nombre, categoria, precio, color, stock, descuento, cuello, manga):
        Producto.__init__(self, codigo, nombre, categoria, precio, color, stock)
        Verano.__init__(self, descuento)
        self.__cuello = cuello
        self.__manga = manga

    @property
    def cuello(self):
        return self.__cuello
    
    @cuello.setter
    def stock(self, cuello):
        self.__cuello == cuello   

    @property
    def manga(self):
        return self.__manga
    
    @manga.setter
    def manga(self, manga):
        self.__manga == manga   