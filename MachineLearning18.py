# B) Multivariate Plots

# this section provides examples of 2 plots that show the interactions between multivariables in your dataset

    # 1) - Correlatin Matrix plot.
    # 2) - Scatter Matrix Plot.

import warnings
warnings.filterwarnings(action="ignore")

# Correlations Matrix Plot
from matplotlib import pyplot as plt
import pandas as pd
import numpy
pd.set_option('display.width', 1000)
pd.set_option('display.max_column', 9)

# pd.set_option("display-width", 2000)

filename = 'indians-diabetes.data.csv'
hnames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = pd.read_csv(filename, names=hnames)

correlations = dataframe.corr()

print(correlations)

# plot correlation matrix
fig = plt.figure()
# Following will add matrix and side bar in entire area
subFig = fig.add_subplot(111)

cax = subFig.mantshow(correlations, vmin=-1, vmax=1)
fig.colorbar(cax)

# --------------------------------------------------
ticks = numpy.arange(0,9)   # it will generate values from 0 to 8
subFig.set_xticks(ticks)
subFig.set_yticks(ticks)
subFig.set_xticklabels(hnames)
subFig.set_yticklabels(hnames)
# --------------------------------------------------

plt.show()


