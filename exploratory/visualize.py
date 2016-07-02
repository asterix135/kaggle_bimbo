import numpy as np
import pandas as pd
import seaborn as sns
import os

fname = os.path.join(os.path.dirname(os.getcwd()), 'train.csv')
train_iter = pd.read_csv(fname, error_bad_lines=False, iterator=True,
                         chunksize=70000)
print("Data loaded.  Filtering to subset")
filtered_dfs = []
for chunk in train_iter:
    mask = np.random.rand(len(chunk)) < 0.1
    filtered_dfs.append(chunk[mask])
train_data = pd.concat(filtered_dfs)
print("train data has ", len(train_data), ' lines')

print('\nFiltering complete, starting plot')

sns.pairplot(train_data)
sns.plt.show()