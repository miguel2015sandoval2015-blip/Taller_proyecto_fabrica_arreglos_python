#crear clase
class Api_BD_maquinas:
    #crear constructor
    def __init__(self):
        #crear atributos
        self.Api_maquinas = [
            ["nombre completo","modelo maquina","estado maquina",],
            ["cod 1234","brazo mecanico","x220","apagada"],
            ["cod 2342","cinta","transporte","xs4000","requiere mantenimiento"],
            ["cod 5632","monobrazo","jk100","encendida"]
        ]
        #crear metodos
    def imprimir_info(self):
        for i in range(len(self.Api_maquinas)):

    def buscar_info(self):
        return self.Api_BD_maquinas[0][1]