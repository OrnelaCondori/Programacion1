import random
#1 
word = input("Ingrese una palabra: ")
if (len(word) == 4):
    word+="!"
else:
    word+="?"
print(word)

#2
lista_palabras=["perro", "tetera", "casa", "vaso", "buzon", "aeropuerto"]
palabra_azar = random.randint(0, len(lista_palabras)-1)

# for i in lista_palabras[palabra_azar]:
#     print("Para adivinar la letra, a continuacion complete: (tiene 3 intentos por letra): ")
#     intento = 1
#     while True:
#         while True:
#             letra_ingresada = input(f"Intento {intento} : ")
#             intento +=1
#             if intento == 3:
#                 break
#             if(letra_ingresada == i):
#                 print("Letra adivinada! ")
#             else:
#                 print("Intenta de nuevo")
#                 continue

#3
frase = input("Ingrese una frase: ")
cant_palabras = 0

if len(frase)> 0:
    cant_palabras+=1
for i in frase:
    if i == " ":
        cant_palabras+=1
print("La cantidad de palabras es: ", cant_palabras)

frase=input("Ingrese una cadena de texto y se devolveran cuantas palabras hay ")
if len(frase)>0:
    before=False
    cont_words=1
    for i in frase:
        if i==" ":
            if before:
                continue
            else:
                cont_words+=1
                before=True
        else:
            if i==" ":
                continue
            else:
                before=False
    print(f" la cantidad de palabras de la frase {frase} es de {cont_words}")
