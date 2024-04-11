<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta http-equiv="refresh" content="5"> <!-- refresh 5S -->
    <title>感測器資料</title>
    <style>
        body {
			margin: 0px;
			padding: 0px;
            font-family: Arial, sans-serif;
			color: cornflowerblue;
            text-align: center;
        }

        #div1 {
            font-size: 24px;
			background-color: #88FDFF;
			padding-top:50px;
			padding-bottom:50px;
        }
		table {
			border: solid;
			width: 80%;
			height: 200px;
			margin: auto;
		}
		
		tr {
			border: solid;
			padding: 10px;
			font-size: 20px;
			font-style: italic;
			
		}
		td {
			border: solid;
			padding: 10px;
			font-size: 20px;
			font-style: italic;
		}
		
    </style>
</head>
<body>
    <div id="div1">
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
					echo "<table>";
                    echo "<tr><td> 時間 </td><td> 溫度 </td><td> 濕度 </td></tr>" ;
					echo "<tr><td>" . $row["time"] . "</td><td>" . $row["temperature"] . "</td><td>" . $row["humidity"] . "</td></tr>";
					echo "</table>";
					
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
