# La base de datos esta totalmente sincronizada con el excel, las opciones se ejecutan en ambas
from Plataforma import Plataforma
Juego=Plataforma()

def Menu():
    print("\n===== GESTION DE EXCEL Y BASE DE DATOS =====")
    print("1- Agregar datos")
    print("2- Mostrar datos")
    print("   1- Clase Padre")
    print("   2- Clase Hijo")
    print("3- Actualizar datos")
    print("4- Eliminar datos")
    print("0- Salir")
    
def changeDate(id):
    print("1- Titulo")
    print("2- Genero")
    print("3- Precio")
    print("4- Desarrolladora")
    print("5- Lanzamiento")
    print("6- Personajes")
    print("7- Consola")   
    print("8- Multijugador")   
    print("9- Clasificación")  
    print("10- Resolución")  
    print("11- Almacenamiento")  
    print("12- En Linea") 
    opcion = input("Ingrese el número de los datos a cambiar: ") 
    if opcion=="1":
        nuevoDato=input("Ingrese el nuevo titulo: ")
        Juego.updateDate(nuevoDato,id,"TITULO")
    elif opcion=="2":
        nuevoDato=input("Ingrese el nuevo genero: ")
        Juego.updateDate(nuevoDato,id,"GENERO")
    elif opcion=="3":
        nuevoDato=float(input("Ingrese el nuevo precio: "))
        Juego.updateDate(nuevoDato,id,"PRECIO")
    elif opcion=="4":
        nuevoDato=input("Ingrese la nueva desarrolladora: ")
        Juego.updateDate(nuevoDato,id,"DESARROLLADORA")
    elif opcion=="5":
       nuevoDato=input("Ingrese el nuevo lanzamiento: ")
       Juego.updateDate(nuevoDato,id,"LANZAMIENTO")
    elif opcion=="6":
        nuevoDato=int(input("Ingrese los nuevos personajes: "))
        Juego.updateDate(nuevoDato,id,"PERSONAJES")
    elif opcion=="7":
        nuevoDato=input("Ingrese la nueva consola: ")
        Juego.updateDate(nuevoDato,id,"CONSOLA")
    elif opcion=="8":
        nuevoDato=input("Ingrese los nuevos multijugador: ")
        Juego.updateDate(nuevoDato,id,"MULTIJUGADOR")
    elif opcion=="9":
        nuevoDato=input("Ingrese la nueva clasificacion: ")
        Juego.updateDate(nuevoDato,id,"CLASIFICACION")
    elif opcion=="10":
        nuevoDato=int(input("Ingrese la nueva resolucion: "))
        Juego.updateDate(nuevoDato,id,"RESOLUCION")
    elif opcion=="11":
        nuevoDato=float(input("Ingrese el nuevo almacenamiento: "))
        Juego.updateDate(nuevoDato,id,"ALMACENAMIENTO")
    elif opcion=="12":
        nuevoDato=input("Ingrese los nuevos en linea: ")
        Juego.updateDate(nuevoDato,id,"ENLINEA")
    else:
        print("Opción no válida.")                                        

while True:
    Menu()
    opcion = input("Ingrese el número de la opción deseada: ")
    
    if opcion == "1":
        print("Ingrese los siguientes datos...")
        titulo = input("Titulo del juego: ")
        genero = input("Genero al que pertenece: ")
        precio = float(input("Precio: "))
        desarrolladora = input("Nombre de la desarrolladora: ")
        lanzamiento = input("Fecha de lanzamiento: ")
        personajes= int(input("Personajes: "))
        consola = input("Consolas en las que esta disponible: ")
        multijugador = input("Modos multijugador: ")
        clasificacion = input("Clasificacion: ")
        resolucion = int(input("Calidad de resolucion: "))
        almacenamiento = float(input("Almacenamiento que ocupa: "))
        enlinea = input("Modos en linea: ")
        
        Juego.setTitulo(titulo)
        Juego.setGenero(genero)
        Juego.setPrecio(precio)
        Juego.setDesarrolladora(desarrolladora)
        Juego.setLanzamiento(lanzamiento)
        Juego.setPersonajes(personajes)
        Juego.setConsola(consola)
        Juego.setMultijugador(multijugador)
        Juego.setClasificacion(clasificacion)
        Juego.setResolucion(resolucion)
        Juego.setAlmacenamiento(almacenamiento)
        Juego.setEnLinea(enlinea)
        
        Juego.addDate()

    elif opcion == "2":
        subopcion = input("Seleccione los datos que desea ver (1-Clase Padre, 2-Clase Hijo): ")
        if subopcion == "1":
            Juego.getExcelPadre()
        elif subopcion == "2":
            Juego.getExcelHijo()
        else:
           print("Opción no válida.") 

    elif opcion == "3":
        id= int(input("Ingrese el ID del que desea actualizar los datos: "))
        if(Juego.BuscarId(id,"ClaseHijo")):
            changeDate(id)
        else:
            print("DB :: Esta ID no se encuentra.") 

    elif opcion == "4":
        id= int(input("Ingrese el ID del que desea eliminar los datos: "))
        Juego.delDate(id)

    elif opcion == "0":
        print("¡Hasta luego!")
        break

    else:
        print("Opción no válida.")