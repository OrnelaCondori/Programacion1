import random;

#EJERCICIO 1
list_numbers =[]
while True:
    number = int(input("Ingrese números a la lista (0 para salir): "))
    if number == 0:
        print("Terminaste de ingresar números en la lista...")
        break
    list_numbers.append(number)
print(list_numbers)

#EJERCICIO 2
delete_number = int(input("Ingrese un número para eliminarlo: "))
if delete_number in list_numbers:
    list_numbers.remove(delete_number)
    print(f"Se eliminó la primera ocurrencia de {delete_number} de la lista.")
    print(list_numbers)
else:
    print("No se puede eliminar, el número no esta en la lista")

#EJERCICIO 3
add_list = [5, 6, 45, 69, 12, 26] 
add_result = 0
for element in add_list:
    add_result += element
print(f"La sumatoria es: {add_result}")

#EJERCICIO 4
new_number = int(input("Ingrese un número: "))
new_list = []
for element in add_list:
    if element < new_number:
        new_list.append(element)
print(f"Los números menores a {new_number}, guardados son {new_list}")

#EJERCICIO 5
numbers = [5,16,2,5,57,5,2]
print(numbers)
print("Tupla que guarda la cantidad de repeticiones por elemento:")
#diccionario para guardar repeticiones, porque pueden agregarse elementos
count_repets = {}
for number in numbers:
    if number in count_repets:
        count_repets[number] += 1
    else:
        count_repets[number] = 1
# Convertir el diccionario en una lista de tuplas
list_tupla = [(numero, cantidad) for numero, cantidad in count_repets.items()]
print(list_tupla)

#EJERCICIO 6
primary_list=[]
secundary_list=[]
print("Ingrese los alumnos de primaria")
while True:
    print("Ingrese el nombre del alumno: ")
    alum=input("(Si desea salir ingrese x): ")
    if alum!="x":
        primary_list.append(alum.capitalize())
    else:
        break

print("Ingrese los alumnos de secundaria")
while True:
    print("Ingrese el nombre del alumno:")
    alum=input("(Si desea salir ingrese x):")
    if alum!="x":
        secundary_list.append(alum.capitalize())
    else:
        break

repeated_names=[]
no_repeated_names=[]
for alum in primary_list:
    if alum in secundary_list:
        repeated_names.append(alum)
    else: 
        no_repeated_names.append(alum)
school_list=primary_list+ secundary_list
for names in repeated_names:
    school_list.remove(names)
print(f"Nombres de los alumnos del nivel primario y secundario son: {school_list}")
print(f" Los nombres repetidos son: {repeated_names}")
print(f" Los nombres del nivel primario que no son repetidos en el nivel secundario son : {no_repeated_names}") 

#EJERCICIO 7
ocurrencias = {}

# Procesa 50 strings ingresados por el usuario
for i in range(50):
    texto = input("Ingrese un string: ")
    for char in texto:
        # Si el carácter ya está en el diccionario, aumenta su conteo en 1
        if char in ocurrencias:
            ocurrencias[char] += 1
        # Si el carácter no está en el diccionario, lo agrega
        else:
            ocurrencias[char] = 1
for char, conteo in ocurrencias.items():
    print(f"'{char}': {conteo}")

#EJERCICIO 8
row = 10
column = 10
#Crea 10 columnas por cada una de las 10 filas de la lista
goles = [[0 for j in range(column)] for i in range(row)]

#Declara la cantidad de goles por partido
for f in range(row):
    for c in range(column):
        if f == c :
            goles[f][c] = 0
        else:
            goles[f][c] = random. randint(0, 6)

#Imprime la matriz
print("La tabla de goles: ")
for fila in goles:
    print(fila)

for f in range(row):
    goals_scored = 0
    goals_allowed = 0
    win = 0
    lose= 0
    tie = 0
    print(f"-----Equipo {(f+1)}-----")
    for c in range(column):
        #Sumar los goles anotados
        goals_scored += goles[f][c]
        #Suma de goles recibidos
        goals_allowed += goles[c][f]
        #Compara con la posicion contraria en la matriz
        if goles[f][c]> goles[c][f]:
            win += 1
        elif goles[f][c]==goles[c][f]:
            tie += 1
        else:
            lose +=1
    print(f"La cantidad de victorias es {win}")
    print(f"La cantidad de derrotas es {lose}")
    print(f"La cantidad de empates es {tie}")
    print(f"Goles hechos {goals_scored}\nGoles recividos {goals_allowed}")

