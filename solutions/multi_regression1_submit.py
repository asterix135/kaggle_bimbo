"""
Uses simple multiple regression model to generate predictions on test set
If a client/product combo doesn't exist in the train set, use mode value as
prediction
"""

import numpy as np
import pandas as pd
import pymysql as mysql
from sklearn import linear_model
from sklearn.externals import joblib
from database_details import *

DEMANDA_MODE = 2

# 1. Load test records that have a match in the reshaped training dataset
#    run multi_regression_1_submit.sql first to create table for this

connection = mysql.connect(host=HOST,
                           password=PASSWORD,
                           port=PORT,
                           user=USER,
                           db=DB)

# Week 10
SQL = 'SELECT * ' \
      'FROM uniques ' \
      'WHERE Week_10_test_id is not null'

week_10_test = pd.read_sql(SQL, connection)

# Week 11
SQL = 'SELECT * ' \
      'FROM unique ' \
      'WHERE Week_11_test_id is not null'

week_11_test = pd.read_sql(SQL, connection)

connection.close()

# Fill NAs with zeros
week_10_test.fillna(0, inplace=True)
week_11_test.fillna(0, inplace=True)

# 2. Load previously saved linear models

week_10_model = joblib.load('Week_10_model1.pkl')
week_11_model = joblib.load('Week_11_model1.pkl')

# 3. Apply appropriate models to test data sets

week_10_preds = week_10_model.predict(week_10_test[['Demanda_uni_equil_4',
                                                    'Demanda_uni_equil_5',
                                                    'Demanda_uni_equil_6',
                                                    'Demanda_uni_equil_7',
                                                    'Demanda_uni_equil_8',
                                                    'Demanda_uni_equil_9']]).\
    astype(int)
week_11_preds = week_11_model.predict(week_11_test[['Demanda_uni_equil_5',
                                                    'Demanda_uni_equil_6',
                                                    'Demanda_uni_equil_7',
                                                    'Demanda_uni_equil_8',
                                                    'Demanda_uni_equil_9']]).\
    astype(int)

# 4. Combine into one data frame, predicting modal value for missing entries

submission = {}
for i in range(6999251):
    if i in week_10_test['Semana']:
        submission[i] = week_10_preds # how to find right value

# 5. sort by id and save as csv