#crear clase
class Maquina_modelo:
    #crear constructor
    def __init__(self,codigo,nombre,modelo,estado):
        #crear atributos
        self.codigo_maquina=codigo
        self.nombre_maquina=nombre
        self.modelo_maquina=modelo
        self.estado_maquina=estado

        #crear metodos
    def set_codigo_maquina(self,nueva_maquina):
        self.codigo_maquina=nueva_maquina
        
    def get_codigo_maquina(self):
        return self.codigo_maquina
    
    def set_nombre_maquina(self,nuevo_maquina):
        self.nombre_maquina=nuevo_maquina 
        
    def get_nombre_maquina(self):
        return self.nombre_maquina
    
    def set_modelo_maquina(self,nuevo_modelo):
        self.modelo_maquina=nuevo_modelo
        
    def get_modelo_maquina(self):
        return self.modelo_maquina
    
    def set_estado_maquina(self,nuevo_estado):
        self.estado_maquina=nuevo_estado
        
    def get_estado_maquina(self):
        return self.estado_maquina
    
    def ver_info_maquina(self):
        ver_info ="Codigo Maquina: " + self.codigo_maquina + "Nombre Maquina: " + self.nombre_maquina + "Modelo Maquina: " + self.modelo_maquina + "Estado Maquina: " + self.estado_maquina
        return ver_info
        