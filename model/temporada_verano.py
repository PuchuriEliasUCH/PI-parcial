class Verano:
    def __init__(self, descuento):
        self.__descuento = descuento

    @property
    def descuento(self):
        return self.__descuento
    
    @descuento.setter
    def descuento(self, descuento):
        self.__descuento == descuento   