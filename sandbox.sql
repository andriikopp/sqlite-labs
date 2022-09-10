--- DB1 Task No. 1
--- Selecting multiple columns
DROP TABLE IF EXISTS products;

CREATE TABLE products (
    productname VARCHAR(32),
    price DECIMAL(8, 2),
    productiondate DATE,
    expirationdate DATE,
    PRIMARY KEY (productname)
);

INSERT INTO
    products (
        productname,
        price,
        productiondate,
        expirationdate
    )
VALUES
    ('Yogurt', 200, '2020-11-19', '2021-01-19'),
    ('Juice', 380, '2020-10-10', '2022-10-10'),
    ('Milk', 520, '2020-08-19', '2020-08-23');

SELECT
    productname,
    productiondate,
    expirationdate
FROM
    products;

--- Cakes
DROP TABLE IF EXISTS cakes;

CREATE TABLE cakes (
    `name` VARCHAR(64),
    calories INT,
    PRIMARY KEY (`name`)
);

INSERT INTO
    cakes (`name`, calories)
VALUES
    ('Apple Cake', 100),
    ('Banana Cake', 200),
    ('Pound Cake', 180),
    ('Sponge Cake', 100),
    ('Genoise Cake', 360),
    ('Chiffon Cake', 250),
    ('Opera Cake', 90),
    ('Cheese Cake', 370);

SELECT
    `name`,
    calories
FROM
    cakes
ORDER BY
    calories ASC
LIMIT
    3;

--- DB1 Task No. 2
--- Apartments
DROP TABLE IF EXISTS appartments;

CREATE TABLE appartments (
    id INT,
    city VARCHAR(64),
    `address` VARCHAR(128),
    price DECIMAL(8, 2),
    `status` VARCHAR(32),
    PRIMARY KEY (id)
);

INSERT INTO
    appartments (id, city, `address`, price, `status`)
VALUES
    (
        1,
        'Las Vegas',
        '732 Hall Street',
        1000,
        'Not rented'
    ),
    (
        2,
        'Marlboro',
        '985 Huntz Lane',
        800,
        'Not rented'
    ),
    (
        3,
        'Moretown',
        '3757 Wines Lane',
        700,
        'Not rented'
    ),
    (
        4,
        'Owatonna',
        '314 Pritchard Court',
        500,
        'Rented'
    ),
    (
        5,
        'Grayslake',
        '3234 Cunningham Court',
        600,
        'Rented'
    ),
    (
        6,
        'Great Neck',
        '1927 Romines Mill Road',
        900,
        'Not rented'
    );

SELECT
    id,
    city,
    `address`,
    price,
    `status`
FROM
    appartments
WHERE
    price > (
        SELECT
            AVG(price)
        FROM
            appartments
    )
    AND `status` = 'Not rented'
ORDER BY
    price DESC;