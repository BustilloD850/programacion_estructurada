#proyecto 3
"""
Crear un proyecto que permita gestionar (administrar) calificaciones, colocar un menu de opciones para agregar, mostrar, calcular promedio calificaciones de un estudiante.
notas:
1.- Utilizar funciones y mandar llamar desde otro archivo
2.- Utilizar list (bidimensional) para almacenar el nombre del alumno asi como sus 3 calificaciones
"""

import os
import calificaciones

def main():
    datos=[]
    opcion=True
    
    while opcion:
        calificaciones.borrarPantalla()
        opcion=calificaciones.menu_principal()
        
        match opcion:
            case "1":
                calificaciones.borrarPantalla()
                calificaciones.agregar_calificaciones(datos)
                calificaciones.esperarTecla()
        
            case "2":
                calificaciones.borrarPantalla()
                calificaciones.mostrar_calificaciones(datos)
                calificaciones.esperarTecla()

            case"3":
                calificaciones.borrarPantalla()
                calificaciones.promedio_calificaciones(datos)
                calificaciones.esperarTecla()
                
            case"4":
                calificaciones.borrarPantalla()
                opcion=False
                input("\t\U0001F6AA Terminaste la ejecucion del SW \U0001F6AA")

            case _:
                calificaciones.borrarPantalla()
                input("\t\u26A0 Opcion invalida, vuelva a intentarlo por favor...")

if __name__ == "__main__":
    main()