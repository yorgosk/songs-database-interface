<html>
<head><title>View Insert Song Result</title></head>
<body>
  <table>
    <tr>
      <td><h1>View Insert Song Result</h1></td>
      <td></td>
      <td><input value="Go Home" type="button" onClick="location.href='/homepage';"></td>
    </tr>
  </table>
  <hr/>
  <table>
    <tr><th>Title</th><th>Production Year</th><th>CD</th><th>Singer</th><th>Composer</th><th>SongWriter</th></tr>
    %for row in rows:
        <tr>
          %for col in row:
            <td>{{col}}</td>
          %end
        </tr>
    %end
  </table>
  <hr/>
</body>
</html>
