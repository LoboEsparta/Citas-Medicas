import Doc.doctor as modelo

class Registro:

    def registro(self):
        

        print("Se procederá a realizar su registro en el sistema")
    nombre = input("¿Cual es tu nombre Doc.?  ")
    apellidos = input("¿Cuales son sus apellidos?  ")
    consultorio = input("Introduce el No.de Consultorio:  ")
    

    doctor = modelo.Doctor(nombre,apellidos,consultorio)
    registro = doctor.registrar()


    if registro[0] >=1:
        print(f"Perfecto se ah registrado a {registro[1].nombre} con consultorio No.  {registro[1].consultorio}")
    else:
        print("No te has registrado correctamente")