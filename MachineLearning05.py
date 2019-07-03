import pandas
import urllib.request

hnames = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
web_path = urllib.request.urlopen("https://goo.gl/QnHW4g")

data_frame = pandas.read_csv(web_path, names = hnames)
print(data_frame.shape)
print(data_frame)
data = data_frame.columns
print(data[1])
