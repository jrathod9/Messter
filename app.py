from flask import Flask, flash, redirect, url_for, render_template, request, session, abort
import datetime
import os
import json
import sqlite3
import hashlib

db = 'Database/db.sqlite3'

conn = sqlite3.connect(db)
app = Flask(__name__)

app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'



@app.route("/",methods = ['POST'])
def index():
	if(request.method == 'GET'):
		rollno = request.form["rollno"]
		passwrd = request.form["pass"]

		hashedpass = hashlib.sha256(str.encode())
		hashedpass = hashedpass.hexdigest()


		with sqlite3.connect(db) as conn:
			cur = con.cursor()
			cur.execute("SELECT * FROM user WHERE rollno=? AND passwrd=?",[rollno,hashedpass])
			details = cur.fetchall()
			if details is not None:
				return render_template("userprofile.html" , rollno = rollno)
			else:
				return render_template("index.html",)	
	return render_template("index.html")


def verifylogin():


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=4000)