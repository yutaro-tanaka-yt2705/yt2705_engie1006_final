# -*- coding: utf-8 -*-
"""
@author: Yutaro Tanaka
"""

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def hello():
    return render_template('index.html')

@app.route('/1006')
def init():
    return render_template('courses.html')

#start the server
if __name__ == "__main__":
    app.run()
