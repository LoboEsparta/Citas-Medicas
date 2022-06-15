
print(""""

¿Que desea hacer? 

      --- Registrar Doctor 
      
      --- Agendar Cita Medica      
      """)

accion = input("Escriba su solicitud: ")


if accion == "2":
    import Doc.registroDoc as registroDoc
    registroDoc.Registro()

elif accion == "1":
    import Usu.registroUsu as registroUsu
    registroUsu.RegistroU()
    

