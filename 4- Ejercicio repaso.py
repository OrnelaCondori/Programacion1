product_list=[]
position =0
discount= 0.1

print(" A continuacion complete con los produtos de su lista de compra: ")
print("------ lista de compras---------")
while True:
    add_product_list =int(input("Agregar producto?       1.SI / 2.NO : "))
    if add_product_list == 1 :
        product = input("Ingrese el producto: ")
        product_list.append(product.upper())
    elif add_product_list == 2 :
        print("Termino de completar su lista de compras")
        print(" ")
        break
    else:
        print("La opcion ingresada no corresponde a ninguna de las solicitadas")
        continue

total_price = 0
print ("---------en el supermercado----------")
for p in product_list:
    print("Conseguiste el producto: ", p , "?")
    find_product =int(input(" 1.SI / 2.NO : "))
    #para verificar que la opcion ingresada sea la correcta
    if (find_product!=1) and (find_product!=2):
        while find_product!=1 or find_product !=2:
            print("La opcion ingresada no es válida, ingrese la opcion elegida nuevamente")
            find_product =int(input(" 1.SI / 2.NO : "))
    elif find_product == 1:
            product_price= int(input("Ingrese el precio del producto: $"))
    else:
        #Si caxmbia el producto, el nuevo se guarda en esa posicion
        change_product= int(input("Desea remplazarlo?       1.SI / 2.NO : "))
        if change_product == 1:
            product=input("Ingrese el nuevo producto : ")
            product_list[position]=product
            product_price= int(input("Ingrese el precio del producto: $"))
        else:
            continue
    #utilizamos position para poder indicar la posicion del array, ya que "p" tiene un valor de string
    position+=1
    total_price+=product_price
print(" ")

print ("---------en la caja----------")
type_of_pay= int(input("Indique si desea pagar en efectivo      1.SI / 2.NO : "))
if type_of_pay!=1 and type_of_pay!=2:
    while type_of_pay!=1 or type_of_pay!=2:
        print("La opcion ingresada no es válida, ingrese la opcion elegida nuevamente")
        type_of_pay =int(input(" 1.SI / 2.NO : "))
elif type_of_pay == 1:
    total_price-= total_price*discount
    print("Aplicando el descuento su total a pagar es $", total_price)
else:
    print("El total a pagar es $",total_price)


