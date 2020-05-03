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

@app.route('/courses')
def courses():
    return render_template('courses.html')

@app.route('/ramen')
def ramen():
    return render_template('ramen.html')

#start the server
if __name__ == "__main__":
    app.run()
