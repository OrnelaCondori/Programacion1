from funciones_tp8 import *

#Función que reciba un número positivo n y devuelva la cantidad de dígitos que tiene.
num1 = int(input("Ingrese un número positivo: "))
while num1 <= 0:
    print("El número ingresado no es correcto, ingréselo nuevamente.")
    num1 = int(input("Número: "))  # Corregido: convertir a entero
digits = digit_count(num1)
print(f"La cantidad de dígitos del número es: {digits}")

#Función que reciba 2 enteros n y b y devuelva True si n es potencia de b.
number = 3
possible_exponent = 81
print(f"Los números ingresados en la funcion son potencia? {es_potencia(possible_exponent, number)}")

#funcion recursiva que devuelva las posiciones en donde se encuentra b dentro de a. 
print(f"La siguiente lista muestra las pociones en las que se encontro a la palabra {pos_string("Un tete a tete", "te")}")

#Funciones mutualmente recursivas par(n) e impar(n) que determinen la paridad del numero natural dado
num2 = int(input("Ingrese un número para saber si es o no par: "))
if impar(num2):
    print("El número es impar")
else:
    print("El número es par")

#Encontrar el elemento más grande de una lista
my_list= [14,34,2,9,47]
greattest_element = largest_element(my_list)
print(f"El número más grande es {greattest_element}")

#Replicar los elementos de una lista una cantidad n de veces
new_list = replic_element(my_list, 2)
print(new_list)

#función recursiva, que resuelva la siguiente sumatoria:  K(n, p) = p + 2 ∗ p + 3 ∗ p + 4 ∗ p + … + n ∗ p
num3 = k(3,4)
print(num3)

#Funcion para calcular el triangulo pascal
column = int(input("Ingrese el número de columna: "))
row = int(input("Ingrese el número de fila: "))
result = pascal(row, column)
print(f"El valor en la fila {row} y la columna {column} es: {result}")

#Todas las ombinaciones de caracteres, de k cantidad
caracteres = ['a', 'b', 'c']
k = 3
combinaciones(caracteres, k)

width, height = hoja_a(2)
print(f"El ancho de la hoja es {width}")
print(f"El largo de la hoja es {height}")

