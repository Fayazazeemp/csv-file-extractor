from logging import debug
from flask import Flask,render_template,request

import csv

filename = ['design.csv','frontend.csv','backend.csv']



app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html',filenames=filename)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/index',methods=['POST','GET'])
def select():
    if request.method == 'POST':
        result = request.form.getlist('selection')
        with open(result[0], newline='') as csvfile:
            data = list(csv.reader(csvfile))
        return render_template('index.html',name=data,length=len(data))


if __name__ == "__main__":
    app.run(debug=True)