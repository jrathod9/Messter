from flask import Flask, flash, redirect, url_for, render_template, request, session, abort
import datetime
import os
import sys
import json
import sqlite3
import hashlib

db = './data/messter'

conn = sqlite3.connect(db)
app = Flask(__name__)

app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'



@app.route("/")
def index():	
	return render_template("index.html", correct = True)


@app.route("/user_home", methods = ['POST'])
def verifylogin():
	rollno = request.form["rollno"]
	password = request.form["pass"]
	with sqlite3.connect(db) as connection:
		cur = connection.cursor()
		details = cur.execute("SELECT * FROM user WHERE roll_no=? AND password=?",[rollno,password]).fetchall()
		print(details, file = sys.stderr)
		if len(details) != 0:
			return render_template("userprofile.html" , rollno = rollno)
		else:
			return render_template("index.html", correct = False)


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=4000)