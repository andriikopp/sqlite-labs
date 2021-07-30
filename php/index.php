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

if (isset($_GET['query']) && $_GET['query'] == 'orders') {
    $orders = new OrdersSQLite;
    $orders->connect();

    // JSONify response
    header('Content-Type: application/json');

    echo json_encode($orders->getOrders());
} else {
?>

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
            <!-- Display data visualization -->
            <div v-if="chart">
                <img v-bind:src="chart" />
            </div>

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

        <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/vue@2"></script>

        <script>
            // Axios.js request to the API endpoint
            axios.get('http://localhost:3000/php/index.php?query=orders')
                .then(function(response) {
                    // Prepare data for visualization
                    const chartJSON = {
                        type: 'bar',
                        data: {
                            labels: response.data.map(order => order.name),
                            datasets: [{
                                label: 'Customers',
                                data: response.data.map(order => order.total)
                            }]
                        }
                    };

                    // Vue.js application
                    const app = new Vue({
                        el: '#app',
                        data: {
                            orders: response.data,
                            chart: 'https://quickchart.io/chart?c=' + JSON.stringify(chartJSON)
                        }
                    });
                })
                .catch(function(error) {
                    alert(error);
                });
        </script>
    </body>

    </html>
<?php
}
