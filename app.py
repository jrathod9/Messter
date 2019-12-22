from flask import Flask, flash, redirect, url_for, render_template, request, session, abort
import datetime
import os
import sys
import json
import sqlite3
import hashlib


db = './data/messter'

app = Flask(__name__)

app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'



@app.route("/")
def index():	
	return render_template("index.html", correct = True, registered = False)


@app.route("/user_home", methods = ['POST'])
def verifylogin():
	if request.form["formname"] == "login_form":
		conn = sqlite3.connect(db)
		cur = conn.cursor()
		rollno = request.form["rollno"]
		print(rollno)
		password = request.form["pass"]
		
		details = cur.execute("SELECT * FROM user WHERE roll_no = ? AND password = ?",[rollno,password]).fetchall()
		print(details, file = sys.stderr)
		breakfast = cur.execute("SELECT breakfast from menu")
		lunch = cur.execute("SELECT lunch from menu")
		dinner = cur.execute("SELECT dinner from menu")
		if len(details) != 0:
			return render_template("userprofile.html" , rollno = rollno, breakfast = breakfast , lunch = lunch , dinner = dinner)
		else:
			return render_template("index.html", correct = False, registered = False)
		conn.commit()
		cur.close()
		conn.close()
	else:
		rollno = request.form["rollno"]
		password = request.form["pass"]
		wt = request.form['weight']
		ht = request.form['height']
		conn = sqlite3.connect(db)
		cur = conn.cursor()
		cur.execute("INSERT INTO user(roll_no, height, weight, password) VALUES (?, ?, ?, ?);", [rollno, ht, wt, password])
		conn.commit()
		cur.close()
		conn.close()
		return render_template("index.html", correct = True, registered = True)

@app.route("/admin")
def admin():
	return render_template("admin.html")


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=4000)