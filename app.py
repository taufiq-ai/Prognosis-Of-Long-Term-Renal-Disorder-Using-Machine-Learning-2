from flask import Flask, render_template, request
import model_joblib as m


app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        specific_gravety = request.form["specific_gravety"]
        albumin = request.form["albumin"]
        blood_urea= request.form["blood_urea"]
        serum_creatinine = request.form["serum_creatinine"]
        hemoglobine = request.form["hemoglobine"]
        red_blood_cells = request.form["red_blood_cells"]
        hypertension = request.form["hypertension"]
        diabetes_mellitias = request.form["diabetes_mellitias"]
        pred = m.CKD_Prediction(specific_gravety, albumin, blood_urea, serum_creatinine, hemoglobine, red_blood_cells, hypertension, diabetes_mellitias)
        r = pred
        if r == 1:
            return render_template("index.html", Result = "High Risk Of CKD. Take appointment of a Nephronogist. Report: {}".format(r))
            # print()
        else:
            return render_template("index.html", Result = "Kidney Status: Healthy. Follow healthy daily routine. Report: {}".format(r))
    else:
        return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
