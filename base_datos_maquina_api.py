#crear la clase 
class Bd_maquina_lista:
    #creo el constructor
    def __init__(self):              #se crea el array de la base de datos de las maquina
        self.maquina_lista_bd = []
        
    def guardar_maquina(self,obj_nueva_maquina):#guardo el metodo de la maquina
        self.maquina_lista_bd.append(obj_nueva_maquina)
        return True
    
    def extend_lista_maquina(self,nueva_lista):
        self.maquina_lista_bd.extend(nueva_lista)
     
        
    def imprimir_info(self):
        print(self.maquina_lista_bd)
        for i in range(len(self.maquina_lista_bd)):    
            print (self.maquina_lista_bd[i].ver_info_maquina())    
        
        