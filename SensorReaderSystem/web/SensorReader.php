<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta http-equiv="refresh" content="5"> <!-- refresh 5S -->
    <title>感測器資料</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
        }

        #dynamicValue {
            font-size: 24px;
            margin: 20px;
            padding: 10px;
        }
    </style>
</head>
<body>
    <div id="dynamicValue">
        <?php
            // database connect set
			$servername = "localhost:3306";
			$username = "root";      
			$password = "12345678"; 
			$dbname = "sensordata"; 

			// connect
			$conn = new mysqli($servername, $username, $password, $dbname);

			// check connect
			if ($conn->connect_error) {
				die("Connection failed: " . $conn->connect_error);
			}

			$sql = "SELECT * FROM nowdata ORDER BY id DESC LIMIT 1";
            $result = $conn->query($sql);
			if ($result->num_rows > 0) {
                // output
                while($row = $result->fetch_assoc()) {
                    echo "時間: " . $row["time"] ;
					echo " 溫度: " . $row["temperature"] ;
					echo " 濕度: " . $row["humidity"] ;
                }
            } else {
                echo "0 results";
            }
			// 關閉連線
			$conn->close();
        ?>
    </div>
</body>
</html>
