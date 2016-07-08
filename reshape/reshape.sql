# Create tables to avoid joins etc on later processing
# Keep uniques and final merged weekly

# Note use of ANY_VALUE.  This might need to be changed somehow
CREATE TABLE uniques
	AS (SELECT 
    Cliente_ID, Producto_ID, 
    ANY_VALUE(Agencia_ID), 
    ANY_VALUE(Canal_ID), 
    ANY_VALUE(Ruta_SAK)
		FROM train
        GROUP BY Cliente_ID,Producto_ID);
        
ALTER TABLE uniques
	ADD (Venta_uni_hoy_3 INT,
		 Venta_uni_hoy_4 INT,
         Venta_uni_hoy_5 INT,
         Venta_uni_hoy_6 INT,
         Venta_uni_hoy_7 INT,
         Venta_uni_hoy_8 INT,
         Venta_uni_hoy_9 INT,
         Venta_hoy_3 FLOAT,
         Venta_hoy_4 FLOAT,
         Venta_hoy_5 FLOAT,
         Venta_hoy_6 FLOAT,
         Venta_hoy_7 FLOAT,
         Venta_hoy_8 FLOAT,
         Venta_hoy_9 FLOAT,
         Dev_uni_proxima_3 INT,
         Dev_uni_proxima_4 INT,
         Dev_uni_proxima_5 INT,
         Dev_uni_proxima_6 INT,
         Dev_uni_proxima_7 INT,
         Dev_uni_proxima_8 INT,
         Dev_uni_proxima_9 INT,
         Dev_proxima_3 FLOAT,
         Dev_proxima_4 FLOAT,
         Dev_proxima_5 FLOAT,
         Dev_proxima_6 FLOAT,
         Dev_proxima_7 FLOAT,
         Dev_proxima_8 FLOAT,
         Dev_proxima_9 FLOAT,
         Demanda_uni_equil_3 INT,
         Demanda_uni_equil_4 INT,
         Demanda_uni_equil_5 INT,
         Demanda_uni_equil_6 INT,
         Demanda_uni_equil_7 INT,
         Demanda_uni_equil_8 INT,
         Demanda_uni_equil_9 INT);


ALTER TABLE uniques
	CHANGE COLUMN `ANY_VALUE(Agencia_ID)` Agencia_ID INT;

ALTER TABLE uniques
	CHANGE COLUMN `ANY_VALUE(Canal_ID)` Canal_ID INT;

ALTER TABLE uniques
	CHANGE COLUMN `ANY_VALUE(Ruta_SAK)` Ruta_SAK INTd;

CREATE TABLE week3 AS (
	SELECT u.*,
		   t3.Venta_uni_hoy AS Venta_uni_hoy_3,
           t3.Venta_hoy AS Venta_hoy_3,
           t3.Dev_uni_proxima AS Dev_uni_proxima_3,
           t3.Dev_proxima AS Dev_proxima_3,
           t3.Demanda_uni_equil AS Demanda_uni_equil_3
		FROM uniques as u
		LEFT OUTER JOIN train as t3
		ON (u.Cliente_ID = t3.Cliente_ID)
			AND (u.Producto_ID = t3.Producto_ID)
			AND t3.Semana = 3
);

CREATE TABLE week4 AS (
	SELECT w3.*,
		   t4.Venta_uni_hoy AS Venta_uni_hoy_4,
           t4.Venta_hoy AS Venta_hoy_4,
           t4.Dev_uni_proxima AS Dev_uni_proxima_4,
           t4.Dev_proxima AS Dev_proxima_4,
           t4.Demanda_uni_equil AS Demanda_uni_equil_4
		FROM week3 as w3
		LEFT OUTER JOIN train as t4
		ON (w3.Cliente_ID = t4.Cliente_ID)
			AND (w3.Producto_ID = t4.Producto_ID)
			AND t4.Semana = 4
);

DROP TABLE week3;

CREATE TABLE week5 AS (
	SELECT w4.*,
		   t5.Venta_uni_hoy AS Venta_uni_hoy_5,
           t5.Venta_hoy AS Venta_hoy_5,
           t5.Dev_uni_proxima AS Dev_uni_proxima_5,
           t5.Dev_proxima AS Dev_proxima_5,
           t5.Demanda_uni_equil AS Demanda_uni_equil_5
		FROM week4 as w4
		LEFT OUTER JOIN train as t5
		ON (w4.Cliente_ID = t5.Cliente_ID)
			AND (w4.Producto_ID = t5.Producto_ID)
			AND t5.Semana = 5
);

DROP TABLE week4;

CREATE TABLE week6 AS (
	SELECT w5.*,
		   t6.Venta_uni_hoy AS Venta_uni_hoy_6,
           t6.Venta_hoy AS Venta_hoy_6,
           t6.Dev_uni_proxima AS Dev_uni_proxima_6,
           t6.Dev_proxima AS Dev_proxima_6,
           t6.Demanda_uni_equil AS Demanda_uni_equil_6
		FROM week5 as w5
		LEFT OUTER JOIN train as t6
		ON (w5.Cliente_ID = t6.Cliente_ID)
			AND (w5.Producto_ID = t6.Producto_ID)
			AND t6.Semana = 6
);

DROP TABLE week5;

CREATE TABLE week7 AS (
	SELECT w6.*,
		   t7.Venta_uni_hoy AS Venta_uni_hoy_7,
           t7.Venta_hoy AS Venta_hoy_7,
           t7.Dev_uni_proxima AS Dev_uni_proxima_7,
           t7.Dev_proxima AS Dev_proxima_7,
           t7.Demanda_uni_equil AS Demanda_uni_equil_7
		FROM week6 as w6
		LEFT OUTER JOIN train as t7
		ON (w6.Cliente_ID = t7.Cliente_ID)
			AND (w6.Producto_ID = t7.Producto_ID)
			AND t7.Semana = 7
);

DROP TABLE week6;

CREATE TABLE week8 AS (
	SELECT w7.*,
		   t8.Venta_uni_hoy AS Venta_uni_hoy_8,
           t8.Venta_hoy AS Venta_hoy_8,
           t8.Dev_uni_proxima AS Dev_uni_proxima_8,
           t8.Dev_proxima AS Dev_proxima_8,
           t8.Demanda_uni_equil AS Demanda_uni_equil_8
		FROM week7 as w7
		LEFT OUTER JOIN train as t8
		ON (w7.Cliente_ID = t8.Cliente_ID)
			AND (w7.Producto_ID = t8.Producto_ID)
			AND t8.Semana = 8
);

DROP TABLE week7;

CREATE TABLE weekly AS (
	SELECT w8.*,
		   t9.Venta_uni_hoy AS Venta_uni_hoy_9,
           t9.Venta_hoy AS Venta_hoy_9,
           t9.Dev_uni_proxima AS Dev_uni_proxima_9,
           t9.Dev_proxima AS Dev_proxima_9,
           t9.Demanda_uni_equil AS Demanda_uni_equil_9
		FROM week8 as w8
		LEFT OUTER JOIN train as t9
		ON (w8.Cliente_ID = t9.Cliente_ID)
			AND (w8.Producto_ID = t9.Producto_ID)
			AND t9.Semana = 9
);

DROP TABLE week8;