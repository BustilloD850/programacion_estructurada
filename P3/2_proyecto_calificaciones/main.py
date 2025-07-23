#proyecto 3
"""
Crear un proyecto que permita gestionar (administrar) calificaciones, colocar un menu de opciones para agregar, mostrar, calcular promedio calificaciones de un estudiante.
notas:
1.- Utilizar funciones y mandar llamar desde otro archivo
2.- Utilizar list (bidimensional) para almacenar el nombre del alumno asi como sus 3 calificaciones
"""

import os
import calificaciones

if __name__ == "__main__":
    dato=True
    while dato:
        calificaciones.borrarPantalla()
        opcion = calificaciones.menu_principal()
        
        if opcion == "1":
            calificaciones.borrarPantalla()
            calificaciones.agregar_calificaciones()
            calificaciones.esperarTecla()

        if opcion == "2":
            calificaciones.borrarPantalla()
            calificaciones.mostrar_calificaciones()
            calificaciones.esperarTecla()
        
        if opcion == "3":
            calificaciones.borrarPantalla()
            calificaciones.promedio_calificaciones()
            calificaciones.esperarTecla()
            
        if opcion == "4":
                calificaciones.borrarPantalla()
                dato=False
                input("\t\U0001F6AA Terminaste la ejecucion del SW \U0001F6AA")

        else:
            calificaciones.borrarPantalla()
            input("\t\u26A0 Opcion invalida, vuelva a intentarlo por favor...")
            calificaciones.esperarTecla()