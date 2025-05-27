from paquete1 import modulos

print(modulos.saludar("Diego Bustillo Aguirre"))

modulos.borrarPantalla()
nom,tel=modulos.SolicitarDatos2()
print(f"\n\t.::Agenda Telefonica::.\n\tNombre: {nom} \n\t\tTelefono:{tel}")
modulos.espereTecla()