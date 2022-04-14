import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    db='shopdb'
)

cursor = db.cursor()

cursor.execute('SELECT * FROM goods')

result = cursor.fetchall()

for row in result:
    print(row)
