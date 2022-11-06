#Pedir al usuario los numero de la loteria y almacenarlos y luego mostrarlos en orden acendente
#German Garcia Siles
#5 de nov

numLote=[]
num=int(input("Cuantos numeros desea ingresar: "))

while True:
    nums = int(input("Ingrese el numero de la loteria: "))
    numLote.append(nums)

    if len(numLote) == num:
        break

for i in range(len(numLote)):
    numLote.sort() #Ordena una lista mutandola es decir si no se mete parameto de menor a menor 
    print(numLote[i])




