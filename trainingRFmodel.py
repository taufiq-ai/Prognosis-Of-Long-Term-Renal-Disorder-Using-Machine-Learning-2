                     # Dependencies list to execute programs

#Data manipulation
import numpy as np
# from numpy.core.numeric import NaN
import pandas as pd

#Extra
# import math
# import warnings
# warnings.filterwarnings(action='ignore')

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import MinMaxScaler
normalizer = MinMaxScaler()

from sklearn.impute import KNNImputer #import Knn Imputer
imputer = KNNImputer(n_neighbors = 5) #Declaring that 5 nearest neighbour should be decided

from sklearn.neighbors import LocalOutlierFactor
lof = LocalOutlierFactor(n_neighbors=15,novelty=False) # identify outliers in the training dataset

from imblearn.over_sampling import SMOTE
oversample = SMOTE()

from sklearn.preprocessing import StandardScaler
standardization  = StandardScaler()

from sklearn.ensemble import RandomForestClassifier


# from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_auc_score
import joblib


#Fetch Data from my GitHub Repo
url= "https://raw.githubusercontent.com/Muhammad-Taufiq-Khan/Prognosis-Of-Long-Term-Renal-Disorder-Using-Machine-Learning/main/FlaskCKD_CleanData.csv"
dataframe = pd.read_csv(url)

""" # Spliting Data Set"""    
Xtrain, X_test, ytrain, y_test = train_test_split(dataframe.drop('ckd',axis=1), dataframe["ckd"], test_size = 0.25, random_state=40)



"""DATA ENGINEERING & MACHINE LEARNING TASKS START HERE"""
#08 Important Feature
Xtrain = Xtrain[['specific_gravety', 'albumin','blood _urea', 'serum_creatinine', 'hemoglobine', 'red_blood_cells', 'hypertension', 'diabetes_mellitias']]



"""NORMALIZATION MIN-MAX NORMALIZER"""
#Normalizing Training Data
Xtrain = normalizer.fit_transform(Xtrain)



"""K-NN Imputation on Training Dataset"""
imputer.fit(Xtrain) #fitting imputer according to Training Features (X_train)
Xtrain = imputer.transform(Xtrain) #Appling Imputation



"""OUTLIER DETECTION & REMOVAL: LOCAL OUTLIER FACTOR (LOF)"""
# lof.fit(Xtrain)
yhat = lof.fit_predict(Xtrain)
# select all rows that are not outliers
mask = yhat != -1
Xtrain, ytrain = Xtrain[mask, :], ytrain[mask]



"""OVERSAMPLING: SYNTHETIC MINORITY OVERSAMPLING TECHNIQUE"""
Xtrain, ytrain = oversample.fit_resample(Xtrain, ytrain)



"""Standard Scalling OR Z-SCORE NORMALIZATION"""
Xtrain = standardization.fit_transform(Xtrain)


"""MODEL TRAINING: RANDOM FOREST"""
RFmodel = RandomForestClassifier(n_estimators=1000).fit(Xtrain, ytrain)

# joblib.dump(RFmodel, 'RF8')
