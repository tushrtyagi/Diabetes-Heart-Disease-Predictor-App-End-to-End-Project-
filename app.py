from flask import Flask,render_template,redirect,url_for,request
import pickle
import numpy as np

from flask_mysqldb import MySQL
import MySQLdb.cursors
import re


app = Flask(__name__)

#mysql connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'py_accounts'

# Intialize MySQL
mysql = MySQL(app)

#diabetes model read
filename = open('Diabetes/diabetespredictmodel.pkl', 'rb')
model = pickle.load(filename)
filename.close()

#heartdiseases model read
filename = open('HeartDiseases/heartdiseasespredictmodel.pkl', 'rb')
clf = pickle.load(filename)
filename.close()


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/admin', methods=['GET','POST'])
def admin():
    if request.method == 'POST':
        aname = request.form['aname']
        pssw = request.form['pssw']

        if(aname == 'admin' and pssw == 'surat'):
            return render_template('index1.html')
    return render_template('admin.html')
    
@app.route("/registration", methods=["GET", "POST"])
def registration():
    if request.method == 'POST':
        username = request.form['uname']
        age = int(request.form['age'])
        email = request.form['email']
        password = request.form['password']
        
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('INSERT INTO accounts VALUES (NULL, %s, %s, %s,%s)', (username,age,email,password))
        mysql.connection.commit()
        print('You have successfully registered!')
        return render_template("login.html")

    return render_template("registration.html")
    

@app.route("/login",methods=["GET", "POST"])
def login():
    if request.method == "POST" :
        email = request.form["email"]
        password = request.form["password"]

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE email = %s AND password = %s', (email, password))
        account = cursor.fetchone()
        if account:
            print('Logged in successfully!')
            return render_template("home.html")
        else:
            print('Incorrect username/password!')
            return render_template("login.html")

    return render_template("login.html")


@app.route('/home')
def home():
	return render_template('home.html')
    

@app.route('/diapredict', methods=['GET','POST'])
def diapredict():
    if request.method == 'POST':
        na = request.form['na']
        pr = int(request.form['pr'])
        gl = int(request.form['gl'])
        bp = int(request.form['bp'])
        st = int(request.form['st'])
        ins = int(request.form['in'])
        bm = float(request.form['bm'])
        dp = float(request.form['dp'])
        ag = int(request.form['ag'])
        
        data = np.array([[pr,gl,bp,st,ins,bm,dp,ag]])
        my_prediction = model.predict(data)
        proba = model.predict_proba(data)[0][1]

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('INSERT INTO diabetes VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (na,pr,gl,bp,st,ins,bm,dp,ag,proba))
        mysql.connection.commit()
        
        return render_template('diashow.html',name=na,prediction=my_prediction,proba=proba)
    return render_template('dia.html')


@app.route('/hdpredict', methods=['GET','POST'])
def hdpredict():
    if request.method == 'POST':
        na = request.form['na']
        ag = int(request.form['ag'])
        cp = int(request.form['cp'])
        chol = int(request.form['chol'])
        fbp = int(request.form['fbp'])
        restecg = int(request.form['restecg'])
        thalach = int(request.form['thalach'])
        exang = float(request.form['exang'])
        sl = float(request.form['sl'])
        
        data = np.array([[ag,cp,chol,fbp,restecg,thalach,exang,sl]])
        my_prediction = clf.predict(data)
        my_prediction_proba = clf.predict_proba(data)[0][1]
        proba = round((my_prediction_proba),2)

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('INSERT INTO hdp VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (na,ag,cp,chol,fbp,restecg,thalach,exang,sl,proba))
        mysql.connection.commit()
        
        return render_template('hdpshow.html',name=na,prediction=my_prediction,proba=proba)
    return render_template('hdp.html')


#ADMIN PART
@app.route('/index1')
def index1():
	return render_template('index1.html')

@app.route('/disallud', methods=['GET','POST'])
def disallud():
    if request.method == 'POST':
        li=[]
    
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts')
        user = cursor.fetchall()
        #print(user)
        #print(len(user))
        for i in range(len(user)):
            li.append(user[i])
        #print(li)
        lt = len(li)

        return render_template('manage1.html',list=li,len=lt)
    return render_template('index1.html')

@app.route('/disalldd', methods=['GET','POST'])
def disalldd():
    if request.method == 'POST':
        li=[]
    
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM diabetes')
        db = cursor.fetchall()
        for i in range(len(db)):
            li.append(db[i])
        lt = len(li)
        #print(li)

        return render_template('manage2.html',list=li,len=lt)
    return render_template('index1.html')


@app.route('/disallhd', methods=['GET','POST'])
def disallhd():
    if request.method == 'POST':
        li=[]
    
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM hdp')
        hd = cursor.fetchall()
        for i in range(len(hd)):
            li.append(hd[i])
        lt = len(li)
        #print(li)

        return render_template('manage3.html',list=li,len=lt)
    return render_template('index1.html')


        
if __name__ == '__main__':
	app.run(debug=True)
