class Persona:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
    

    def get_name(self):
        return self. name
    def set_name(self, valor):
        self.name = valor
    
    def get_age(self):
        return self. age
    def set_age(self, valor):
        self.age = valor

    def get_id(self):
        return self. id
    def set_id(self, valor):
        self.id = valor

    def mostrar(self):
        print(f"Nombre: {self.name}")
        print(f"Edad: {self.age}")
        print(f"DNI: {self.id}")

    def es_mayor_de_edad(self):
        if self.age>=18:
            return True
        else:
            return False


