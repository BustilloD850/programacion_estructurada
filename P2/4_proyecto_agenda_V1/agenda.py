def borrarPantalla():
  import os  
  os.system("cls")

def esperarTecla():
  input("\n \U0001F552 \t ...Oprima cualquier tecla para continuar \U0001F552...")  

def menu_principal():
  print("\t\t  📆..::: Sistema de Gestión de Gestión de Agenda de contactos :::... 📆\n\t\t\t1️⃣  Agregar contacto  \n\t\t\t2️⃣  Mostrar todos los contactos  \n\t\t\t3️⃣  Buscar contacto por nombre \n\t\t\t4️⃣  Modificar Contactos  \n\t\t\t5️⃣  Elimminar Contactos  \n\t\t\t6️⃣  SALIR  ")
  opcion=input("\t\t\t 👉 Elige una opción (1-6): ").upper()
  return opcion

def agregar_contacto(agenda):
  borrarPantalla()
  print("\n\t\t.:: Agregar Contactos ::.")
  nombre=input("Nombre del contacto: ").upper().strip()

  if nombre in agenda: #SOLO EN DICCIONARIO FUNCIONA
    print("\n\t\t*️⃣ El cotacto ya existe...")
  else:
      telefono=input("Telefono: ").strip()
      email=input("E-mail: ").lower().strip()
      #Agregar el atributo "nombre" al dict con los valores de tel y email en una listas
      agenda[nombre]=[telefono,email]
      print("\n\t\t.::✅Accion realizada con exito✅::.")

def mostrar_contacto(agenda):
  borrarPantalla()
  print("\n\t't .:: Mostrar Contactos ::.")
  if not agenda:
    print("\n\t\t❌  No hay contactos")
  else:
    for nombre,datos in agenda.items():
      print(f"\n\t{'Nombre: '+nombre}\n\t{'Telefono: '+datos[0]}\n\t{'E-mail:'+datos[1]}")

def buscar_contacto(agenda):
    borrarPantalla()
    print("\n\t\t.::🔍  Buscar Contacto  🔍::.")
    nombre = input("Ingrese el nombre del contacto a buscar: ").upper().strip()

    if nombre in agenda:
        datos = agenda[nombre]
        print(f"\n\tNombre: {nombre}\n\tTelefono: {datos[0]}\n\tE-mail: {datos[1]}")
    else:
        print("\n\t\tNo se encontró el contacto.")

def eliminar_contacto(agenda):
    borrarPantalla()
    print("\n\t\t.::🆑  Eliminar Contacto  🆑::.")
    nombre = input("Ingrese el nombre del contacto a eliminar: ").upper().strip()

    if nombre in agenda:
        del agenda[nombre]
        print(f"\n\t\tContacto '{nombre}' eliminado con éxito.")
    else:
        print("\n\t\t❌  No se encontró el contacto para eliminar.")

def modificar_contacto(agenda):
    borrarPantalla()
    print("\n\t\t.:: Modificar Contacto ::.")
    nombre = input("Ingrese el nombre del contacto a modificar: ").upper().strip()

    if nombre in agenda:
        telefono = input("Nuevo teléfono (dejar vacío para no modificar): ").strip()
        email = input("Nuevo e-mail (dejar vacío para no modificar): ").strip()

        if telefono:
            agenda[nombre][0] = telefono
        if email:
            agenda[nombre][1] = email

        print(f"\n\t\tContacto '{nombre}' modificado con éxito.")
    else:
        print("\n\t\tNo se encontró el contacto para modificar.")
