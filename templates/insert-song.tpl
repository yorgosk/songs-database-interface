<html>
<head>
  <title>Insert Song</title>
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
  <h1>Insert Song</h1>
        <hr/>
        <form action="/view-insert-song-result" method="POST">
            <label>Title</label><input type="text" name="Title" required placeholder="Enter a valid title"><br>
            <label>Production Year</label><input type="text" name="ProductionYear" required placeholder="Enter a production year"><br><br>
            <label>CD</label>
            <select name="cd">
              %for row in rows1:
                <option value={{str(row[0])}}>{{row[0]}}</option>
              %end
            </select><br>
            <label>Singer</label>
            <select name="singer">
              %for row in rows2:
                <option value={{str(row[0])}}>{{row[0]}}</option>
              %end
            </select><br>
            <label>Composer</label>
            <select name="composer">
              %for row in rows3:
                <option value={{str(row[0])}}>{{row[0]}}</option>
              %end
            </select><br>
            <label>SongWriter</label>
            <select name="songwriter">
              %for row in rows4:
                <option value={{str(row[0])}}>{{row[0]}}</option>
              %end
            </select><br><br>
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
