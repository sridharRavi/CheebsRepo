import pandas as pd;
import matplotlib.pyplot as plt;
import seaborn as sns
from sklearn.linear_model import LogisticRegression;
import numpy as np;
titantrain=pd.read_csv('C:\Kaggle\\train.csv');
titantest=pd.read_csv('C:\Kaggle\\test.csv');
finRes=pd.read_csv('C:\Kaggle\\gender_submission.csv')
newdf=pd.DataFrame();
Classdf=pd.DataFrame();
Agedf=pd.DataFrame();
Famdf=pd.DataFrame();
finTrain=pd.DataFrame();
finTest=pd.DataFrame();
newdf['sex']=titantrain['Sex'];
finTrain['survived']=titantrain['Survived'];
finTest['sex']=titantest['Sex'];
finTest['age']=titantest['Age'];
finTest['pclass']=titantest['Pclass'];
finTest['sibsp']=titantest['SibSp'];
finTest['parch']=titantest['Parch'];
newdf['sibsp']=titantest['SibSp'];
newdf['sex'].replace('female',0,inplace=True);
newdf['sex'].replace('male',1,inplace=True);
finTest['sex'].replace('female',0,inplace=True);
finTest['sex'].replace('male',1,inplace=True);
newdf['pclass']=titantrain['Pclass'];
newdf['sibsp']=titantrain['SibSp'];
newdf['age']=titantrain['Age'];
newdf['parch']=titantrain['Parch'];
finTest['age']=finTest['age'].fillna(finTest['age'].mean());
newdf['age']=newdf['age'].fillna(newdf['age'].mean());
X_train=newdf[['age','sex','pclass','sibsp','parch']].values;
Y_train=finTrain.survived.values;
X_test=finTest[['age','sex','pclass','sibsp','parch']].values;
lg=LogisticRegression();
lg.fit(X_train, Y_train);
finVal=lg.predict(X_test);
#print finVal;
mySol=pd.DataFrame({'Survived':np.array(finVal)}, index=titantest.PassengerId);
mySol.to_csv('finalSol.csv');

'''

Classdf['pclass']=titantrain['Pclass'];
Classdf['survived']=titantrain['Survived'];
Agedf['survived']=titantrain['Survived'];
Agedf['age']=titantrain['Age'];
Famdf['survived']=titantrain['Survived'];
Famdf['sibsp']=titantrain['SibSp'];
Agedf['age']=Agedf['age'].fillna(Agedf['age'].mean());
print Agedf.describe();
print Famdf.describe();
print Classdf.describe();
Agedf.plot(kind='scatter', x='age', y='survived', figsize=(12,8));
sns.lmplot(x='age', y='survived', data=Agedf,title="age-survival");
sns.lmplot(x='pclass', y='survived', data=Classdf,title="Class-survival");
sns.lmplot(x='sex',y='survived',data=newdf,title="gender-survival");
sns.lmplot(x='sibsp',y='survived',data=Famdf,"relations-survival");
plt.show();
'''