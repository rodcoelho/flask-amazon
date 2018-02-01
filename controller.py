#!/usr/bin/env python3

import requests

from flask import Flask, render_template, request
app = Flask(__name__)

import sqlite3

import orm, wrapper

connection = sqlite3.connect('db/amazon.db')
cursor = connection.cursor()

@app.route('/')
def index():
    h1 = 'Home'
    title = 'Flask-Amazon'
    username = 'rodrigo'
    return render_template('index.html',h1=h1,title=title)

@app.route('/cart',methods = ["GET","POST"])
def cart():
    h1 = 'Cart'
    title = 'Flask-Amazon'
    username = 'rodrigo'
    return render_template('cart.html',h1=h1,title=title)


@app.route('/lookup',methods = ["GET","POST"])
def lookup():
    h1 = 'Look Up'
    title = 'Flask-Amazon'
    username = 'rodrigo'
    query = request.form['item']
    r = requests.get('http://newyork.craigslist.org/search/sss?format=rss&query={}'.format(query))


    return render_template('lookup.html',h1=h1,title=title)





if __name__ == '__main__':
    app.run(debug=True)
