from empleado_mod import empleado_modelo
from api_BD import Api_BD
from Api_BD_maquinas import Api_BD_maquinas

#codigo principal

#creo base de datos de empleados
obj_Api = Api_BD()
obj_Api_maquina = Api_BD_maquinas()
obj_Api_maquina.imprimir_info()
print(obj_Api_maquina.buscar_info())
#creo el objecto que voy aguardar
obj_empleado= empleado_mod("Miguel","ortega","1093593748","3118353246")
obj_empleado2=empleado_mod("peter","talarga","7654326544","3222223456")
obj_empleado3=empleado_mod("sarah","connor","12345432223","3222222313")
obj_Api.agregar_empleado(obj_empleado)
obj_Api.agregar_empleado(obj_empleado2)
obj_Api.agregar_empleado(obj_empleado3)
obj_Api.imprimir_api()
