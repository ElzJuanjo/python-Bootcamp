class Estudio:
    def __init__(self,titulo,inicio,fin,horas):
        self.titulo=titulo
        self.inicio=inicio
        self.fin=fin
        self.horas=horas
    def __str__(self):
        return f"| ESTUDIO |\nTitulo: {self.titulo}\nFecha inicio: {self.inicio}\nFecha fin: {self.fin}\nHoras: {self.horas}"