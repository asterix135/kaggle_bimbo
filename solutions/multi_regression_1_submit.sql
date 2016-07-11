CREATE TABLE submit1 AS (
	SELECT t.Cliente_ID, t.Producto_ID,
		   u.Demanda_uni_equil_4,
		   u.Demanda_uni_equil_5,
		   u.Demanda_uni_equil_6,
		   u.Demanda_uni_equil_7,
		   u.Demanda_uni_equil_8,
		   u.Demanda_uni_equil_9
	FROM test as t 
	INNER JOIN uniques as u
	ON (t.Cliente_ID = u.Cliente_ID)
		AND (t.Producto_ID = t.Producto_ID));
        