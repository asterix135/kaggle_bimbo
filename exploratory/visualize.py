import pandas as pd
import seaborn as sns
import os

fname = os.path.join(os.path.dirname(os.getcwd()), 'train.csv')
train_data = pd.read_csv('train.csv', error_bad_lines=False)
sns.pairplot(train_data)
sns.plt.show()