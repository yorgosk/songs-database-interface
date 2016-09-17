<html>
<head><title>Update Artist Information Error Page</title></head>
<body>
  <h1>Insertion Error!</h1>
  <hr/>
  %if(name_exception):
    <p>An exception has occured while reading artist's Name.</p>
  %elif(surname_exception):
    <p>An exception has occured while reading artist's Surname.</p>
  %elif(birthyear_exception):
    <p>An exception has occured while reading artist's Birth Year.</p>
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
