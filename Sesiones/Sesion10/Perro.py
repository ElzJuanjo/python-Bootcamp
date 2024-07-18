from Animal import Animal
class Perro(Animal):
    def __init__(self, color, habitat, movilidad, comunicacion, raza, nombre):
        self.raza=raza
        self.nombre=nombre
        super().__init__(color, habitat, movilidad, comunicacion)
        
    def Caracteristicas(self):
        return f"| PERRO |\nRaza: {self.raza}\nNombre: {self.nombre}"
    def Jugar(self):
        print(f"{self.nombre} Se puso a jugar con la pelota")
    def Comer(self):
        print(f"A {self.nombre} le gustan los huesos")
    def Hablar(self):
        print(f"{self.nombre} dijo !GUAU!")