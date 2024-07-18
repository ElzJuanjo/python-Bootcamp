import sqlite3
import json

class Conexion:
    def __init__(self):
        self.DB=sqlite3.connect("./Tkinter/Peliculas/DataBase.sqlite")
        self.Pointer=self.DB.cursor()
        self.ObtenerQuerys()
        
    def ObtenerQuerys(self):
        with open("./Tkinter/Peliculas/Queries.json","r") as File:
            self.Querys=json.load(File)
            
    def BuscarId(self, ID, Tabla):
        Seleccionar=self.Querys["VerDatos"].format(Tabla,"ID",ID)
        self.Pointer.execute(Seleccionar)
        resultado = self.Pointer.fetchone()[0]   
        return resultado   

    def VerTodo(self, Tabla):
        Seleccionar=self.Querys["SeleccionarTodo"].format(Tabla)
        self.Pointer.execute(Seleccionar)
        resultado = self.Pointer.fetchall()
        return resultado    
       
    def CrearTabla(self,Nombre="",Query=""):
        if Nombre!="" and Query!="":
            Info=self.Querys["CrearTabla"].format(Nombre,self.Querys[Query])
            self.Pointer.execute(Info)
            self.DB.commit()
        else:
            print("DB :: No puede dejar un campo vacio.")
    
    def InsertarDatos(self,Tabla="",Columns=0,Values=""):
        if Tabla!="" and Values!="":
            Info=self.Querys["InsertarDatos"].format(Tabla,', '.join(['?'] * Columns))
            self.Pointer.executemany(Info,Values)
            self.DB.commit()
        else:
            print("DB :: No puede dejar un campo vacio.")  
            
    def ActualizarDatos(self, NuevoDato, Tabla="", Columna="", ID=0):
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