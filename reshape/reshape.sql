# Create tables to avoid joins etc on later processing

CREATE TABLE uniques
	AS (SELECT 
    Cliente_ID, Producto_ID
		FROM train
        GROUP BY Cliente_ID,Producto_ID);

