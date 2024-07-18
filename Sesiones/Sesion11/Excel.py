import pandas as pd

class Excel:
    def __init__(self,xlsl=""):
        self.xlsl=f"./Sesiones/Sesion11/{xlsl}"
    def LeerHoja(self, hoja=""):
        self.hoja=pd.read_excel(self.xlsl,sheet_name=hoja)
        return self.hoja