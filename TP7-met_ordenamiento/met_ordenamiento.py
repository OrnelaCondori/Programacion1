def selection_sort(arr):
    n = len(arr)
    #Para ubicar en cada posicion
    for i in range(n-1):
        #La posicion del valor mínimo
        min_index = i
        for j in range(i+1, n):
            #si la posicion siguiente es menor, guarda su posicion
            if arr[j] < arr[min_index]:
                min_index = j
        #guarda en el lugar correspondiente a los valores pequeños
        arr[i], arr[min_index] = arr[min_index], arr[i]

def bubble_sort(arr):
    n = len(arr)
    #la cantidad e veces que recorremos el array 
    for i in range (n-1):
        #Comparacion e intercabios
        for j in range(n-1):
            if arr[j] >arr[j+1]:
                temp = arr[j]
                arr[j]=arr[j+1]
                arr[j+1] = temp
    return arr

def insertion_sort(arr):
    #permite ordenar listas
    n = len(arr)
    #Considera la primer pos ordenada, compara desde la segunda hacia atras
    for i in range(1, n):
        #guarda el valor con el que esta comparando
        key = arr[i]
        j = i - 1
        #que el indice sea mayor que 0, y compara en reversa
        while j >= 0 and arr[j] > key:
            #Desplazamos el valor
            arr[j + 1] = arr[j]
            #Disminuir a posicion
            j -= 1
        arr[j + 1] = key
    return arr

def len_insert_sort(arra):
    for i in range (len(arra)):
        actual=arra[i]
        j=i-1
        while j>=0  and len(actual)< len(arra[j]):
            arra[j+1]=arra[j]
            j-=1
        arra[j + 1] = actual

def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        #Itera de la mitad de la lista al ultimo elemento
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                #Indica cuantas posiciones antes
                j -= gap
            arr[j] = temp
        #Luego disminuye el intervalo
        gap //= 2

def autor_sort(arra):
    n = len(arra)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arra[j]["autor"] > arra[j + 1]["autor"]:
                arra[j], arra[j + 1] = arra[j + 1], arra[j]

def des_bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def count_sort(array):
    count_list=[0 for i in range(10)]
    output=[0 for i in range(len(array))]
    
    for i in array:
        count_list[i]+=1
    for i in range(1,10):
        count_list[i]+=count_list[i-1]
    for i in range(len(array)):
        output[count_list[array[i]]-1]=array[i]
        count_list[array[i]]-=1
    return output

def order_by_type(array):
    for j in range(len(array)):
        for i in range(0, len(array) - j - 1):
            if type(array[i +1]) is not str:
                if type(array[i]) is str:
                    array[i],array[i+1]=array[i+1],array[i] 
            if type(array[i +1]) is type(array[i]):
                if array[i]>array[i+1]:
                    array[i],array[i+1]=array[i+1],array[i] 

def merge_sort(array):
    if len(array) <= 1:
        return array
    middle = len(array) // 2
    left_array = array[:middle]
    right_array = array[middle:]

    sorted_left_array = merge_sort(left_array)
    sorted_right_array = merge_sort(right_array)
    return merge(sorted_left_array, sorted_right_array)

def merge(left_arr, right_arr):
    result = []
    left_index, right_index = 0, 0

    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            result.append(left_arr[left_index])
            left_index += 1
        else:
            result.append(right_arr[right_index])
            right_index += 1

    result.extend(left_arr[left_index:])
    result.extend(right_arr[right_index:])

    return result

