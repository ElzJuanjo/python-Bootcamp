from Hospital import Hospital
from Paciente import Paciente
from Conexion import Conexion

class Consulta(Hospital,Paciente,Conexion):
    def __init__(self,idC=0,fecha="",paciente=Paciente(),hospital=Hospital(),diagnostico=""):
        Hospital.__init__(self,hospital) # Metodo Super 1
        Paciente.__init__(self,paciente) # Metodo Super 2
        Conexion.__init__(self) # Metodo Super 3
        self.idC=idC # Id de la clase
        self.fecha=fecha
        self.paciente=paciente
        self.hospital=hospital
        self.diagnostico=diagnostico
        self.CrearTabla("Consultas","Consulta")
    
    def addDBConsultas(self):
        Datos=[
            (f"{self.idC}",f"{self.fecha}",f"{self.paciente.get_nombreP()}",f"{self.hospital.get_nombreH()}",
             f"{self.diagnostico}")
        ] 
        self.InsertarDatos("Consultas",5,Datos)
        print("DB :: Se agregaron datos en la tabla Consultas.")
        
    # Getter y Setter para idC
    def get_idC(self):
        return self.idC

    def set_idC(self, idC):
        self.idC = idC

    # Getter y Setter para fecha
    def get_fecha(self):
        return self.fecha

    def set_fecha(self, fecha):
        self.fecha = fecha

    # Getter y Setter para paciente
    def get_paciente(self):
        return self.paciente

    def set_paciente(self, paciente):
        self.paciente = paciente

    # Getter y Setter para hospital
    def get_hospital(self):
        return self.hospital

    def set_hospital(self, hospital):
        self.hospital = hospital

    # Getter y Setter para diagnostico
    def get_diagnostico(self):
        return self.diagnostico

    def set_diagnostico(self, diagnostico):
        self.diagnostico = diagnostico

    # Método __str__
    def __str__(self):
        return f"Consulta(idC={self.idC}, fecha={self.fecha}, paciente={self.paciente}, hospital={self.hospital}, diagnostico={self.diagnostico})"