import numpy as np
import pandas as pd
from sklearn import linear_model
from matplotlib import pyplot as plt
import os
import time

start_time = time.time()
fname = os.path.join(os.path.dirname(os.getcwd()), 'train.csv')

#####################
# Load Data subset
#####################
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

print('all_data loaded')

mask = np.random.rand(len(all_data)) < 0.7
test_set = all_data[-mask]
train_set = all_data[mask]

mid1_time = time.time()
mid1_duration = mid1_time - start_time
print('Data loaded.  Time: ', mid1_duration)


def create_plot(x_val, y_val, fname, plt_title='Plot', regr_vals=None):
    plt.scatter(x_val, y_val, color='black')
    if regr_vals is not None:
        plt.plot(x_val, regr_vals, color='blue')
    plt.title = plt_title
    plt.savefig(fname, format='png')

################################
# Model 1
# Simple regression
# Venta_uni_hoy vs 'Demanda_uni_equil'
################################

mod1 = linear_model.LinearRegression()
x_val_train = np.array(train_set['Venta_uni_hoy'].reshape(len(train_set), 1))
mod1.fit(x_val_train, train_set['Demanda_uni_equil'])

x_val_test = np.array(test_set['Venta_uni_hoy'].reshape(len(test_set), 1))
mod1_preds = mod1.predict(x_val_test)
print('\n=======================')
print('Results for model 1 (venta_uni_hoy')
print('Coefficients: \n', mod1.coef_)
print('RSS: %.2f' % np.mean((mod1_preds - test_set['Demanda_uni_equil'])))
print('Variance score %.2f' % mod1.score(x_val_test,
                                         test_set['Demanda_uni_equil']))
print('=======================\n')

create_plot(test_set['Venta_uni_hoy'], test_set['Demanda_uni_equil'],
            'Venta_uni_hoy_regr.png',
            'Venta_uni_hoy simple regression', mod1_preds)

#################################
# Model 2
# Simple regresion
# Venta_hoy vs 'Demanda_uni_equil'
#################################

mod2 = linear_model.LinearRegression()
x_val_train = np.array(train_set['Venta_hoy'].reshape(len(train_set), 1))
mod2.fit(x_val_train, train_set['Demanda_uni_equil'])

x_val_test = np.array(test_set['Venta_hoy'].reshape(len(test_set), 1))
mod2_preds = mod2.predict(x_val_test)
print('\n=======================')
print('Results for model 2 (venta_hoy)')
print('Coefficients: \n', mod2.coef_)
print('RSS: %.2f' % np.mean((mod2_preds - test_set['Demanda_uni_equil'])))
print('Variance score %.2f' % mod2.score(x_val_test,
                                         test_set['Demanda_uni_equil']))
print('=======================\n')

create_plot(test_set['Venta_hoy'], test_set['Demanda_uni_equil'],
            'Venta_hoy_regr.png',
            'Venta_hoy simple regression', mod2_preds)

#################################
# Model 3
# Simple regresion
# Dev_uni_proxima vs 'Demanda_uni_equil'
#################################

mod3 = linear_model.LinearRegression()
x_val_train = np.array(train_set['Dev_uni_proxima'].reshape(len(train_set), 1))
mod3.fit(x_val_train, train_set['Demanda_uni_equil'])

x_val_test = np.array(test_set['Dev_uni_proxima'].reshape(len(test_set), 1))
mod3_preds = mod3.predict(x_val_test)
print('\n=======================')
print('Results for model 3 (Dev_uni_proxima)')
print('Coefficients: \n', mod3.coef_)
print('RSS: %.2f' % np.mean((mod3_preds - test_set['Demanda_uni_equil'])))
print('Variance score %.2f' % mod3.score(x_val_test,
                                         test_set['Demanda_uni_equil']))
print('=======================\n')

create_plot(test_set['Dev_uni_proxima'], test_set['Demanda_uni_equil'],
            'Dev_uni_proxima_regr.png',
            'Dev_uni_proxima simple regression', mod3_preds)

#################################
# Model 4
# Simple regresion
# Dev_proxima vs 'Demanda_uni_equil'
#################################

mod4 = linear_model.LinearRegression()
x_val_train = np.array(train_set['Dev_proxima'].reshape(len(train_set), 1))
mod4.fit(x_val_train, train_set['Demanda_uni_equil'])

x_val_test = np.array(test_set['Dev_proxima'].reshape(len(test_set), 1))
mod4_preds = mod4.predict(x_val_test)
print('\n=======================')
print('Results for model 4 (Dev_proxima)')
print('Coefficients: \n', mod4.coef_)
print('RSS: %.2f' % np.mean((mod4_preds - test_set['Demanda_uni_equil'])))
print('Variance score %.2f' % mod4.score(x_val_test,
                                         test_set['Demanda_uni_equil']))
print('=======================\n')

create_plot(test_set['Dev_proxima'], test_set['Demanda_uni_equil'],
            'Dev_proxima_regr.png',
            'Dev_proxima simple regression', mod3_preds)

#################################
# Model 5
# Multiple regresion
# 4 values vs 'Demanda_uni_equil'
#################################

mod5 = linear_model.LinearRegression()
mod5.fit(train_set[[
    'Venta_uni_hoy', 'Venta_hoy', 'Dev_uni_proxima', 'Dev_proxima'
]], train_set['Demanda_uni_equil'])

mod5_preds = mod4.predict(test_set[[
    'Venta_uni_hoy', 'Venta_hoy', 'Dev_uni_proxima', 'Dev_proxima'
]])

print('\n=======================')
print('Results for model 4 (Multiple)')
print('Coefficients: \n', mod5.coef_)
print('RSS: %.2f' % np.mean((mod5_preds - test_set['Demanda_uni_equil'])))
# print('Variance score %.2f' % mod5.score(x_val_test,
#                                          test_set['Demanda_uni_equil']))
print('=======================\n')


mid2_time = time.time()
mid2_duration = mid2_time - mid1_time
print('Models Built.  Time: ', mid2_duration)



entire_duration = time.time() - start_time
print("Entire process took: ", entire_duration)