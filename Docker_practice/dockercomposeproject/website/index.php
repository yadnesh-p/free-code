<!DOCTYPE html>
<html lang="en">
<head>
	<title>Fruit Service</title>
</head>
<body>
	<h1>Welcome to India's Fruit shop</h1>
	<u1>
		<?php
			$json = file_get_contents('http://fruit-service');
			$obj = json_decode($json);
			$fruits = $obj->fruits; 
			foreach ($fruits as $fruit){
				echo "<li>$fruit</li>";
			}
		?>
	</ul>
</body>
</html>
