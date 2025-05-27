"""
  Una función es un conjunto de instrucciones agrupadas bajo un nombre en particular como un programa mas pequeño que cumple una funcion especifica. La funcion se puede reutulizar con el simple hecho de invocarla es decir mandarla llamar 

  Sintaxis:

   def nombredeMifuncion(parametros):
      bloque o conjunto de instrucciones

   nombredeMifuncion(parametros)

   Las funciones pueden ser de 4 tipos
  
    Funciones de tipo "Procedimiento" 
   1.- Funcion que no recibe parametros y no regresa valor
   3.- Funcion que recibe parametros y no regresa valor
    
    Funciones de tipo "Funcion"
   2.- Funcion que no recibe parametros y regresa valor
   4.- Funcion que recibe parametros y regresa valor

"""

#1.- Funcion que no recibe parametros y no regresa valor
def SolicitarDatos1():
    nombre=input("Nombre: ")
    telefono=input("Telefono: ")
    print(f"soy funcion 1 \n el nombre es: {nombre} y su telefono es: {telefono}")

#3.- Funcion que recibe parametros y no regresa valor
def SolicitarDatos3(nombre,telefono):
    nom=nombre
    tel=telefono
    print(f"soy funcion 3 \n el nombre es: {nom} y su telefono es: {tel}")

#2.- Funcion que no recibe parametros y regresa valor
def SolicitarDatos2():
    nombre=input("Nombre: ")
    telefono=input("Telefono: ")
    return f"soy funcion 2 \n el nombre es: {nombre} y su telefono es: {telefono}"

#4.- Funcion que recibe parametros y regresa valor
def solicitarDatos4(nombre,telefono):
    nom=nombre
    tel=telefono
    return "soy funcion 1 \n",nom,tel

#llamar mis funciones
SolicitarDatos1()

nombre=input("Nombre: ")
telefono=input("Telefono: ")
SolicitarDatos3(nombre,telefono)

nom2,tel2=SolicitarDatos2()
print(f"Nombre: {nom2} \n Telefono: {tel2}")

nom4=input("Nombre: ")
tel4=input("Telefono: ")
nombre4,telefono4=solicitarDatos4(nom4,tel4)
print(f"Nombre: {nombre4} \n Telefono: {telefono4}")