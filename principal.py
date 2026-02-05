from Base_datos_empleados import Base_datos_empleados
from Empleado_modelo import Empleado_modelo

#crear la base de datos de empleados
obj_bd_empleado_lista = Base_datos_empleados()

#crear el objecto que se va a guardar
obj_empleado1 = Empleado_modelo("robert","ramirez","65432345")
obj_empleado2 = Empleado_modelo("sarah","connor","98765434")

#crear una lista para guardar masivamente
lista_empleados_nuevos = [obj_empleado2,obj_empleado1]

#llamo al metodo para guardar el empleado
obj_bd_empleado_lista.guardar_empleado(obj_empleado1)
obj_bd_empleado_lista.guardar_empleado(obj_empleado2)

obj_bd_empleado_lista.extender_varios_empleados(lista_empleados_nuevos)

#limpiar toda la lista de empleados
obj_bd_empleado_lista.imprimir_info()