from Perro import Perro
from Gato import Gato
from Pajaro import Pajaro
from Animal import Animal
print("\n\t* SESION #10 *\n")
print("» HERENCIA «\n")
Teo=Perro("Cafe","Domestico","Terrestre","Ladrar","Labrador","Teo")
Wilson=Gato("Naranja","Domesstico","Terrestre","Maullar","Persa","Wilson")
Buho=Pajaro("Gris","Bosques","Volar","Trinar","Buho")
print(Teo.Caracteristicas())
print(Teo.Morfologia())
print(Wilson.Caracteristicas())
print(Wilson.Morfologia())
print(Buho.Caracteristicas())
print(Buho.Morfologia())
print("\n» POLIMORFISMO «\n")
Animal.HacerComer(Teo)
Animal.HacerComer(Wilson)
Animal.HacerHablar(Teo)
Animal.HacerHablar(Wilson)
Animal.HacerJugar(Teo)
Animal.HacerJugar(Wilson)
Animal.HacerHablar(Buho)
Animal.HacerComer(Buho)