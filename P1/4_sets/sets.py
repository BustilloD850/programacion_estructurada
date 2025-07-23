"""
Sets.
Es una coleccion de datos para tener una coleccion de valores pero no tiene indice ni orden

Set es una coleccion desordenada, inmutable* y no indexada
#No hay miembros duplicados.#
"""
import os
os.system("cls")

personas={"Ramiro","Choche","Lupe"}
print(personas)
personas.add("Choche") #añada un dato
print(personas)
#personas.pop() #borra al ultimo
#print(personas)
#personas.clear() #limpia todo el set
#print(personas)

varios={3.12,3,True,"Hola"}
print(varios)

#Ejemplo Crear un programa que solicita los emails de los alumnos de la UTD, almacenar en una lista y posteriormente mostrar en pantalla los emails sin duplicados

os.system("cls")

opc="si"
emails=[]
while opc=="si":
    emails.append(input("Dame el email "))
    #print(emails)
    opc=input("¿Desea solicitar otro email (si/no)?").lower()

#imprimir los emails sin duplicados

print(emails)