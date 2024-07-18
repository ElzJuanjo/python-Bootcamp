from Conexion import Conexion

class Proyecto(Conexion):
    def __init__(self, projectNombre="", devID=0):
        """| CONSTRUCTOR PROJECT |

        Args:
            projectNombre (str): Nombre del Proyecto.
            devID (int): Identificador de el encargado del proyecto.
        """
        Conexion.__init__(self)
        self.projectNombre = projectNombre
        self.devID = devID
        self.CrearDB()
        
    # FUNCIONES CRUD
    
    def CrearDB(self):
        self.CrearTabla("Projects","Proyecto")
        
    def LeerDB(self):
        self.listaDeDatos = self.VerTodo("Projects")
        
    def EditarDB(self, nuevoDato, columna, id):
        if self.ActualizarDatos(nuevoDato,"Projects",columna,id):
            return True
        else:
            return False
        
    def EliminarDB(self, id):
        if self.EliminarDatos("Projects", id):
            return True
        else:
            return False
        
    def InsertarDB(self):
        datos = [
            (f"{self.projectNombre}",f"{self.devID}")
        ]
        self.InsertarDatos("Projects",2,datos)
        
    # FUNCION ESPECIAL PARA ELIMINAR TODOS LOS PROYECTOS DE UN DEVELOPER QUE SE ELIMINO
    
    def EliminarProyectosDev(self, devID=0):
        Info="DELETE FROM {} WHERE {}={}".format("Projects", "DEV_ID", devID)
        self.Pointer.execute(Info)              
        self.DB.commit()