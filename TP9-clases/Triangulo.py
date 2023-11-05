class Triangulo:
    def __init__(self, lado_1, lado_2, lado_3):
        self.lado_1 = lado_1
        self.lado_2 = lado_2
        self.lado_3 = lado_3
    
    def lado_mas_grande(self):
        mayor = max(self.lado1, self.lado2, self.lado3)
        print(f"El lado con tamaño mayor es: {mayor}")

    def determinar_tipo(self):
        if self.lado1 == self.lado2 == self.lado3:
            print("El triángulo es equilátero")
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            print("El triángulo es isósceles")
        else:
            print("El triángulo es escaleno")
