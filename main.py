#!/usr/bin/python3
"""
    Flask framework
"""
from flask import Flask, render_template, request, redirect



app = Flask(__name__)

@app.route("/")
def hello():
    	return render_template('index1.html')

@app.route('/forward', methods = ['POST'])
def forward():
	
	return redirect('/')

if __name__ == "__main__":
    app.run('0.0.0.0')

