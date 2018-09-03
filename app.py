from flask import Flask, request, render_template,flash,redirect,url_for
from flask_restful import Resource, Api , reqparse
from flask_mysqldb import MySQL
from passlib.hash import pbkdf2_sha256 as sha256
import os
import datetime


app = Flask(__name__)
api = Api(app)


@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')



if __name__=='__main__':
    app.run(debug=True)
    app.run(port=5000)
