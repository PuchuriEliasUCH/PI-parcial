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

    # Métodos personalizados

    # Calcular subtotal de la venta
    def subtotal(self):
        return self.__producto[0]['precio'] * self.__cantidad

    # Calcular IGV
    def aplicar_impuesto(self):
        return round(self.subtotal() * 0.18, 2)

    # Calcular importe total de la venta
    def total(self):
        return self.subtotal() + self.aplicar_impuesto()