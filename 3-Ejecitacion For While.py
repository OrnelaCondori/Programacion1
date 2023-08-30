#1
lugares = int(input("Ingrese la cantidad de lugares con los que desea encpiptar el mensaje: "))
abc = "abcdefghijklmnñopqrstuvwxyz"
for i in range(5):
    mensaje_encri = " "
    mensaje= input("Ingrese el mensaje a enscriptar: ")
    for letra in mensaje:
        if letra in abc:
            pos = abc.find(letra)
            pos = (pos+lugares)%27
            letra = abc[pos]
            mensaje_encri+=letra
    print(mensaje_encri)


#2

#num= 1
#while num != 0:
#    num = input("Ingrese un número: ")
#    posi = 