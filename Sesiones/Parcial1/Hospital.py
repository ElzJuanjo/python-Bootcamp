from Conexion import Conexion

class Hospital(Conexion):
    def __init__(self,idH=0,nombreH="",direccion="",telefono="",especialidades=[],director="",capacidad=0):
        super().__init__()
        self.idH=idH # Id de la clase
        self.nombreH=nombreH
        self.direccion=direccion
        self.telefono=telefono
        self.especialidades=especialidades
        self.director=director
        self.capacidad=capacidad
        self.CrearTabla("Hospitales","Hospital")

    def addDBHospitales(self):
        concatenar = ','.join(self.especialidades)
        Datos=[
            (f"{self.idH}",f"{self.nombreH}",f"{self.direccion}",f"{self.telefono}",f"{concatenar}",
             f"{self.director}",f"{self.capacidad}")
        ] 
        self.InsertarDatos("Hospitales",7,Datos)
        print("DB :: Se agregaron datos en la tabla Hospitales.")
                
    # Getter y Setter para idH
    def get_idH(self):
        return self.idH

    def set_idH(self, idH):
        self.idH = idH

    # Getter y Setter para nombreH
    def get_nombreH(self):
        return self.nombreH

    def set_nombreH(self, nombreH):
        self.nombreH = nombreH

    # Getter y Setter para direccion
    def get_direccion(self):
        return self.direccion

    def set_direccion(self, direccion):
        self.direccion = direccion

    # Getter y Setter para telefono
    def get_telefono(self):
        return self.telefono

    def set_telefono(self, telefono):
        self.telefono = telefono

    # Getter y Setter para especialidades
    def get_especialidades(self):
        return self.especialidades

    def set_especialidades(self, especialidades):
        self.especialidades = especialidades

    # Getter y Setter para director
    def get_director(self):
        return self.director

    def set_director(self, director):
        self.director = director

    # Getter y Setter para capacidad
    def get_capacidad(self):
        return self.capacidad

    def set_capacidad(self, capacidad):
        self.capacidad = capacidad

    # Método __str__
    def __str__(self):
        return f"Hospital(idH={self.idH}, nombreH={self.nombreH}, direccion={self.direccion}, telefono={self.telefono}, especialidades={self.especialidades}, director={self.director}, capacidad={self.capacidad})"