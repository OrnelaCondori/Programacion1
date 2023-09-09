#1
x = int(0)
while x <30 :
    x = x+1
    if x== 15:
        print("The execution of the loop was broken when x was " , x)
        break
    if (x==4) or (x==6) or (x==10):
        print('The value ', x ,' of x was skipped')
        continue

    print('The value of the loop is: ', x)

#2
# Escriba un programa que acepte una secuencia de líneas e imprima todas las líneas convertidas en mayúsculas. Deje una línea en blanco para indicar que ha finalizado la entrada de líneas.