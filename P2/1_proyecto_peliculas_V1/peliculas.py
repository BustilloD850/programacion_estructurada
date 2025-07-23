peliculas=[]

def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    print("Oprima cualquier letra para continuar...")
    input()

def agregarPeliculas():
    borrarPantalla()
    print("Alta de peliculas")
    pelicula=input("Ingresa el nombre: ")
    peliculas.append(pelicula)

def eliminarPeliculas():
    borrarPantalla()
    print("Eliminar pelicula")
    pelicula=input("Ingresa el nombre: ")
    peliculas.pop(pelicula)

def buscarPeliculas():
    buscar=input("Nombre de pelicula:")
    for i in range(0,len(peliculas)):
        if peliculas[i]== buscar:
            print("Pelicula disponible")
        else:
            print("pelicula No disponible")

def vaciarPeliculas():
    borrarPantalla()
    print("Vaciar lista de peliculas")
    peliculas.clear()

def consultarPeliculas():
    borrarPantalla()
    print("consultar las peliculas")
    busqueda=input(f"pelicula a buscar: ")
    if busqueda in peliculas:
        print("Pelicula disponible")
    else:
        print("Pelicula no disponible")

def modificarPeliculas():
    borrarPantalla()
    print("Modificar lista de peliculas")
    posicion=int(input("eliga la pelicula a modificar (considera el 0 como primer inciso)"))
    peliculas[posicion]= input("pelicula a cambiar")