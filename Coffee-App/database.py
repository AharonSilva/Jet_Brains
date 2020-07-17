import sqlite3


CREATE_BEANS_TABLE = '''CREATE TABLE IF NOT EXISTS beans 
        (id INTEGER PRIMARY KEY, name TEXT, method TEXT, rating INTEGER);'''

INSERT_BEAN = '''INSERT INTO beans (name, method, rating) VALUES (?, ?, ?);'''

GET_ALL_BEANS = '''SELECT * FROM beans'''

GET_BEANS_BY_NAME = '''SELECT * FROM beans WHERE name = ?;'''

GET_BEST_PREPARATION_FOR_BEAN = '''
SELECT method FROM beans
WHERE name = ?
ORDER BY rating DESC
LIMIT 1;
'''


def connect():
    connection = sqlite3.connect('data.s3db')
    return connection


def create_tables(connection):
    with connection:
        connection.execute(CREATE_BEANS_TABLE)


def add_bean(connection, name, method, rating):
    with connection:
        return connection.execute(INSERT_BEAN, (name, method, rating)).fetchall()


def get_all_beans(connection):
    with connection:
        return connection.execute(GET_ALL_BEANS)


def get_beans_by_name(connection, name):
    with connection:
        return connection.execute(GET_BEANS_BY_NAME, (name,)).fetchall()


def get_best_preparation_for_bean(connection, name):
    with connection:
        return connection.execute(GET_BEST_PREPARATION_FOR_BEAN, (name,)).fetchone()
