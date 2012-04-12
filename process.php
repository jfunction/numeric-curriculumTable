<!--Step 4, parse user data... TODO: handle data to pdf or another type of printable format-->
<html>
	<body>
		Hello... You checked: 
		<?php
		for ($i=1;$i<300;$i++)//upper bound can be larger than 300 but gets laggy and couldn't think of a way to do this yet...
		{
			if ($_POST["number_" . $i]==$i)
			{
				echo $i . ',';
			}
		}
		$userText = $_POST["test"];
		echo "etc ... and you entered: \"";
		echo $userText;
		echo "\" in the textbox..."
		?>
		ok bye
	</body>
</html>
