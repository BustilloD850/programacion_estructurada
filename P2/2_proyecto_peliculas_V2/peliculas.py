pelicula=[]

def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    print("\t\U0001F501 Oprima cualquier letra para continuar... \U0001F501")
    input()

def crearPeliculas():
  borrarPantalla()
  print(".:: Alta de Peliculas ::.\n ")
  pelicula.update({"nombre":input("Ingrese  el nommbre: ").upper().strip()})
  pelicula.update({"categoria":input("Ingrese  la categoria: ").upper().strip()})
  pelicula.update({"clasificacion":input("Ingrese  la clasificación : ").upper().strip()})
  pelicula.update({"genero":input("Ingrese el genero: ").upper().strip()})
  pelicula.update({"idioma":input("Ingrese el idioma: ").upper().strip()})
  print("\n\t\t \u2705 ¡LA OPERACION SE REALIZO CON EXITO! \u2705")
  esperarTecla()
  borrarPantalla()

def borrarPeliculas():
    borrarPantalla()
    print("\t\U0001F4DBEliminar pelicula\U0001F4DB")
    peliculas=input("Ingresa el nombre: ")
    pelicula.pop(pelicula)
    print("\n\t\t \u2705 ¡LA OPERACION SE REALIZO CON EXITO! \u2705")
    esperarTecla()
    borrarPantalla()

def buscarPeliculas():
    buscar=input("\t\U0001F50DNombre de pelicula\U0001F50D:")
    for i in range(0,len(pelicula)):
        if pelicula[i]== buscar:
            print("\t\u2705Pelicula disponible\u2705")
            print("\n\t\t \u2705 ¡LA OPERACION SE REALIZO CON EXITO! \u2705")
            esperarTecla()
            borrarPantalla()
        else:
            print("\t\u274Cpelicula No disponible\u274C")

def vaciarPeliculas():
    borrarPantalla()
    print("\t\U0001F4C2Vaciar lista de peliculas\U0001F4C2")
    pelicula.clear()
    print("\n\t\t \u2705 ¡LA OPERACION SE REALIZO CON EXITO! \u2705")
    esperarTecla()
    borrarPantalla()

def consultarPeliculas():
    borrarPantalla()
    print("\t\U0001F4C2consultar las peliculas\U0001F4C2")
    busqueda=input(f"pelicula a buscar: ")
    if busqueda in pelicula:
        print("\t\u2705Pelicula disponible\u2705")
        print("\n\t\t \u2705 ¡LA OPERACION SE REALIZO CON EXITO! \u2705")
        esperarTecla()
        borrarPantalla()
    else:
        print("\t\u274Cpelicula No disponible\u274C")
        esperarTecla()

def modificarPeliculas():
    borrarPantalla()
    print("\t\U0001F501Modificar lista de peliculas\U0001F501")
    posicion=int(input("eliga la pelicula a modificar (considera el 0 como primer inciso)"))
    pelicula[posicion]= input("pelicula a cambiar")

def modificarCaracteristicasPeliculas():
    borrarPantalla()
    print(f"\n\t \U0001F501 Modificar Caracteristicas a Peliculas \U0001F501 \n")
    if len(pelicula)>0:
        print("\n\t Valor actuales: \n")
        for i in pelicula:
            print(f"\t {(i)} : {pelicula[i]}")
            resp=input(f"\t ¿Deseas cambiar el valor de {i}? (Si/No)")
            if resp=="si":
                pelicula.update({f"{i}":input("\t\U0001f501 el nuevo valor: ").upper().strip()})
                print("\n\t\t \u2705 ¡LA OPERACION SE REALIZO CON EXITO! \u2705")
                esperarTecla()
                borrarPantalla()
            else:
                print("\t\u26A0 No hay peliculas en Sistema \u26a0")
                esperarTecla()

def borrarCaracteristicasPeliculas():
    borrarPantalla()
    print("\n\t \U0001F4DB Borrar Caracteristicas a Peliculas \U0001F4DB \n")
    if len(pelicula)>0:
        print(f"\n\t Valor actuales: \n")
        for i in pelicula:
            print(f"\t {(i)} : {pelicula[i]}")
            resp=input(f"\t ¿Deseas borrar una caracteristica? (Si/No) ")
            if resp=="si":
                atributo=input("Escribe la caracteristica que deseas borrar o quitar: ")
                pelicula.pop(atributo)
                print("\n\t\t \u2705 ¡LA OPERACION SE REALIZO CON EXITO! \u2705")
                esperarTecla()
                borrarPantalla()
            else:
                print("\t\u26A0 No hay peliculas en Sistema \u26a0")
                esperarTecla()

def AgregarCaracteristicaPeliculas():
    borrarPantalla()
    print(f"\n\t \U0001F4DD Añadir Caracteristicas a Peliculas \U0001F4DD \n")
    if len(pelicula)>0:
        print("\n\t Valor actuales: \n")
        for i in pelicula:
            print(f"\t {(i)} : {pelicula[i]}")
            resp=input(f"\t ¿Deseas añadir una nueva categoria en {i}? (Si/No)")
            if resp=="si":
                pelicula.append({f"{i}":input("\t\U0001f501 nueva categoria: ").upper().strip()})
                print("\n\t\t \u2705 ¡LA OPERACION SE REALIZO CON EXITO! \u2705")
                esperarTecla()
                borrarPantalla()
            else:
                print("\t\u26A0 No hay peliculas en Sistema \u26a0")
                esperarTecla()