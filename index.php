<!--
Index page which has a table on it. TODO: pdf generation..
-->
<html>
	<head>
		<script src=maketable.js></script>
		<link rel="stylesheet" type="text/css" href="test.css" />
	</head>

	<body onload="refresh()">
		This is an example...
		<form action="process.php" method = "post" id = "myForm" name = "theForm">
			Enter something: <input type="text" name = "test" />
			<input type="button" onclick="refresh()" value="Refresh Me"/>
			<input type="submit" value="Submit Me"/> 
			Select <a href="javascript:selectToggle(true, 'theForm');">All</a> | <a href="javascript:numeric('theForm');">Numeric</a> | <a href="javascript:selectToggle(false, 'theForm');">None</a><p>
			<table id="myTable" border="1"/>
				<tr>
					<b>
					<th>Title</th>
					<th>Time</th>
					<th>My Curriculum</th>
					<th>Exercise</th>
					</b>
				</tr>
			</table>
			<br />
		</form>
		
		
	</body>
</html>
