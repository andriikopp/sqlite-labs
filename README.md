# SQLite Database Labs

For software engineering and computer science students.

*Working examples are given in this repository as reference materials.*

**Data Modeling**

- [Lab 0. Data modeling as code.](https://github.com/andriikopp/sqlite-labs#lab-0-data-modeling-as-code) (*PlantUML, Entity-Relationship modeling*)

**Python + SQLite**

- [Lab 1. Learning essentials of DBMS.](https://github.com/andriikopp/sqlite-labs#lab-1-learning-essentials-of-dbms) (*Python, SQLite, DDL SQL*)
- [Lab 2. Basic data manipulation commands of SQL.](https://github.com/andriikopp/sqlite-labs#lab-2-basic-data-manipulation-commands-of-sql) (*Python, SQLite, DML SQL*)

**Python + Web**

- [Lab 3. Create simple database Web API.](https://github.com/andriikopp/sqlite-labs#lab-3-create-simple-database-web-api) (*Python, Flask, SQLite, DML SQL, JSON*)

**Frontend**

- [Lab 4. Display database records on web pages.](https://github.com/andriikopp/sqlite-labs#lab-4-display-database-records-on-web-pages) (*Python, Flask, HTML, Bootstrap, JavaScript, axios.js, Vue.js*)

**Other languages + SQLite**

- [Lab 5. Use databases in PHP.](https://github.com/andriikopp/sqlite-labs#lab-5-use-databases-in-php) (*PHP, OOP, PDO, SQLite, HTML, Bootstrap, JavaScript, axios.js, Vue.js*)
- [Lab 6. Use databases in NodeJS.](https://github.com/andriikopp/sqlite-labs#lab-6-use-databases-in-nodejs) (*NodeJS, SQLite, express, HTML, Bootstrap, JavaScript, axios.js, Vue.js*)

#### Report requirements:

- Briefly describe main steps of the work.
- Insert the source code and execution results.

## Problem description.

*Some enterprise purchases products from various suppliers (both legal en-tities and individual entrepreneurs). Purchasing is performed using batches and formalized as supply contracts. Each supply contract has unique number and might be concluded with a single supplier. Documents for each contract include product name, supplied amount, and price (in UAH).*

- The following entities could be used to describe the problem domain:

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

## Lab 0. Data modeling as code.

- Get familiar with the PlantUML [Entity-Relationship (ER) diagram](https://plantuml.com/ie-diagram) syntax.
- Build the data model of entities mentioned above using the PlantUML ER diagram [here](http://www.plantuml.com/plantuml/uml/SyfFKj2rKt3CoKnELR1Io4ZDoSa70000).

See the example below:

```java
@startuml
entity Student {
   * StudentID
   FullName
   BirthDate
   EnrollmentDate
}

entity Course {
   * StudentID
   * CourseName
   Credits
   Hours
   Score
}

Student |o--o{ Course
@enduml
```

Sample output:

![ER-model](http://www.plantuml.com/plantuml/png/SoWkIImgAStDuKhDAyaigLG8BYbD0J8LghaK51IqO5nF5n3NhJGdnoynDnN4TieiAibmIIm1SrppYl9pSdA12i4YjLmmqvppIukAKx4QfWMLX1deN9IQabbI369w02N0ZE3a_2AmSJ1NrUJhwkPNGtLoEQJcfG2T3W00)

## Lab 1. Learning essentials of DBMS.

- Create a database.

See the example below:

```python
# import sqlite3 python module

import sqlite3


# --- CONNECT TO A DB

# if the database does not exist, then it will be created
# and a database object will be returned

conn = sqlite3.connect("lab.db")
```

### Implementation.

- Create required database tables (see the entities mentioned above).

See the example below:

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

- Create records in a database tables.

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

See the example below:

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

See the example below:

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

See the example below:

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

See the example below:

```python
# --- FINISH THE WORK

# commit the current transaction

conn.commit()


# close the database connection when finished

conn.close()
```

## Lab 3. Create simple database Web API.

### Preparation.

- Install [Flask](https://flask.palletsprojects.com/en/2.0.x/) web development framework for Python:

```shell
pip install Flask
```

- Create new Python script with basic Flask routing.

See the example below:

```python
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app.run()
```

- Go to ```http://127.0.0.1:5000/``` to check that everything works fine. The web page with only a "Hello, World!" message is expected.

### Experimenting with Flask.

- Create the API endpoint to ask for the **1st** SQL SELECT query written before - *Print a list of products deliveredby the supplier 1 (Ivanov I.I. PE) for the contract 1*.

See the example below:

```python
from flask import Flask
from flask import jsonify

import sqlite3


app = Flask(__name__)


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

    conn.close()

    return jsonify(response)


if __name__ == "__main__":
    app.run()
```

When ```http://127.0.0.1:5000/orders``` visited, the following JSON response is expected:

```json
[["Esther Q. Harris","2690 Central Avenue Rochelle Park, NJ 07662","CERAMIC fork",10,2.99,29.900000000000002],["Jennie M. Burns","4007 Poplar Street Tinley Park, IL 60477","FLEXIBLE mail sorter",4,29.99,119.96],["Charles M. Smith","4166 Stuart Street Gibsonia, PA 15044","PLASTER coat hanger",3,49.99,149.97],["Jennie M. Burns","4007 Poplar Street Tinley Park, IL 60477","FABRIC bike seat",1,199.99,199.99]]
```

### Implementation.

Create and verify API endpoints for all of the previously written SQL SELECT queries:

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

## Lab 4. Display database records on web pages.

### Preparation.

- Create the basic [Bootstrap template](https://getbootstrap.com/docs/4.4/getting-started/introduction/) in the ```index.html``` file.

```html
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">

    <title>Hello, world!</title>
  </head>
  <body>
    <h1>Hello, world!</h1>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
  </body>
</html>
```

- Remove ```<!-- Optional JavaScript -->``` part.
- Reference ```axios.js``` and ```vue.js``` instead.

```html
<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/vue@2"></script>
```

- Install Flask [CORS](https://developer.mozilla.org/ru/docs/Web/HTTP/CORS) module to enable using HTTP API.
- Modify Web API headers:

```python
from flask import Flask
from flask import jsonify
from flask_cors import CORS

import sqlite3


app = Flask(__name__)

CORS(app)

# ...
```

### Experimenting with axios and Vue.

- Get familiar with [axios](https://github.com/axios/axios) and [Vue](https://ru.vuejs.org/v2/guide/index.html) for web development.
- Add respective HTML and JavaScript code to display result set of the **1st** SQL SELECT query written before - *Print a list of products deliveredby the supplier 1 (Ivanov I.I. PE) for the contract 1*.

See the example below:

```html
<!doctype html>
<html lang="en">

<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">

    <title>Orders</title>
</head>

<body class="mb-2 mt-2 mr-2 ml-2">
    <h1>Orders</h1>

    <!-- Vue.js application -->
    <div id="app">
        <!-- List orders -->
        <div class="alert alert-info" role="alert" v-for="order in orders">
            <!-- Display orders data -->
            <h4 class="alert-heading">{{ order[0] }}</h4>
            <p><b>Address:</b> {{ order[1] }}</p>
            <hr>
            <p class="mb-0"><b>Product:</b> {{ order[2] }}, ${{ order[4] }}</p>
            <p class="mb-0"><b>Amount:</b> {{ order[3] }}</p>
            <p class="mb-0"><b>Total:</b> ${{ order[5].toFixed(2) }}</p>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/vue@2"></script>

    <script>
        // Axios.js request to the API endpoint
        axios.get('http://127.0.0.1:5000/orders')
            .then(function(response) {

                // Vue.js application
                const app = new Vue({
                    el: '#app',
                    data: {
                        orders: response.data
                    }
                });
            })
            .catch(function(error) {
                alert(error);
            });
    </script>
</body>

</html>
```

- Open the web page in a browser to check the results.
- Separate HTML and JS code to follow best practices.

### Implementation.

For each of the previously developed API endpoints create respective web pages using axios.js and vue.js to display database records:

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

## Lab 5. Use databases in PHP.

### Preparation.

- In order to simplify development, it is recommended to use *Visual Studio Code with [PHP Server](https://github.com/brapifra/vscode-phpserver) extension*.
- Create PHP script ```index.php```.

### Experimenting with [PDO](https://www.php.net/manual/ru/book.pdo.php).

- Create the API endpoint to ask for the **1st** SQL SELECT query written before - *Print a list of products deliveredby the supplier 1 (Ivanov I.I. PE) for the contract 1*.

See the example below:

```php
<?php

class OrdersSQLite
{
    // path to SQLite database
    const PATH_TO_SQLITE_FILE = '../python/lab.db';

    private $pdo;

    /**
     * Returns connection object.
     */
    public function connect()
    {
        if ($this->pdo == null) {
            $this->pdo = new \PDO("sqlite:" . OrdersSQLite::PATH_TO_SQLITE_FILE);
        }

        return $this->pdo;
    }

    /**
     * Returns orders result set.
     */
    public function getOrders()
    {
        $stmt = $this->pdo->query('SELECT 
                name, address, product, amount, price, (amount * price) AS total
            FROM 
                customer INNER JOIN customer_order 
                    ON customer.id = customer_order.customer_id
            ORDER BY 
                price');

        $orders = [];

        while ($row = $stmt->fetch(\PDO::FETCH_ASSOC)) {
            $orders[] = [
                'name' => $row['name'],
                'address' => $row['address'],
                'product' => $row['product'],
                'amount' => $row['amount'],
                'price' => $row['price'],
                'total' => $row['total']
            ];
        }

        return $orders;
    }
}

$orders = new OrdersSQLite;
$orders->connect();

// JSONify response
header('Content-Type: application/json');

echo json_encode($orders->getOrders());
```

### Completing the web page.

- Make JSON response conditional depending on the GET HTTP parameter.
- Close PHP tag and insert in the ```else``` body the content of ```index.html``` web page created earlier.

```php
# ...

if (isset($_GET['query']) && $_GET['query'] == 'orders') {
    $orders = new OrdersSQLite;
    $orders->connect();

    // JSONify response
    header('Content-Type: application/json');

    echo json_encode($orders->getOrders());
} else {
?>
    <!doctype html>

    <!-- ... -->
<?php
}
```

- Use actual PHP endpoint inside the ```axios.get()``` method:

See the example below:

```javascript
// ...
axios.get('http://localhost:3000/php/index.php?query=orders')
// ...
```

- Edit the Vue.js rendering part to correspond responded JSON data:

See the example below:

```html
<div id="app">
    <!-- List orders -->
    <div class="alert alert-info" role="alert" v-for="order in orders">
        <!-- Display orders data -->
        <h4 class="alert-heading">{{ order.name }}</h4>
        <p><b>Address:</b> {{ order.address }}</p>
        <hr>
        <p class="mb-0"><b>Product:</b> {{ order.product }}, ${{ order.price }}</p>
        <p class="mb-0"><b>Amount:</b> {{ order.amount }}</p>
        <p class="mb-0"><b>Total:</b> ${{ order.total }}</p>
    </div>
</div>
```

- Separate PHP API endpoint, JavaScript code, and HTML page to follow best practices.

## Lab 6. Use databases in NodeJS.

### Preparation.

- Install SQLite module:

```shell
npm install sqlite3
```

### Experimenting with sqlite3 in NodeJS.

- Create ```index.js``` file to place code that works with the SQLite database.

See the example below:

```javascript
const sqlite3 = require('sqlite3').verbose();

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

        console.log(row);
    });
});

db.close((err) => {
    if (err) {
        console.error(err.message);
    }

    console.log('Close the database connection.');
});
```

When run this script using ```node index.js``` command, the following result is expected:

```shell
Connected to the database.
{
  name: 'Esther Q. Harris',
  address: '2690 Central Avenue Rochelle Park, NJ 07662',
  product: 'CERAMIC fork',
  amount: 10,
  price: 2.99,
  total: 29.900000000000002
}
...
```

### Transforming to a web application.

- Install the ```express``` web development [module](https://expressjs.com/ru/starter/installing.html):

```shell
npm install express
```

- Create the API endpoint to ask for the **1st** SQL SELECT query written before - *Print a list of products deliveredby the supplier 1 (Ivanov I.I. PE) for the contract 1*.

See the example below:

```javascript
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

        res.send(response);
    });
});

app.listen(port, () => {
    console.log(`Serving at http://localhost:${port}`)
});
```

When ```http://127.0.0.1:3001/orders``` visited, the following JSON response is expected:

```json
[{"name":"Esther Q. Harris","address":"2690 Central Avenue Rochelle Park, NJ 07662","product":"CERAMIC fork","amount":10,"price":2.99,"total":29.900000000000002},{"name":"Jennie M. Burns","address":"4007 Poplar Street Tinley Park, IL 60477","product":"FLEXIBLE mail sorter","amount":4,"price":29.99,"total":119.96},{"name":"Charles M. Smith","address":"4166 Stuart Street Gibsonia, PA 15044","product":"PLASTER coat hanger","amount":3,"price":49.99,"total":149.97},{"name":"Jennie M. Burns","address":"4007 Poplar Street Tinley Park, IL 60477","product":"FABRIC bike seat","amount":1,"price":199.99,"total":199.99}]
```

- Create the ```nodejs/orders.html``` web page and copy there content of ```index.html``` used before.
- Enable CORS for the created NodeJS endpoint.

See the example below:

```javascript
// ...
res.setHeader('Access-Control-Allow-Origin', '*');
res.setHeader('Access-Control-Allow-Headers', 'origin, content-type, accept');

res.send(response);
```

- Do other necessary changes to ```nodejs/orders.html``` in order to make the web page work properly (use previous laboratory works as the reference).
