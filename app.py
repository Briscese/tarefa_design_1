from flask import Flask
from flask import render_template, redirect



app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

DEBUG = True
PORT = 5000
HOST = 'localhost'

if __name__ == '__main__':
   app.run( HOST , PORT , DEBUG)