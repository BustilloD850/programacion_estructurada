#from numpy import append

def borrarPantalla():
  import os  
  os.system("cls")

def esperarTecla():
  print("\U0001F552 Oprima cualquier tecla para continuar ...")
  input()

def agregar_calificaciones(lista):
  borrarPantalla()
  print("\t\U0001F4C2 Agregar Calificaciónes \U0001F4C2")
  nombre=input("\t\t\U0001F464 Nombre del alumno: ").upper().strip()
  calificaciones=[]
  for i in range (1,4):
    continua=True
    while continua:
      try:
        cal=float(input(f"\t\t\U0001F4DD Calificacion {i}: "))
        if cal>=0 and cal<11:
          calificaciones.append(cal)
          continua=False
        else:
          print("\t\u274C Ingresa un número valido")
      except ValueError:
        print("\t\u274C Ingresa un valor númerico")
  lista.append([nombre]+calificaciones)
  print(f"\t\U0001F389 Acción realizada con exíto \U0001F389")

def mostrar_calificaciones(lista):
  borrarPantalla()
  print("\t\U0001F4E7 Mostrar Calificaciones \U0001F4E7")
  if len(lista)>0:
    print(f"{'📝 Nombre':<10}{'📝 Calif 1':<10}{'📝 Calif 2':<10}{'📝 Calif 3':<10}")
    print(f"{'-'*40}")
    for fila in lista:
      print(f"{fila[0]:<15}{fila[1]:<10}{fila[2]:<10}{fila[3]:<10} ")
    print(f"{'-'*40}")
    cuantos=len(lista)
    print(f"\t\U0001F4E7 Son {cuantos} alumnos")
  else:
    print("\t\u274C No hay calificaciones registradas en el sistema \u274C")

def promedio_calificaciones(lista):
  borrarPantalla()
  print("\t\U0001F4BE Calificacion Promedio \U0001F4BE")
  if len(lista)>0:
      print(f"{'👤 Alumno':<15}{'📝 Promedio':<10}")
      print(f"{'-'*30}")
      promedio_grupal=0
      for fila in lista:
        nombre=fila[0]
        promedio=sum(fila[1:])/3
        print(f"{nombre:<15}{promedio:.2f}")
        promedio_grupal+=promedio
      print(f"{'-'*30}")
      promedio_grupal=promedio_grupal/len(lista)
      print(f"\t\U0001F4E7  El promedio grupal es: {promedio_grupal}")
  else:
    print("\t\u274C No hay calificaciones registradas en el sistema \u274C")

def menu_principal():
  print("\n\t\t\U0001F464 Sistema de Gestion de Calificaciones \U0001F464 \n\t\t\t 1. \U0001F4C2 Agregar Calificaciones \n\t\t\t 2. \U0001F4E7 Mostrar Calificaciones \n\t\t\t 3. \U0001F50D Calcular Promedio \n\t\t\t 4. \U0001F6AA SALIR")
  opcion=input("\t\t\t\U0001F4DD Eliga una opcion (1-4): ").upper()
  return opcion