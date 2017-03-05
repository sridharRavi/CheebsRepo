import pandas
import sklearn
from pandas.tools.plotting import scatter_matrix
import matplotlib.pyplot as plt;
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
url="https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data";
names=['sepal-length','sepal-width','petal-length','petal-width','class']
dataset=pandas.read_csv(url,names=names);
array = dataset.values
X = array[:,0:4]
Y = array[:,4]
#About 20% of iris dataset is used for validation and about 80% is used for training the KNN Algorithm
validation_size = 0.20
seed = 7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)
# Make predictions on validation dataset
knn = KNeighborsClassifier()
knn.fit(X_train, Y_train)
predictions = knn.predict(X_validation)
#accuracy of KNN algorithm ~90% efficiency
print(accuracy_score(Y_validation, predictions))
#Some error results
print(confusion_matrix(Y_validation, predictions))
#Detailed analysis of the Algorithm
print(classification_report(Y_validation, predictions))
val=raw_input();
