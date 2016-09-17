<html>
<head><title>View Insert Artist Result</title></head>
<body>
  <table>
    <tr>
      <td><h1>View Insert Artist Result</h1></td>
      <td><input value="Go Home" type="button" onClick="location.href='/homepage';"></td>
      <td></td>
    </tr>
  </table>
  <hr/>
  <table>
    <tr><th>National ID</th><th>Name</th><th>Surname</th><th>Birth Year</th></tr>
    %for row in rows:
        <tr>
          %for col in row:
            <td>{{col}}</td>
          %end
          <td>
            <form "{{str(row[0])}}"></form>
          </td>
        </tr>
    %end
  </table>
  <hr/>
</body>
</html>
