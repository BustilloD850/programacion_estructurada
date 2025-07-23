import os
#Ejemplo 1 Crear una lista de numeros e imprimir el contenido
#numeros=[23,45,56,78]

#print(numeros)

#for i in numeros:
#    print (i)

#for i in range(0, len(numeros)):
#    print(numeros[i])
#os.system("cls")

#Ejemplo 2 crear una lista de palabras y posteriormente buscar la coincidencia de una palabra

#palabras=["Hola","mes","2024","saludo","mes"]
#print(palabras)
#palabras[0]="Hola"
#palabras[1]="mes"
#palabras[2]="2024"
#palabras[3]="saludo"

#palabra_buscar=input("Dame la palabra a buscar: ")

#1ra forma
#if palabra_buscar in palabras:
#    print(f"Si encontro la palabra")
#    print(f"El numero de veces que se encontro la palabra es: {palabras.cout(palabra_buscar)}")
#else:
#    print(f"No encontro la palabra")

#2da forma
#for i in palabras:
#    if i==palabra_buscar:
#        encontro=True

#if encontro:
#    print(f"Si encontro la palabra")
#else:
#    print(f"No encontro la palabra")

#3ra forma
#encontro=False
#for i in range(0, len(palabras)):
#    if palabras[i]==palabra_buscar:
#        encontro=True
    
#if encontro:
#    print(f"Si encontro la palabra")
#else:
#    print(f"No encontro la palabra")

#input("Oprima tecla...")

#Ejemplo 3 Añadir elementos a una lista

os.system("cls")
#numeros=[]
#print(numeros)

#opc=True
#while opc:
#    numero=float(input("Dame un numero entero o decimal: "))
#    numeros.append(numero)
#    resp=input("¿Deseas agregar otro numero?").lower()
#    if resp=="si":
#        opc=True
#    else:
#        opc=False

#print(numeros)
#input("Oprima tecla...")

#Ejemplo 4 Crear una lista multidimensional que sea una agenda

agenda=[
        ["Carlos","6181234567"],
        ["Alberto","6671234567"],
        ["Martin","6785678923"]
    ]

print(agenda)

for i in agenda:
    print(i)

cadena=""
for r in range(0,3):
    for c in range(0,2):
        #print(agenda[r][c])
        cadena+=f"{agenda[r][c]} "
    cadena+="\n"
print(cadena)