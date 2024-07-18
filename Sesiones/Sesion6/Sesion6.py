print("\n\t* SESION #6 *\n")

# 1.Imprimir Hola Mundo
print("\n1.\nHola Mundo\n\n2/3.")

# 2. Variables y asignación
# 3. Tipos de datos básicos
nombre="Juan Jose"
print(f"String: {type(nombre)}")
entero=19
print(f"Int: {type(entero)}")
flotante=8.5
print(f"Float: {type(flotante)}")
booleano=True
print(f"Bool: {type(booleano)}")

# 4. Operaciones aritméticas básicas
print(f"\n4.\nNumeros: 10,5\nSuma: {10+5}")
print(f"Resta: {10-5}")
print(f"Producto: {10*5}")
print(f"Division: {10/5}")
print(f"Modulo: {10%5}")

# 5. Conversion entre tipos de datos
a = 123
b = float(a)
print(f"\n5.\nEInt a float: {b}")

c = 123.456
d = int(c)
print(f"Float a Int: {d}")

e = "123"
f = int(e)
print(f"String a Int: {f}")

g = 123
h = str(g)
print(f"Int a String: {h}\n\n6.")

# 6. Solicitar entrada de usuario
Entrada=input("Ingrese entrada: ")
print(f"Ingreso: {Entrada}\n\n7/8/9.")

# 7. Condicional if
# 8. Condicional if-elif
# 9. Condicional if-elif-else
print("Numeros: 7,8")
if 7>8:
    print("El primero es mayor")
elif 7==8:
    print("Ambos son iguales")
else:
    print("El segundo es mayor")
    
# 10. Bucle for
print("\n10.")
for i in range(1,6):
    print(i,end=" ")

# 11. Bucle while
# 12. Uso de break y continue
print("\n\n11/12.")
i=0
while i<15:
    i=i+1
    if i%2==0:
        if(i==10):
            break
        continue
    print(i,end=" ")

# 13. Listas y sus operaciones básicas
# 17. Listas funciones básicas
print("\n\n13/17.")   
Lista=[2,4,6,8,10]
print(f"Lista inicial: {Lista}")
Lista.append(14)
print(f"Operacion append: {Lista}")
Lista.insert(5, 12)
print(f"Operacion insert: {Lista}")
Lista.remove(4)
print(f"Operacion remove: {Lista}")
Numero=Lista.pop(0)
print(f"Operacion pop: {Numero} {Lista}")
print(f"Operacion index: 10 ({Lista.index(10)})")
Lista2=Lista.copy()
print(f"Operacion copy: {Lista2}")
Lista.clear()
print(f"Operacion clear: {Lista}")

# 14. Tuplas y su inmutabildad
print("\n14.")   
Tupla=(1,3,5,7,9)
print(f"Tupla inicial: {Tupla}")
print(f"Operacion count: 5 ({Tupla.count(5)})")
print(f"Operacion index: 9 ({Tupla.index(9)})")

# 15. Conjuntos y operaciones
print("\n\n15.") 
Conjunto1={1,2,3,4,5}
Conjunto2={5,6,7,8,9}
print(f"Primer conjunto: {Conjunto1}")
print(f"Segundo conjunto: {Conjunto2}")
Conjunto2.add(10)
print(f"Operacion add: {Conjunto2}")
print(f"Operacion difference: {Conjunto1.difference(Conjunto2)} {Conjunto2.difference(Conjunto1)}")
Conjunto1.discard(1)
print(f"Operacion discard: {Conjunto1}")
print(f"Operacion intersection: {Conjunto1.intersection(Conjunto2)}")
print(f"Operacion isdisjoint: {Conjunto1.isdisjoint(Conjunto2)}") # Elementos en común, true si no tiene
print(f"Operacion union: {Conjunto1.union(Conjunto2)}")

# 16. Diccionarios y operaciones
print("\n16.") 
Diccionario={
    "Nombre":"Andres",
    "Edad":"20",
    "Documento":"1001"    
}
print(f"Diccionario: {Diccionario}")
print(f"Keys: {Diccionario.keys()}")
print(f"Values: {Diccionario.values()}")
Nombre=Diccionario.get("Nombre")
Edad=Diccionario.get("Edad")
Documento=Diccionario.get("Documento")
print(f"Operacion get: {Nombre} {Edad} {Documento}")

