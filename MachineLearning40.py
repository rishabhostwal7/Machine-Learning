import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

import warnings
warnings.filterwarnings(action="ignore")

filename = 'indians-diabetes.data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

dataframe = pd.read_csv(filename, names=names)
array = dataframe.values
X = array[:,0:8]
Y = array[:,8]

test_size = 0.33
seed = 7
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=test_size, random_state=seed
)
model = LogisticRegression()
model.fit(X_train, Y_train)     # 67% of X and 67% of Y k data use krke we are calculation best fit hypothesis

predicted = model.predict(X_test)   # after training of model we apply it in 33% of X
matrix = confusion_matrix(Y_test, predicted)

print(matrix)