class Venta:
    def __init__(self, producto, cantidad):
        self.__producto = producto
        self.__cantidad = cantidad
    
    @property
    def cantidad(self):
        return self.__cantidad
    
    @cantidad.setter
    def cantidad(self, cantidad):
        self.__cantidad == cantidad
    
    @property
    def producto(self):
        return self.__producto
    
    @producto.setter
    def producto(self, producto):
        self.__producto == producto