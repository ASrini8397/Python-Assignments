
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'Open_Sesame'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/results', methods=['POST'])
def survey():
    session['fullname']= request.form['fullname']
    session['location']= request.form['location']
    session['language']= request.form['language']
    session['comments']=request.form['comments']
    return render_template("results.html",fullname=session['fullname'], location=session['location'], language=session['language'], comments=session['comments'])

@app.route('/goback', methods=['POST'])
def reload():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)