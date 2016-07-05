import os
import pandas as pd
import numpy as np


def load_train(subset=False, pct=0.05):
    """
    Loads training data (or subset) into a data frame and returns df
    """
    fname = os.path.join(os.path.dirname(os.getcwd()), 'train.csv')
    if subset:
        train_iter = pd.read_csv(fname, error_bad_lines=False, usecols=[
            'Venta_uni_hoy', 'Venta_hoy', 'Dev_uni_proxima', 'Dev_proxima',
            'Demanda_uni_equil'
        ],
                                 iterator=True, chunksize=100000)
        filtered_dfs = []
        for chunk in train_iter:
            mask = np.random.rand(len(chunk)) < pct
            filtered_dfs.append(chunk[mask])
        all_data = pd.concat(filtered_dfs)
    else:
        all_data = pd.read_csv(fname, error_bad_lines=False)
    return all_data
