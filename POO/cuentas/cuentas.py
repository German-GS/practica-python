class Cuentas:
    def __init__(self,cantidad):
        self.__titular= []
        self.__cantidad = cantidad

    @property
    def titular(self):
        return self.__titular
    
    @titular.setter
    def titular(self):
        self.__titular=[]
    
    @property
    def cantidad(self):
        return self.__cantidad

    @cantidad.setter
    def cantidad(self, cantidad):
        self.__cantidad=cantidad
    

    def __str__(self):
        return f"{self.__titular} debe {self.__cantidad}"
    
    def regPersona (self, persona):
        self.__titular=persona

    def ingresar (self, cantidad):
        if cantidad >=0:
            self.__cantidad += cantidad
            return f"El monto es {self.__cantidad}"
        else :
            return "No se suma"

    def retirar (self, cantidad):
        self.__cantidad = self.__cantidad-cantidad
        return f"El saldo actual es {self.__cantidad}"

    

titular = 'German Garcia'

miCuenta=Cuentas(233)
miCuenta.regPersona(titular)
print (miCuenta)
print(miCuenta.ingresar(344))
print(miCuenta.retirar(23))



        