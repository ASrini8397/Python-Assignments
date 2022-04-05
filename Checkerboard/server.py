
from flask import Flask, render_template  
app = Flask(__name__)    

@app.route('/')          
def basic():
    return render_template('index.html')  

@app.route('/<int:num>')          
def play(num):
    return render_template('index2.html', num=num) 

@app.route('/<int:num>/<int:numa>')          
def play2(num,numa):
    return render_template('index3.html', num=num, numa=numa) 

@app.route('/<int:num>/<int:numa>/<string:clr>')          
def play3(num,numa,clr):
    return render_template('index4.html', num=num, numa=numa,clr=clr) 



if __name__=="__main__":     
    app.run(debug=True)    
