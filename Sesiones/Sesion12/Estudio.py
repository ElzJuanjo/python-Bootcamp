from Conexion import Conexion

class Estudio(Conexion):
    def __init__(self):
        super().__init__()
        self.CrearDB()
        
    def CrearDB(self):
        self.CrearTabla("Estudio","DatosEstudio")
        
    def AgregarUnDato(self,carrera="",inicio="",final="",horas=""):
        Datos=[
            (f"{carrera}",f"{inicio}",f"{final}",f"{horas}")
        ]       
        self.InsertarDatos("Estudio",4,Datos)