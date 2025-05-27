'''Crear un programa que calcule e imprima cualquier tabla de multiplicar
con funciones que regresen valor y parametro
'''

#mult=int(input("Numero de la tabla a multiplicar: "))
#m1=1*mult
#print(f"{mult}x1= {m1}")
#m2=2*mult
#print(f"{mult}x2= {m2}")
#m3=3*mult
#print(f"{mult}x3= {m3}")
#m4=4*mult
#print(f"{mult}x4= {m4}")
#m5=5*mult
#print(f"{mult}x5= {m5}")
#m6=6*mult
#print(f"{mult}x6= {m6}")
#m7=7*mult
#print(f"{mult}x7= {m7}")
#m8=8*mult
#print(f"{mult}x8= {m8}")
#m9=9*mult
#print(f"{mult}x9= {m9}")
#m10=10*mult
#print(f"{mult}x10= {m10}")

#version2
#i=1
#mult=int(input("Numero de la tabla a multiplicar: "))
#while i<=10:
#    m=i*mult
#    print(f"{mult}x{i}= {m}")
#    i+=1

#version3
def multiplicacion(num):
    numero=num
    respuesta=""
    for i in range(1,11):
        multi=numero*i
        respuesta+=f"\t{num} x {i} = {multi}\n"
    return respuesta

numero=int(input("Dame el numero de la tabla a multiplicar a calcular: "))
print(f"tabla de multiplicar del numero {numero}")
resultado=multiplicacion(numero)
print(f"{resultado}")