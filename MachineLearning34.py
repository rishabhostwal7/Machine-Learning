# Evaluation using k fold cross validation
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

model = LogisticRegression()

num_folds = 10

kfold = KFold(n_splits=num_folds)
results = cross_val_score(model, X, Y, cv = kfold)

print("results: ", results)
print()
print("Accuracy : %.3f%% " % ( results.mean()*100.0))
print()
print("Set.Deviation : %.3f%% " % ( results.std()*100.0))