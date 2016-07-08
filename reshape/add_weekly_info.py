import csv
import pymysql as mysql
import os
import time
from database_details import *

fname = os.path.join(os.path.dirname(os.getcwd()), 'train.csv')
csv_file = csv.reader(open(fname, 'r'))

connection = mysql.connect(host=HOST,
                           password=PASSWORD,
                           port=PORT,
                           user=USER,
                           db=DB)


def update_db(row):
    SQL = {3: 'UPDATE uniques '
              'SET Venta_uni_hoy_3 = %s, Venta_hoy_3 = %s, '
              'Dev_uni_proxima_3 = %s, Dev_proxima_3 = %s, '
              'Demanda_uni_equil_3 = %s '
              'WHERE (Cliente_ID = %s AND Producto_ID = %s)',
           4: 'UPDATE uniques '
              'SET Venta_uni_hoy_4 = %s, Venta_hoy_4 = %s, '
              'Dev_uni_proxima_4 = %s, Dev_proxima_4 = %s, '
              'Demanda_uni_equil_4 = %s '
              'WHERE (Cliente_ID = %s AND Producto_ID = %s)',
           5: 'UPDATE uniques '
              'SET Venta_uni_hoy_5 = %s, Venta_hoy_5 = %s, '
              'Dev_uni_proxima_5 = %s, Dev_proxima_5 = %s, '
              'Demanda_uni_equil_5 = %s '
              'WHERE (Cliente_ID = %s AND Producto_ID = %s)',
           6: 'UPDATE uniques '
              'SET Venta_uni_hoy_6 = %s, Venta_hoy_6 = %s, '
              'Dev_uni_proxima_6 = %s, Dev_proxima_6 = %s, '
              'Demanda_uni_equil_6 = %s '
              'WHERE (Cliente_ID = %s AND Producto_ID = %s)',
           7: 'UPDATE uniques '
              'SET Venta_uni_hoy_7 = %s, Venta_hoy_7 = %s, '
              'Dev_uni_proxima_7 = %s, Dev_proxima_7 = %s, '
              'Demanda_uni_equil_7 = %s '
              'WHERE (Cliente_ID = %s AND Producto_ID = %s)',
           8: 'UPDATE uniques '
              'SET Venta_uni_hoy_8 = %s, Venta_hoy_8 = %s, '
              'Dev_uni_proxima_8 = %s, Dev_proxima_8 = %s, '
              'Demanda_uni_equil_8 = %s '
              'WHERE (Cliente_ID = %s AND Producto_ID = %s)',
           9: 'UPDATE uniques '
              'SET Venta_uni_hoy_9 = %s, Venta_hoy_9 = %s, '
              'Dev_uni_proxima_9 = %s, Dev_proxima_9 = %s, '
              'Demanda_uni_equil_9 = %s '
              'WHERE (Cliente_ID = %s AND Producto_ID = %s)',
           }
    week = int(row[0])
    params = [row[6], row[7], row[8], row[9], row[10],
              row[4], row[5]]
    with connection.cursor() as cursor:
        cursor.execute(SQL[week], params)
    connection.commit()

start_time = time.time()
i = 0

for row in csv_file:
    if i > 0:
        update_db(row)
    i += 1
    if i % 10000 == 1:
        elapsed_time = time.time() - start_time
        total_records = i - 1
        print(total_records, ' records processed in ',
              elapsed_time, ' seconds.')

elapsed_time = time.time() - start_time
print('\n==================\nOWARI\nTotal Time: %s seconds\n=================='
      % elapsed_time)
