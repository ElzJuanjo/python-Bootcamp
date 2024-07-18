from Conexion import Conexion

class Desarrollador(Conexion):
    def __init__(self, devNombre="", habilidad=""):
        """| CONSTRUCTOR DEV |

        Args:
            devNombre (str): Nombre del desarrollador.
            habilidad (str): Habilidad del desarrollador.
        """
        Conexion.__init__(self)
        self.devNombre = devNombre
        self.habilidad = habilidad
        self.CrearDB()
        
    # FUNCIONES CRUD
    
    def CrearDB(self):
        self.CrearTabla("Developers","Desarrollador")
        
    def LeerDB(self):
        self.listaDeDatos = self.VerTodo("Developers")
        
    def EditarDB(self, nuevoDato, columna, id):
        if self.ActualizarDatos(nuevoDato,"Developers",columna,id):
            return True
        else:
            return False
        
    def EliminarDB(self, id):
        if self.EliminarDatos("Developers", id):
            return True
        else:
            return False
        
    def InsertarDB(self):
        datos = [
            (f"{self.devNombre}",f"{self.habilidad}")
        ]
        self.InsertarDatos("Developers",2,datos)