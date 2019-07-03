# feature importance with ExtraTreesClassifier
# Also known as Extremely randomised trees classifier

import pandas as pd
from sklearn.ensemble import ExtraTreesClassifier

import warnings
warnings.filterwarnings(action="ignore")

# load data
filename = 'indians-diabetes.data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

dataframe = pd.read_csv(filename, names=names)
array = dataframe.values
X = array[:,0:8]
Y = array[:,8]

# feature extraction
model = ExtraTreesClassifier()
model.fit(X, Y)
scores = model.feature_importances_
print(scores)

result = list(zip(names, scores))
print("\n\n")
print(result)
print("\n\n")

from operator import itemgetter
print( sorted( result, key = itemgetter(1), reverse=True))      # to tell the compiler according to which it is sorted ie sort using name or value so we use itemgetter which will tell the compiler to sort according to 2nd element
