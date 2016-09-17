<html>
<head><title>View Song Results</title></head>
<body>
  <table>
    <tr>
      <td><h1>View Song Results</h1></td>
      <td><input value="Go Home" type="button" onClick="location.href='/homepage';"></td>
      <td></td>
    </tr>
  </table>
  <hr/>
  <table>
    <tr><th>Titlos</th><th>Sinthetis</th><th>Etos Paragogis</th><th>Stixourgos</th><th>Etaireia</th></tr>
    %for row in rows:
        <tr>
          %for col in row:
            <td>{{col}}</td>
          %end
          <td>
        </tr>
    %end
  </table>
  <hr/>
</body>
</html>
