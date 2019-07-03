import pandas as pd
from sklearn.decomposition import PCA

# load data
filename = 'indians-diabetes.data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

dataframe = pd.read_csv(filename, names=names)
array = dataframe.values
X = array[:,0:8]
Y = array[:,8]

# feature extraction
pca = PCA(n_components=3)
                                    # vaLue should be condesed such that varinace is higher. whenever the value is condensed there is some chance tha some values are lost or change but our data alwaysbecomes minimum
fit = pca.fit(X)

resultX = pca.transform(X)      # transform() will reduce it to 3 columns
print("Result : ", resultX)

# Summarise components
print("Explained Variance = %s" % fit.explained_variance_ratio_)