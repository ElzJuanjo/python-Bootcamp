# primary key implica que no puede repetirse ese valor en otro elemento
# autoincrement implica que el valor de la fila aumente solo cuando se agregue otra
# not null implica que debe haber algo en ese campo
# if not exists implica que no se sobreescriba o duplique
# unique implica que no se repita un valor en la columna
# foreign key (value) implica que es una columna con valores pertenecientes a otra tabla...
# references otratabla (columna) esta es la tabla y su columna a la que hace referencia lo anterior
# ', '.join(['?'] * len) Contiene una serie de ? separados por comas, su cantidad es la del len
from Personal import Personal
from Laboral import Laboral
from Estudio import Estudio
from Habilidad import Habilidad
print("\n\t* SESION #12 *\n")
print("\t| CREACION DE TABLAS EN LA DB |")
TablaPersonal=Personal()
TablaEstudio=Estudio()
TablaHabilidad=Habilidad()
TablaLaboral=Laboral()
print("\n\t| AGREGAR DATOS A LAS TABLAS |")
TablaPersonal.AgregarUnDato("Juan","Jose","Jaramillo","Vera","1007","314701","juanjo@elpoli.edu.co")
TablaPersonal.AgregarUnDato("Adeliria","","Bernal","","43861","321637","adeliria@hotmail.com")
TablaEstudio.AgregarUnDato("Ing. Informatica","2022-2","2027-2","27")
TablaEstudio.AgregarUnDato("Reg. Farmacia","2014-1","2015-2","10")
TablaHabilidad.AgregarUnDato("Programar","Java, C++, Python")
TablaHabilidad.AgregarUnDato("Perseverancia","Animar e Insistir")
TablaLaboral.AgregarUnDato("Salsamentaria","Junio-2021","Agosto-2022","Bodega","Pedido")
TablaLaboral.AgregarUnDato("Dempos","Enero-2020","Febrero-2023","Auxiliar","Multiples")