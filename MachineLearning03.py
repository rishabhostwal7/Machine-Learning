# Older Version of numpy

import numpy
filename = 'indians-diabetes.data.csv'
raw_data = open(filename,'r')

data = numpy.loadtxt(raw_data, delimiter=' ,')

print("Numpy Loadtxt : ", data.shape)   # Tells the dimension of a file
raw_data.close()

print("\n\n\n")

for l in data:
    print(l)


# numpy can categorise data from server also ie it can perform both offline
# numpy opens in integer and in floting format
# numpy prints values in the format of tab seperated format
# ML works mainly with numeric data as compared to text data

# Newer version of numpy

"""import numpy
import urllib.request

web_path = urllib.request.urlopen("https://goo.gl/QnHW4g")
dataset = numpy.genfromtxt(web_path, delimiter=",")

# print(dataset)
for l in dataset:
    print(l)

print("Shape of data from url : ", dataset.shape)

# numpy doesn't read data other than numeric, so to solve this problem we use pandas
"""
