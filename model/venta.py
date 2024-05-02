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

    def subtotal(self):
        return self.__producto[0]['precio'] * self.__cantidad
    def aplicar_impuesto(self):
        return self.subtotal() * 0.18

    def total(self):
        return self.subtotal() + self.aplicar_impuesto()