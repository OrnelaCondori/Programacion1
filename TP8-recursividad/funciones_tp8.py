def digit_count(num):
    num_str = str(num)
    digits = len(num_str)
    return digits

def es_potencia(n, b):
    if n == 1:
        return True  # Cualquier número elevado a la potencia 0 es 1, por lo que es una potencia de sí mismo.
    potencia = b
    #Multiplicamoa hasta que el valor sea mayor o igual que b
    while potencia < n:
        potencia *= b
    #Devolvemos el valor veradadero o falso
    return potencia == n

def pos_string(frase,word, index=0):
    length_frase = len(frase)
    length_word = len(word)
    position=[]

    if index >= length_frase:  #Compruebo si llego al final de la frase
        return position
    else:
        pos = frase.find(word, index)
        if pos == -1:   #Si no escontro mas ocurrencias, devuelve las posiciones
            return position
        
        position.append(pos)  #Agrego el valor a la lista
        index = pos +length_word
        #acumula todas las listas de posiciones de cada llamada recursiva en una sola lista
        position+= pos_string(frase,word,index)
        #Despues de toda la recursividad, devolvemos los valores encontrados
        return position

def par(n):
    if n == 0:
        return True
    else:
        #Retornar el valor resultante
        return impar(n-1)

def impar(n):
    if n == 0:
        return False
    else:
        return par(n-1)

def largest_element(lista):
    if len(lista) == 1:
        return lista[0]
    
    # Divide la lista en dos mitades.
    mitad = len(lista) // 2
    izquierda = lista[:mitad]
    derecha = lista[mitad:]
    # Encuentra el mayor elemento en cada mitad de la lista.
    mayor_izquierda = largest_element(izquierda)
    mayor_derecha = largest_element(derecha)
    # Compara los mayores de ambas mitades y devuelve el mayor de ellos.
    return max(mayor_izquierda, mayor_derecha)

def replic_element(my_list, times, index=0):
    length_list = len(my_list)
    new_list = []
    if index >= length_list:
        return new_list
    else:
        number = my_list[index]
        for i in range(times):
            new_list.append(number)
        index += 1
        new_list += replic_element(my_list, times, index) 
        return new_list

def k(n,p):
    multi = p*n
    if n <= 0:
        return multi
    else:
        n-=1
        multi += k(n,p)
        return multi

def pascal(n, k):
    #Los bodes siempre son 1
    if n == 0 or k == 0:
        return 1
    else:
        #Calcular las sumatorias del triangulo
        return(pascal(n-1, k-1)+pascal(n-1, k))

def combinaciones(lista, k, prefix=""):
    if k == 0:
        print(prefix)  # Si hemos construido una cadena de longitud k, la imprimimos.
    else:
        for char in lista:
            # Generamos combinaciones recursivamente con un carácter menos y el carácter actual añadido al prefijo.
            combinaciones(lista, k - 1, prefix + char)

def hoja_a(N):
    # Caso base: A0
    if N <= 0:
        return (1189, 841)
    
    width_before, height_before = hoja_a(N-1)
    # Calcula las medidas de la hoja A(N) doblando al medio la hoja A(N-1)
    width = height_before
    height = width_before/2
    return (width, height)

