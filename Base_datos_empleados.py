class Base_datos_empleados:
    def __init__(self):
        #este es el array
        self.bd_empleados_lista = []
        
    def guardar_empleado(self,obj_empleado):
        self.bd_empleados_lista.append(obj_empleado)
        return True
    
    def extender_varios_empleados(self,varios_obj):
        self.bd_empleados_lista.extend(varios_obj)
        
    def imprimir_info(self):
        for i in range(len(self.bd_empleados_lista)):
            print(self.bd_empleados_lista[i].ver_info_empleado())