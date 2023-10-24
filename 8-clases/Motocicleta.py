class Motocicleta:
    new = True
    engine = False

    def __init__(self, color, enrollment, fuel_liters, number_wheels, brand, model, production_date,top_speed, weight):
        self.color = color
        self.enrollment = enrollment
        self.fuel_liters = fuel_liters
        self.number_wheels = number_wheels
        self.brand = brand
        self.model = model
        self.production_date = production_date
        self.top_speed = top_speed
        self.weight = weight

    def start_engire(self):
        if self.engine:
            print("El motor ya esta arrancado")
        else:
            self.engine = True
            print("Se arranco el motor")

    def stop_engire(self):
        if self.engine:
            self.engine = False
            print("El motor se freno")
        else:
            print("El motor ya esta frenado")

    def getPrice(self):
        print(f"El preio es {self.price}$")


