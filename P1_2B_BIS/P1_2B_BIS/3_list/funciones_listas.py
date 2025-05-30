"""
List(Array)
son colecciones o conjunto de datos/valores bajo un mismo nombre, para acceder a los valores se hace con un indice numerico

Nota: sus valores si son modificables

La lista es una coleccion ordenada y modificable.
Permite miembros duplicados.
"""
import os
os.system("cls")
#Funciones más comunes en las listas

paises=["Mexico","Brasil","España","Canada"]

numeros=[23,12,100,34]

#Ordenar ascendentemente
print (numeros)
numeros.sort()
print(numeros)

print(paises)
paises.sort()
print(paises)

#Añadir o Ingresar o Insertar elementos a una lista

#1er forma
print(paises)
paises.append("Honduras")

#2da forma
paises.insert(1,"Honduras")
print(paises)

#Eliminar o Borrar o Quitar elementos de una lista

#1er forma con el indice
paises.pop(1)
print(paises)

#2da forma forma con el valor
paises.remove("Honduras")
print(paises)

#Buscar un elemento dentro de la lista

#1ra forma
resp="Brasil" in paises
if resp:
    print("Si encontre el pais")
else:
    print("No encontre el pais")

#2da forma
for i in range(0,len(paises)):
    if paises[i]== "Brasil":
        print("Si encontre el pais")
    else:
        print("No encontre el pais")

#Cuantas veces aparece un elemento dentro de una lista
print(f"este numero 12 aparece: {numeros.count(12)} vez o veces")

numeros.append(12)
print(f"este numero 12 aparece: {numeros.count(12)} vez o veces")

#Identificar o conocer el indice de un valor

indice=paises.index("España")
print(indice)
paises.pop(indice)
print(paises)

#Recorrer los valores de la lista

#1er forma con los valores
for i in paises:
    print(i)

#2da forma con los indices
for i in range(0,len(paises)):
    print(f"El valor {i} es: {paises[i]}")

#Unir contenido de listas

print(paises)
print (numeros)
paises.extend(numeros)
print(paises)