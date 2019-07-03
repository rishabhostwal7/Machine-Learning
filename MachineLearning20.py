import pandas as pd
from numpy import set_printoptions
from sklearn.preprocessing import MinMaxScaler

filename = 'indians-diabetes.data.csv'
hnames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = pd.read_csv(filename, names=hnames)

array = dataframe.values
# Seperate array into input and putput components
X = array[ :, 0:8]      # [row, columns]
Y = array[ :, 8]
scaler = MinMaxScaler( feature_range=(1,5) )        # Min =1 and Max=5

# First Method
rescaledX = scaler.fit_transform(X)

# summary of transformed data
set_printoptions(precision=2)
print( rescaledX [ :30, : ] )   # [row,col]

# all the values are larger than 1 and smaller than 5