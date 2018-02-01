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

