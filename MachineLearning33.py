import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

import warnings
warnings.filterwarnings(action="ignore")

# load data
filename = 'indians-diabetes.data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

dataframe = pd.read_csv(filename, names=names)
array = dataframe.values
X = array[:,0:8]
Y = array[:,8]

test_data_size = 0.33
seed = 7
X_train, X_test, Y_train, Y_test = train_test_split(
                        X, Y, test_size=test_data_size, random_state=seed )

model = LogisticRegression()
model.fit(X_train, Y_train)
result = model.score(X_test,Y_test)

print("Accuracu=y = %f %%" % (result*100))