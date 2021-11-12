<?php
	// Database connection
	$conn = new mysqli('3306','xs1cdlbk6b7o','4QHWqXT{2XHAEU#','information_schema');
    
    if ($conn->connect_error) {
      echo "$conn->connect_error";
      die("Connection failed: " . $conn->connect_error);
    }

    else {
      echo "Connect successfully..."
    }

    $conn->close();    
?>


