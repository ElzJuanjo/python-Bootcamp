from Conexion import Conexion

class Habilidad(Conexion):
    def __init__(self):
        super().__init__()
        self.CrearDB()
        
    def CrearDB(self):
        self.CrearTabla("Habilidad","DatosHabilidad")
        
    def AgregarUnDato(self,tipo="",descripcion=""):
        Datos=[
            (f"{tipo}",f"{descripcion}")
        ]       
        self.InsertarDatos("Habilidad",2,Datos)