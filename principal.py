from Base_datos_lista_empleado  import Bd_empleados_lista
from Empleado_modelo import Empleado_modelo
from diccionario import datos_diccionario


obj_empleado_lista = Bd_empleados_lista( ) #se hace la instancia de la lista

obj_empleado = Empleado_modelo("miguel: ","ortega: ","1093593748: ","3232435108: ")
obj_empleado2 = Empleado_modelo("marco: ","ramo: ","10923433232: ","3212323443: ")
obj_empleado3 = Empleado_modelo("ana: ","maya: ","1092873456:  ","356323323: ")
 
obj_empleado_lista.guardar_empleado(obj_empleado)
obj_empleado_lista.guardar_empleado(obj_empleado2)
obj_empleado_lista.guardar_empleado(obj_empleado3)

nuevos_empleados=[obj_empleado,obj_empleado2,obj_empleado3]
obj_empleado_lista.extend_lista_empleado(nuevos_empleados)

obj_empleado_lista.imprimir_info()

obj_diccionario = datos_diccionario()
info = obj_diccionario.sacar_valores()
print(info)

nuevo_diccionario = {"1093593748": {"nombre":"marcos","apellido": "rosales", "maquina": {"maquina pinturas",
"maquina hidraulica"}}}

obj_diccionario.actualizar_info(nuevo_diccionario)
obj_diccionario.imprimir_info()