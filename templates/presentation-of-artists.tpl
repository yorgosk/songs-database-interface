<html>
<head>
  <title>Presentation of Artists</title>
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
  <h1>Presentation of Artists</h1>
        <hr/>
        <form action="/view-artist-results" method="POST">
            <label>Name</label><input type="text" name="name"><br>
            <label>Surname</label><input type="text" name="surname"><br>
            <label>Birth Year - From</label><input type="number" name="birthYearFrom"><br>
            <label>Birth Year - To</label><input type="number" name="birthYearTo"><br>
            <br>
            <table>
              <tr>
                <td></td>
                <td><label><input type="radio" name="type" value="Singer">Singer</label></td>
              </tr>
              <tr>
                <td><label>Type</label></td>
                <td><label><input type="radio" name="type" value="SongWriter">SongWriter</label></td>
              </tr>
              <tr>
                <td></td>
                <td><label><input type="radio" name="type" value="Composer">Composer</label></td>
              </tr>
            </table>
            <br>
            <table>
              <tr>
                <td><label><input value="Submit" type="submit"></label></td>
                <td><label><input value="Reset" type="reset"></label></td>
                <td><label><input value="Go Home" type="button" onClick="location.href='/homepage';"></label></td>
              </tr>
            </table>
        </form>
        <hr/>
</body>
</html>
