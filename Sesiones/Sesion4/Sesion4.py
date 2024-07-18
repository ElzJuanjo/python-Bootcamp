print("\n\t* SESION #4 *\n")

#diccionario={
#    "Columna1":["PrimerDato",2],
#    El encabezado es Columna1, El primer renglon en esa columna es PrimerRenglon,El segundo es 2
#    "Columna2":["SegundoDato",3]
#    El encabezado es Columna2, El primer renglon en esa columna es SegundoDato,El segundo es 3
#}

import pandas as pd

convertir=pd.read_excel(".\Sesiones\Sesion4\Clase4v1.xlsx") # Guarda el DataFrame en una variable
# convertir.loc[Fila,"Fecha"]="23/08/2023" Agregar nueva columna al excel
# convertir.loc[len(convertir)]= ["Juanjo",19,"Informatica",31051502,"23/08/203"] Agregar nueva fila al excel
# nombre=convertir.loc[Fila,"Nombre"] Obtener el dato en esa casilla
# print(convertir.columns) Imprime el nombre de las columnas
# print(convertir.dtypes) Tipos de datos en columna (object para string, int64 para numeros)
# print(convertir.iloc[Fila]) Imprime una fila determinada
# print(convertir["Nombre"]) Imprime un columna determinada
# print(convertir["Nombre"].iloc[Fila]) Imprime el nombre en la fila especificada

for i in range(0,len(convertir)):
    convertir.loc[i,"Fecha"]="23/08/2023"
    
convertir.loc[len(convertir)]= ["Juanjo",19,"Informatica",31051502,"23/08/2023"]
print(convertir)

convertir.to_excel("C:\Visual\juan_jaramillo82222\Sesiones\Sesion4\Clase4v2.xlsx",index=False)

#for index,row in convertir.iterrows():
#    print("la fila {}, columna {}". format(index,row["Profesión"]))
# Imprime el indice de la fila, y lo que hay en la columna "Profesion" de esa fila

# | AGREGAR USANDO DICCIONARIO |
#datos = {
#    "Nombre": ["Andrés"],
#    "Edad": [21],
#    "Profesión": ["Informatica"],
#    "Teléfono": [3234108779],
#    "Fecha:" ["23/08/2023"]
#}
# convertir.loc[len(convertir)]=datos

# | AGREGAR USANDO LISTAS |
# datos=["Andres",21,"Informatica",3234108779,"23/08/2023"]
# convertir.loc[len(convertir)]=datos

# | DICCIONARIO A EXCEL |
#diccionario={
#    "Nombre":["Ricardo","Jhonki"],
#    "Documento":[1001757,1023485]
#}
#dataframe=pd.DataFrame.from_dict(diccionario)
#print(dataframe)

# | EXCEL A DICCIONARIO |
# diccionario=convertir.to_dict("records") Convierte el DataFrame a un diccionario
# for record in diccionario: Imprimir en el orden que se ve en Excel
#    print(record)

print("\n\t* Sesion lograda! *\n")