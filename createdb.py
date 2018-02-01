import sqlite3

connection = sqlite3.connect('db/amazon.db')
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE users(
pk INTEGER,
name VARCHAR(32),
password VARCHART(64),
PRIMARY KEY(pk))
;""")

cursor.execute("""
CREATE TABLE cart(
pk INTEGER,
userID INTEGER,
item VARCHAR(32),
url VARCHAR,
quantity INTEGER,
FOREIGN KEY(userID) REFERENCES users(pk),
PRIMARY KEY(pk))
;""")

cursor.execute("""
CREATE TABLE transactions(
pk INTEGER,
userID INTEGER,
item VARCHAR(32),
url VARCHAR,
price INTEGER,
quantity INTEGER,
FOREIGN KEY(userID) REFERENCES users(pk),
PRIMARY KEY(pk))
;""")

cursor.execute("""
INSERT INTO users(name, password)
VALUES ('{}','{}');
    """.format('rodrigo', 'swordfish'))

connection.commit()
cursor.close()
