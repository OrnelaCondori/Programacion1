#1
word = input("Ingrese una palabra y se le mostrara 10 veces: ")
for i in range(10):
    print(word)

#2
birthday_year = int(input("Ingrese su edad: "))
for year in range(birthday_year+1):
    if year != 0:
        print(year)

#3
positive_num = int(input("Ingrese un número positivo: "))
odd_numbers = ""

for e in range (1,positive_num+1,1):
    if e%2!=0:
        odd_num = str(e)
        odd_numbers+=odd_num
        odd_numbers+=", "
print("Los números impares son: ", odd_numbers)

#4
num= int(input("Ingrese un número entero positivo: "))
for r in range(num, -1,-1):
    print(r, end=", ")
print(" ")

#5
investment=int(input("Ingrese cuanto desea invertir ")) 
annual_interest= int(input(" Cual es el interes anual ?  ")) 
year=int(input("Ingrese cuantos años desea invertir ")) 

for y in range(year): 
    annual_earnings=(investment*annual_interest)/100 
    investment+= annual_earnings 
    print( f" En el año { y+1 } el usuario gano un { annual_earnings}") 

#6
heigth= int(input("Ingrese un numero para la altura de su triangulo: ")) 
for i in range(heigth+1): 
    print(" ") 
    for j in range(i): 
        print("*",end=" ") 
print(" ") 

#7
for i in range(1,11): 
    print(" ")
    print(f"tabla del {i}: ")
    for j in range(1,11): 
        multiplo = i*j
        print(multiplo, end=" ")
print(" ")

#8
n=int(input("introduce la altura del triangulo (entero positivo):")) 
for i in range(1 , n+1 , 2): 
    for j in range(i, 0 ,-2): 
        print(j, end=" ") 
    print(" ")  

#9
password="contraseña" 
password2="u" 
while (password!=password2):  
    password2= input("ingrese la contraseña: ").lower() 

#10
while True:
    num = int(input("Ingrese un número positivo, para indicar si es o no primo: "))
    if num<=0:
        break

    divider = 0
    for i in range(num):
        if num%(i+1) == 0 :
            divider += 1
    
    if divider == 2:
        print("Es un número primo")
    else:
        print("No es primo")

#11
word=input("Ingrese una palabra: ")
for l in reversed(word):
    print(l)

#12
phrase=str(input("Ingrese una frase: ")) 
letter=input("Ingrese la letra que quiere buscar: ") 

count=phrase.count(letter) 
print(f"La letra elegida se repite {count} de veces en la frase escrita")

#13
word='' 
while word!='salir': 
    word=str(input("Escriba algo: ")).lower() 
    echo=word
    print(f"Eco: {echo}")

#14
number=int(input("Ingrese un numero: ")) 
number_2=int(input("Ingrese otro numero: ")) 
print(f"Vamos a ver si los numeros que se encuentran entre {number} y {number_2} son pares o impares: ") 
for i in range(number,number_2+1): 
    if i %2==0: 
        print(f"Numero par: {i}") 
    else: 
        print(f"Numero impar: {i}")  

#15
while True: 
    divider = ""
    num = int(input("Escriba el numero del cual quiere conocer sus divisores: ")) 
    if num <= 0: 
        break 
    for i in range(1,num):  
        if num%(i) == 0: 
            divider +=i 
            divider+= " "
            print("los divisores de ",num, "son: ", divider) 

#16
amount = int(input("indique cuantos numeros va ingresar: ")) 
negative = 0 
for i in range(amount): 
    num = int(input("ingrese el numero: ")) 
    if num < 0: 
        negative +=1 
print("se han introducido: ", negative, " numeros negativos") 

#17
phrase = (input("ingrese una frase: ")).lower() 
print("Vocales que aparecen: ")
vowel = "aeiou" 
for i in vowel: 
    if i in phrase:  
            print(i) 

#18 
print("Secuencia Fibonacci: ")
anterior1 = 0
anterior2 = 1
secuencia = "0 1 "
for i in range(9) :
    nuevo = anterior1 +anterior2
    anterior1 = anterior2
    anterior2 = nuevo
    num3 = str(nuevo)
    secuencia += num3
    secuencia += " "
print(secuencia)

#19
objetive=int(input("ingrese la cantidad de dinero que desa ahorrar: ")) 
save = 0
while (save<=objetive): 
    money=int(input("Cuanto vas a ingresar?")) 
    if (money>=0): 
        save+=money 
        print(save) 
    else: 
        print("no se pueden ingresar numeros negativos")
        continue 
print("objetivo alcanzado") 

#20
addition=0 
num=1 

while (num!=0): 
    num=int(input("ingrese un numero distinto de 0: ")) 
    addition+=num 
print("la sumatoria de los numeros ingresados es: ", addition) 

#21
number=1 
max=0 
while (number!=0): 
    number=int(input("ingrese un numero distirnto a 0: ")) 
    if(number>max): 
        max=number 
print("El mayor numero ingresado es: ", max) 

#22
number=0 
addition=0 
addition_2=0 
while(number!=-1): 
    number=int(input("Ingrese un numero, para salir ingrese '-1': ")) 
    if (number>=0): 
        for n in str(number): 
            n=int(n) 
            addition+=n 
        print(addition) 
    else: 
        print("el numero ingresado debe ser positivo") 
    if (number % 2==0): 
        addition_2+=1 
print("la cantidad de numeros ingresados pares son: ", addition_2) 

#23
amount_enter = 1
while amount_enter!= 0:
    amount_enter= float(input("Ingrese el monto de la compra: "))
print("Termino de cargar los montos")

#24 
print("Ingreese los montos, para calcular el total de su compra")
total_amount = 0
while True:
    amount = float(input("Ingrese el monto(Ingrese un valor negativo para salir): "))

    if amount < 0:
        print("Monto inválido. Por favor, ingrese un nuevo monto.")
        continue
    
    total_amount += amount
    if total_amount > 1000:
        total_amount *= 0.9
    if amount == 0:
        break
print("El total a pagar es: $" + str(total_amount))

#25
number = int(input("Ingrese un número entero positivo: "))
factorial = 1
if number < 0:
    print("El número ingresado debe ser positivo.")
elif number == 0:
    print("El factorial de 0 es 1.")
else:
    for i in range(1, number + 1):
        factorial *= i
    
    print("El factorial de", number, "es", factorial)
