from sqlite3 import DatabaseError
import mysql.connector


database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="jhjo_DBD"
    
)

print(database)



cursor = database.cursor(buffered = True)


class Doctor:

    def __init__(self, nombre,apellidos,consultorio):
        self.nombre = nombre
        self.apellidos = apellidos
        self.consultorio = consultorio
    

    def registrar(self):
        

        sql = "INSERT INTO Doctor VALUES(null, %s, %s, %s) "
        doctor = (self.nombre,self.apellidos,self.consultorio)

        cursor.execute(sql, doctor)
        database.commit()

        return [cursor.rowcount, self]

    def identificar(self):
        return self.nombre 
        