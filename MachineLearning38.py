# 2 Cross validation using classification LogLoss

import warnings
warnings.filterwarnings(action="ignore")

import pandas as pd

from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score

from sklearn.linear_model import LogisticRegression
# load data
filename = 'indians-diabetes.data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

dataframe = pd.read_csv(filename, names=names)
array = dataframe.values
X = array[:,0:8]
Y = array[:,8]

kfold = KFold(n_splits=10)
model = LogisticRegression()

scoringMethod = 'neg_log_loss'      # Value will always be -ve and it will be within range 0 to 1

results = cross_val_score(model, X, Y, cv = kfold, scoring = scoringMethod)

print("LogLoss : %.3f (%.3f)" % (results.mean(), results.std()))
