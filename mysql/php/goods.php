<?php

$host = "localhost";
$user = "root";
$password = "";
$db = "shopdb";

$conn = new mysqli($host, $user, $password, $db);

if ($conn->connect_error) {
    die("MySQL connection failed\n");
}

$result = $conn->query("SELECT * FROM goods");

if ($result->num_rows > 0) {
    while ($row = $result->fetch_assoc()) {
        foreach ($row as $name => $value) {
            print($name . ": " . $value . "\n");
        }

        print("\n");
    }
} else {
    print("0 results\n");
}
