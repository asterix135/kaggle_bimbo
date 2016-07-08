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
	CHANGE COLUMN `ANY_VALUE(Ruta_SAK)` Ruta_SAK INT;

CREATE INDEX `idx_uniques_Cliente_ID_Producto_ID`  
	ON uniques (Cliente_ID, Producto_ID) 
    COMMENT '' 
    ALGORITHM DEFAULT 
    LOCK DEFAULT;
