#1
corrimiento = int(input("Ingrese la cantidad de lugares con los que desea encriptar el mensaje: "))
abc = "abcdefghijklmnñopqrstuvwxyz"

#Repite por la cantidad de veces que se tienen que enviar mensajes
for i in range(5):
    mensaje_encri = " "
    mensaje= input("Ingrese el mensaje a encriptar: ")
    mensaje= mensaje.lower()

    #Por cada letra del mensaje
    for letra in mensaje:
        if letra in abc:
            #Cuando encuentre la posicion en la que se encuentra, suma los lugares y los guarda en una nueva variable
            pos = abc.find(letra)
            pos = (pos+corrimiento)%27
            letra = abc[pos]
            #Concatenamos las letras
            mensaje_encri+=letra
        else:
            #Para los caracteres que no son letras
            mensaje_encri+=letra
    print(mensaje_encri)

print("-----------------")

#2
total_pares = 0
total_impares = 0

while True:
    numero = int(input("Ingresa un número entero positivo: "))
    
    # Salir del ciclo si se ingresa 0
    if numero == 0:
        break
    # Contadores de pares e impares para cada número
    pares = 0
    impares = 0
    
    while numero > 0:
        digito = numero % 10
        if digito % 2 == 0:
            pares += 1
        else:
            impares += 1
        numero //= 10
    
    total_pares += pares
    total_impares += impares
    #resultados para cada número
    print(f"Dígitos pares: {pares}")
    print(f"Dígitos impares: {impares}")
#resultados finales
print(f"Total de dígitos pares: {total_pares}")
print(f"Total de dígitos impares: {total_impares}")
