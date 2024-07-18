import sqlite3
import json

class Conexion:
    def __init__(self):
        self.DB=sqlite3.connect("./Sesiones/Parcial1/DataBase.sqlite")
        self.Pointer=self.DB.cursor()
        self.ObtenerQuerys()
        
    def ObtenerQuerys(self):
        with open("./Sesiones/Parcial1/Queries.json","r") as File:
            self.Querys=json.load(File)
            
    def BuscarId(self, ID, Tabla):
        Seleccionar=self.Querys["VerDatos"].format(Tabla,"ID",ID)
        self.Pointer.execute(Seleccionar)
        resultado = self.Pointer.fetchone()[0]   
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
                print("DB :: Esta ID no se encuentra.")  
                return False
        else:
            print("DB :: No puede dejar un campo vacio.")  
            return False      
    
    def EliminarDatos(self, Tabla="", ID=0):
        if Tabla!="" and ID!=0:
            if(self.BuscarId(ID, Tabla)):
                Info=self.Querys["EliminarDatos"].format(Tabla,"ID",ID)
                self.Pointer.execute(Info)                    
                self.DB.commit()
                return True
            else:
                print("DB :: Esta ID no se encuentra.")  
                return False
        else:
            print("DB :: No puede dejar un campo vacio.")  
            return False