import warnings
warnings.filterwarnings(action="ignore")

# Scatter

from  matplotlib import pyplot as plt

from pandas import read_csv
# import pandas
from pandas.plotting import scatter_matrix

import warnings
warnings.filterwarnings(action="ignore")

filename = 'indians-diabetes.data.csv'
hnames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = read_csv(filename, names=hnames)

scatter_matrix((dataframe))
plt.show()
