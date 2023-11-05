class Cuenta:
    def __init__(self,titular, cantidad = 0.0):
        self.titular = titular
        self.cantidad = cantidad

    #Getters
    def get_titular(self):
        return self. titular
    def get_cantidad(self):
        return self. cantidad
    
    #Mostrar los datos del objeto
    def mostrar(self):
        print(f"Titular: {self.titular}")
        print(f"Cantidad: {self.cantidad}")

    def ingresar(self, valor):
        if valor <0 :
            print("El valor ingresado no es correcto")
        else:
            self.cantidad += valor
    
    def retirar(self, valor):
        self.cantidad -= valor