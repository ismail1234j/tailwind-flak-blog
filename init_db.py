import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Test 1', 'Content for test 2')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Test 2', 'Content for test 2')
            )

connection.commit()
connection.close()
