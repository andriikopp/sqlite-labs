# import sqlite3 python module

import sqlite3


# --- CONNECT TO A DB

# if the database does not exist, then it will be created
# and a database object will be returned

conn = sqlite3.connect("lab.db")


# --- CREATE TABLES

# execute an SQL statement to create `customer` table

conn.execute('''
    CREATE TABLE customer (
        id INT PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        address TEXT NOT NULL
    );
''')


# execute an SQL statement to create `customer_order` table

conn.execute('''
    CREATE TABLE customer_order (
        customer_id INT NOT NULL,
        product VARCHAR(30) NOT NULL,
        amount INT NOT NULL,
        price DECIMAL(8,2) NOT NULL,
        PRIMARY KEY (customer_id, product),
        FOREIGN KEY (customer_id) REFERENCES customer(id)
    );
''')


# --- INSERT RECORDS

# insert to the `customer` table

conn.execute("INSERT INTO customer (id, name, address) \
    VALUES (1, 'Jennie M. Burns', '4007 Poplar Street Tinley Park, IL 60477')")

conn.execute("INSERT INTO customer (id, name, address) \
    VALUES (2, 'Esther Q. Harris', '3644 Ottis Street Oklahoma City, OK 73109')")

conn.execute("INSERT INTO customer (id, name, address) \
    VALUES (3, 'Charles M. Smith', '4166 Stuart Street Gibsonia, PA 15044')")


# insert to the `customer_order` table

conn.execute("INSERT INTO customer_order (customer_id, product, amount, price) \
    VALUES (1, 'FABRIC bike seat', 1, 199.99)")

conn.execute("INSERT INTO customer_order (customer_id, product, amount, price) \
    VALUES (1, 'FLEXIBLE mail sorter', 4, 29.99)")

conn.execute("INSERT INTO customer_order (customer_id, product, amount, price) \
    VALUES (2, 'CERAMIC fork', 10, 2.99)")

conn.execute("INSERT INTO customer_order (customer_id, product, amount, price) \
    VALUES (3, 'CERAMIC fork', 5, 2.99)")

conn.execute("INSERT INTO customer_order (customer_id, product, amount, price) \
    VALUES (3, 'PLASTER coat hanger', 3, 49.99)")


# --- SELECT RECORDS

# fetch records from `customer` and `customer_order` tables

cursor = conn.execute('''
    SELECT 
        name, address, product, amount, price, (amount * price)
    FROM 
        customer INNER JOIN customer_order 
            ON customer.id = customer_order.customer_id
    ORDER BY 
        price
''')


# display fetched records

for row in cursor:
    print(row)


# --- UPDATE RECORDS

# update the record in a `customer` table

conn.execute('''
    UPDATE 
        customer
    SET
        address = '2690 Central Avenue Rochelle Park, NJ 07662' 
    WHERE 
        id = 2
''')

conn.commit()

# fetch the updated record from a `customer` table

cursor = conn.execute('''
    SELECT 
        *
    FROM 
        customer 
    WHERE id = 2
''')

# display the updated record

for row in cursor:
    print(row)


# --- DELETE RECORDS

# delete the record from a `customer_order` table

conn.execute('''
    DELETE FROM 
        customer_order 
    WHERE 
        customer_id = 3 AND product = 'CERAMIC fork'
''')

# fetch the records from a `customer_order` table

cursor = conn.execute('''
    SELECT 
        *
    FROM 
        customer_order 
''')

# display the record is removed

for row in cursor:
    print(row)


# --- FINISH THE WORK

# commit the current transaction

conn.commit()


# close the database connection when finished

conn.close()
