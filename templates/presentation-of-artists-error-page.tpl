<html>
<head><title>Presentation of Artists Error Page</title></head>
<body>
  <h1>Insertion Error!</h1>
  <hr/>
  %if(name_exception):
    <p>An exception has occured while reading artist's Name.</p>
  %elif(surname_exception):
    <p>An exception has occured while reading artist's Surname.</p>
  %elif(birthyearfrom_exception):
    <p>An exception has occured while reading artist's Birth Year From.</p>
  %elif(birthyearto_exception):
    <p>An exception has occured while reading artist's Birth Year To.</p>
  %else:
    <p>Ooops! Something's wrong! Please go back and try again.</p>
  %end
  <table>
    <tr>
      <td><input value="Go Back" type="button" onClick="location.href='/insert-artist';"></td>
      <td><input value="Go Home" type="button" onClick="location.href='/homepage';"></td>
    </tr>
  </table>
  <hr/>
</body>
</html>
