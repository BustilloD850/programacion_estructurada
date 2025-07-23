import peliculas_BD

opcion=True
while opcion:
    peliculas_BD.borrarPantalla()
    print("\n\t\t\t..::: CINEPOLIS CLON :::... \n\t\t..::: Sistema de Gestión de Peliculas :::...\n\t\t 1.- Crear  \n\t\t 2.- Borrar \n\t\t 3.- Mostrar \n\t\t 4.- Modificar \n\t\t 5.- Buscar \n\t\t 6.- SALIR ")
    opcion=input("\t Elige una opción: ").upper()

    match opcion:
        case "1":
            peliculas_BD.crearPeliculas()
            peliculas_BD.esperarTecla()
        case "2":
            peliculas_BD.borrarPeliculas()
            peliculas_BD.esperarTecla()
        case "3":
            peliculas_BD.mostrarPeliculas()
            peliculas_BD.esperarTecla()
                
        case "4":
            peliculas_BD.modificarPeliculas()
            peliculas_BD.esperarTecla()
        case "5":
            peliculas_BD.buscarPeliculas()
            peliculas_BD.esperarTecla()
        case "6":
            opcion=False   
            peliculas_BD.borrarPantalla() 
            print("\n\tTerminaste la ejecucion del SW")
        case _:
             
            input("\n\tOpción invalida vuelva a intentarlo ... por favor")