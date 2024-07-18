import pandas as pd

class Excel:
    def __init__(self):
        self.xlsl="./Sesiones/2doEntregable/Clases.xlsx"
        
    def LeerHoja(self, hoja=""):
        if hoja!="":
            self.hoja=pd.read_excel(self.xlsl,sheet_name=hoja)
            return self.hoja