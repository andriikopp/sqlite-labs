import sqlite3

conn = sqlite3.connect('sandbox.db')

# drop old tables
conn.execute('''
DROP TABLE product;
''')

# create new tables
conn.execute('''
CREATE TABLE product (
  productname VARCHAR(100),
  price DECIMAL(8,2),
  productiondate DATE,
  expirationdate DATE,
  
  PRIMARY KEY (productname)
);
''')

# insert data
conn.execute('''
INSERT INTO 
  product (productname, price, productiondate, expirationdate) 
VALUES 
  ('Yogurt', 200, '2020-11-19', '2021-01-19'),
  ('Juice', 380, '2020-10-10', '2022-10-10'),
  ('Milk', 520, '2020-08-19', '2020-08-23');
''')

# query data
cursor = conn.execute('''
SELECT 
  productname, productiondate, expirationdate 
FROM 
  product;
''')

# display results
for row in cursor:
    print(row)
