class Habilidad:
    def __init__(self,tipo,nivel,id):
        self.tipo=tipo
        self.nivel=nivel
        self.id=id
    def __str__(self):
        return f"| HABILIDAD |\nTipo: {self.tipo}\nNivel: {self.nivel}\nID: {self.id}"