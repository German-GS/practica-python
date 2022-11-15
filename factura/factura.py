class Factura:
    def __init__(self, monto, productos, fecha):
        self.__monto = monto
        self.__productos =productos
        self.__fecha=fecha

    
    @property
    def monto(self):
        return self.__monto

    @monto.setter
    def monto(self, monto):
        self.__monto=monto
#================================
    @property
    def productos(self):
        return self.__productos

    @productos.setter
    def productos(self, productos):
        self.__productos=productos

#================================

    @property
    def fecha(self):
        return self.__fecha
    
    @fecha.setter
    def fecha(self, fecha):
        self.__fecha=fecha

    def __str__(self):
        return ""
    
    
        
        