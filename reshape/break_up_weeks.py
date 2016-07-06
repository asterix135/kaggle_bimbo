"""
Break up train data to each individual week
"""
import pandas as pd

from load_data import load_train

all_data = load_train()

for week in range(3, 10):
    fname = '../week' + str(week) + '.csv'
    all_data[all_data['Semana']==week].to_csv(fname)
