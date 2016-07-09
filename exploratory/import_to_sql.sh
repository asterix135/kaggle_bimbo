#!/usr/bin/env bash
# Shell commands to import data files into MySQL

# Import train.csv into train table
mysqlimport --ignore-lines=1 --fields-terminated-by=, --columns='Semana,Agencia_ID,Canal_ID,Ruta_SAK,Cliente_ID,Producto_ID,Venta_uni_hoy,Venta_hoy,Dev_uni_proxima,Dev_proxima,Demanda_uni_equil' --local -u root -p bimbo /Users/christophergraham/documents/code/kaggle/bimbo/train.csv

# Import client info
mysqlimport --ignore-lines=1 --fields-terminated-by=, --columns='Cliente_ID,NombreCliente' --local -u root -p bimbo /Users/christophergraham/documents/code/kaggle/bimbo/cliente_tabla.csv

# Import Products
mysqlimport --ignore-lines=1 --fields-terminated-by=, --columns='Cliente_ID,NombreCliente' --local -u root -p bimbo /Users/christophergraham/documents/code/kaggle/bimbo/producto_tabla.csv;

# Import test.csv
mysqlimport --ignore-lines=1 --fields-terminated-by=, --columns='Semana,Agencia_ID,Canal_ID,Ruta_SAK,Cliente_ID,Producto_ID' --local -u root -p bimbo /Users/christophergraham/documents/code/kaggle/bimbo/test.csv