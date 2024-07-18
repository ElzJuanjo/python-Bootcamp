print("\n\t* SESION #8 *\n")

# 6. Determine si un #n es >6
print("\n6.",end="")
jjjv_6=5
print()
if jjjv_6>6:
    print("Si cumple.")
else:
    print("No cumple.")
    
# 16. Dar un numero flotante y tomar solo el decimal
jjjv_16=15.885
print("\n16.")
print(f"Parte decimal: {round((jjjv_16%1),3)}")

#26. Devolver el elemento mas grande y mas pequeño de una lista
print("\n26.")
jjjv_26=[2,4,7,9,3,1,6]
import numpy as np
print(f"Mas grande: {np.max(jjjv_26)}")
print(f"Mas pequeño: {np.min(jjjv_26)}")

#36. Devolver las claves de un diccionario
print("\n36.")
jjjv_36={
    "Nombre":"Alejo",
    "Edad":"20",
    "Documento":"1001", 
    "Residencia":"Colombia",   
    "Genero":"Hombre"
}
print(f"Claves: {list(jjjv_36.keys())}")

#46. Eliminar una columna de un archivo CSV
print("\n46.")
import pandas as pd
jjjv_46=pd.read_csv("./Sesiones/1erEntregable/Clase8v1.csv",sep=";")
jjjv_46=jjjv_46.drop("Fecha",axis=1)
jjjv_46.to_csv("./Sesiones/1erEntregable/Clase8v2.csv",sep=";")
print("Se ha guardado en Clase8v2.csv\nSe elimino la columna Fecha.")

#56. Cambiar el nombre en una columna de un archivo CSV
print("\n56.")
jjjv_56=pd.read_csv("./Sesiones/1erEntregable/Clase8v1.csv",sep=";")
jjjv_56=jjjv_56.rename(columns={"N° sesión":"Clases"})
jjjv_56.to_csv("./Sesiones/1erEntregable/Clase8v3.csv",sep=";")
print("Se ha guardado en Clase8v3.csv\nSe cambio el nombre de la columna N° sesión por Clases.")

#66. Agregar nueva fila a un archivo Excel
print("\n66.")
jjjv_66=pd.read_excel("./Sesiones/1erEntregable/Clase8v1.xlsx")
jjjv_66.loc[len(jjjv_66)]=["Ricardo",21,"Informatica",57108231,"06/09/2023"]
jjjv_66.to_excel("./Sesiones/1erEntregable/Clase8v2.xlsx",index=False)
print("Se ha guardado en Clase8v2.xlsx\nSe agrego la fila de Ricardo.")

#76. Filtrar filas basandose en una condición compuesta de un Excel
print("\n76.")
jjjv_76=pd.read_excel("./Sesiones/1erEntregable/Clase8v2.xlsx")
jjjv_76=jjjv_76.loc[(jjjv_76["Profesión"]=="Informatica") & (jjjv_76["Edad"]<25)]
print(jjjv_76)

#86. Leer archivo CSV y usar función pivot_table() para crear tabla dinámica
print("\n86.")
jjjv_86=pd.read_csv("./Sesiones/1erEntregable/Clase8v4.csv")
jjjv_86=jjjv_86.pivot_table(values="Ventas", index=["Region", "Producto"], aggfunc=sum)
jjjv_86.to_excel("./Sesiones/1erEntregable/Clase8v3.xlsx")
print("Se ha guardado en Clase8v3.xlsx\nSe ha ordenado el total de ventas por región y producto.")

#96. Mostrar filas con valores duplicados basados en una columna especifica de un Excel
print("\n96.")
jjjv_96=pd.read_excel("./Sesiones/1erEntregable/Clase8v4.xlsx")
jjjv_96=jjjv_96[jjjv_96["edad"].duplicated()]
print(jjjv_96)

print("\n\t* Sesion lograda! *\n")