from met_ordenamiento import *
#1
number_array = [14, 345, 2, 62, 32, 114, 143]
print(f"Array Desordenado : {number_array}")
bubble_sort(number_array)
print("Arreglo ordenado:")
print(f"Array ordenado : {number_array}")

#2
arr_word = ["perro", "tarea", "programacion","gato"]
selection_sort(arr_word)
print("Lista ordenada:")
print(arr_word)

#3 
book_list=[
    {"titulo":"Harry Poter","autor":"J. K. Rowling","anio_pub":1997,"genero":"ficcion"},
    {"titulo":"Payaso Plin Plin","autor":"Jaimito","anio_pub":1923,"genero":"comedia"},
    {"titulo":"Harry Popoter","autor":"El tio Luis","anio_pub":2023,"genero":"terror"},
    {"titulo":"Futbolito","autor":"Bielsa","anio_pub":2005,"genero":"deporte"},
    {"titulo":"El Despertar","autor":"Mariela Fernandez","anio_pub":2013,"genero":"novela"}
]
print(f"Libros sin ordenar ")
for i in book_list:
    print(i)
autor_sort(book_list)
print(f"Libros ordenados por autor ")
for i in book_list:
    print(i)

#4
string_arra=["hola","como estas","cirujano","papas a la crema","uno","no"]
print(f"Lista desosrdenada {string_arra}")
len_insert_sort(string_arra)
print(f"Lista Ordenada {string_arra}")

#5
print(f"Ascendente :  {number_array}")
des_bubble_sort(number_array)
print(f"Descendente :  {number_array}")

#6
number_list=[3,2,4,9,6,4,1]
number=count_sort(number_list)
print(f"Lista de numeros ; {number}")

#7
list= ["Manzana", 42, "Gato", 3,"Arbol", "Python", 7, "Libro", 99, "Soleado", "Montaña",33, "Pelota", 1,43,"Elefante"]
order_by_type(list)
print(f"{list}")

#8
number_array = [14, 345, 2, 62, 32, 114, 143]
number_array = merge_sort(number_array)
print (number_array)