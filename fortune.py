from random import randint
from flask import Flask, redirect, render_template,request, url_for
app = Flask(__name__, template_folder='template')

@app.route("/", methods = ['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('home.html')
    if request.method == 'POST':
        print(request.form['name_field'])
        nam = request.form['name_field']
        if (nam == '') :
            return render_template('home.html')
        return redirect(url_for('fortune', name = nam))
    return render_template('home.html')

@app.route("/fortune/<string:name>/")
def fortune(name):
    fortunes = ["You are very lucky today. Good fortune will rain upon you.",
    "Today is your lucky day. Any efforts you make will be rewarded generously.",
    "You neither lucky nor unlucky today. You will be rewarded with fortune equivalent to the effort you put in.",
    "Today is an unlucky day. Err on the side of caution in any activities you participate in."]
    randomNumber = randint(0,(len(fortunes)-1))
    fortune = fortunes[randomNumber]
    return render_template('fortune.html',**locals())

@app.route("/members/<string:name>/")
def getMember(name):
    return render_template('test2.html',name = name)

if __name__ == "__main__":
    app.run(debug = True, host='0.0.0.0', port = 80)
