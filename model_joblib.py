                     # Dependencies list to execute programs

#Data manipulation
import numpy as np
from numpy.core.numeric import NaN
from trainingRFmodel import *
import joblib
RF8 = joblib.load("RF8")

def CKD_Prediction(specific_gravety, albumin, blood_urea, serum_creatinine, hemoglobine, red_blood_cells, hypertension, diabetes_mellitias):
   
    """PREDICTION"""
    
    #Using Numpy Array
    Xtest = np.array([[specific_gravety, albumin, blood_urea, serum_creatinine, hemoglobine, red_blood_cells, hypertension, diabetes_mellitias]])
    print(f"Xtest: {Xtest}")
    # # Using List
    # Xtest = [[specific_gravety, albumin, blood_urea, serum_creatinine, hemoglobine, red_blood_cells, hypertension, diabetes_mellitias]]

    Xtest = normalizer.transform(Xtest)
    print(f"Scalled result: {Xtest}")
    Xtest = imputer.transform(Xtest) #Appling Imputation
    print(f"Impute result: {Xtest}")
    Xtest = standardization.transform(Xtest)
    result = RF8.predict(Xtest)
    for i in result:  
        r = (i)
    return r
