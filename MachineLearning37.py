# Cross Validation Classification Accuracy
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

scoringMethod = 'accuracy'      # This is the default method of accuracy

results = cross_val_score(model, X, Y, cv = kfold, scoring = scoringMethod)

print("results: ", results)
print()
print("Accuracy : %.3f%% " % ( results.mean()*100.0))
print()
print("Set.Deviation : %.3f%% " % ( results.std()*100.0))