# EJERCICIO 9
card=[["X", "X", "X", "X"], 
["X", "X", "X", "X"], 
["X", "X", "X", "X"]]
card_value=[["S", "R", "C", "C"],["V", "S", "P", "H"],["R", "H", "V", "P"]]
count=0
while(count!=len(card)):
    position_1=input("Ingrese la primera posicion: ")
    position_2=input("ingrese la segunda posicion: ")
    position_1_in_card_1=int(position_1[0:position_1.find(",")])
    position_1_in_card_2=int(position_1[position_1.find(" ")+1:len(position_1)])
    position_2_in_card_1=int(position_2[0:position_2.find(",")])
    position_2_in_card_2=int(position_2[position_2.find(" ")+1:len(position_2)])
    if card_value[position_1_in_card_1][position_1_in_card_2]==card_value[position_2_in_card_1][position_2_in_card_2]:
        print("par encontrado")
        card[position_1_in_card_1][position_1_in_card_2]=card_value[position_1_in_card_1][position_1_in_card_2]
        card[position_2_in_card_1][position_2_in_card_2]=card_value[position_2_in_card_1][position_2_in_card_2]
        for i in card:
            print(i)
        count+=2
    else:
        print(f"La primera carta es: ",{card_value[position_1_in_card_1][position_1_in_card_2]})
        print(f"La segunda carta es: ",{card_value[position_2_in_card_1][position_2_in_card_2]})

# EJERCICIO 10
size_matrix=int(input("Ingresa el tamaño que desea de la matriz cuadrada: "))
square_matrix=[[None]*size_matrix for _ in range(size_matrix)]
for row in range(size_matrix):
    for col in range(size_matrix):
        print(f"Ingrese que numero desea en el casillero {row}: {col}")
        num=int(input("Número: "))
        square_matrix[row][col]=num

main_diagonal=[]
reverse_diagonal=[]

for i in range(0,size_matrix):
    main_diagonal.append(square_matrix[i][i])
    reverse_diagonal.append(square_matrix[i][size_matrix-1-i])
print(f"Matriz Cuadrada ")
for row in square_matrix:
    print(row)
print(f"diagonal principal {main_diagonal}")
print(f"diagonal inversa {reverse_diagonal}")

# EJERCICIO 11
foreign_currency={
    'Euro':'€', 
    'Dollar':'$',
    'Yen':'¥',
    "Peso":"$",
    'Libra':'£'
}
print("Ingrese la moneda que desea y se le mostrara su simbolo")
user_currency=input().capitalize()
if user_currency in foreign_currency:
    print(foreign_currency[user_currency])
else:
    print(f"La divisa {user_currency} no esta registrada")

# EJERCICIO 12
print("Ingrese los siguientes datos")
name=input("nombre :")
age=input("edad :")
loc=input("direccion :")
tel=input("Telefono :")
person={
    "name":name.capitalize(),
    "age":age,
    "loc":loc.capitalize(),
    "tel":tel
}
print(f"El usuario {name} tien {age} , vive en {loc}, y su numero de telefono es {tel}")

# EJERCICIO 13
fruit_prices = {
    "apple": 1.0,
    "banana": 0.5,
    "orange": 1.2,
    "grape": 2.0,
    "pear": 0.8
}
fruit = input("Ingresa el nombre de la fruta: ").lower() 
# verifica que la fruta este en el diccionario
if fruit in fruit_prices:
    # pide que se ingrese la cantidad
    try:
        kilos = float(input(f"Ingresa el número de kilos {fruit}: "))
        # Calcula el precio
        total_price = fruit_prices[fruit] * kilos
        print(f"El precio de {kilos} kilos de {fruit} es: ${total_price:.2f}")
    except ValueError:
        print("Porfavor, ingresa un valor correcto de kilos")
else:
    print("La fruta ingresada, no esta en la lista de precios.")




