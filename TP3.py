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

#23
amount_enter = 1
while amount_enter!= 0:
    amount_enter= float(input("Ingrese el monto de la compra: "))
print("Termino de cargar los montos")

#24 Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto. 
# Al finalizar, informar el total a pagar teniendo que cuenta que, si las ventas superan el total de $1000, 
# se le debe aplicar un 10% de descuento. 
print("Ingreese los montos, para calcular el total de su compra")
total_amount = 0
amount = 1
while amount > 0:
    amount = float(input("Ingrese el monto: "))
    total_amount += amount
else:
    print("-----Ingrese un monto prositivo-----")

if total_amount >1000:
    total_amount*0.9
print("El total a pagar es: ", total_amount)


