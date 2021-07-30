from flask import Flask
from flask import jsonify
from flask_cors import CORS

import sqlite3


app = Flask(__name__)

CORS(app)


@app.route("/orders")
def orders():
    conn = sqlite3.connect("lab.db")

    cursor = conn.execute('''
        SELECT 
            name, address, product, amount, price, (amount * price)
        FROM 
            customer INNER JOIN customer_order 
                ON customer.id = customer_order.customer_id
        ORDER BY 
            price
    ''')

    response = []

    for row in cursor:
        response.append(row)

    return jsonify(response)


if __name__ == "__main__":
    app.run()
