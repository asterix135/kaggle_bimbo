import csv
import pymysql as mysql
import os
import time
from database_details import *

fname = os.path.join(os.path.dirname(os.getcwd()), 'test.csv')
csv_file = csv.reader(open(fname, 'r'))

connection = mysql.connect(host=HOST,
                           password=PASSWORD,
                           port=PORT,
                           user=USER,
                           db=DB)


def add_test_week(row):
    sql = {10: 'UPDATE uniques '
               'SET Week_10_test_id = %s '
               'WHERE (Cliente_ID = %s AND Producto_ID = %s)',
           11: 'UPDATE uniques '
               'SET Week_11_test_id = %s '
               'WHERE (Cliente_ID = %s AND Producto_ID = %s)'}
    week = int(row[1])
    params = [row[0], row[5], row[6]]
    with connection.cursor() as cursor:
        cursor.execute(sql[week], params)
    connection.commit()


start_time = time.time()
i = 0

for row in csv_file:
    if i > 0:
        add_test_week(row)
    i += 1
    if i % 10000 == 1:
        elapsed_time = time.time() - start_time
        total_records = i - 1
        print(total_records, ' records processed in ',
              elapsed_time, ' seconds.')

elapsed_time = time.time() - start_time
print('\n==================\nOWARI\nTotal Time: %s seconds\n=================='
      % elapsed_time)