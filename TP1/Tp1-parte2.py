#1.
base = float(input("Ingrese la base del rectangulo: "))
altura = float(input("Ingrese la altura del rectangulo: "))
peri = 2* base + 2*altura 
area = base * altura
print( "El perimetro es : ", peri)
print("El area es: ", area)

#2
cate1 = float(input("Ingrese el cateto 1: "))
cate2 = float(input("Ingrese el cateto 2: "))
hipo = (cate1**2 + cate2**2)** (1/2)
print("La hipotenusa es: ", hipo)

#3.	
num1 = float(input("Ingrese un número: "))
num2 = float(input("Ingrese otro número: "))
suma = num1 +num2
resta = num1 - num2
divi = num1 /num2
multi = num1 * num2
print("Suma = ", suma )
print("Resta = ", resta )
print("Divison = ", divi )
print("Multiplicación = ", multi)

#4
fahre = float(input("Ingrese la temperatura en grados fahrenheit: "))
cels= (fahre -32)*5/9
print("Los grados en celcius son: ", cels)

#5 
    #a 
nombre = input("¿Cual es tu canción favorita?")
    #b
precio = int(input("Precio: "))
total = precio + (precio * 0.1)
    #c
edad = int(input("Edad: "))
print("tu edad es: ", edad)
    #d
edad2 = int(input("Edad: "))
edad18 = bool(edad2 == 18)
print("Veamos si tu edad es 18: ", edad18)

#6
val1 = float(input("Ingrese el primer valor a premediar: "))
val2 = float(input("Ingrese el segundo valor a promediar: "))
val3 = float(input("Ingrese el tercer valor a promediar: "))
promedio = (val1+val2+val3)/3
print("El promedio de los números ingresados es: ", promedio)