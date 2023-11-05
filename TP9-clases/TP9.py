from Persona import Persona
from Cuenta import Cuenta
from Triangulo import Triangulo

mi_person = Persona("Ornela", 18, 46473413)
edad = mi_person.es_mayor_de_edad()
print (edad)
mi_person.set_age(17)
mi_person.mostrar()

mi_count = Cuenta("Camila", 80000)
mi_count.ingresar(20000)
mi_count.mostrar()

lado1 = float(input("Ingrese el primer lado del triángulo: "))
lado2 = float(input("Ingrese el segundo lado del triángulo: "))
lado3 = float(input("Ingrese el tercer lado del triángulo: "))

tri = Triangulo(lado1, lado2, lado3)
tri.lado_mas_grande()
tri.determinar_tipo()