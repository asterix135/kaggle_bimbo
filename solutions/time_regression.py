"""
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
from load_data import load_train
from sklearn import linear_model


all_data = load_train()
modal_demanda = 2
print('data loaded')

# Step 1: Get only unique Cliente/Producto IDs as a df
uniques = all_data[['Cliente_ID', 'Producto_ID']].drop_duplicates()
print('uniques calculated')

# Step 2: Add Demanda_uni_equil for each week 3-9
for week in range(3, 10):
    # uniques = pd.concat([uniques, all_data[all_data['Semana'==week]]],
    #                     axis=1,
    #                     join='inner')
    uniques = pd.merge(uniques,
                       all_data[['Cliente_ID',
                                 'Producto_ID',
                                 'Demanda_uni_equil']][
                           all_data['Semana'==week]
                       ],
                       # all_data[all_data[['Cliente_ID',
                       #                    'Producto_ID',
                       #                    'Demanda_uni_equil']][
                       #     'Semana'==week]],
                       on=['Cliente_ID', 'Producto_ID'],
                       how='left',
                       suffixes=('', '_' + str(week)))
print('reshaped dataframe built')

# Step 3: Replace all NaNs with zero (assume no demand for week)
uniques = uniques.fillna(0)
print('NAs filled with zeros')

# Step 4: Split train/test (70/30)
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
                                             'Demanda_uni_equil_7']])
week_9_preds = week_11_mod.predict(test_set[['Demanda_uni_equil',
                                             'Demanda_uni_equil_4',
                                             'Demanda_uni_equil_5',
                                             'Demanda_uni_equil_6',
                                             'Demanda_uni_equil_7']])
