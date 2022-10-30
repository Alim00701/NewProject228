import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as er:
        print(er)
    return conn


def create_products(conn, product: tuple):
    try:
        sql = '''
        INSERT INTO products (product_title, price, quantity) VALUES (?, ?, ?)'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except Error as er:
        print(er)


def select_product(conn):
    try:
        sql = '''SELECT * FROM products'''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Error as er:
        print(er)


def create_product(conn):
    create_product(conn, ('Мясо', 395.34, 6))
    create_product(conn, ('Апельсин', 123.45, 58))
    create_product(conn, ('Паста', 99.00, 65))
    create_product(conn, ('Арбуз', 10.40, 43))
    create_product(conn, ('Вафли', 101.01, 78))
    create_product(conn, ('Зубная паста', 146.54, 77))
    create_product(conn, ('Чипсы', 110.10, 10))
    create_product(conn, ('Суши', 756.44, 36))
    create_product(conn, ('Ашлянфу', 69.69, 44))
    create_product(conn, ('Сендвич', 70.00, 10))
    create_product(conn, ('Газированная вода', 56.06, 8))
    create_product(conn, ("Let's Go", 50.00, 7))
    create_product(conn, ('Мыло', 18.70, 33))
    create_product(conn, ('Краска для стен', 400.55, 9))
    create_product(conn, ('Пильмени', 99.66, 8))


def update_products_quantity(conn, product):
    try:
        sql = '''UPDATE products SET quantity = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except Error as er:
        print(er)


def update_products_price(conn, product):
    try:
        sql = '''UPDATE products SET price = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except Error as er:
        print(er)


def delete_products(conn, id):
    try:
        sql = '''DELETE FROM products WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
    except Error as er:
        print(er)


def search_by_price_and_quantity(conn):
    try:
        sql = '''SELECT * FROM products WHERE price < 100.00 AND quantity > 5'''
        cursor = conn.cursor()
        cursor.execute(sql)

        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Error as er:
        print(er)


def search_by_word(conn, word):
    try:
        sql = '''SELECT * FROM products WHERE product_title LIKE ?'''
        cursor = conn.cursor()
        cursor.execute(sql, ('%' + word + '%',))

        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Error as er:
        print(er)


def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except Error as er:
        print(er)



sql_create_products_table = '''
CREATE TABLE products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
PRODUCT_TITLE VARCHAR(200) NOT NULL,
PRICE DOUBLE(10, 2) NOT NULL DEFAULT 0.0,
QUANTITY INTEGER(5) NOT NULL DEFAULT 0,
)
'''

connection = create_connection(r"hw.db")
if connection is not None:
    create_table(connection, sql_create_products_table)
    create_product(connection)
    update_products_quantity(connection, (3, 1))
    update_products_price(connection, (33.33, 7))
    delete_products(connection, 9)
    select_product(connection)
    search_by_price_and_quantity(connection)
    search_by_word(connection, 'Арбуз')
    connection.close()
    print('Successfully connected!!!')
