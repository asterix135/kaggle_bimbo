import numpy as np
import pandas as pd
import os
import time

start_time = time.time()
fname = os.path.join(os.path.dirname(os.getcwd()), 'train.csv')
subset = False

#####################
# Load Data subset
#####################
if subset:
    train_iter = pd.read_csv(fname, error_bad_lines=False, usecols=[
        'Venta_uni_hoy', 'Venta_hoy', 'Dev_uni_proxima', 'Dev_proxima',
        'Demanda_uni_equil'
    ],
                             iterator=True, chunksize=100000)
    filtered_dfs = []
    for chunk in train_iter:
        mask = np.random.rand(len(chunk)) < 0.05
        filtered_dfs.append(chunk[mask])
    all_data = pd.concat(filtered_dfs)
else:
    all_data = pd.read_csv(fname, error_bad_lines=False)

print('all_data loaded')

print('\n=========================')
print('data frame description')
print('=========================\n')
print(all_data.describe())

print('\n=========================')
print('unique values')
print('=========================')

for column in all_data:
    print(column, ' - ', len(all_data[column].unique()))
