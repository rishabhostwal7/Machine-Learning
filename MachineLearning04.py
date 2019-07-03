import pandas
filename = 'indians-diabetes.data.csv'
hnames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

dataframe = pandas.read_csv(filename, names = hnames) # this provides heading to the file
# if we don't supply heading then pandas library will take first instance(row) as a heading of a coloumn

print("pandas data : ", dataframe.shape)    # Size of the matrix will be printed
# print(dataframe)
print("\n\n")
print(type(dataframe))
#   preg, pals, ... are coloumn heading
# and in the left 0,1,2,3... are called  "Row Index"