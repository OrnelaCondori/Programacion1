from mutantes_funciones import *

while True:
    genetic_information =[]
    print(" \n----------VERIFICACIÓN DE ADN----------\n ")
    print("A continuacion ingrese las 6 cadenas de datos (Ejemplo: ATGCGA)")

    #Ingreso de datos por el usuario, funcion para verificarlos
    for i in range(6):
        while True:
            dna_text = input(f"Cadena {(i+1)}: ")
            dna_text = dna_text.upper()
            if verify_genetic_information(dna_text):
                genetic_information.append(dna_text)
                break
            else:
                print("! La cadena ingresada no es válida, verifique que las letras utlizadas sean A/T/C/G")
    print("----------------------------------------")
    print(f"DNA= {genetic_information}")

    #creo una matriz para guardar letra por letra
    matriz_dna = [['' for _ in range(len(genetic_information[0]))] for _ in range(len(genetic_information))]
    #Guardo en la matriz, las letras del arreglo
    for i in range(len(genetic_information)):
        for j in range(len(genetic_information[i])):
            matriz_dna[i][j] = genetic_information[i][j]
    for filas in matriz_dna:
        print (filas)


    #Uso de la funcion principal
    print("----------------------------------------")
    result_analisis = is_mutant(matriz_dna)
    print(f"Resultado de Analisis: {result_analisis}")
    if result_analisis:
        print("ES UN MUTANTE")
    else:
        print("NO ES UN MUTANTE")
    
    #menú para el usuario, indica si desea continuar utlizando el programa o salir, verifica que la opcion ingresada sea correcta
    while True:
        try:
            print("----------------------------------------")
            continue_program = int(input("Indique que desea hacer:\n          1. Ingresar otro ADN\n          2. Salir del programa\nEleccion (1/2): "))
            if continue_program!= 1 and continue_program!=2:
                print("! El número ingresado no corresponde a ninguna opcion, ingreselo nuevamente")
            else:
                break
        except ValueError:
            print("! Entrada no válida, ingrese un número entero válido")
    
    if continue_program ==2:
        break

#Ejemplo para cuando la función es false:
# acggca
# cagcac
# attagg
# ggtttg
# aatcgc
# agtgta

#Ejemplo para que la función sea True:
# ctgcga
# cactgc
# ttatgt
# agaagg
# ccccat
# tcactg