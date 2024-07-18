from VideoJuego import VideoJuego
import pandas as pd

class Plataforma(VideoJuego):
    def __init__(self, titulo="", genero="", precio=0, desarrolladora="", lanzamiento="", personajes=0,
                 consola="",multijugador="",clasificacion="",resolucion=144,almacenamiento=1.0,enLinea=""):
        """| Constructor |
        
        Atributos:
            titulo (String) : Nombre del videojuego                
            genero (String) : Tipo de entretenimiento
            precio (Float) : Costo del videojuego
            desarrolladora (String) : Empresa creadora
            lanzamiento (String) : Fecha en que salio al mercado
            personajes (Integer) : Cantidad de seleccionables
            consola (String) : Medio en el que se juega
            multijugador (String) : Modos de varias personas
            clasificacion (String) : Publico al que va dirigido
            resolucion (Integer) : Calidad en la que se juega
            almacenamiento (Float) : Cantidad que ocupa en el dispositivo
            enLinea (String ) : Modos usando conexion    
        """
        super().__init__(titulo, genero, precio, desarrolladora, lanzamiento, personajes)
        self.consola=consola
        self.multijugador=multijugador
        self.clasificacion=clasificacion
        self.resolucion=resolucion
        self.almacenamiento=almacenamiento
        self.enLinea=enLinea
        self.crearDBHijo()

    def crearDBHijo(self):
        """| Crear tabla clase hijo en la base de datos |
        
        Info:
            Se añadira mientras no este ya creada
        """
        self.CrearTabla("ClaseHijo","Plataforma")
        
    def addDBHijo(self):
        """| Agregar a la tabla hijo en la base de datos |

        Info:
            Se añadiran los datos de las instancia actual 
            en una nueva fila
        """   
        Datos=[
            (f"{self.consola}",f"{self.multijugador}",f"{self.clasificacion}",f"{self.resolucion}",
             f"{self.almacenamiento}",f"{self.enLinea}")
        ]       
        self.InsertarDatos("ClaseHijo",6,Datos)  
         
    def addDate(self):
        """| Agregar al excel y DB |

        Info:
            Se añadiran los datos de la instancia actual 
            en una nueva fila de las hojas correspondientes y en la DB
        """
        if self.addExcelPadre(): # Se agrega en simultaneo con el padre
            self.ClaseHijo=self.LeerHoja("ClaseHijo")
            DatosHijo=pd.DataFrame({
                "ID":[self.id],
                "TITULO":[self.getTitulo()],
                "GENERO":[self.getGenero()],
                "PRECIO":[self.getPrecio()],
                "DESARROLLADORA":[self.getDesarrolladora()],
                "LANZAMIENTO":[self.getLanzamiento()],
                "PERSONAJES":[self.getPersonajes()],
                "CONSOLA":[self.getConsola()],
                "MULTIJUGADOR":[self.getMultijugador()],
                "CLASIFICACION":[self.getClasificacion()],
                "RESOLUCION":[self.getResolucion()],
                "ALMACENAMIENTO":[self.getAlmacenamiento()],
                "ENLINEA":[self.getEnLinea()]
            })
            self.ClaseHijo=pd.concat([self.ClaseHijo,DatosHijo])        
            with pd.ExcelWriter(self.xlsl) as writer:
                self.ClasePadre.to_excel(writer, sheet_name="ClasePadre", index=False)
                self.ClaseHijo.to_excel(writer, sheet_name="ClaseHijo", index=False)
            self.addDBHijo()  # Se agrega en simultaneo con la DB        
            print("DB :: Se agregaron los datos al correctamente.")
            
    def delDate(self, ID):
        """| Eliminar en el excel y DB |
        
        Parametros:
            ID (Integer) : Se eliminaran los datos en la fila especificada
            de las hojas correspondientes y en la DB
        """
        if self.delExcelPadre(ID): # Se elimina en simultaneo con el padre
            self.ClaseHijo=self.LeerHoja("ClaseHijo")
            self.ClaseHijo = self.ClaseHijo[self.ClaseHijo["ID"] != ID]
            with pd.ExcelWriter(self.xlsl) as writer:
                self.ClasePadre.to_excel(writer, sheet_name="ClasePadre", index=False)
                self.ClaseHijo.to_excel(writer, sheet_name="ClaseHijo", index=False)  
            self.EliminarDatos("ClaseHijo",ID) # Se elimina en simultaneo con la DB
            print("DB :: Se eliminaron los datos correctamente.")   
            
    def updateDate(self, NuevoDato, ID=0, Columna=""):
        """| Cambiar en el excel y DB |
        
        Parametros:
            ID (Integer) : Se cambiaran los datos en la id especificada
            Columna (String) : Se cambiaran los datos en la columna especificada
            NuevoDato : Se asignara el dato especificado en ese lugar    
        """
        self.ClaseHijo=self.LeerHoja("ClaseHijo")
        columnas = ["CONSOLA", "MULTIJUGADOR", "CLASIFICACION", "RESOLUCION", "ALMACENAMIENTO", "ENLINEA"]
        if self.updateExcelPadre(NuevoDato,ID,Columna): # Se actualiza en simultaneo con el padre
            if Columna in columnas:
                self.ActualizarDatos(NuevoDato,"ClaseHijo",Columna,ID) # Se actualiza en simultaneo con la DB
            Actual=self.ClaseHijo.loc[self.ClaseHijo["ID"] == ID]
            Actual=Actual[Columna]
            self.ClaseHijo[Columna] = self.ClaseHijo[Columna].replace({Actual.iloc[0]: NuevoDato})             
            with pd.ExcelWriter(self.xlsl) as writer:
                self.ClasePadre.to_excel(writer, sheet_name="ClasePadre", index=False)
                self.ClaseHijo.to_excel(writer, sheet_name="ClaseHijo", index=False)    
            print("DB :: Se actualizaron los datos correctamente.")   
         
    def getExcelHijo(self):
        """| Obtener la hoja de ClaseHijo en el excel |
        
        Info:
            Imprimirá los datos actuales       
        """
        self.ClaseHijo=self.LeerHoja("ClaseHijo")
        if not self.ClaseHijo.empty:
            self.ClaseHijo=self.ClaseHijo.drop(["TITULO","GENERO","PRECIO","DESARROLLADORA","LANZAMIENTO",
                                                "PERSONAJES"],axis=1)
            print()
            print(self.ClaseHijo.to_string(index=False))      
        else:
            print("DB :: No hay datos.") 
                        
    def setConsola(self, nuevaConsola):
        """| Cambiar consola |

        Parametros:
            nuevaConsola : String
        """
        self.consola = nuevaConsola

    def getConsola(self):
        """| Obtener consola |
        
        Return:
            consola : String
        """
        return self.consola

    def setMultijugador(self, nuevoMultijugador):
        """| Cambiar multijugador |

        Parametros:
            nuevoMultijugador : String
        """
        self.multijugador = nuevoMultijugador

    def getMultijugador(self):
        """| Obtener multijugador |
        
        Return:
            multijugador : String
        """
        return self.multijugador

    def setClasificacion(self, nuevaClasificacion):
        """| Cambiar clasificacion |

        Parametros:
            nuevaClasificacion : String
        """
        self.clasificacion = nuevaClasificacion

    def getClasificacion(self):
        """| Obtener clasificacion |
        
        Return:
            clasificacion : String
        """
        return self.clasificacion

    def setResolucion(self, nuevaResolucion):
        """| Cambiar resolucion |

        Parametros:
            nuevaResolucion : Integer
        """
        self.resolucion = nuevaResolucion

    def getResolucion(self):
        """| Obtener resolucion |
        
        Return:
            resolucion : Integer
        """
        return self.resolucion

    def setAlmacenamiento(self, nuevoAlmacenamiento):
        """| Cambiar almacenamiento |

        Parametros:
            nuevoAlmacenamiento : Float
        """
        self.almacenamiento = nuevoAlmacenamiento

    def getAlmacenamiento(self):
        """| Obtener almacenamiento |
        
        Return:
            almacenamiento : Float
        """
        return self.almacenamiento

    def setEnLinea(self, nuevoEnLinea):
        """| Cambiar enLinea |

        Parametros:
            nuevoEnLinea : String
        """
        self.enLinea = nuevoEnLinea

    def getEnLinea(self):
        """| Obtener enLinea |
        
        Return:
            enLinea : String
        """
        return self.enLinea