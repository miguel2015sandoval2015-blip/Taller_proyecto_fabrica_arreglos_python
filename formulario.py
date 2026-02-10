import tkinter as ventana
def enviar_info():
    print("datos enviadados a la base de datos: ")


formulario = ventana.Tk()
formulario.title("Registro de maquinas")


codigo_maquina=ventana.Label(formulario,text="codigo maquina: ")
codigo_maquina.pack()
codigo_maquina = ventana.Entry(formulario)
codigo_maquina.pack()

nombre_maquina = ventana.Label(formulario,text="Nombre maquina: ")
nombre_maquina.pack()
nombre_maquina = ventana.Entry(formulario)
nombre_maquina.pack()

modelo_maquina=ventana.Label(formulario,text="modelo maquina: ")
modelo_maquina.pack()
modelo_maquina = ventana.Entry(formulario)
modelo_maquina.pack()

estado_maquina=ventana.Label(formulario,text="estado maquina: ")
estado_maquina.pack()
estado_maquina = ventana.Entry(formulario)
estado_maquina.pack()


boton_maquina = ventana.Button(formulario, text="guardar maquina")
boton_maquina.pack()



formulario.mainloop()

