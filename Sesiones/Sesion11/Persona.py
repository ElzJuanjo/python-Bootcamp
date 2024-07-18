from Excel import Excel

class Persona:
    def __init__(self,id):
        self.id=id       
        self.Excel=Excel("HojaVida.xlsx")
    def MostrarInfoPersonal(self):
        Hoja=self.Excel.LeerHoja("Personal")
        if(self.id in Hoja["ID"]):
            print("\n\t| INFO PERSONAL |")
            resultado = Hoja.loc[Hoja["ID"] == self.id]
            resultado = resultado.drop("ID", axis=1)
            print(resultado.to_string(index=False))
    def MostrarInfoLaboral(self):
        Hoja=self.Excel.LeerHoja("Laboral")
        if(self.id in Hoja["ID"]):
            print("\n\t| INFO LABORAL |")
            resultado = Hoja.loc[Hoja["ID"] == self.id]
            resultado = resultado.drop("ID", axis=1)
            print(resultado.to_string(index=False))    
    def MostrarInfoHabilidad(self):
        Hoja=self.Excel.LeerHoja("Habilidad")
        if(self.id in Hoja["ID"]):
            print("\n\t| INFO HABILIDAD |")
            resultado = Hoja.loc[Hoja["ID"] == self.id]
            resultado = resultado.drop("ID", axis=1)
            print(resultado.to_string(index=False))
    def MostrarInfoEstudio(self):
        Hoja=self.Excel.LeerHoja("Estudio")
        if(self.id in Hoja["ID"]):
            print("\n\t| INFO ESTUDIO |")
            resultado = Hoja.loc[Hoja["ID"] == self.id]
            resultado = resultado.drop("ID", axis=1)
            print(resultado.to_string(index=False))            
        
                            