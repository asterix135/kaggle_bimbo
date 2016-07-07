# Basic MySQL setup

create database bimbo;
use bimbo;
create table test(
	id INT PRIMARY KEY,
    Semana INT,
    Agencia_ID INT,
    Canal_ID INT,
    Ruta_SAK INT,
    Cliente_ID INT,
    Producto_ID INT
);
create table train(
	PK_ID INT PRIMARY KEY AUTO_INCREMENT,
    Semana INT,
    Agencia_ID INT,
    Canal_ID INT,
    Ruta_SAK INT,
    Cliente_ID INT,
    Producto_ID INT,
    Venta_uni_hoy INT,
    Venta_hoy FLOAT,
    Dev_uni_proxima INT,
    Dev_proxima FLOAT,
    Demanda_uni_equil INT
);
create table cliente_tabla (
	PK_ID INT PRIMARY KEY AUTO_INCREMENT,
    Cliente_ID INT,
    NombreCliente VARCHAR(255)
);
CREATE TABLE producto_tabla (
	PK_ID INT PRIMARY KEY AUTO_INCREMENT,
    Producto_ID INT,
    NombreProducto VARCHAR(255)
);
CREATE TABLE town_state (
	Agencia_ID INT PRIMARY KEY,
    Town VARCHAR(255),
    State VARCHAR(255)
);