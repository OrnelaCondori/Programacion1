
def letter_find(palabra, palabra_a_adivinar, letra):
    cant_letras = int(len(palabra))
    # Convierto palabra_a_adivinar a una lista mutable
    palabra_a_adivinar_lista = list(palabra_a_adivinar)

    for i in range(cant_letras):
        #compara la posicion en la que se encuentra la letra en la palabra original
        if palabra[i]==letra:
            #y la remplaza en la palabra que esta adivinando el jugador
            palabra_a_adivinar_lista[i] = letra
        else:
            continue
    #el resultado de remplazar las letras, se guarda en una nueva variable, convierto la lista a una cadena
    palabra_encontrada = ''.join(palabra_a_adivinar_lista)
    #Se devuelve la variable
    return palabra_encontrada


import random
user_attempts = 6
word_list = ["variables", "terminal", "computadora", "programa"]
#El progrma selecciona aleatoramente la palabra con la que va a jugar el usuario
word_selected = word_list[random.randint(0, len(word_list))]
word_guess=""

#guarda en otra variable la palabra a adivinar (comienza "imcompleta")
for i in range(len(word_selected)):
    word_guess += "_"

print("----------------------------------------")
print("COMENCEMOS A JUGAR:")
print(f"Posee {user_attempts} intentos\n  ")
print(f"La palabra a adivinar tiene {len(word_guess)} letras: {word_guess}")
print("----------------------------------------")

while True:
    if (user_attempts == 0):
        print(" \n----------------------------------------")
        print("Te quedaste sin intentos")
        print(f"La palabra era: {word_selected}")
        print("----------------------------------------")
        break

    letter = input(" \nIngrese una letra: ")
    letter= letter.lower()

    #Lo comparo con -1, porque es el resultado que da en caso de que find sea falso
    if word_selected.find(letter) != -1:
        print("  :) La letra es correcta!")
        word = letter_find(word_selected, word_guess, letter)
    else:
        print("  ! La no es correcta - pierdes un intento")
        user_attempts-=1
    #La nueva palabra con las letras cambiadas se guarda en la variable que completa el usuario
    #Para que en las repeticiones siga trabajando con esta
    word_guess = word
    print(f"  Palabra actual: {word_guess}")

    if word_guess == word_selected:
        print(" \n----------------------------------------")
        print("CORRECTO! adivinaste la palabra")
        print("----------------------------------------")
        break
