#crear la clase
class Bd_empleados_lista:
    #crear el contructor
    def __init__(self): #creo el array de la base de datos de los empleados
        self.empleado_lista_bd = []
            
    
    def guardar_empleado(self,obj_nuevo_empleado):# metodo guarda el empleado
        self.empleado_lista_bd.append(obj_nuevo_empleado)
        return True
        
    
    def extend_lista_empleado(self,nueva_lista):
        self.empleado_lista_bd.extend(nueva_lista)
               
    def imprimir_info(self):
        print(self.empleado_lista_bd)
        for i in range(len(self.empleado_lista_bd)):
            print (self.empleado_lista_bd[i].ver_info()) 