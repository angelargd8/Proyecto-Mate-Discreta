"""
-- Proyecto: Criptografía --
Descripcion: Realizar una implementación de un programa de computadora
             escrito en python que realice: 
                - Encriptación RSA
                - Desencriptación RSA
Autores: 
        - Diego García #22404
        - Angela García #22869
        
fecha de ultima modificacion: 24/11/2023
"""
# CLAVE DE ACCESO: HURRICANE

#--- modulos ---
import os
import csv

#--- variables ---
menu = True
os.system("cls") # limpia la consola

#--- funciones ---

def MostrarMenu():
    print("\n\n Bienvenido alsistema RSA, ingrese una opción: \n1. Encriptar Mensaje\n2. Desencriptar Mensaje\n3. Salir")



#----Encriptación----
"""
Dado un mensaje M, p y q números primos y un entero 𝑒 > 1 primo relativo con 𝜙 = (𝑝 − 1)(𝑞 − 1),
encriptar el mensaje M usando el sistema criptográfico RSA y la llave pública (𝑒, 𝑛)

-- Input: 𝑀, 𝑝, 𝑞 & 𝑒
-- Output: el mensaje encriptado en bloques de 4 dígitos
"""

def encriptacion():
    pass


#----Desencriptación----
"""
Dado un mensaje encriptado C usando el sistema criptográfico RSA y la llave pública (𝑒, 𝑛), encontrar
la llave privada 𝑑 y desencriptar el mensaje

-- Input: 𝐶 & (𝑛, 𝑒)
-- Output: la llave privada d y el mensaje desencriptado 𝑀

"""

def desencriptacion():
    #pedir datos
    C = int(input("Ingrese el valor de C (mensaje encriptado): "))
    n = int(input("Ingrese el valor de n: "))
    e = int(input("Ingrese el valor de e: "))

    #encontrar la llave privada

    #desencriptar el mensaje

    #eee sigo mañana xd


#---- menu principal ----
try: 
    while menu:
        MostrarMenu()
        opcion = int(input("Ingrese la opción: "))
        if opcion == 1: 
            encriptacion()
        elif opcion == 2:
            desencriptacion()
        elif opcion > 2:
            break
        else: 
            print("esta opción no es válida")
except:
    print("Esta opción no es válida, vuelva a intentarlo con los datos correctos \n\n")
    MostrarMenu() 
input("pulse una tecla para continuar... ")