def verify_genetic_information(cadena):
    if len(cadena) != 6:
        return False
    else:
        for l in cadena:
            if l != "A" and l != "T" and l != "C" and l != "G":
                return False
    return True

def diagonal_sequence(matriz):
    sequence_counter = 0
    #Solamente recorre las primeras 3 columnas de las 3 primeras filas, porque al ser secuencias de 4 letras
    #en las demas posiciones no se cumpliría la condición
    for f in range(3):
        for c in range(3):
            #Recorre las 3 posiciones diagonales siguientes, si se cumple que sean iguales incremeta un contador
            if matriz[f][c] == matriz[f +1][c +1] == matriz[f +2][c + 2] == matriz[f +3][c+ 3]:
                sequence_counter += 1
    #Devualve un contador en caso de que hayan 2 o mas secuencias diagonales
    return sequence_counter

def inverse_diagonal_sequence(matriz):
    sequence_counter = 0
    # Recorre de la fila tercer fila a la ultima
    for f in range(3,6):
        for c in range(3):
            #Si las 3 posiciones siguientes son iguales, incremeta un contador
            if matriz[f][c] == matriz[f -1][c +1] == matriz[f -2][c + 2] == matriz[f -3][c+ 3]:
                sequence_counter += 1
    return sequence_counter

def vertical_sequence(matriz):
    sequence_counter = 0
    # Recorre las filas 3 primeras filas
    for f in range(3):
        for c in range(6):
            #Si las 3 posiciones siguientes son iguales, incremeta un contador
            if matriz[f][c] == matriz[f +1][c] == matriz[f +2][c] == matriz[f +3][c]:
                sequence_counter += 1
    return sequence_counter

def horizontal_sequence(matriz):
    sequence_counter = 0
    # Recorre todas las filas
    for f in range(6):
        for c in range(3):
            if matriz[f][c] == matriz[f][c + 1] == matriz[f][c + 2] == matriz[f][c + 3]:
                sequence_counter += 1
    return sequence_counter

def is_mutant(matriz):
    
    sum_sequence = diagonal_sequence(matriz) + inverse_diagonal_sequence(matriz) + vertical_sequence(matriz) + horizontal_sequence(matriz)

    if sum_sequence >= 2:
        return True
    else:
        return False

#Este es un ejemplo de como lo estaba haciendo al principio, pero como en realidad conozco el tamaño de la matriz y la condiciión es que sean iguales 4 posicones
#Es más sencillo si simplemente las indico con sus posiciones, por eso cambie la forma de las funciones


# def diagonal_sequence(matriz):
#     sequence_counter=0
#     #Solamente recorre las primeras 3 columnas de las 3 primeras filas, porque al ser secuencias de 4 letras
#     #en las demas posiciones no se cumpliría la condición
#     for f in range(3):
#         for c in range(3):
#             principal_letter = matriz[f][c]
#             repet_letter = 1
#             #Recorre las 3 posiciones diagonales siguientes, si se cumple que sean iguales incremeta un contador
#             for t in range(1,4):
#                 if f + t < 6 and c + t < 6 and matriz[f + t][c + t] == principal_letter:
#                     repet_letter+=1
#                 else:
#                     break
#             #Si es contador es 4, es decir que se cumple la secuencia, suma 1 al contador de secuencias
#             if repet_letter == 4:
#                 sequence_counter+=1
#     #Devualve un contador en caso de que hayan 2 o mas secuencias diagonales
#     return sequence_counter


