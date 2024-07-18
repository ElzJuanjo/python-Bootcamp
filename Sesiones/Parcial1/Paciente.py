from Conexion import Conexion

class Paciente(Conexion):
    def __init__(self,idP=0,nombreP="",apellidoP="",dniP="",fechaNacimiento="",grupoSanguineo="",historiaMedica=""):
        super().__init__()
        self.idP=idP # Id de la clase
        self.nombreP=nombreP
        self.apellidoP=apellidoP
        self.dniP=dniP
        self.fechaNacimiento=fechaNacimiento
        self.grupoSanguineo=grupoSanguineo
        self.historiaMedica=historiaMedica
        self.CrearTabla("Pacientes","Paciente")
        
    def addDBPacientes(self):
        Datos=[
            (f"{self.idP}",f"{self.nombreP}",f"{self.apellidoP}",f"{self.dniP}",
             f"{self.fechaNacimiento}",f"{self.grupoSanguineo}",f"{self.historiaMedica}")
        ] 
        self.InsertarDatos("Pacientes",7,Datos)
        print("DB :: Se agregaron datos en la tabla Pacientes.")
           
    # Getter y Setter para idP
    def get_idP(self):
        return self.idP

    def set_idP(self, idP):
        self.idP = idP

    # Getter y Setter para nombreP
    def get_nombreP(self):
        return self.nombreP

    def set_nombreP(self, nombreP):
        self.nombreP = nombreP

    # Getter y Setter para apellidoP
    def get_apellidoP(self):
        return self.apellidoP

    def set_apellidoP(self, apellidoP):
        self.apellidoP = apellidoP

    # Getter y Setter para dniP
    def get_dniP(self):
        return self.dniP

    def set_dniP(self, dniP):
        self.dniP = dniP

    # Getter y Setter para fechaNacimiento
    def get_fechaNacimiento(self):
        return self.fechaNacimiento

    def set_fechaNacimiento(self, fechaNacimiento):
        self.fechaNacimiento = fechaNacimiento

    # Getter y Setter para grupoSanguineo
    def get_grupoSanguineo(self):
        return self.grupoSanguineo

    def set_grupoSanguineo(self, grupoSanguineo):
        self.grupoSanguineo = grupoSanguineo

    # Getter y Setter para historiaMedica
    def get_historiaMedica(self):
        return self.historiaMedica

    def set_historiaMedica(self, historiaMedica):
        self.historiaMedica = historiaMedica

    # Método __str__
    def __str__(self):
        return f"Paciente(idP={self.idP}, nombreP={self.nombreP}, apellidoP={self.apellidoP}, dniP={self.dniP}, fechaNacimiento={self.fechaNacimiento}, grupoSanguineo={self.grupoSanguineo}, historiaMedica={self.historiaMedica})"