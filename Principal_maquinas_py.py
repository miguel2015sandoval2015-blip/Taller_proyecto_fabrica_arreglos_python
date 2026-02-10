from base_datos_maquina_api import Bd_maquina_lista
from Maquina_modelo import Maquina_modelo
 
obj_maquina_lista = Bd_maquina_lista() # se crea la instancia de la lista de las maquinas


obj_maquina1 = Maquina_modelo("4321: ", "Brazo Mecanico: ","XTZ 490: ", "APAGADA: ")
obj_maquina2 = Maquina_modelo("5675: ", "Cinta Transportadora: ", "NHR 800: ", "REQUIERE MANTENIMIENTO")
obj_maquina3 = Maquina_modelo("6574: " , "Mono Brazo: " , "KRH200: " , "ENCENDIDA: " )

obj_maquina_lista.guardar_maquina(obj_maquina1)
obj_maquina_lista.guardar_maquina(obj_maquina2)
obj_maquina_lista.guardar_maquina(obj_maquina3)

nuevas_maquinas=[obj_maquina1,obj_maquina2,obj_maquina3]
obj_maquina_lista.extend_lista_maquina(nuevas_maquinas)

obj_maquina_lista.imprimir_info()