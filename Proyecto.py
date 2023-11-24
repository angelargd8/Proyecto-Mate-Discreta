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

#--- diccionario ---
diccionario= {chr(i + ord('A')): i for i in range(26)}

#--- funciones ---

def MostrarMenu():
    print("\n\nBienvenido al sistema RSA, ingrese una opción: \n1. Encriptar Mensaje\n2. Desencriptar Mensaje\n3. Salir")



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
    C = str(input("Ingrese el valor de C (mensaje encriptado) sin espacios en bloques de 4: "))
    n = int(input("Ingrese el valor de n: "))
    e = int(input("Ingrese el valor de e: "))

    if( n>0 and e>0 ):
        #---1. encontrar la llave privada----

        #calcular los valores de p y q (factorizar n)
        lista_primos= factorizar(n)
        p = lista_primos[0]
        q = lista_primos[1]
        #print(p,q)

        #funcion de euler
        fi = (p-1)*(q-1)
        #print(fi)

        #encontrar la llave privada
        #numero que e*d sea congruente a 1 y mcd(fi)
        d= encontrarD(e, fi)
        print("la llave privada es: "+str(d)+","+str(n))

        #----2. desencriptar el mensaje-----
        #separar el mensaje en bloques de 4
        lista_mensaje = []
        for i in range(0, len(C), 4):
            lista_mensaje.append(C[i:i+4])
        #print(str(lista_mensaje))

        #print(diccionario)
        mensaje=[]

        for i in lista_mensaje:
            i = int(i)
            m = (i**(d)) % n
            #convertir m a 2 strings y luego compararlo con el diccionario
            strM= str(m)
            #print(strM)
            mitad= len(strM)//2
            mitad1= int(strM[:mitad])
            mitad2= int(strM[mitad:])
            #print("primera mitad: "+str(mitad1))
            #print("segunda mitad: "+str(mitad2))
            mensaje.append(buscarLlave(mitad1) + buscarLlave(mitad2))

        #3. mostrar el mensaje desencriptado
        mensajeFinal= ''.join(mensaje)
        print("el mensaje es: "+str(mensajeFinal))
    else:
        print("ingrese numeros enteros positivos")

    
    

#buscar llave
def buscarLlave(valor):
    for llave, value in diccionario.items():
        if value == valor:
            return llave
    return "No existe la llave" #jjk anque no debería de pasar porque como es mod 26

#maximo comun divisor
def mcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        MCD, x, y = mcd(b % a, a)
        return MCD, y - (b // a) * x, x
    

def encontrarD(e, fi):
    MCD, x, y = mcd(e, fi)
    if MCD != 1: 
        print("No se puede encontrar la llave privada")
    else: 
        return x % fi

#factorizar n
def factorizar(n):
    primo = 2 #primer numero primo
    factores = []
    while primo * primo <= n: #es primo^2 porque se bucan factores hasta sqrt(n)
        if n % primo:
            primo += 1
        else:
            #comprobar que sea divisible
            n = n// primo 
            factores.append(primo)
    if n > 1:
        factores.append(n)
    return factores


#---- menu principal ----
try: 
    while menu:
        MostrarMenu()
        opcion = int(input("Ingrese la opción: "))
        if opcion == 1: 
            #print(diccionario)
            encriptacion()
        elif opcion == 2:
            desencriptacion()
        elif opcion == 3:
            break
        else: 
            print("esta opción no es válida")
except:
    print("Esta opción no es válida, vuelva a intentarlo con los datos correctos \n\n")
input("pulse una tecla para continuar... ")