class Personas:
    def __init__(self, nombre, edad, dni):
        self.__nombre=nombre
        self.__edad=edad
        self.__dni=dni
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, valor):
        self.__nombre=valor
    
#######################
    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, valor):
        self.__edad=valor
#######################
    @property
    def dni(self):
        return self.__dni
    @dni.setter
    def dni(self,valor):
        self.__dni=valor

    def __str__(self):
        return f"La persona numero {self.__dni}, y nombre {self.__nombre}, con edad {self.__edad} "

    def valEdad(self):
        if self.__edad>=18:
            return "Es mayor de edad"
        else:
            return "Es menor de edad"


miPersona = Personas("Ana", 23, 2033304)
print(miPersona)
print (miPersona.valEdad())
