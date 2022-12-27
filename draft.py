import numpy as np

name = "Ada"
age = 25
sex = 'male'
specific_gravety = 1
albumin = 2
blood_urea= 3
serum_creatinine = ''
hemoglobine = 5
red_blood_cells = 6
hypertension = 7
diabetes_mellitias = 8

context = {'name' : name, 'age' : age, 'sex' : sex, 'specific_gravety' : specific_gravety, 'albumin' : albumin, 'blood_urea' :blood_urea, 'serum_creatinine' : serum_creatinine,  'red_blood_cells' : red_blood_cells, 'hemoglobine' : hemoglobine, 'hypertension' : hypertension, 'diabetes_mellitias' : diabetes_mellitias}

context['serum_creatinine'] = 10

print(context['serum_creatinine'])
print(context)