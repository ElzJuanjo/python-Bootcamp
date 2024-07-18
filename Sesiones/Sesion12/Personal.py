from Conexion import Conexion

class Personal(Conexion):
    def __init__(self):
        super().__init__()
        self.CrearDB()
        
    def CrearDB(self):
        self.CrearTabla("Personal","DatosPersonal")
        
    def AgregarUnDato(self,nombre1="",nombre2="",apellido1="",apellido2="",documento="",celular="",correo=""):
        Datos=[
            (f"{nombre1}",f"{nombre2}",f"{apellido1}",f"{apellido2}",f"{documento}",f"{celular}",f"{correo}")
        ]       
        self.InsertarDatos("Personal",7,Datos)