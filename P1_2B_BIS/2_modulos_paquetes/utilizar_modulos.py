#1er utilizar los modulos
import modulos
modulos.borrarPantalla
print(modulos.saludar("Bustillo Aguirre Diego Alberto"))

#2da forma de utilizar modulos
from modulos import saludar,borrarPantalla
borrarPantalla()
print(saludar("Daniel Contreras Renecio"))

nombre=input("Ingresa el nombre del contacto: ")
telefono=input("Ingresa su numero de telefono con clave lada: ")
nom,tel=modulos.solicitarDatos4(nombre,telefono)
print(f"\t Nombre Completo: {nom}\nTelefono: {tel}")