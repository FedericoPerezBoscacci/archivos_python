#!/usr/bin/env python
'''
Archivos [Python]
Ejercicios de clase
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

import csv
import re


def ej1():
    # Ejercicios con archivos txt
    cantidad_lineas = 0

   
    def contar_lineas(archivo):
        
        

        lineas_texto = open (archivo,"r")

        lineas = lineas_texto.readlines()      ##convierto a una lista lo que se encuentra en "notas.txt"

        cantidad_lineas = len(lineas)      ## cuento la cantidad de lineas 
    
        #print ("La cantidad de lineas que tiene el archivo es : {} ".format (cantidad_lineas))
        
        lineas_texto.close()  # Cierro el archivo
        
        return (cantidad_lineas)  # Devuelvo el resultado


    cantidad_lineas = contar_lineas("notas.txt") # Llamo a la funcion y le asigno el archivo que deseo que cuente las lineas

    print ("La cantidad de lineas que tiene el archivo es : {} ".format (cantidad_lineas))


    '''
    Realizar un prorgrama que cuenta la cantidad de líneas
    de un archivo. Abra el archivo "notas.txt" en modo "lectura",
    lea linea alinea el archivo, y cuente la cantidad de líneas.
    Al finalizar el proceso, imprimir en pantalla la cantidad
    de líneas leaidas.

    Como práctica de funciones, puede realizar la función
    "contar_lineas" que reciba como parámetro el nombre del archivo
    y cumpla el objetivo especificado, retornando la cantidad
    de líneas encontradas.
    '''


def ej2():
    # Ejercicios con archivos txt
    cantidad_lineas = 0
    '''
    Copy paste!!
    Deberá abrir dos archivo txt, uno para lectura (fi) y otro
    para escritura (fo) (un archivo nuevo).
    El archivo abierto para lectura (fi) debe ser el archivo
    "notas.txt"

    Debe leer "línea por línea" el archivo "nota.txt" y copiar
    "línea a línea" en el archivo para escritura.

    A su vez, mientras va escribiendo "línea a línea" debe
    contar la cantidad de línea que se copiaron e imprimir
    al final del proceso el valor.
    '''

    # fi = open('nota.txt', 'r')
    # fo = open(.......)

    # Recuerde cerrar los archivos al final ;)
    

    fi = open ("notas.txt","r")    #archivo abierto para lectura
    fo = open ("copia_notas.txt","w")

    lineas = fi.read() # asigno las lineas del archivo a una lista
    
    fo.write(lineas)

    fi.close()
    fo.close()

    def contar_lineas(archivo):
        
        

        lineas_texto = open (archivo,"r")

        lineas = lineas_texto.readlines()      ##convierto a una lista lo que se encuentra en "notas.txt"

        cantidad_lineas = len(lineas)      ## cuento la cantidad de lineas 
    
        #print ("La cantidad de lineas que tiene el archivo es : {} ".format (cantidad_lineas))
        
        lineas_texto.close()  # Cierro el archivo
        
        return (cantidad_lineas)  # Devuelvo el resultado


    cantidad_lineas = contar_lineas("copia_notas.txt") # Llamo a la funcion y le asigno el archivo que deseo que cuente las lineas

    print ("La cantidad de lineas que tiene el archivo es : {} ".format (cantidad_lineas))

    
    





def ej3():
    # Ejercicios con archivos CSV
    archivo = 'propiedades.csv'
    '''
    Realice un programa que abra el archivo CSV "propiedades.csv"
    en modo lectura. Recorrar dicho archivo y contar
    la cantidad de departamentos de 2 ambientes y la cantidad
    de departamentos de 3 ambientes disponibles.
    Al finalizar el proceso, imprima en pantalla los resultados.
    '''


    #fi = open ("propiedades","r")
    
    with open ("propiedades.csv") as fi:
        data = list (csv.DictReader(fi))

    depto_2 = 0
    depto_3 = 0
    
    cantidad = len(data)
   
    for i in range(0,cantidad):

        row = data [i]
        
        ambiente = row.get("ambientes")
        
        if ambiente == "2":
           
            depto_2 += 1
        
        elif ambiente == "3":

            depto_3 += 1

    
        continue
    

    print("Hay {} departamentos de 2 ambientes, y hay {} cantidad de departamentos de 3 ambientes".format(depto_2,depto_3))
        
    

def ej4():
    # Ejercicios con diccionarios
    inventario = {'manzanas': 6}

    '''
    Realice un programa que pida por consola
    el nombre de una fruta o verdura y luego
    pida la cantidad que hay en stock
    Agregar al diccionario el par:
    <fruta>:<cantidad>
    Esta operacion se debe realizar en un bucle
    hasta ingresar como fruta/verdura la palabra "FIN"

    Al finalizar el bucle anterior, debe generar otro bucle
    en donde se pida ingresar la fruta o verdura que desea
    conocer su estado de stock.
    Deberá imprimir en pantalla la cantidad de esa fruta en
    inventario, y en caso de no exista ese elemento en nuestro
    inventario se debe imprimir en pantalla "Elemento no encuentrado"
    NOTA: Proponemos utilizarel método "get" que devuelve "None" si el
    elemeto no existe en el diccionario.

    Se debe terminar ese segundo bucle cuando se ingrese la palabra FIN
    '''

    # 1) Bucle 1
    # Generar y completar el diccionario con las frutas y cantidades
    # ingresadas por consola hasta ingresar la palabra "FIN"

    # 2) Bucle 2
    # Ingresar por consola la fruta que desea conocer en stock
    # Finalizar cuando la fruta ingresada sea igual a "FIN"

    fin = 0
    while fin != "fin":

        print("Ingrese fruta:")
        fruta = str(input())
        print("Ingrese cantidad")
        cantidad = int(input())

        inventario[fruta] = cantidad
        print("Si termino de agregar frutas escriba: fin ")
        fin = str(input())
        
        continue

    fin = 0

    while fin != "fin":


        print("Ingrese nombre de la fruta para conocer la cantidad en stock: ")
        opcion = str(input())

        resultado = inventario[opcion]

        print(" {} de cantidad en stock".format(resultado))

        print("Si desea seguir buscando tocar cualquier letra o para terminar escribir: fin")
        fin = str(input())

        continue
    

    



def ej5():
    # Ejercicios con archivos CSV
    

    '''
    Basado en el ejercicio anterior, genere un archivo CSV
    (abrir un archivo CSV como escritura) que posea las siguientes
    columnas:
    1) 'Fruta Verdura'
    2) 'Cantidad'

    Estas dos columnas representan el nombre de las dos "claves"
    del diccionario que utilizaremos para escribir en el archivo CSV

    writer.writerow({'Fruta Verdura': ....., 'Cantidad': ....})

    Deberá realizar un bucle en donde en cada iteracion del bucle
    se le socilitará por consola que ingrese un tipo de fruta o verdura
    y su cantidad, deberá escribir una línea en el archivo CSV (una fila)
    con esa información ingresada.
    El bucle finalizará cuando se ingrese como fruta o verdura
    la palabra "FIN"

    Al finalizar deberá tener un archivo (con el nombre que usted haya
    elegido) con todas las filas completas en las dos columnas especificadas
    con todas las frutas o verduras ingresadas y sus cantidades
    '''
    # Recuerde crear el header correspondiente con "writeheader", el cual
    # se debe especificar al abrir el archivo.

    # Bucle....

    # writer.writerow({'Fruta Verdura': ....., 'Cantidad': ....})


    inventario = {}

    fi = open ("ejercicio5.csv","w")


    fin = 0
    while fin != "fin":

        print("Ingrese fruta:")
        fruta = str(input())
        print("Ingrese cantidad")
        cantidad = str(input())

        inventario[fruta] = cantidad
        print("Si termino de agregar frutas escriba: fin ")
        fin = str(input())
        
        continue

    
    header = ["Frutas" , "cantides" ] # asigno las columnas en una lista
    
    encabezados = csv.DictWriter(fi, fieldnames= header  )  # " creando el escritor" aun no escribi nada
   
    encabezados.writeheader()
    
    for k in inventario.keys():
        
        frutas = k
        cantidades = inventario[k]

        fi.write(frutas)  # escribo en el programa las lineas
        fi.write(cantidades)

    fi.close()


        
        
        










if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    #ej1()
    #ej2()
    #ej3()
    #ej4()
    ej5()
