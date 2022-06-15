import Usu.usuario as modelo

class RegistroU:

    def registro(self):
        

        print("Se procederá a realizar el registro en el sistema")
    nombre = input("¿Cual es tu nombre paciente?  ")
    apellidos = input("¿Cuales son sus apellidos?  ")
    edad = input("¿Cual es su edad? ")
    sintomas = input("¿Cuales son sus sintomas? ")
    

    usuario = modelo.Usuario(nombre,apellidos,edad,sintomas)
    registro = usuario.registrar()


    if registro[0] >=1:
        print(f"Perfecto {registro[1].nombre} tu cita se ah agendado.")
    else:
        print("No se ha registrado correctamente")