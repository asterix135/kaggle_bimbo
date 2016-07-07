"""
DO PREPROCESSING IN SQL to avoid blowing up memory

Attempt to predict based on compiled regression of historical
1. Put data into dataframe by customer/product code with each week's data
    included as a column
2. Infer missing data (this is going to be an area to play with)
3. Build a regression model for weeks 8 and 9 based on each of the previous
    weeks (How to deal with missing data?)
4. Build a meta-regression model based on results from 3 (how to deal with
    missing data?)
5. Apply to test set (how to deal with missing data?)
"""

import numpy as np
import pandas as pd
from sklearn import linear_model
import MySQLdb as mysql
from database_details import *

# Step 1: Get data from MySQL
connection = mysql.connect(host=HOST,
                           passwd=PASSWORD,
                           port=PORT,
                           user=USER,
                           db=DB)
SQL = 'SELECT Demanda_uni_equil_3, Demanda_uni_equil_4, Demanda_uni_equil_5, ' \
      'Demanda_uni_equil_6, Demanda_uni_equil_7, Demanda_uni_equil_8, ' \
      'Demanda_uni_equil_9 ' \
      'FROM train'
uniques = pd.read_sql(SQL, connection)
connection.close()

modal_demanda = 2
print('data loaded')


# Step 2: Replace all NaNs with zero (assume no demand for week)
uniques.fillna(0, inplace=True)
print('NAs filled with zeros')

# Step 3: Split train/test (70/30)
mask = np.random.rand(len(uniques)) < 0.7
test_set = uniques[-mask]
train_set = uniques[mask]

# Step 5: Generate a multiple regression model for weeks 8 & 9 based on
#   weeks 3-7


week_10_mod = linear_model.LinearRegression()
week_10_mod.fit(train_set[['Demanda_uni_equil',
                           'Demanda_uni_equil_4',
                           'Demanda_uni_equil_5',
                           'Demanda_uni_equil_6',
                           'Demanda_uni_equil_7']],
                train_set['Demanda_uni_equil_8'])
week_11_mod = linear_model.LinearRegression()
week_11_mod.fit(train_set[['Demanda_uni_equil',
                           'Demanda_uni_equil_4',
                           'Demanda_uni_equil_5',
                           'Demanda_uni_equil_6',
                           'Demanda_uni_equil_7']],
                train_set['Demanda_uni_equil_9'])

week_8_preds = week_10_mod.predict(test_set[['Demanda_uni_equil',
                                             'Demanda_uni_equil_4',
                                             'Demanda_uni_equil_5',
                                             'Demanda_uni_equil_6',
                                             'Demanda_uni_equil_7']]).\
    astype(int)

week_9_preds = week_11_mod.predict(test_set[['Demanda_uni_equil',
                                             'Demanda_uni_equil_4',
                                             'Demanda_uni_equil_5',
                                             'Demanda_uni_equil_6',
                                             'Demanda_uni_equil_7']]).\
    astype(int)

