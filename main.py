from flask import Flask,render_template,request,flash, redirect,url_for
from database import Patient, engine
from sqlalchemy.orm import session

app = Flask(__name__)
app.secret_key = "hello"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login" , methods =["POST", "GET"])
def login():
    return render_template("login_page.html")

@app.route('/fill_details', methods = ["POST"])
def fill_details():
    username = request.form.get('username').strip()
    password = request.form.get('password').strip()
    if username == 'ashish' and password == '7201099243':
        return render_template('pateint_detail_form.html', username = username , password = password)
    else: 
        # message = "invalid login credentials"
        # flash(message)
        # return redirect(url_for('login'))
        return "invalid credentials."

@app.route('/family_login', methods = ["POST","GET"])
def family_login():
    return render_template('family_member_login.html')

@app.route('/show_details', methods = ["POST"])
def show_details():
    phone_number = request.form.get('phone_number').strip()
    if phone_number == "7201099243":
        return render_template('Familly_page.html')
    else: 
        return "Invalid Number Plz Check" 

@app.route('/submit_patient', methods= ["POST", "GET"])
def submit_patient():
    patient_data  = {
            "firstname" : request.form.get('firstname'),
            "lastname" : request.form.get('lastname'),
            "age" : request.form.get('age'),
            "gender" : request.form.get('gender'),
            "patientId" : request.form.get('patientId'),
            "emergency_number" : request.form.get('emergency_number'),
            "date_n_time" : request.form.get('date_n_time'),
            "hospital_name" : request.form.get('hospital_name'),
            "ward_name" : request.form.get('ward_name'),
            "bed_number" : request.form.get('bed_number'),
            "condition" : request.form.get('condition'),
            "funds" : request.form.get('funds'),
            "Urgency" : request.form.get('Urgency'),
            "Initial_info" : request.form.get('Initial_info')
        }
    submit_patient = Patient(patient_data)

if __name__ == '__main__':
    app.run(debug=True)