from Consulta import Consulta
from Conexion import Conexion

class Medico(Consulta, Conexion):
    def __init__(self,idM=0,nombreM="",apellidoM="",dniM="",especialidad="",matricula="",aniosExperiencia=0):
        Consulta.__init__(self) # Metodo Super 1
        Conexion.__init__(self) # Metodo Super 2
        self.idM=idM # Id de la clase
        self.nombreM=nombreM
        self.apellidoM=apellidoM
        self.dniM=dniM
        self.especialidad=especialidad
        self.matricula=matricula
        self.aniosExperiencia=aniosExperiencia 
        self.CrearTabla("Medicos","Medico")

    def addDBMedicos(self):
        Datos=[
            (f"{self.idM}",f"{self.nombreM}",f"{self.apellidoM}",f"{self.dniM}",
             f"{self.especialidad}",f"{self.matricula}",f"{self.aniosExperiencia}")
        ] 
        self.InsertarDatos("Medicos",7,Datos)
        print("DB :: Se agregaron datos en la tabla Medicos.")
                
    # Getter y Setter para idM
    def get_idM(self):
        return self.idM

    def set_idM(self, idM):
        self.idM = idM

    # Getter y Setter para nombre
    def get_nombreM(self):
        return self.nombreM

    def set_nombreM(self, nombreM):
        self.nombreM = nombreM

    # Getter y Setter para apellido
    def get_apellidoM(self):
        return self.apellidoM

    def set_apellidoM(self, apellidoM):
        self.apellidoM = apellidoM

    # Getter y Setter para dni
    def get_dniM(self):
        return self.dniM

    def set_dniM(self, dniM):
        self.dniM = dniM

    # Getter y Setter para especialidad
    def get_especialidad(self):
        return self.especialidad

    def set_especialidad(self, especialidad):
        self.especialidad = especialidad

    # Getter y Setter para matricula
    def get_matricula(self):
        return self.matricula

    def set_matricula(self, matricula):
        self.matricula = matricula

    # Getter y Setter para aniosExperiencia
    def get_aniosExperiencia(self):
        return self.aniosExperiencia

    def set_aniosExperiencia(self, aniosExperiencia):
        self.aniosExperiencia = aniosExperiencia

    # Getter y Setter para consultas
    def get_consultas(self):
        return self.consultas

    def set_consultas(self, consultas):
        self.consultas = consultas

    # Método __str__
    def __str__(self):
        return f"Medico(idM={self.idM}, nombre={self.nombre}, apellido={self.apellido}, dni={self.dni}, especialidad={self.especialidad}, matricula={self.matricula}, aniosExperiencia={self.aniosExperiencia}, consultas={self.consultas})"     