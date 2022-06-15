from sqlite3 import DatabaseError
import mysql.connector


database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="jhjo_UBD"
    
)

print(database)

cursor = database.cursor(buffered = True)


class Usuario:

    def __init__(self, nombre,apellidos,edad,sintomas):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.sintomas = sintomas    

    def registrar(self):
        

        sql = "INSERT INTO Usuario VALUES(null, %s, %s, %s,%s) "
        usuario = (self.nombre,self.apellidos,self.edad,self.sintomas)

        cursor.execute(sql, usuario)
        database.commit()

        return [cursor.rowcount, self]

    def identificar(self):
        return self.nombre 