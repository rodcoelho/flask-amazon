import sqlite3
import datetime

connection = sqlite3.connect('db/amazon.db')
cursor = connection.cursor()

def add_session_to_cart(username, d):
    connection = sqlite3.connect('db/amazon.db')
    cursor = connection.cursor()

    # get primary key from users first
    cursor.execute("""
            SELECT pk FROM users WHERE name = '{}'
                        ;
                            """.format(username))
    id = cursor.fetchone()
    try:
        cursor.execute("""
                INSERT INTO cart(userID, item, url, quantity, price, zero_or_one)
                VALUES ('{}','{}','{}','{}','{}', 1)
                ;
                    """.format(id[0], d[0], d[3], d[1], d[2]))
        connection.commit()
        return True
    except:
        connection.commit()
        return False

def get_all_cart_items(username):
    connection = sqlite3.connect('db/amazon.db')
    cursor = connection.cursor()

    # get primary key from users first
    cursor.execute("""
                SELECT pk FROM users WHERE name = '{}'
                            ;
                                """.format(username))
    id = cursor.fetchone()
    try:
        cursor.execute("""
        SELECT item, price, url, quantity
        FROM cart
        WHERE userID = '{}' and zero_or_one = 1
        ;
            """.format(id[0]))
        fetch = cursor.fetchall()
        connection.commit()
        return fetch
    except:
        connection.commit()
        return False


def add_cart_to_transaction(username):
    connection = sqlite3.connect('db/amazon.db')
    cursor = connection.cursor()

    # get primary key from users first
    cursor.execute("""
                    SELECT pk FROM users WHERE name = '{}'
                                ;
                                    """.format(username))
    id = cursor.fetchone()
    try:
        cursor.execute("""
        SELECT item, price, url, quantity
        FROM cart
        WHERE userID = '{}' and zero_or_one = 1
        ;
            """.format(id[0]))
        fetch = cursor.fetchall()
        for _ in fetch:
            cursor.execute("""
                    INSERT INTO transactions(userID, item, url, price, quantity)
                    VALUES ('{}','{}','{}','{}','{}');
                        """.format(id[0], _[0], _[2], _[1], _[3]))
            connection.commit()

    except:
        print("ERROR adding to Transaction table")


def set_cart_items_to_zero(username):
    connection = sqlite3.connect('db/amazon.db')
    cursor = connection.cursor()

    # get primary key from users first
    cursor.execute("""
                        SELECT pk FROM users WHERE name = '{}'
                                    ;
                                        """.format(username))
    id = cursor.fetchone()
    try:
        cursor.execute("""
                        UPDATE cart
                        SET zero_or_one = 0
                        WHERE cart.userID = '{}';
                            """.format(id[0]))
        connection.commit()

    except:
        print("ERROR setting cart to zero")
