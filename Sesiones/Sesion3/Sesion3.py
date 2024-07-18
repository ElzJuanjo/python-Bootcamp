print("\n\t* SESION #3 *\n")

with open(".\Sesiones\Sesion2\Clase2.txt","r") as documento:
    Lineas=documento.readlines() # Copiar todo el documento en forma de lista, cada renglon es una posicion
    Conjunto=Lineas[0].split("\n") # Copiar el renglon hasta encontrar un salto de linea (O lo del parametro)
    print(Lineas[1]) # El contenido que se encuentra en esa posicion
    
    TLineas=1
    Cont=1
    Found=False
    for Frase in Conjunto: # Evaluar si la frase o palabra se encuentra ahi
        if Frase=="Hola Mundo":
            Found=True
        if Found==False:
            Cont+=1
        TLineas+=1
    print("Total de Lineas en el documento: "+str(TLineas))
    if Found:
        print("La frase esta en el conjunto! renglon: "+str(Cont))
    else:
        print("La frase no esta en el conjunto!")
        
# | IMPORTACION DE LIBRERIAS |
import pandas as pd
archivo = pd.read_csv(".\Sesiones\Sesion3\Clase3.txt",sep=";") 
# Crear una DataFrame (Hoja de calculo), el segundo parametro indica en que caracter se considera una nueva fila

archivo["Referencias"] = "https://pandas.pydata.org/docs/user_guide/index.html#user-guide"
# Agrega una nueva columna y asigna la url a todas las filas de ésta columna

archivo.to_excel("C:\Visual\juan_jaramillo82222\Sesiones\Sesion3\Clase3.xlsx",index=False)
# Exportar el DataFrame a un archivo de excel

print("\n\t* Sesion lograda! *\n")