<html>
<head>
  <title>Update Artist Information</title>
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
  <h1>Update Artist Information</h1>
  <hr/>
  <form action="/artist-information-updated/{{id}}" method="POST">
    <label>Name</label><input type="text" name="name" value={{name}}><br>
    <label>Surname</label><input type="text" name="surname" value={{surname}}><br>
    <label>Birth Year</label><input type="number" name="birthYear" value={{birthYear}}><br>
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
