
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'Open_Sesame'

@app.route('/')
def index():
    count=0
    if 'count' not in session:
        session['count']=0
    else:
        session['count']+=1
    return render_template("index.html", count= session['count'])

@app.route('/increment', methods=['post'])
def increment():
    session['count']+=1
    return redirect('/')


@app.route('/special_increment', methods=['get','post'])
def special_increment():
    increment=request.form.get("number1")
    session['count']+=increment
    return redirect('/', count=session['count'])

@app.route('/clear',methods=['post'])
def clear():
    session['count']=0
    return redirect('/')



@app.route('/destroy_session')
def destroy():
    session['count']=0
    return redirect('/')


app.run(debug=True)