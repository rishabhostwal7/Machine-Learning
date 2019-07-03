# Binarise Data
from sklearn.preprocessing import Binarizer
from pandas import read_csv
from numpy import set_printoptions

filename = 'indians-diabetes.data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

dataframe = read_csv(filename, names=names)

array = dataframe.values

# Seprate array into input and output components
X = array[:, 0:8]
Y = array[:, 8]

binarizer = Binarizer(threshold=5)
binaryX = binarizer.fit_transform(X)

# summarize transform data
set_printoptions(precision=2)
print( binaryX[0:20, : ] )