# How to load Machine Learning Data

# 1. Load CSV Files with the Python standard library.
# 2. Load CSV Files with numpy.
# 3. Load CSV Files with Pandas.

# -------------------------------------------------------------------------------------------

import csv

filename = open('indians-diabetes.data.csv', 'r')
reader = csv.reader(filename, delimiter=',')
lines = list(reader)
print("\n\nNo of rows:", len(lines), "\n\n")
print(lines)

for l in lines :
    print("\n\n", l)\

# Every value is in text format

