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

'''
#spamham model read
filename = open('Spam_Ham/spam-sms-mnb-model.pkl', 'rb')
classifier = pickle.load(filename)
files = open('Spam_Ham/cv-transform.pkl','rb')
cv = pickle.load(files)
filename.close()
files.close()
'''

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/admin', methods=['GET','POST'])
def admin():
    if request.method == 'POST':
        aname = request.form['aname']
        pssw = request.form['pssw']

        if(aname == 'admin' and pssw == 'surat'):
            return render_template('home.html')
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
        
        data = np.array([[ag,cp,chol,fbs,restecg,thalach,exang,sl]])
        my_prediction = clf.predict(data)
        my_prediction_proba = clf.predict_proba(data)[0][1]
        proba = round((my_prediction_proba),2)

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('INSERT INTO hdp VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (na,ag,cp,chol,fbp,restecg,thalach,exang,sl,proba))
        mysql.connection.commit()
        
        return render_template('hdpshow.html',name=na,prediction=my_prediction,proba=proba)
    return render_template('hdp.html')
'''
@app.route('/sphampredict',methods=['GET','POST'])
def sphampredict():
    if request.method == 'POST':
        na = request.form['na']
        message = request.form['message']
        data = [message]
        vect = cv.transform(data).toarray()
        predict = classifier.predict(vect)

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('INSERT INTO spham VALUES (NULL, %s, %s, %s)', (na,message,predict))
        mysql.connection.commit()

        return render_template('sphamshow.html', prediction=predict)
    return render_template('spham.html')
'''
        
if __name__ == '__main__':
	app.run(debug=True)
