import sqlite3

conn = sqlite3.connect('sandbox.db')

with open('sandbox.sql', 'r') as file:
    scripts = file.read().rstrip()
    statements = scripts.split(';')

    for statement in statements:
        cursor = conn.execute(statement + ';')

        for row in cursor:
            print(row)
