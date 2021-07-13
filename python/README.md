# SQLite with Python

- [Lab 1. Learning essentials of DBMS.](https://github.com/andriikopp/sqlite-labs/tree/main/python#lab-1-learning-essentials-of-dbms)
- [Lab 2. Basic data manipulation commands of SQL.](https://github.com/andriikopp/sqlite-labs/tree/main/python#lab-2-basic-data-manipulation-commands-of-sql)

## Lab 1. Learning essentials of DBMS.

- Create a database. See example below:

```python
# import sqlite3 python module

import sqlite3


# --- CONNECT TO A DB

# if the database does not exist, then it will be created
# and a database object will be returned

conn = sqlite3.connect("lab.db")
```

### Problem description

*Some enterprise purchases products from various suppliers (both legal en-tities and individual entrepreneurs). Purchasing is performed using batches and formalized as supply contracts. Each supply contract has unique number and might be concluded with a single supplier. Documents for each contract include product name, supplied amount, and price (in UAH).*

### Implementation steps

- Create database tables:

**Suppliers**

| Field name   | Data type | Field size | Description   |
| ------------ | --------- | ---------- | ------------- |
| SupplierID   | INT       |            | Supplier ID   |
| SupplierName | VARCHAR   | 50         | Supplier name |
| Note         | Text      |            | Note          |

**LegalEntities**

| Field name | Data type | Field size | Description            |
| ---------- | --------- | ---------- | ---------------------- |
| SupplierID | INT       |            | Supplier ID            |
| TaxNumber  | VARCHAR   | 20         | Tax number             |
| VATNumber  | VARCHAR   | 20         | VAT certificate number |

**IndividualEntrepreneurs**

| Field name         | Data type | Field size | Description                     |
| ------------------ | --------- | ---------- | ------------------------------- |
| SupplierID         | INT       |            | Supplier ID                     |
| LastName           | VARCHAR   | 20         | Last name                       |
| FirstName          | VARCHAR   | 20         | First name                      |
| SecondName         | VARCHAR   | 20         | Second name                     |
| RegistrationNumber | VARCHAR   | 20         | Registration certificate number |

**Contracts**

| Field name     | Data type | Field size | Description              |
| -------------- | --------- | ---------- | ------------------------ |
| ContractNumber | INT       |            | Contract number          |
| ContractDate   | DATE      |            | Contract conclusion date |
| SupplierID     | INT       |            | Supplier ID              |
| ContractName   | VARCHAR   | 50         | Contract name            |
| Comment        | TEXT      |            | Note                     |

**Supplied**

| Field name     | Data type | Field size | Description             |
| -------------- | --------- | ---------- | ----------------------- |
| ContractNumber | INT       |            | Contract number         |
| Product        | VARCHAR   | 50         | Product name            |
| AmountNumber   | INT       |            | Batch size (items)      |
| PricePerItem   | DECIMAL   | 8,2        | Price per item (in UAH) |

See example below:

```python
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
```

- Create records in a database tables:

**Suppliers**

| SupplierName      | SupplierID | Note                                                                 |
| ----------------- | ---------- | -------------------------------------------------------------------- |
| Petrov P. P. PE   | 3          | Kharkiv, Nauky Av., 55, office 108, tel. 32-18-44                    |
| “Interfrut” LLC   | 2          | Kyiv, Peremohy Av., 154, office 3                                    |
| Ivanov I. I. PE   | 1          | Kharkiv, Pushkinska Str., 77 (tel. 33-33-44, 12-34-56, fax 22-12-33) |
| “Transservis” LLC | 4          | Odesa, Deribasivska Str., 75                                         |
| Sidorov S. S. PE  | 5          | Poltava, Svobody Str., 15, apt. 43                                   |

**LegalEntities**

| SupplierID | TaxNumber | VATNumber |
| ---------- | --------- | --------- |
| 2          | 00123987  | 19848521  |
| 4          | 29345678  | 25912578  |

**IndividualEntrepreneurs**

| SupplierID | LastName | FirstName | SecondName  | RegistrationNumber |
| ---------- | -------- | --------- | ----------- | ------------------ |
| 1          | Ivanov   | Illia     | Illich      | 00123987           |
| 3          | Petrov   | Pavlo     | Petrovych   | 12345678           |
| 5          | Sidorov  | Serhii    | Stepanovych | 09876541           |

**Contracts**

| ContractNumber | ContractDate | SupplierID | ContractName | Comment                    |
| -------------- | ------------ | ---------- | ------------ | -------------------------- |
| 1              | 9/1/1999     | 1          | Contract 1   | Invoice 34 from 8/30/99    |
| 2              | 9/10/1999    | 1          | Contract 2   | Invoice 08-78 from 8/28/99 |
| 3              | 9/10/1999    | 3          | Contract 3   | Invoice 08-78 from 8/28/99 |
| 4              | 9/23/1999    | 3          | Contract 4   | Order 56 from 8/28/99      |
| 5              | 9/24/1999    | 2          | Contract 5   | Invoice 74 from 9/11/99    |
| 6              | 10/1/1999    | 1          | Contract 6   | Invoice 9-12 from 9/28/99  |
| 7              | 10/2/1999    | 2          | Contract 7   | Invoice 85 from 9/21/99    |

**Supplied**

| ContractNumber | Product       | Amount | PricePerItem |
| -------------- | ------------- | ------ | ------------ |
| 1              | TV            | 10     | 1253.45      |
| 1              | Audio Player  | 25     | 655.12       |
| 1              | Video Player  | 12     | 722.33       |
| 2              | Stereo System | 11     | 511.43       |
| 2              | Audio Player  | 5      | 455.14       |
| 2              | Video Player  | 8      | 450.67       |
| 1              | Stereo System | 12     | 220.45       |
| 1              | PC            | 24     | 1554.22      |
| 2              | PC            | 43     | 1453.18      |
| 3              | TV            | 52     | 899.99       |
| 3              | Audio Player  | 11     | 544.00       |
| 3              | Display       | 85     | 545.32       |
| 4              | TV            | 56     | 990.56       |
| 4              | Audio Player  | 22     | 323.19       |
| 4              | Printer       | 41     | 350.77       |
| 5              | TV            | 14     | 860.33       |
| 5              | Audio Player  | 33     | 585.67       |
| 5              | Video Player  | 17     | 850.12       |
| 4              | Stereo System | 27     | 330.55       |
| 5              | Display       | 44     | 590.23       |
| 6              | TV            | 34     | 810.15       |
| 6              | PC            | 32     | 1850.24      |
| 6              | Display       | 51     | 520.95       |
| 7              | TV            | 62     | 900.58       |
| 7              | PC            | 15     | 1234.56      |
| 7              | Display       | 22     | 389.75       |

See example below:

```python
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
```

## Lab 2. Basic data manipulation commands of SQL.

### SELECT SQL command. Data processing using SELECT queries.

Create following queries:

- Print a list of products deliveredby the supplier 1 (Ivanov I.I. PE) for the contract 1.
- Print a list of products delivered by supplier 1 (Ivanov I.I. PE) between 9/1/1999 and 9/12/1999 (using “mm/dd/yyyy” dateformat).
- Print a list of products supplied in September of 1999 with supplier name and supply date.
- Print a list of contracts (number, date), total amount of the sup-plied products and total price for each contract (multiply and sum amount and price for each contract). The list should be sorted by contract numbers (ascending).
- Print a list of contracts (number, date) with total price for each contract. The list should be sorted by total price for each contract. Records for which contract number is greater than 3 should be excluded from query results.
- Print information about the largestproduct batch among allcon-tracts. Include information aboutsupplier, contract number, and date.
- Print a list of suppliers (name and ID) that have not concluded any contracts.
- Print a list of supplied product names with the average price per item (regardless of supplier).
- Print a list of products (name, amount andprice, supplier) for which price per item is greater than average.
- Print information about top five expensive products (name, price per item, supplier).
- For each day of September 1999 define price of products delivered by each supplier (include only delivery days).
- Create a list of contracts (only numbers), total amount of the supplied products, and total price for each contract. Print full names (last name, first name, and second name) of suppliers that are private entrepreneurs, as well as tax numbers of legal entities.
- Define amounts of eachdeliveredproductbyeach supplier.
- Print a list of contracts (number, date) and total price for each contract. The list should be sorted by total price for each contract. Exclude records for which the contract number is greater than a given value from the query result.
- Create a list of products delivered by the suppliers 1 and 2 (“Interfruit” LLC).
- Create a list of products supplied more than once.

See example below:

```python
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
```

### Data manipulation using SQL commands UPDATE and DELETE.

- Increase amount of each product delivered by the supplier 1 by 10.
- Delete all “empty” contracts (with no records about supplied products).

See example below:

```python
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
```

### Finish the work.

See example below:

```python
# --- FINISH THE WORK

# commit the current transaction

conn.commit()


# close the database connection when finished

conn.close()
```
