from Animal import Animal
class Pajaro(Animal):
    def __init__(self, color, habitat, movilidad, comunicacion, especie):
        self.especie=especie
        super().__init__(color, habitat, movilidad, comunicacion)
    def Caracteristicas(self):
        return f"| PAJARO |\nEspecie: {self.especie}"
    def Comer(self):
        print(f"A los {self.especie} le gustan los insectos")
    def Hablar(self):
        print(f"El {self.especie} está trinando")