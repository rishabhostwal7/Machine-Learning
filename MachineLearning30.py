import pandas as pd
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression

import warnings
warnings.filterwarnings(action="ignore")

# Load data
filename = 'indians-diabetes.data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

dataframe = pd.read_csv(filename, names=names)
array = dataframe.values
X = array[:,0:8]
Y = array[:,8]

# feature extraction
model = LogisticRegression()
rfe = RFE(model, 3)
fit = rfe.fit(X,Y)
result = fit.transform(X)

print("Num features : ", fit.n_features_)
print("Selected fetures : ", fit.support_)
print("Feature ranking : ", fit.ranking_)
print("\n\n\n", result[:30,:])

