#main.py
from funciones import borrarPantalla, esperarTecla
from usuarios.usuario import registrar, iniciar_sesion
from dulcerias.dulceria import agregar_producto, ver_inventario, buscar_por_codigo, entrada_producto, salida_producto
from ventas.venta import realizar_venta, mostrar_ventas
from recargas.recarga import recargar_stock, mostrar_recargas
import getpass

def main():
    while True:
        borrarPantalla()
        print("\n\t=== MENÚ DE USUARIOS ===")
        print("\t1. Registrar usuario 📝")
        print("\t2. Iniciar sesión 🔑")
        print("\t3. Salir 🚪")

        opcion = input("\n\tSeleccione una opción: ").strip()
        if opcion == "1":
            borrarPantalla()
            print("\n\t..:: Registro de Usuario ::..")
            nombre = input("\tNombre: ").upper().strip()
            apellidos = input("\tApellidos: ").upper().strip()
            email = input("\tEmail: ").lower().strip()
            password = getpass.getpass("\tContraseña: ")
            registrar(nombre, apellidos, email, password)
            esperarTecla()

        elif opcion == "2":
            borrarPantalla()
            print("\n\t..:: Inicio de Sesión ::..")
            email = input("\tEmail: ").lower().strip()
            password = getpass.getpass("\tContraseña: ")
            usuario_id = iniciar_sesion(email, password)
            if usuario_id:
                menu_dulceria(usuario_id)
            else:
                print("\n\t⚠️ Usuario o contraseña incorrectos")
                esperarTecla()

        elif opcion == "3":
            borrarPantalla()
            print("\n\tSaliendo del sistema...")
            break
        else:
            borrarPantalla()
            print("\n\t⚠️ Opción inválida")
            esperarTecla()

def menu_dulceria(id_usuario):
    while True:
        borrarPantalla()
        print("\n\t📋 === SISTEMA DE INVENTARIO ===")
        print("\t1. Agregar producto 💾")
        print("\t2. Ver inventario 📂")
        print("\t3. Entrada de producto ➕")
        print("\t4. Salida de producto ➖")
        print("\t5. Buscar por código 🔍")
        print("\t6. Venta de producto 💲")
        print("\t7. Recarga de producto 🔁")
        print("\t8. Listar ventas 📑")
        print("\t9. Listar recargas 📑")
        print("\t0. Cerrar sesión 🔒")

        opcion = input("\n\tSeleccione una opción: ").strip()
        if opcion == "1":
            borrarPantalla()
            agregar_producto()

        elif opcion == "2":
            borrarPantalla()
            ver_inventario()
            if ver_inventario():
                print("\n\t=== Inventario ===")
                for p in ver_inventario():
                    print(f"{p['codigo']} | {p['nombre']} | stock: {p['stock']} | {p['precio']}")
            else:
                print("No hay productos para mostrar.")

        elif opcion == "3":
            borrarPantalla()
            entrada_producto()
        elif opcion == "4":
            borrarPantalla()
            salida_producto(id_usuario)
        elif opcion == "5":
            borrarPantalla()
            buscar_por_codigo()
        elif opcion == "6":
            borrarPantalla()
            realizar_venta(id_usuario)
        elif opcion == "7":
            borrarPantalla()
            recargar_stock(id_usuario)
        elif opcion == "8":
            borrarPantalla()
            mostrar_ventas()
        elif opcion == "9":
            borrarPantalla()
            mostrar_recargas()
        elif opcion == "0":
            borrarPantalla()
            break
        else:
            borrarPantalla()
            print("\n\t⚠️ Opción inválida")
        esperarTecla()

if __name__ == "__main__":
    main()
