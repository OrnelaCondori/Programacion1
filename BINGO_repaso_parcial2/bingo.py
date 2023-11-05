from bingo_funciones import *
import random

#Ingresa y verifica los núemros ingresados por el usuario, hasta completar 25
bingo=[]
for i in range(25):
    while True:
        # number = int(input(f"Ingrese el numero {(i+1)}: "))
        number = random.randint(1,75)
        repet = search_number(number, bingo)
        if repet or number<1 or number>75:
            print("! El número no es válido, ingreselo nuevamente")
        else:
            break
    bingo.append(number)
print(bingo)

#Guarda en una matriz, los valores ya ingresados
print("TU CARTON DE BINGO ES: ")
row = 5
column = 5
bingo_card = [[0 for j in range(column)] for i in range(row)]
bingo_process = [[0 for j in range(column)] for i in range(row)]
pos = 0
for f in range(row):
    for c in range(column):
        bingo_card[f][c]=bingo[pos]
        bingo_process[f][c]=bingo[pos]
        pos+=1
for fila in bingo_card:
    print(fila)

#Numeros random del 1 al 75 sin repetir
random_balls=[]
for i in range(75):
    while True:
        number_random = random.randint(1, 75)
        repet = search_number(number_random, random_balls)
        if not repet:
            break
    random_balls.append(number_random)
print(random_balls)


for element in random_balls:
    print(f"Bola número {element}")
    if search_number(element, bingo):
        print(" :) El número esta en tu carton! ")
        new_card = bingo_complete(bingo_card, bingo_process, element)
        for row in new_card:
            print(row)
        bingo_process = new_card
    else:
        print(" ! Tu carton no contiene este número")
        continue
    if find_column(bingo_process):
        print("columna completa")
        break
    elif find_row(bingo_process):
        print("Fila completa")
        break
    elif find_diagonal(bingo_process):
        print("Diagonal completa")
        break
    elif find_diagonal_inversa(bingo_process):
        print("Diagonal inversa")
        break
    


