from flask import Flask, render_template, request
from app_pred import CKD_Prediction
from datetime import datetime

app = Flask(__name__)

@app.route("/")
@app.route("/home", methods=["GET","POST"])
def home():
	return render_template("index.html")


@app.route("/documentation")
def documentation():
	# return render_template("eda.html")
    return render_template("eda.html")


@app.route("/eda")
def eda():
	return render_template("eda.html")


@app.route("/notebook")
def notebook():
	return render_template("notebook.html")

    
@app.route("/report", methods=["GET","POST"])
def report():
    issue_date = datetime.now().strftime("%d %B %Y, %H:%M %p")
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

        pred = CKD_Prediction(age, specific_gravety, albumin, serum_creatinine, hemoglobine, red_blood_cells, pus_cell_clumps, hypertension, diabetes_mellitias)
        r = pred

        context = {'issue_date' : issue_date, 'name' : name, 'age' : age, 'sex' : sex, 'specific_gravety' : specific_gravety, 'albumin' : albumin, 'serum_creatinine' : serum_creatinine,  'red_blood_cells' : red_blood_cells, 'pus_cell_clumps': pus_cell_clumps, 'hemoglobine' : hemoglobine, 'hypertension' : hypertension, 'diabetes_mellitias' : diabetes_mellitias}

        if r == 0:
            return render_template("report.html", Result = 'positive', context = context, status = "unhealthy", risk = "yes")
    
        else:
            return render_template("report.html", Result = 'negative', context = context, status = "healthy", risk = "no")
   
    else:
        return render_template("index.html")
# name = name, age = age, sex = sex,specific_gravety = specific_gravety,albumin =albumin,blood_urea = blood_urea, serum_creatinine = serum_creatinine,  red_blood_cells = red_blood_cells, hemoglobine = hemoglobine, hypertension = hypertension, diabetes_mellitias=diabetes_mellitias,

if __name__ == '__main__':
    app.run(debug=True)