CREATE DATABASE IF NOT EXISTS jhjo_UBD

CREATE TABLE IF NOT EXISTS Usuario(
     id  int (25) auto_increment not null,
     nombre varchar (100),
     apellidos varchar (255),
     edad int (255),
     sintomas varchar (255),
     CONSTRAINT pk_Usuario PRIMARY KEY (id)
)
