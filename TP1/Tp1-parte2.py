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
print("El promedio de los números es: ", promedio)

#7
total_min = int(input("Ingrese la cantidad de minutos delos que quiere calcular las horas: "))
horas = total_min/60
minutos = total_min - (horas*60)
print(f"Son {horas} horas y {minutos} minutos")

#8
sueldo = int(input("Ingrese su sueldo base"))
venta1 = int(input("Ingrese el total de la primer venta: "))
venta2 = int(input("Ingrese el total de la segundaventa: "))
venta3 = int(input("Ingrese el total de la tercer venta: "))
comision = (venta1+venta2+venta3)*0.10
sueldo = sueldo +comision
print(f"El sueldo de este mes corresponde a ${sueldo}")

#9
compra = float(input("Ingrese el total de su compra: $"))
descuento = compra*0.15
compra = compra-descuento
print(f"Con el descuento su total es: ${compra}")

#10
parc1 = float(input("Nota del primer parcial: "))
parc2 = float(input("Nota del segundo parcial: "))
parc3 = float(input("Nota del tercer parcial: "))
examen = float(input("Nota del examen final: "))
trabajo = float(input("Nota del trabajo final: "))

promedio_parciales = (parc1+parc2+parc3)/3
pp = promedio_parciales * 0.55
pe = examen * 0.30
pt = trabajo * 0.15

calificacion_final = pp +pe+pt
print("Sua calificacion final es: ", calificacion_final)

#11 
n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))
dis = abs(n1 -n2)
print(f"La distancia entre estos números es: {dis}")

#12 
n3 = int(input("Ingrese un número para calcular sus raises: "))
r_cuadrada = n3 ** (1/2)
r_cubica = n3 **(1/3)
print(f"Su raiz cuadrada es {r_cuadrada} y su raiz cubica es {r_cubica}")

#13 
n4 = input("Ingrese un número de dos cifras: ")
inverso = n4[::-1]
print(f"El número invertido es: {inverso}")

#14 
a = int(input("Ingrese el valor de A: "))
b = int(input("Ingrese el valor de B: "))

aux = a
a = b
b = a
print(f"Ahora el valor de B es {b} y el valor de A es {a}")

#15 
print("A continuacion complete con hora, minutos y segundos, la hora de partida")
hh = int(input("Hora: "))
mm = int(input("Minutos: "))
ss = int(input("Segundos: "))
t = int(input("Ingrese en segundos cuanto tiempo es el viaje: "))

total_segundos = (hh * 3600)+ (mm * 60) + ss + t
#Separamos "total_segundos" y almacenamos la nueva hora
hh = total_segundos /3600
segundos_restantes = total_segundos % 3600
mm = segundos_restantes /60
ss = segundos_restantes % 60
print(f"La hora de llegada es {hh}:{mm}:{ss}")

#16
nombre =input( "Ingrese su nombre ")
primer_apellido =input( "Ingrese su primer_apellido ")
segundo_apellido =input( "Ingrese su segundo_apellido ")
inicales= (nombre[0]+primer_apellido[0]+segundo_apellido[0]).upper()
print (inicales )

#17
usuario =input( " Ingrese su nombre ")
print(f"Ahora estás en la matrix , [{usuario}]")

#18 
cena = float(input("Costo de la cena: "))
servicio = cena*0.062
propina = cena%0.1
total = cena + propina + servicio
print("El total a pagar es: ", total)

#19
dia=int(input("Ingrese su dia de nacimiento: "))
mes=int(input("Ingrese su mes de nacimiento: "))
anio=int(input("Ingrese su anio de nacimiento: "))
print("Su feche de nacimiento es: ", dia,"/", mes, "/",anio);

20
completo=input("Ingrese su dia de nacimiento: en el formato DDMMAAAA: "))
dia=completo[:2]
mes=completo[2:4]
anio=completo[4:]
print(f"Su día de nacimiento es {dia}/{mes}/{anio}")

#21
km_por_litro=int(input("cuantos kilometros puede recorrer su vehículo con 1 litro de combustible: "))
km_a_recorrer=int(input("cuantos kilometros van a recorrer?: "))
capacidad_del_tanque=int(input("de cuantos litros es su tanque?: "))
tanques=(km_a_recorrer/km_por_litro)/capacidad_del_tanque
print("necesitan ", tanques, " tanques de combustible")

