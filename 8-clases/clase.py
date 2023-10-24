from Motocicleta import Motocicleta

my_motocicleta = Motocicleta("Rojo", "1234XYZ", 10, 2, "Honda", "CBR1000RR", "2023-01-15", 280, 200)
motocicleta2 = Motocicleta("Negro", "4564XYZ", 8, 2, "Honda", "PBR1000MM", "2023-04-16", 250, 200)

#Uso de metodos
my_motocicleta.start_engire()
motocicleta2.stop_engire()

#Creacion de atributo
my_motocicleta.price = 130000
# "El precio de la motocicleta 'x (marca y modelo)' es de 'x_precio' $."
print(f"El precio de la motocicleta: marca={my_motocicleta.brand} y modelo={my_motocicleta.model} es de {my_motocicleta.price}$.")
#Metodo para obtener precio
my_motocicleta.getPrice()
#El segundo objeto no tiene el atributo declarado en la clase ni en el objeto, asiq marca un error, porque no existe
motocicleta2.getPrice()