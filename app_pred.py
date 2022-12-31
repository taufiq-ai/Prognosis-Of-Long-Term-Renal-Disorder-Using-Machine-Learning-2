import pandas as pd
import numpy as np
from joblib import load

ordinal_enc =   load('joblib_dump/ordinal_enc.joblib')
minmax_norm =   load('joblib_dump/minmax_norm.joblib')
knn_imp     =   load('joblib_dump/knn_imp.joblib')
model       =   load('joblib_dump/9_RandomForestClassifier_99')

def NewTest(Xtest, ordinal_enc, minmax_enc,knn_imp, model):
    # encoding
    categoricals = Xtest.select_dtypes(include=object)
    numericals = Xtest.select_dtypes(include=['int64','float64'])
    numericals.reset_index(drop=True, inplace=True)
    enc_categoricals = ordinal_enc.transform(categoricals)
    enc_categoricals_df = pd.DataFrame(enc_categoricals, columns = list(categoricals.columns))
    enc_Xtest = pd.concat([numericals, enc_categoricals_df], axis=1)
    # normalization
    test_new = minmax_enc.transform(enc_Xtest)
    # imputation
    test_new = knn_imp.transform(test_new)
    # prediction
    pred = model.predict(test_new)
    return pred[0]

def CKD_Prediction(age, specific_gravety, albumin, serum_creatinine, hemoglobine, red_blood_cells, pus_cell_clumps, hypertension, diabetes_mellitias):
    data = {
        "age": [age], 
        "specific_gravety": [specific_gravety], 
        "albumin": [albumin],  
        "serum_creatinine": [serum_creatinine], 
        "hemoglobine": [hemoglobine], 
        "red_blood_cells": [red_blood_cells], 
        "pus_cell_clumps": [pus_cell_clumps],  
        "hypertension": [hypertension], 
        "diabetes_mellitias": [diabetes_mellitias]
    }
    # print(data)
    print()
    
    cat = ['red_blood_cells', 'pus_cell_clumps', 'hypertension', 'diabetes_mellitias']
    num = ['age', 'specific_gravety', 'albumin', 'serum_creatinine', 'hemoglobine']
    
    new_data={}
    for key,val in data.items():
        l = []
        for e in val:
            if e == '' and key in num:
                e = np.nan
            elif e == '' and key in cat:
                e = 'NaN'
            elif e and key in num:
                e = float(e)
            elif e and key in cat:
                e = str(e)
            l.append(e)
        new_data[key] = l
    print(new_data)
    df = pd.DataFrame(new_data)
    result = NewTest(df, ordinal_enc, minmax_norm,knn_imp, model)
    return result


# result = CKD_Prediction('10', '', '0', '', '', '', 'present', 'yes', 'yes')
# print(result)