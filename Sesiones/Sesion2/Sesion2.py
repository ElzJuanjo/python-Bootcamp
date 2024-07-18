print("\n\t* SESION #2 *\n")

# Declaracion de variables
nombre="Juan Jose"
entero=20
flotante=8.5
booleano=True
# Listas
lista=[1,2,3,4,5]

# » Las listas están asociadas, si cambio una lista2=lista, también se cambia la primera
# La solución es usar copy, ejemplo :: lista2=lista.copy

# Diccionario
diccionario={
    "nombre":"Andres",
    "edad":25
}

# Tupla :: No se le puede cambiar ningún valor (No mutable)
tupla=(10,20,30)

# Conjuntos
conjunto={40,50,60}

# Evaluar tipo de variable
print(type(nombre))
print(type(entero))
print(type(flotante))
print(type(booleano))
print(type(lista))
print(type(tupla))
print(type(conjunto))
print(diccionario["nombre"])

# | LECTURA DE ARCHIVOS PLANOS |
with open(".\Sesiones\Sesion2\Clase2.txt","w") as documento: # Establecer
    documento.write("Hola Mundo\nPrueba #1: ")

with open(".\Sesiones\Sesion2\Clase2.txt","a") as documento: # Agregar
    documento.write("Anexar\n")
    
with open(".\Sesiones\Sesion2\Clase2.txt","r") as documento: # Leer
    print(documento.read())

print("\n\t* Sesion lograda! *\n")