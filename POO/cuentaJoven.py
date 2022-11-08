from personas import Personas

class CuentaJoven(Personas):
    def __init__(self, titular,cantidad, bonificacion):
        self.__titular=titular
        self.__cantidad=cantidad
        self.__bonificacion=bonificacion

@property
def titular(self):
    return self.__titular
@titular.setter
def titular(self, valor):
    self.__titular=valor

###########################

@property
def cantidad(self):
    return self.__cantidad

@cantidad.setter
def cantidad(self, valor):
    self.__cantidad=valor

###########################

@property
def bonificacion(self):
    return self.__bonificacion

@bonificacion.setter
def bonificacion(self, valor):
    self.__bonificacion=valor

############################

def esTitularValido(self):
    edad = Personas.enviarEdad()
    if edad >=18 and edad <= 25:
        return True
    else:
        return False


    

nuevoJoven=CuentaJoven("German", 2333, 23)
print(esTitularValido)