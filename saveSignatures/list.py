#Pedir una asignatura y la nota y guardarla en un array
#German Garcia 
#5 de nov




notas=[]
signatures=[]
cantMat= int(input("Cuantas materias desea ingresar"))

while True:
    signature= input("Ingrese la materia: ")
    signatures.append(signature)

    if len(signatures)==cantMat:
        break


for i in range(len(signatures)):
    nota = int(input(f"Que nota saco en {signatures[i]}: "))
    notas.append(nota)

for i in range(len(signatures)):
    print (f"Se saco {notas[i]} en {signatures[i]}")

