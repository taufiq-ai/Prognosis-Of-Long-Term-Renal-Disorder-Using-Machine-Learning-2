from flask import Flask, render_template, request
# from test import CKD_Prediction
from app_pred import CKD_Prediction
import time
import datetime


app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def main():
	return render_template("index.html")

@app.route("/eda")
def eda():
	return render_template("eda.html")
    
@app.route("/report", methods=["GET","POST"])
def report():
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        sex = request.form["sex"]
        specific_gravety = request.form["specific_gravety"]
        albumin = request.form["albumin"]
        # blood_urea= request.form["blood_urea"]
        serum_creatinine = request.form["serum_creatinine"]
        hemoglobine = request.form["hemoglobine"]
        pus_cell_clumps = request.form["pus_cell_clumps"]
        red_blood_cells = request.form["red_blood_cells"]
        hypertension = request.form["hypertension"]
        diabetes_mellitias = request.form["diabetes_mellitias"]

 
        # print(f"specific_gravety: {specific_gravety}, albumin: {albumin}, blood_urea: {blood_urea}, serum_creatinine: {serum_creatinine}, hemoglobine: {hemoglobine}, red_blood_cells: {red_blood_cells}, hypertension: {hypertension}, diabetes_mellitias: {diabetes_mellitias}")

        pred = CKD_Prediction(age, specific_gravety, albumin, serum_creatinine, hemoglobine, red_blood_cells, pus_cell_clumps, hypertension, diabetes_mellitias)
        r = pred

        context = {'name' : name, 'age' : age, 'sex' : sex, 'specific_gravety' : specific_gravety, 'albumin' : albumin, 'blood_urea' :'blood_urea', 'serum_creatinine' : serum_creatinine,  'red_blood_cells' : red_blood_cells, 'hemoglobine' : hemoglobine, 'hypertension' : hypertension, 'diabetes_mellitias' : diabetes_mellitias}

        # if hypertension == "1":
        #     context['hypertension'] = "positive"
        # elif hypertension == "0": 
        #     context['hypertension'] = "positive"
        # else: 
        #     context['hypertension'] = "null"

        # if diabetes_mellitias == "1":
        #     context['diabetes_mellitias'] = "positive"
        # elif diabetes_mellitias == "0": 
        #     context['diabetes_mellitias'] = "positive"
        # else: 
        #     context['diabetes_mellitias'] = "null"


        if r == 0:
            return render_template("report.html", Result = "{}".format(r), context = context, status = "unhealthy", risk = "yes")
            # return render_template("report.html", Result = "{}".format(r), name = name, age = age, sex = sex,specific_gravety = specific_gravety,albumin =albumin,blood_urea = blood_urea, serum_creatinine = serum_creatinine,  red_blood_cells = red_blood_cells, hemoglobine = hemoglobine, hypertension = hypertension, diabetes_mellitias=diabetes_mellitias, status = "unhealthy", risk = "yes")
            # return render_template("index.html", Result = "High Risk Of CKD. Take appointment of a Nephronogist. Report: {}".format(r))
            # print()
        else:
            return render_template("report.html", Result = "{}".format(r), context = context, status = "healthy", risk = "no")
            # return render_template("report.html", Result = "{}".format(r), name = name, age = age, sex = sex,specific_gravety = specific_gravety,albumin =albumin,blood_urea = blood_urea, serum_creatinine = serum_creatinine,  red_blood_cells = red_blood_cells, hemoglobine = hemoglobine, hypertension = hypertension, diabetes_mellitias=diabetes_mellitias, status = "healthy", risk = "no")
            # return render_template("index.html", Result = "Kidney Status: Healthy. Follow healthy daily routine. Report: {}".format(r))
    else:
        return render_template("index.html")
# name = name, age = age, sex = sex,specific_gravety = specific_gravety,albumin =albumin,blood_urea = blood_urea, serum_creatinine = serum_creatinine,  red_blood_cells = red_blood_cells, hemoglobine = hemoglobine, hypertension = hypertension, diabetes_mellitias=diabetes_mellitias,

if __name__ == '__main__':
    app.run(debug=True)
