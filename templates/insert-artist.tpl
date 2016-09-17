<html>
<head>
  <title>Insert Artist</title>
  <style type="text/css">
    label{
      display: inline-block;
      float: left;
      clear: left;
      width: 150px;
      text-align: left;
    }
  </style>
</head>
<body>
  <h1>Insert Artist</h1>
        <hr/>
        <form action="/view-insert-artist-result" method="POST">
            <label>National Id</label><input type="text" name="Nationalid" required placeholder="Enter a valid ID"><br>
            <label>Name</label><input type="text" name="Name" required placeholder="Enter a name"><br>
            <label>Surname</label><input type="text" name="Surname" required placeholder="Enter a surname"><br>
            <label>Birth Year</label><input type="text" name="Birthyear" required placeholder="Enter a birth year"><br>
            <br>
            <table>
              <tr>
                <td><label><input value="Update Information" type="submit"></label></td>
                <td><label><input value="Reset" type="reset"></label></td>
                <td><label><input value="Go Home" type="button" onClick="location.href='/homepage';"></label></td>
              </tr>
            </table>
        </form>
        <hr/>
</body>
</html>
