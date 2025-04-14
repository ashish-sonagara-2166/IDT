from flask import Flask,render_template,request,flash, redirect,url_for
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

@app.route('/show_details')
def show_details():
    return render_template('Familly_page.html')

if __name__ == '__main__':
    app.run(debug=True)