import pandas as pd;
import numpy as np;
from sklearn.ensemble import RandomForestClassifier
digitDf=pd.read_csv('C:\Kaggle\\DigitRecog\\train.csv');
subDf=pd.read_csv('C:\Kaggle\\DigitRecog\\sample_submission.csv')
#print digitDf.head();
X_test=digitDf[[0]].values.ravel();
X_train=digitDf.iloc[:,1:].values;
testDf=pd.read_csv('C:\Kaggle\\DigitRecog\\test.csv');
rf = RandomForestClassifier(n_estimators=100)
rf.fit(X_train, X_test)
pred = rf.predict(testDf);
#print pred;
mySol=pd.DataFrame({'Label':np.array(pred)}, index=subDf.ImageId);
mySol.to_csv('digitSol.csv');
