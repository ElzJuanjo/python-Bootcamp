from Conexion import Conexion

class Laboral(Conexion):
    def __init__(self):
        super().__init__()
        self.CrearDB()
        
    def CrearDB(self):
        self.CrearTabla("Laboral","DatosLaboral")
        
    def AgregarUnDato(self,empresa="",inicio="",final="",cargo="",funciones=""):
        Datos=[
            (f"{empresa}",f"{inicio}",f"{final}",f"{cargo}",f"{funciones}")
        ]       
        self.InsertarDatos("Laboral",5,Datos)