import pandas as pd
import pickle
df=pd.read_csv('medic_data.csv')
df["Diseases"]=df['Diseases'].replace(["Common cold","Allergies","Jaundice","Malaria","Chicken Pox","Dengue","Tuberculosis","Thyroid","Fungal"],[1,2,3,4,5,6,7,8,9])
X = df.drop(['Diseases'], axis=1)
Y=df['Diseases']
from sklearn.svm import SVC 
from sklearn.ensemble import BaggingClassifier
clf = BaggingClassifier(base_estimator=SVC(),n_estimators=10, random_state=0).fit(X,Y)

filename = 'finalized_model.sav'
pickle.dump(clf, open(filename, 'wb'))