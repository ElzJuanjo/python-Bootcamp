import sqlite3
import json

class Conexion:
    def __init__(self):
        self.DB=sqlite3.connect("./Sesiones/3erEntregable/DataBase.sqlite")
        self.Pointer=self.DB.cursor()
        self.ObtenerQuerys()
        
    def ObtenerQuerys(self):
        with open("./Sesiones/3erEntregable/Queries.json","r") as File:
            self.Querys=json.load(File)
            
    def BuscarId(self, ID, Tabla):
        """| BUSCAR ID |

        Args:
            ID (int): ID que se desea buscar en la tabla.
            Tabla (str): Tabla en el que se desea buscar la ID.

        Returns:
            bool: True si se encuentra o False si no se encuentra.
        """
        Seleccionar=self.Querys["VerDatos"].format(Tabla,"ID",ID)
        self.Pointer.execute(Seleccionar)
        resultado = self.Pointer.fetchone()[0]   
        return resultado   

    def VerTodo(self, Tabla):
        """| VER TABLA |

        Args:
            Tabla (str): Tabla que se desea obtener.

        Returns:
            list: Elementos de la tabla.
        """
        Seleccionar=self.Querys["SeleccionarTodo"].format(Tabla)
        self.Pointer.execute(Seleccionar)
        resultado = self.Pointer.fetchall()
        return resultado    
       
    def CrearTabla(self,Nombre="",Query=""):
        """| CREAR TABLA |

        Args:
            Nombre (str): Nombre que tendra la tabla a crear.
            Query (str): Nombre del query que esta en el json para las columnas.
        """
        if Nombre!="" and Query!="":
            Info=self.Querys["CrearTabla"].format(Nombre,self.Querys[Query])
            self.Pointer.execute(Info)
            self.DB.commit()
        else:
            print("DB :: No puede dejar un campo vacio.")
    
    def InsertarDatos(self,Tabla="",Columns=0,Values=""):
        """| INSERTAR DATOS |

        Args:
            Tabla (str): Nombre de la tabla donde se agregaran los datos.
            Columns (int): Cantidad de columnas que posee la tabla.
            Values (str): Valores que se asignaran en el nuevo dato.
        """
        if Tabla!="" and Values!="":
            Info=self.Querys["InsertarDatos"].format(Tabla,', '.join(['?'] * Columns))
            self.Pointer.executemany(Info,Values)
            self.DB.commit()
        else:
            print("DB :: No puede dejar un campo vacio.")  
            
    def ActualizarDatos(self, NuevoDato, Tabla="", Columna="", ID=0):
        """| ACTUALIZAR DATOS |

        Args:
            NuevoDato (str): Dato por el que se cambiara en la tabla.
            Tabla (str): Nombre de la tabla donde se cambiara el dato.
            Columna (str): Nombre de la columna donde se cambiara el dato.
            ID (int): Numero del ID donde se cambiara el dato.

        Returns:
            bool: True si se cambio correctamente o False si hubo algun fallo.
        """
        if Tabla!="" and ID!=0:
            if(self.BuscarId(ID, Tabla)):
                Info=self.Querys["ActualizarDatos"].format(Tabla,Columna,NuevoDato,"ID",ID)
                self.Pointer.execute(Info)                    
                self.DB.commit()
                return True
            else:
                return False
        else:
            return False      
    
    def EliminarDatos(self, Tabla="", ID=0):
        """| ELIMINAR DATOS |

        Args:
            Tabla (str): Nombre de la tabla donde se eliminara el dato.
            ID (int): Numero del ID donde se eliminara el dato.

        Returns:
            bool: True si se cambio correctamente o False si hubo algun fallo.
        """
        if Tabla!="" and ID!=0:
            if(self.BuscarId(ID, Tabla)):
                Info=self.Querys["EliminarDatos"].format(Tabla,"ID",ID)
                self.Pointer.execute(Info)                    
                self.DB.commit()
                return True
            else:
                return False
        else:
            return False
        
    def CerrarDB(self):
        self.DB.commit()
        self.DB.close()