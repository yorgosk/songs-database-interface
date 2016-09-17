<html>
<head>
  <title>Presentation of Songs</title>
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
  <h1>Presentation of Songs</h1>
        <hr/>
        <form action="/view-song-results" method="POST">
            <label>Song Title</label><input type="text" name="song-title"><br>
            <label>Production Year</label><input type="number" name="production-year"><br>
            <label>Company</label><input type="text" name="company"><br>
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
