from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/passwordcheck', methods=['GET', 'POST'])
def index2():
    if request.method == 'POST':
        firstname = request.form["firstname"]
        lastname = request.form["lastname"]
        createpassword = request.form["createpassword"]
        retypepassword = request.form["retypepassword"]
        if createpassword != retypepassword:
            return render_template("index.html")
        elif len(createpassword) < 8 or model.countUpper(createpassword) == 0 or model.countLower(createpassword) == 0 or firstname.lower() in createpassword or lastname.lower() in createpassword or model.countSymbols(createpassword) == 0 or model.countNumbers(createpassword) == 0:
            return render_template("weak.html")
        elif len(createpassword) in range(8,12) or model.countUpper(createpassword) == 1 or model.countLower(createpassword) == 1 or model.countSymbols(createpassword) == 1 or model.countNumbers(createpassword) in range(2,4):
            return render_template("ok.html") 
        else:
            return render_template("strong.html")
    else: 
        return render_template("index.html")
