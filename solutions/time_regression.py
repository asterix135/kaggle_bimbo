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
from sklearn import metrics
from sklearn.externals import joblib
import pymysql as mysql
from database_details import *

SUBSET_OF_DATA = False

# Step 1: Get data from MySQL
connection = mysql.connect(host=HOST,
                           password=PASSWORD,
                           port=PORT,
                           user=USER,
                           db=DB)
SQL = 'SELECT Demanda_uni_equil_3, Demanda_uni_equil_4, Demanda_uni_equil_5, ' \
      'Demanda_uni_equil_6, Demanda_uni_equil_7, Demanda_uni_equil_8, ' \
      'Demanda_uni_equil_9 ' \
      'FROM uniques'
if SUBSET_OF_DATA:
    SQL += ' LIMIT 5000000'
uniques = pd.read_sql(SQL, connection)
connection.close()

modal_demanda = 2
mean_demanda = 7
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
week_10_mod.fit(train_set[['Demanda_uni_equil_3',
                           'Demanda_uni_equil_4',
                           'Demanda_uni_equil_5',
                           'Demanda_uni_equil_6',
                           'Demanda_uni_equil_7',
                           'Demanda_uni_equil_8']],
                train_set['Demanda_uni_equil_9'])
week_11_mod = linear_model.LinearRegression()
week_11_mod.fit(train_set[['Demanda_uni_equil_3',
                           'Demanda_uni_equil_4',
                           'Demanda_uni_equil_5',
                           'Demanda_uni_equil_6',
                           'Demanda_uni_equil_7']],
                train_set['Demanda_uni_equil_9'])

prev_6_week_preds = week_10_mod.predict(test_set[['Demanda_uni_equil_3',
                                                  'Demanda_uni_equil_4',
                                                  'Demanda_uni_equil_5',
                                                  'Demanda_uni_equil_6',
                                                  'Demanda_uni_equil_7',
                                                  'Demanda_uni_equil_8']]).\
    astype(int)

no_prev_week_preds = week_11_mod.predict(test_set[['Demanda_uni_equil_3',
                                                   'Demanda_uni_equil_4',
                                                   'Demanda_uni_equil_5',
                                                   'Demanda_uni_equil_6',
                                                   'Demanda_uni_equil_7']]).\
    astype(int)

mock_week_10_preds = metrics.mean_squared_error(test_set['Demanda_uni_equil_9'],
                                                prev_6_week_preds)
mock_week_11_preds = metrics.mean_squared_error(test_set['Demanda_uni_equil_9'],
                                                no_prev_week_preds)

week_9_mode_rss = metrics.mean_squared_error(np.full(len(test_set),
                                                     modal_demanda),
                                             no_prev_week_preds)
week_9_mean_rss = metrics.mean_squared_error(np.full(len(test_set),
                                                     mean_demanda),
                                             no_prev_week_preds)

print('\n=============================')
print('RESULTS')
print('=============================')
print('Mock Week 10 RSS: ', mock_week_10_preds)
print('Mock Week 11 RSS: ', mock_week_11_preds)
print('Mode RSS: ', week_9_mode_rss)
print('Mean RSS: ', week_9_mean_rss)
print('=============================\n')

##################
# Save models for test prediction
##################

joblib.dump(week_10_mod, 'Week_10_model1.pkl')
joblib.dump(week_11_mod, 'Week_11_model1.pkl')


