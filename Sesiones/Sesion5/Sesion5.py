print("\n\t* SESION #5 *\n")

import pandas as pd

convertir=pd.read_html("https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)_per_capita") 
# Guardar la pagina
convertir[1].rename(columns={ # Cambiar el nombre de los encabezados, en la posición 1 está el DataFrame
    "Country/Territory": "País",
    "UN Region": "Región",
    "IMF[4][5]": "FMI",
    "Estimate": "Estimación",
    "Year": "Año",
    "World Bank[6]": "Banco Mundial",
    "United Nations[7]": "Naciones Unidas",
}, inplace=True)

convertir=convertir[1].drop(0, inplace=False) # Borrar la fila 0 que se genero vacía
convertir.fillna(method="ffill", inplace=True) # Subir el resto de elementos 

convertir.to_excel("C:\Visual\juan_jaramillo82222\Sesiones\Sesion5\Clase5v1.xlsx")

convertir2=pd.read_html("https://www.colombia.com/cambio-moneda/monedas-del-mundo/")
convertir2[0].to_excel("C:\Visual\juan_jaramillo82222\Sesiones\Sesion5\Clase5v2.xlsx")

print("\n\t* Sesion lograda! *\n")