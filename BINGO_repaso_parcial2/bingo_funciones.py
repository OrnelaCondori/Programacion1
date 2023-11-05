#verifica si el número dado esta o no en un array
def search_number(numero, array):
    if numero in array:
        return True
    return False

#Remplaza el número correspondiente por una f (found), en su posicion
def bingo_complete(matriz, bingo_process, number):
    row = len(matriz)
    column = len(matriz[0])

    for f in range(row):
        for c in range(column):
            if matriz[f][c] == number:
                bingo_process[f][c]="F"
            else:
                continue
    
    return bingo_process

#comprueba si la fila esta completa
def find_row(matriz):
    for row in matriz:
        #inicializa un contador en 0 por cada fila, en caso que alguna este completa devuelve true
        cantidad = 0
        for column in row:
            if column == "F":
                cantidad+=1
        if cantidad == 5:
            return True
    return False

def find_column(matriz):
    row = len(matriz)
    column = len(matriz[0])
    for c in range(column):
        cantidad = 0
        for f in range(row):
            if matriz[f][c] == "F":
                cantidad += 1
        if cantidad == 5:
            return True
    return False

def find_diagonal(matriz):
    row = len(matriz)
    cantidad = 0
    for f in range(row):
        if matriz[f][f] == "F":
            cantidad += 1
    if cantidad == 5:
        return True
    else:
        return False

def find_diagonal_inversa(matriz):
    row = len(matriz)
    cantidad = 0
    for f in range(row):
        if matriz[f][row - 1 - f] == "F":
            cantidad += 1
    if cantidad == 5:
        return True
    else:
        return False





