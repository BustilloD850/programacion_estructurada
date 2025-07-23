#from numpy import append
import mysql.connector
from mysql.connector import Error

def borrarPantalla():
  import os  
  os.system("cls")

def esperarTecla():
  print("\U0001F552 Oprima cualquier tecla para continuar ...")
  input()

def conectar():
  try:
      conexion=mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="bd_calificaciones"
      )
      return conexion
  except Error as e:
    print(f"El error que sucedio es: {e}")
    esperarTecla()
    return None

def agregar_calificaciones():
  borrarPantalla()
  conexionBD=conectar()
  if conexionBD is not None:
    print("\t\U0001F4C2 Agregar Calificaciónes \U0001F4C2")
    nombre=input("\t\t\U0001F464 Nombre del alumno: ").upper().strip()
    calificaciones=[]
    for i in range(1, 4):
      while True:
        try:
          cal=float(input(f"\t\t📝 Calificacion {i}: "))
          if 0 <= cal <= 10:
            calificaciones.append(cal)
            break
          else:
            print("\t\u274C Ingresa un número válido entre 0 y 10.")
        except ValueError:
          print("\t\u274C Ingresa un valor numérico válido.")
    
    try:
      cursor = conexionBD.cursor()
      sql = "INSERT INTO calificacion (alumno, calificacion1, calificacion2, calificacion3) VALUES (%s, %s, %s, %s)"
      valores = (nombre, calificaciones[0], calificaciones[1], calificaciones[2])
      cursor.execute(sql, valores)
      conexionBD.commit()
      print(f"\t\U0001F389 Registro insertado con éxito \U0001F389")
    except Error as e:
      print(f"❌ Error al insertar registro: {e}")
      esperarTecla()

def mostrar_calificaciones():
  borrarPantalla()
  conexionBD=conectar()
  if conexionBD!=None:
    print("\n\t.:: \U0001F50D Consultar o Mostrar calificaciones \U0001F50D ::.\n ")
    cursor=conexionBD.cursor()
    sql="select * from calificacion"
    cursor.execute(sql)
    registros=cursor.fetchall()
    if registros:
      print(f"\n\tMostrar Calificaciones")
      print(f"{'ID':<10}{'alumno':<15}{'calificacion1':<15}{'calificacion2':<15}{'calificacion3':<15}")
      print(f"-"*70)
      for fila in registros:
        print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}")
        print(f"-"*70)
    else:
      print("\t .:: \u26A0 No hay calificaciones en el sistema \u26A0 ::.")
      esperarTecla() 

def promedio_calificaciones():
  borrarPantalla()
  conexionBD=conectar()
  if conexionBD!=None:
    print("\t\U0001F4BE Calificacion Promedio \U0001F4BE")
    cursor=conexionBD.cursor()
    sql="SELECT alumno, calificacion1, calificacion2, calificacion3 FROM calificacion"
    cursor.execute(sql)
    lista = cursor.fetchall()
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