# 18. Leer un archivo de texto
# 19. Escribir en un archivo de texto
print("\n18/19.") 
with open(".\Sesiones\Sesion6\Clase6.txt","w") as documento:
    documento.write("Mi nombre es Juan Jose.")
with open(".\Sesiones\Sesion6\Clase6.txt","r") as documento:
    print(documento.read())

# 20. Modos de apertura: r, w, a, rb, wb
print("\n20.\nr: Lectura\nw: Escritura \na: Anexar")
print("rb: Leer imagenes o comprimidos \nwb: Insertar imagenes o comprimidos")

# 21. Trabajar con archivos JSON
print("\n21.")
import json

Datos={
    "Nombre":"Juanjo",
    "Edad":"19",
    "Documento":"20002"    
}
with open(".\Sesiones\Sesion6\Clase6v1.json","w") as js:
    json.dump(Datos, js)
with open(".\Sesiones\Sesion6\Clase6v1.json","r") as js:
    Archivo=json.load(js)
    print(Archivo)
    
# 22. Leer un archivo CSV
# 23. Filtrar datos en un DataFrame
print("\n22/23.")
import pandas as pd

Documento = pd.read_csv(".\Sesiones\Sesion3\Clase3.txt",sep=";") 
Filtrar=Documento[Documento["Fecha"]=="30/08/2023"]
print(Filtrar.to_string(index=False))

# 24. Operaciones básicas: sum(), mean(), max(), min()
print("\n24.")
import numpy as np

Numeros=[1,2,3,4,5]
print(f"Numeros: {Numeros}")
Sum=np.sum(Numeros)
print(f"Operacion sum: {Sum}")
Mean=np.mean(Numeros)
print(f"Operacion mean: {Mean}")
Max=np.max(Numeros)
print(f"Operacion max: {Max}")
Min=np.min(Numeros)
print(f"Operacion min: {Min}")

# 25. Uso de iloc y loc
print("\n25.")

df=pd.DataFrame({
  "Edad": [18, 25, 30, 40],
  "Genero": ["Hombre", "Hombre", "Mujer", "Mujer"]
})
print(f"Iloc:\n{df.iloc[0]}")
print("Loc:\n",df.loc[df["Edad"]==30])
print("Casilla:\n",df.loc[1]["Edad"])
print("Filtro:\n",df.loc[df["Edad"]==25,"Genero"])

# 26. Agrupar datos con groupby
print("\n26.")

df=pd.DataFrame({
    "nombre": ["Juan", "Pedro", "María", "José"],
    "edad": [20, 25, 30, 35]
})
df.groupby("nombre")
for name in df.groupby("nombre"):
    print(name)

# 27. Unir DataFrames con merge y concat
print("\n27.")

df1=pd.DataFrame({
    "A": [1, 2, 3],
    "B": [4, 5, 6]
})

df2=pd.DataFrame({
    "A": [1, 2, 3],
    "C": [7, 8, 9],
    "D": [10, 11, 12]
})

concat=pd.concat([df1, df2], axis=1)
print(f"Concat:\n{concat}")

merge=pd.merge(df1, df2, on="A")
print(f"Merge:\n{merge}")

# 28. Manipular series temporales
# Son datos que están ordenados cronológicamente
# Están asociados a un tiempo específico
print("\n28.")

Valores=(1,2,3,4,5)
series=pd.Series(Valores)

print(series)

# 29. Exportar un DataFrame a un CSV 
print("\n29.")

df=pd.DataFrame({
    "nombre": ["Juan", "Pedro", "María"],
    "edad": [20, 25, 30]
})
print(df)
df.to_csv(".\Sesiones\Sesion6\Clase6.csv")

# 30. Convertir un DataFrame a JSON
print("\n30.")

df=pd.DataFrame({
    "nombre": ["Juan", "Pedro", "Maria"],
    "edad": [20, 25, 30]
})

df.to_json(".\Sesiones\Sesion6\Clase6v2.json")
print(df.to_json())
print("\n\t* Sesion lograda! *\n")