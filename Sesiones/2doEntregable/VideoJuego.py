from Excel import Excel
import pandas as pd
from Conexion import Conexion

class VideoJuego(Excel, Conexion):
    def __init__(self, titulo="", genero="", precio=0.0, desarrolladora="", lanzamiento="", personajes=0):
        Conexion.__init__(self)
        super().__init__()
        self.titulo=titulo
        self.genero=genero
        self.precio=precio
        self.desarrolladora=desarrolladora
        self.lanzamiento=lanzamiento
        self.personajes=personajes
        self.crearDBPadre()
        self.id=1
                  
    def crearDBPadre(self):
        """| Crear tabla clase padre en la base de datos |
        
        Info:
            Se añadira mientras no este ya creada
        """
        self.CrearTabla("ClasePadre","VideoJuego")
        
    def addDBPadre(self):
        """| Agregar a la tabla padre en la base de datos |

        Info:
            Se añadiran los datos de la instancia actual 
            en una nueva fila
        """   
        Datos=[
            (f"{self.titulo}",f"{self.genero}",f"{self.precio}",f"{self.desarrolladora}",
             f"{self.lanzamiento}",f"{self.personajes}")
        ]       
        self.InsertarDatos("ClasePadre",6,Datos)     
            
    def addExcelPadre(self):
        """| Agregar a la hoja padre en el excel |

        Info:
            Se añadiran los datos de la instancia actual 
            en una nueva fila
            
        Return:
            True si se ejecuto correctamente, False si no se agregó
        """       
        self.ClasePadre=self.LeerHoja("ClasePadre")
        if not self.ClasePadre.empty:
            self.Pointer.execute("SELECT * FROM sqlite_sequence WHERE seq")
            self.id = self.Pointer.fetchmany()[0][1]      
            self.id=int(self.id)+1
        if(self.titulo not in self.ClasePadre["TITULO"].values and self.titulo!=""):
            DatosPadre=pd.DataFrame({
                "ID":[self.id],
                "TITULO":[self.getTitulo()],
                "GENERO":[self.getGenero()],
                "PRECIO":[self.getPrecio()],
                "DESARROLLADORA":[self.getDesarrolladora()],
                "LANZAMIENTO":[self.getLanzamiento()],
                "PERSONAJES":[self.getPersonajes()]
            })
            self.ClasePadre=pd.concat([self.ClasePadre,DatosPadre])   
            self.addDBPadre() # Se agrega en simultaneo con la DB
            return True
        else:
            print("DB :: El titulo ya está en uso o no fue ingresado.") 
            return False
        
    def delExcelPadre(self, ID):
        """| Eliminar de la hoja padre en el excel |
        
        Parametros:
            ID (Integer) : Se eliminaran los datos en la fila especificada
            
        Return:
            True si se ejecuto correctamente, False si no se eliminó
        """
        if self.EliminarDatos("ClasePadre",ID): # Se elimina en simultaneo con la DB
            self.ClasePadre=self.LeerHoja("ClasePadre")        
            self.ClasePadre = self.ClasePadre[self.ClasePadre["ID"] != ID]
            return True
        else:
            return False
        
    def updateExcelPadre(self, NuevoDato, ID=0, Columna=""):
        """| Cambiar de la hoja padre en el excel |
        
        Parametros:
            ID (Integer) : Se cambiaran los datos en la id especificada
            Columna (String) : Se cambiaran los datos en la columna especificada
            NuevoDato : Se asignara el dato especificado en ese lugar
            
        Return:
            True si se ejecuto correctamente, False si no se eliminó      
        """
        self.ClasePadre=self.LeerHoja("ClasePadre")
        columnas = ["TITULO", "GENERO", "PRECIO", "DESARROLLADORA", "LANZAMIENTO", "PERSONAJES"]
        if Columna in columnas:
            if Columna=="TITULO":
                if NuevoDato not in self.ClasePadre["TITULO"].values and NuevoDato!="":
                    if self.ActualizarDatos(NuevoDato,"ClasePadre",Columna,ID): # Se actualiza en simultaneo con la DB
                        Actual=self.ClasePadre.loc[self.ClasePadre["ID"] == ID]
                        Actual=Actual[Columna]
                        self.ClasePadre[Columna] = self.ClasePadre[Columna].replace({Actual.iloc[0]: NuevoDato})   
                        return True 
                else:
                    print("DB :: El titulo ya está en uso o no fue ingresado.") 
                    return False
            else:
                if self.ActualizarDatos(NuevoDato,"ClasePadre",Columna,ID): # Se actualiza en simultaneo con la DB
                    Actual=self.ClasePadre.loc[self.ClasePadre["ID"] == ID]
                    Actual=Actual[Columna]
                    self.ClasePadre[Columna] = self.ClasePadre[Columna].replace({Actual.iloc[0]: NuevoDato})   
                    return True                     
        else:
            return True                
               
    def getExcelPadre(self):
        """| Obtener la hoja de ClasePadre en el excel |
        
        Info:
            Imprimirá los datos actuales       
        """
        self.ClasePadre=self.LeerHoja("ClasePadre")
        if not self.ClasePadre.empty:
            print()
            print(self.ClasePadre.to_string(index=False))
        else:
            print("DB :: No hay datos.")  
               
    def setTitulo(self, nuevoTitulo):
        """| Cambiar titulo |

        Parametros:
            nuevoTitulo : String
        """
        self.titulo=nuevoTitulo
        
    def getTitulo(self):
        """| Obtener titulo |
        
        Return:
            titulo : String
        """
        return self.titulo
    
    def setGenero(self, nuevoGenero):
        """| Cambiar genero |

        Parametros:
            nuevoGenero : String
        """
        self.genero=nuevoGenero
    
    def getGenero(self):
        """| Obtener genero |
        
        Return:
            genero : String
        """
        return self.genero
    
    def setPrecio(self, nuevoPrecio):
        """| Cambiar precio |

        Parametros:
            nuevoPrecio : Float
        """
        self.precio=nuevoPrecio
    
    def getPrecio(self):
        """| Obtener precio |
        
        Return:
            precio : Float
        """
        return self.precio
    
    def setDesarrolladora(self, nuevaDesarrolladora):
        """| Cambiar desarrolladora |

        Parametros:
            nuevaDesarrolladora : String
        """
        self.desarrolladora=nuevaDesarrolladora
    
    def getDesarrolladora(self):
        """| Obtener desarrolladora |
        
        Return:
            desarrolladora : String
        """
        return self.desarrolladora
    
    def setLanzamiento(self, nuevoLanzamiento):
        """| Cambiar lanzamiento |

        Parametros:
            nuevoLanzamiento : String
        """
        self.lanzamiento=nuevoLanzamiento
    
    def getLanzamiento(self):
        """| Obtener lanzamiento |
        
        Return:
            lanzamiento : String
        """
        return self.lanzamiento
    
    def setPersonajes(self, nuevosPersonajes):
        """| Cambiar personajes |

        Parametros:
            nuevosPersonajes : Integer
        """
        self.personajes=nuevosPersonajes
    
    def getPersonajes(self):
        """| Obtener personajes |
        
        Return:
            personajes : Integer
        """
        return self.personajes