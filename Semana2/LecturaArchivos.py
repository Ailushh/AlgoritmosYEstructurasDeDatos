# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 14:55:25 2022

@author: ailen
"""

archivo = open("ruta del archivo")
contenido = archivo.read()
print(contenido)
archivo.close()

#%% Abro un nuevo contexto de phyton
#Si abro el archivo con WITH, cuando salgo del contexto, se cierra

with open("ruta del arhivo") as arch:
    contenido = arch.readline() #lee una línea
    print(contenido)
    contenido = arch.readline() #lee la otra línea
    print(contenido)
    
#%% Otra forma de leer

with open("ruta del arhivo") as arch:
    for linea in arch:
        print(linea, end=" ")
        
#%% Otra forma de leer, creando una lista

with open("ruta del arhivo") as arch:
    lista_arch = list(arch)
    
print (lista_arch)

#%% Otra forma, guardando cada línea en un elemento de la lista

with open("ruta del arhivo") as arch:
    lista_arch = arch.readlines()
    
print(lista_arch)

#%% Escribo Archivos

with open("archivoNuevo", mode = 'w') as arch: #Con 'w' escribo al principio. Con 'a' escribo al final
    n = arch.write('Hola, archivo de prueba jeje') #write me devuelve cuántos caracteres escribí
    
print(n)

#%% Leo y escribo, ambas
with open("archivoNuevo", mode = 'r+') as arch:
    contenido = arch.read()
    n= arch.write('Holiwis')
    
print(contenido)
print(n)

#%% Enumero lo que leo
with open("archivoNuevo") as arch:
    for nro_linea, linea in enumerate(arch):
        print(nro_linea, linea)
        
        