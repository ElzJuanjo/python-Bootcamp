import sqlite3
import json
import pandas as pd

class Conexion:
    def __init__(self):
        self.DB=sqlite3.connect("./Sesiones/Sesion12/DataBase.sqlite")
        self.Pointer=self.DB.cursor()
        self.ObtenerQuerys()
        
    def ObtenerQuerys(self):
        with open("./Sesiones/Sesion12/Querys.json","r") as File:
            self.Querys=json.load(File)
    
    def CrearTabla(self,Nombre="",Query=""):
        if Nombre!="" and Query!="":
            Info=self.Querys["CrearTabla"].format(Nombre,self.Querys[Query])
            self.Pointer.execute(Info)
            self.DB.commit()
            print(f"DB :: Se ha creado '{Nombre}' con exito.")
        else:
            print("DB :: No puede dejar un campo vacio.")
    
    def InsertarDatos(self,Tabla="",Columns=0,Values=""):
        if Tabla!="" and Values!="":
            Info=self.Querys["InsertarDatos"].format(Tabla,', '.join(['?'] * Columns))
            self.Pointer.executemany(Info,Values)
            self.DB.commit()
            print(f"DB :: Se ha agregado a '{Tabla}' con exito.")
        else:
            print("DB :: No puede dejar un campo vacio.")           