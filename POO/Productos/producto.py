#Realiza un programa que registre productos
#German Garcia
# 5 de nov de 2022


class Producto:
    def __init__(self, codigo, nombre, precio):
        self.__codigo=codigo
        self.__nombre=nombre
        self.__precio=precio


    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self,valor):
        self.__codigo=valor

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,valor):
        self.__nombre=valor
    
    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self,valor):
        self.__precio=valor


    def __str__(self):
        return f"Codigo {self.__codigo}\n, Nombre {self.__nombre}\n, Precio {self.__precio}\n"
    
    def calcTotal(self, unidades):
        return "En total es: ", self.__precio*unidades

espaguetis=Producto (1, "Espaguetis", 1400)
arroz=Producto (2, "Arroz", 2300)
frijoles=Producto (3, "Frijoles", 3400)

print(espaguetis, arroz, frijoles)
print("===========Corte==========")

print(espaguetis.calcTotal(20)) 
print(arroz.calcTotal(98))
print(frijoles.calcTotal(3))



    



