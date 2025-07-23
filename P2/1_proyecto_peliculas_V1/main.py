"""
Crear un proyecto que permita gestionar (administrar) peliculas, colocar numero de opciones para agregar, eliminar, modificar y consultar peliculas.
notas:
1.- Utilizar funciones y mandar llamar desde otro archivo
2.- Utilizar listas para almacenar los nombres de peliculas"""

import os
opcion=True
from peliculas import agregarPeliculas, borrarPantalla, buscarPeliculas,consultarPeliculas, eliminarPeliculas, esperarTecla, modificarPeliculas, peliculas, vaciarPeliculas

while opcion:
    borrarPantalla()
    print("\n\t CARTELERA DE PELICULAS \n 1. Agregar \n 2. Eliminar \n 3. Modificar \n 4. Consultar \n 5. Buscar \n 6. Vaciar \n 7. SALIR")
    opcion=input("\t Eliga una opcion: ").upper()

    match opcion:
        case"1":
            borrarPantalla()
            print("\tAgregar Peliculas")
            agregarPeliculas()
            esperarTecla()
        
        case"2":
            borrarPantalla()
            print("Eliminar Peliculas")
            eliminarPeliculas()
            esperarTecla()

        case"3":
            borrarPantalla()
            print("Modificar Peliculas")
            modificarPeliculas()
            esperarTecla()
        
        case"4":
            borrarPantalla()
            print("Consultar Peliculas")
            consultarPeliculas()
            esperarTecla()

        case"5":
            borrarPantalla()
            print("Buscar Peliculas")
            buscarPeliculas()
            esperarTecla()
        case"6":
            borrarPantalla()
            print("Vaciar Peliculas")
            vaciarPeliculas()
            esperarTecla()

        case"7":
            borrarPantalla()
            opcion=False
            input("Terminaste la ejecucion del SW")

        case _:
            borrarPantalla()
            input("Opcion invalida, vuelva a intentarlo por favor...")