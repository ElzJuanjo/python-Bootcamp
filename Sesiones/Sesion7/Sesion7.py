print("\n\t* SESION #7 *\n")

import pandas as pd
# 1. Lee una tabla HTML desde página
# 2.Guardar la tabla de html  en un excel
print("1/2.")
Tabla=pd.read_html("https://www.x-rates.com/table/?from=USD&amount=1")[1]
Tabla.to_excel(".\Sesiones\Sesion7\Clase7v1.xlsx")
print("Guardado en Clase7v1.xlsx")

# 3. Exporta los primeros 10 a un archivo CSV
print("\n3.")
Tabla.head(10).to_csv(".\Sesiones\Sesion7\Clase7v1.csv")
print("Guardado en Clase7v1.csv")

# 4. Lee tres tablas HTML y guárdalas en tres hojas
print("\n4.")
Hoja1=pd.read_html("https://help.netflix.com/es/node/24926")[0]
Hoja2=pd.read_html("https://www.x-rates.com/table/?from=USD&amount=1")[1]
Hoja3=pd.read_html("https://www.colombia.com/cambio-moneda/monedas-del-mundo/")[0]
Hoja2=Hoja2.tail(5)
Hoja3=Hoja3.head(5)
with pd.ExcelWriter(".\Sesiones\Sesion7\Clase7v2.xlsx") as writer:
    Hoja1.to_excel(writer,sheet_name="Hoja1")
    Hoja2.to_excel(writer,sheet_name="Hoja2")
    Hoja3.to_excel(writer,sheet_name="Hoja3")
print("Guardado en Clase7v2.xlsx")

# 5. Filtra los registros donde la columna "edad" sea >=30
print("\n5.")
Documento=pd.read_excel(".\Sesiones\Sesion4\Clase4v1.xlsx")
Edades=Documento.loc[Documento["Edad"]>=30]
Edades.to_csv(".\Sesiones\Sesion7\Clase7v2.csv")
print("Guardado en Clase7v2.csv")

# 6. Lee un archivo CSV, guardar columnas "Nombre" y "Profesion"
print("\n6.")
Archivo=pd.read_csv(".\Sesiones\Sesion7\Clase7v3.csv")

Columnas = ['Nombre', 'Profesión']
Archivo[Columnas].to_excel(".\Sesiones\Sesion7\Clase7v3.xlsx")
print("Guardado en Clase7v3.xlsx")

# 7. # Combinar dos hojas de un excel en un DataFrame
print("\n7.")
xlsx=pd.ExcelFile(".\Sesiones\Sesion7\Clase7v2.xlsx")
Hoja1=pd.read_excel(xlsx,"Hoja1")
Hoja2=pd.read_excel(xlsx,"Hoja2")
Combinar=pd.concat([Hoja1,Hoja2])
Combinar.to_excel(".\Sesiones\Sesion7\Clase7v4.xlsx")
print("Guardado en Clase7v4.xlsx")
print("\n\t* Sesion lograda! *\n")