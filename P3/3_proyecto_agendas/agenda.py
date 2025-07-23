import mysql.connector
from mysql.connector import Error

def borrarPantalla():
  import os  
  os.system("cls")

def esperarTecla():
  input("\n \U0001F552 \t ...Oprima cualquier tecla para continuar \U0001F552...")  

def conectar():
  try:
      conexion=mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="bd_agenda"
      )
      return conexion
  except Error as e:
    print(f"El error que sucedio es: {e}")
    return None

def menu_principal():
  print("\t\t  📆..::: Sistema de Gestión de Gestión de Agenda de contactos :::... 📆\n\t\t\t1️⃣  Agregar contacto  \n\t\t\t2️⃣  Mostrar todos los contactos  \n\t\t\t3️⃣  Buscar contacto por nombre \n\t\t\t4️⃣  Modificar Contactos  \n\t\t\t5️⃣  Elimminar Contactos  \n\t\t\t6️⃣  SALIR  ")
  opcion=input("\t\t\t 👉 Elige una opción (1-6): ").upper()
  return opcion

def agregar_contacto(agenda):
  borrarPantalla()
  conexionBD=conectar()
  if conexionBD!=None:
    print("\n\t\t.:: Agregar Contactos ::.")
    nombre=input("Nombre del contacto: ").upper().strip()

    if nombre in agenda: #SOLO EN DICCIONARIO FUNCIONA
      print("\n\t\t*️⃣ El contacto ya existe...")
    else:
        telefono=input("Telefono: ").strip()
        email=input("E-mail: ").lower().strip()
        #Agregar el atributo "nombre" al dict con los valores de tel y email en una listas
        agenda[nombre]=[telefono,email]
        print("\n\t\t.::✅Accion realizada con exito✅::.")
    
        ###### AGREGAR REGISTRO A LA BD
    try:
      cursor=conexionBD.cursor()
      sql="insert into agenda (nombre,telefono,email) values (%s,%s,%s)"
      val=(nombre,telefono,email)
      cursor.execute(sql,val)
      conexionBD.commit()
      print("\n\t\t ::: \u2705 ¡LA OPERACION SE REALIZO CON EXÍTO! \u2705 :::")
    except Error as e:
      print(f"Error al intentar insertar un registro en la BD: {e}")

def mostrar_contacto(agenda):
  borrarPantalla()
  print("\n\t\t .:: Mostrar Contactos ::.")
  if not agenda:
    print("\n\t\t❌  No hay contactos")
  else:
    for nombre,datos in agenda.items():
      print(f"\n\t{'Nombre: '+nombre}\n\t{'Telefono: '+datos[0]}\n\t{'E-mail:'+datos[1]}")

def buscar_contacto(agenda):
    borrarPantalla()
    conexionBD=conectar()
    if conexionBD!=None:
      print("\n\t\t.::🔍  Buscar Contacto  🔍::.")
      cursor=conexionBD.cursor()
      nombre=input("Ingrese el nombre del contacto a buscar: ").upper().strip()
      sql="select * from agenda where nombre=%s"
      val=(nombre,)
      cursor.execute(sql,val)
      registros=cursor.fetchall()
      if registros:
        print("\n\t Contacto Encontrado!")
        print(f"{'ID':<10}{'Nombre':<15}{'Telefono':<15}{'Email':<15}")
        print(f"-"*60)
      for fila in registros:
        print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}")
        print(f"-"*60)
    else:
      print("\n\t\tNo se encontró el contacto.")

def eliminar_contacto():
    borrarPantalla()
    conexionBD=conectar()
    if conexionBD!=None:
      print("\n\t\t.::🆑  Eliminar Contacto  🆑::.")
      cursor=conexionBD.cursor()
      nombre = input("Ingrese el nombre del contacto a eliminar: ").upper().strip()
      sql="select * from agenda where nombre=%s"
      val=(nombre,)
      cursor.execute(sql,val)
      registros=cursor.fetchall()
      if registros:
         print("\n\t.::Contactos::.")
         print(f"{'ID':<10}{'Nombre':<15}{'Telefono':<15}{'Email':<15}")
         print(f"-"*60)
         for fila in registros:
          print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}")
          print(f"-"*60)
          resp=input(f"¿Deseas borrar al contacto {nombre}? (Si/No)").lower().strip()
         if resp== "si":
          sql="delete from agenda where nombre=%s"
          val(nombre,)
          cursor.execute(sql,val)
          conexionBD.commit()
          print("\n\t\t ::: \u2705 ¡LA OPERACION SE REALIZO CON EXÍTO! \u2705 :::")
      else:
          print("\n\t\t❌  No se encontró el contacto para eliminar.")

def modificar_contacto(agenda):
    borrarPantalla()
    conexionBD=conectar()
    if conexionBD!= None:
      print("\n\t\t.:: Modificar Contacto ::.")
      cursor=conexionBD.cursor()
      nombre = input("Ingrese el nombre del contacto a modificar: ").upper().strip()
      sql="select * from agenda where nombre=%s"
      val=(nombre,)
      cursor.execute(sql,val)
      registros=cursor.fetchall()
    if registros:
        print("\n\t .::Contactos::.")
        print(f"{'ID':<10}{'Nombre':<15}{'Telefono':<15}{'Email':<15}")
        print(f"-"*60)
        for fila in registros:
           print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}")
           print(f"-"*60)
           resp=input(f"¿Deseas modificar la informacion de {nombre}? (Si/No)")
           if resp=="si":
             agenda["nombre"]=input("\U0001F4DD nombre: ").upper().strip()
             agenda["telefono"]=int(input("\U0001F4DD telefono: ")).upper().strip()
             agenda["email"]=input("\U0001F4DD email: ").upper().strip()
             sql="update agenda set nombre=%s, telefono=%s, email=%s where nombre=%s"
             val=(agenda["nombre"],agenda["telefono"],agenda["email"])
             cursor.execute(sql,val)
             conexionBD.commit()
             print("\n\t\t ::: \u2705 ¡LA OPERACION SE REALIZO CON EXÍTO! \u2705 :::")
        else:
          print("\t .:: \u26A0 La pelicula a modificar no se encuentra \u26A0 ::.")