class Empleado_modelo:
    def __init__(self,nombre,apellido,celular):
        self.nombre_empleado = nombre
        self.apellido_empleado = apellido
        self.celular_empleado = celular
        print ("Empleado creado como objecto")
        
    def get_nombre_empleado(self):
        return self.nombre_empleado
    
    def set_nombre_empleado(self,nuevo_nombre):
        self.nombre_empleado = nuevo_nombre
        
    def ver_info_empleado(self):
        info_empleado = "Nombre empleado: " + self.nombre_empleado
        return info_empleado        
        