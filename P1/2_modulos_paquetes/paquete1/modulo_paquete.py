#Un módulo es simplemente un archivo con extension .py que contiene código de Python (funciones, clases, variables, etc.).

#Un paquete es una carpeta que contiene varios módulos (archivos .py) y un archivo especial llamado __init__.py que le indica a Python que esa carpeta debe tratarse como un paquete.

import os

def SolicitarDatos1():
    nombre=input("Nombre: ")
    telefono=input("Telefono: ")
    print(f"soy funcion 1 \n el nombre es: {nombre} y su telefono es: {telefono}")

def SolicitarDatos3(nombre,telefono):
    nom=nombre
    tel=telefono
    print(f"soy funcion 3 \n el nombre es: {nom} y su telefono es: {tel}")

def SolicitarDatos2():
    nombre=input("Nombre: ")
    telefono=input("Telefono: ")
    return f"soy funcion 2 \n el nombre es: {nombre} y su telefono es: {telefono}"

def solicitarDatos4(nombre,telefono):
    nom=nombre
    tel=telefono
    return "soy funcion 1 \n",nom,tel