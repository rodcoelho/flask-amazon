#!/usr/bin/env python3

from random import randint

from flask import Flask, render_template, request, make_response, session
app = Flask(__name__)

import sqlite3

import orm, wrapper

connection = sqlite3.connect('db/amazon.db')
cursor = connection.cursor()

@app.route('/',methods=["GET","POST"])
def index():
    h1 = 'Home'
    title = 'Flask-Amazon'
    return render_template('index.html',h1=h1,title=title)


@app.route('/lookup', methods=["GET", "POST"])
def lookup():
    h1 = 'Results'
    title = 'Flask-Amazon'
    item = request.form['item']
    # session[item] = [quantity, price]
    session[item] = [request.form['quantity'],randint(1, 100)]
    cost = int(session[item][0]) * int(session[item][1])
    return render_template('lookup.html', h1=h1, title=title, item=item,
                           quantity=session[item][0], price=session[item][1], cost=cost)


@app.route('/addtocart', methods=["GET", "POST"])
def addtocart():
    h1 = 'Added to Cart'
    title = 'Flask-Amazon'
    username = 'rodrigo'
    return render_template('index.html',h1=h1,title=title)


@app.route('/cart', methods=["GET", "POST"])
def cart():
    h1 = 'Cart'
    title = 'Flask-Amazon'
    username = 'rodrigo'
    return render_template('cart.html',h1=h1,title=title)


app.secret_key = 'poop'

if __name__ == '__main__':
    app.run(debug=True)
    session['SECRET_KEY'] = 'poop'

