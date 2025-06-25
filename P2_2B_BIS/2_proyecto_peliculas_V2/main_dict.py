"""
Crear un proyecto que permita gestionar (administrar) peliculas, colocar numero de opciones para agregar, eliminar, modificar y consultar peliculas.
notas:
1.- Utilizar funciones y mandar llamar desde otro archivo
2.- Utilizar dict para almacenar los siguientes atributos: (nombre, categoria, clasificacion, genero) de las peliculas"""

import os
opcion=True
from peliculas import AgregarCaracteristicaPeliculas, borrarPantalla, crearPeliculas, esperarTecla, borrarPeliculas, borrarCaracteristicasPeliculas, modificarCaracteristicasPeliculas, consultarPeliculas

while opcion:
    borrarPantalla()
    print("\n\t\U0001F464 CARTELERA DE PELICULAS\U0001F464 \n 1. \U0001F4C2 Crear \n 2. \U0001F4DB Borrar \n 3. \U0001F50D Mostrar \n 4. \U0001F501 Agregar Caracteristicas \n 5. \U0001F4BE Modificar Caracteristicas \n 6. \u274C Borrar Caracteristicas \n 7. \U0001F6AA SALIR")
    opcion=input("\t Eliga una opcion: ").upper()

    match opcion:
        case"1":
            borrarPantalla()
            print("\tCrear Peliculas")
            crearPeliculas()
            esperarTecla()
        
        case"2":
            borrarPantalla()
            print("\tBorrar Peliculas")
            borrarPeliculas()
            esperarTecla()

        case"3":
            borrarPantalla()
            print("\tMostrar Peliculas")
            consultarPeliculas()
            esperarTecla()
        
        case"4":
            borrarPantalla()
            print("\tAgrgar caracteristicas de las Peliculas")
            AgregarCaracteristicaPeliculas()
            esperarTecla()

        case"5":
            borrarPantalla()
            print("\tModificar caracteristicas de las Peliculas")
            modificarCaracteristicasPeliculas()
            esperarTecla()
        case"6":
            borrarPantalla()
            print("\tBorrar caracteristicas de las Peliculas")
            borrarCaracteristicasPeliculas()
            esperarTecla()

        case"7":
            borrarPantalla()
            opcion=False
            input("\tTerminaste la ejecucion del SW")

        case _:
            borrarPantalla()
            input("\t\u26A0Opcion invalida, vuelva a intentarlo por favor...\u26A0")