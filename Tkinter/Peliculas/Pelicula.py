from Conexion import Conexion

class Pelicula(Conexion):
    def __init__(self, nombre="", duracion="", genero=""):
        Conexion.__init__(self)
        self.nombre=nombre
        self.duracion=duracion
        self.genero=genero
        self.crearDB()
        
    def crearDB(self):
        self.CrearTabla("Peliculas","Pelicula")
        
    def insertarDato(self):
        datos=[
            (f"{self.nombre}",f"{self.duracion}",f"{self.genero}")
        ] 
        self.InsertarDatos("Peliculas",3,datos)
        
    def verTabla(self):
        self.datosEnDB = self.VerTodo("Peliculas")