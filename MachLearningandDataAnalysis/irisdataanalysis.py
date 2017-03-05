#This is a basic data analysis snippet describing the features of sklearn's iris dataset
import pandas
import sklearn
from pandas.tools.plotting import scatter_matrix
import matplotlib.pyplot as plt;
url="https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data";
names=['sepal-length','sepal-width','petal-length','petal-width','class']
dataset=pandas.read_csv(url,names=names);
#getting the dimensions of the dataset
print(dataset.shape)
#Peeking at the first 20 values of our dataset
print(dataset.head(20));
#Let us describe some features of our data such as mean,min,max values etc
print(dataset.describe());
#Let us groupby using classes. Tells the number of flowers belonging to a particular category
print(dataset.groupby('class').size())
#Plotting a Box and Cluster graph using the dataset
dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
plt.show();
#creating a histogram using our four classifiers
dataset.hist();
plt.show();
#creating a scatter matrix using the dataset
scatter_matrix(dataset)
plt.show();
