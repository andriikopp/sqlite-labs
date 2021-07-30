const sqlite3 = require('sqlite3').verbose();
const express = require('express')

const app = express()
const port = 3001

app.get('/orders', (req, res) => {
    let response = [];

    let db = new sqlite3.Database('../python/lab.db', sqlite3.OPEN_READWRITE, (err) => {
        if (err) {
            console.error(err.message);
        }

        console.log('Connected to the database.');
    });

    db.serialize(() => {
        db.each(`SELECT 
                name, address, product, amount, price, (amount * price) AS total
            FROM 
                customer INNER JOIN customer_order 
                    ON customer.id = customer_order.customer_id
            ORDER BY 
                price`, (err, row) => {
            if (err) {
                console.error(err.message);
            }

            response.push(row);
        });
    });

    db.close((err) => {
        if (err) {
            console.error(err.message);
        }

        console.log('Close the database connection.');

        res.setHeader('Access-Control-Allow-Origin', '*');
        res.setHeader('Access-Control-Allow-Headers', 'origin, content-type, accept');

        res.send(response);
    });
});

app.listen(port, () => {
    console.log(`Serving at http://localhost:${port}`)
});