class datos_diccionario:
    def __int__(self):
        self.datos_diccionario = {"1093593748": {"nombre":"miguel", "apellido": "ortega", 
        "maquina": ("maquinas1","maquinas2","maquinas3")}}
        
        def longitud_dicionario(self):
            longitud=len(self.datos_diccionario)
            return
            
        def limpiar_diccionario(self):
            limpiar=self.datos_diccionario.clear()
            self.datos_diccionario=limpiar
            
        def copiar_diccionario(self):
            copiar=self.datos_diccionario.copy() 
            return copiar
        
        def sacar_elementos(self):
            sacar=self.dato_diccionario.intems()
            return sacar
               
        def devolver_llaver(self):
            devolver = self.datos_diccionario.keys()
            return devolver
            
        def sacar_valores(self):
            dato_valores = self.datos_diccionario.values()
            return dato_valores
            
        def eliminar_elementos(self):
            eliminar = self.datos_diccionario.pop()
            return eliminar
            
        def eliminar_elemento(self):
            eliminar = self.datos_diccionario.popitem()
            return eliminar
        
        def actualizar_info(self,nuevo_diccionario):
            actualizar = self.datos_diccionario.update(nuevo_diccionario)  
            
        def imprimir_info(self):
            for clave in self.datos_diccionario.keys():
                print(f"dato_info: (self.datos_diccionario[clave])")           