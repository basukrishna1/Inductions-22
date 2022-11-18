from flask import Flask,render_template,request,flash
from flask_sqlalchemy import SQLAlchemy
import pickle
import numpy as np
import sqlite3
import pandas    
dat = sqlite3.connect('./instance/project.db')
model= pickle.load(open('iris.pkl','rb'))

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db = SQLAlchemy(app)
app.secret_key="Hello"
class todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Slen = db.Column(db.Float, nullable=False)
    Swid = db.Column(db.Float, nullable=False)
    Plen = db.Column(db.Float, nullable=False)
    Pwid = db.Column(db.Float, nullable=False)
    typ = db.Column(db.String, nullable=False)
    
    

with app.app_context():
    db.create_all()

@app.route('/')
def pro2():
    return render_template("welcome.html") 


@app.route('/addData',methods=['GET','POST'])
def hello_world():
    if request.method=='POST':
        sl=request.form["Slength"]
        sw=request.form["Swidth"]
        pl=request.form["Plength"]
        pw=request.form["Swidth"]
        tp=request.form["Species"]
        seek=todo(Slen=sl,Swid=sw,Plen=pl,Pwid=pw,typ=tp)
        db.session.add(seek)
        db.session.commit()
    alli=todo.query.all()
    return render_template("addData.html",alli=alli)

 

@app.route('/predict',methods=['GET','POST'])
def pro():
    pred=[9]  
    if request.method=='POST':
    
        sl2=request.form["Slength2"]
        sw2=request.form["Swidth2"]
        pl2=request.form["Plength2"]
        pw2=request.form["Swidth2"]
        arr=np.array([[sl2,sw2,pl2,pw2]])
        pred=model.predict(arr)
     
    return render_template("predict.html",pred=pred[0])   



if __name__=="__main__":
    app.run(debug=True)