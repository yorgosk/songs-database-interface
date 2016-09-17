<html>
<head><title>View Artist Results</title></head>
<body>
  <table>
    <tr>
      <td><h1>View Artist Results</h1></td>
      <td></td>
      <td><input value="Go Home" type="button" onClick="location.href='/homepage';"></td>
    </tr>
  </table>
  <hr/>
  <table>
    <tr><th>National ID</th><th>Name</th><th>Surname</th><th>Birth Year</th><th>Edit?</th></tr>
    %for row in rows:
        <tr>
          %for col in row:
            <td>{{col}}</td>
          %end
          <td>
            <form action="update-artist-information/{{str(row[0])}}">
              <input value="Edit Me!" type="submit">
            </form>
          </td>
        </tr>
    %end
  </table>
  <hr/>
</body>
</html>
