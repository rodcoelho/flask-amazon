#!/usr/bin/env python3

from random import randint

from flask import Flask, render_template, request, session
app = Flask(__name__)

import sqlite3

import orm, wrapper

connection = sqlite3.connect('db/amazon.db')
cursor = connection.cursor()

@app.route('/',methods=["GET","POST"])
def index():
    h1 = 'Home'
    title = 'Flask-Amazon'
    # if bool(session['cart']):
    #     cost = 0
    #     temp = session['cart']
    #     for _ in temp:
    #         p_q = int(_[1])*int(_[2])
    #         cost += p_q
    #     return render_template('index.html', h1=h1, title=title,
    #                            cost=cost, items=session['cart'])
    return render_template('index.html', h1=h1, title=title)


@app.route('/lookup', methods=["GET", "POST"])
def lookup():
    h1 = 'Results'
    title = 'Flask-Amazon'
    item = request.form['item']
    # session[temp_cart] = [item, quantity, price, url]
    price = randint(1, 100)
    session['temp_cart'] = [item, 0, price, '']
    return render_template('lookup.html', h1=h1, title=title, item=item, price=price)


@app.route('/addtocart', methods=["GET", "POST"])
def addtocart():
    h1 = 'Item Info'
    title = 'Flask-Amazon'
    username = 'rodrigo'
    quantity = request.form['quantity']
    temp = session['temp_cart']
    temp[1] = quantity
    session['temp_cart'] = temp
    # session[temp_cart] = [item, quantity, price, url]
    orm.add_session_to_cart(username, session['temp_cart'])
    return render_template('addtocart.html', h1=h1, title=title, quantity=quantity,
                           item=session['temp_cart'][0])


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

