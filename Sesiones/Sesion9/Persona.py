from Estudio import Estudio
from Habilidad import Habilidad

class Persona:
    def __init__(self,primernombre,segundonombre,apellido,nacionalidad,telefono,email):
        self.primernombre=primernombre
        self.segundonombre=segundonombre
        self.apellido=apellido
        self.nacionalidad=nacionalidad
        self.telefono=telefono
        self.email=email       
        
    def __str__(self):
        return f"Primer nombre: {self.primernombre}\n"\
            f"Segundo nombre: {self.segundonombre}\n"\
                f"Apellido: {self.apellido}\n"\
                    f"Nacionalidad: {self.nacionalidad}\n"\
                        f"Telefono: {self.telefono}\n"\
                            f"Email: {self.email}"
                            
    def setHabilidad(self, tipo, nivel, id):
        self.habilidad=Habilidad(tipo,nivel,id)
    def setEstudio(self, titulo, inicio, fin, horas):
        self.estudio=Estudio(titulo,inicio,fin,horas)
    def getHabilidad(self):
        print(self.habilidad)
    def getEstudio(self):
        print(self.estudio)