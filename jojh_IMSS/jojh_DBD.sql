CREATE DATABASE IF NOT EXISTS jhjo_DBD;

USE jhjo_DBD;

CREATE TABLE Doctor(
     id  int (25) auto_increment not null,
     nombre varchar (100),
     apellidos varchar (255),
     consultorio int (255),
     CONSTRAINT pk_Doctor PRIMARY KEY (id),
) ENGINE=InnoDb;
