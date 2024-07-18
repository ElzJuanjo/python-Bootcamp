class Animal:
    def __init__(self, color, habitat, movilidad, comunicacion):
        self.color=color
        self.habitat=habitat
        self.movilidad=movilidad
        self.comunicacion=comunicacion
        
    def Morfologia(self):
        return f"Color: {self.color}\n"\
            f"Habitat: {self.habitat}\n"\
                f"Movilidad: {self.movilidad}\n"\
                    f"Comunicacion: {self.comunicacion}"
    def HacerHablar(self):
        self.Hablar()
    def HacerJugar(self):
        self.Jugar()
    def HacerComer(self):
        self.Comer()