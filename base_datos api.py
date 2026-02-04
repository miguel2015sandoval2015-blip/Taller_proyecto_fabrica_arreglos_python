class Api_BD:
    def __init__(self):
        self.api_datos= []

    def guardar_empleado(self,obj_nuevo_empleado):
        self.api_datos.append(obj_nuevo_empleado)

    def imprimir_api(self):
        for empleados in self.api_datos:
            print (empleado)

