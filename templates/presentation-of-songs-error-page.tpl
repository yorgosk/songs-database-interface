<html>
<head><title>Presentation of Songs Error Page</title></head>
<body>
  <h1>Insertion Error!</h1>
  <hr/>
  %if(title_exception):
    <p>An exception has occured while reading song's Title.</p>
  %elif(year_exception):
    <p>An exception has occured while reading song's Year.</p>
  %elif(company_exception):
    <p>An exception has occured while reading song's Company.</p>
  %else:
    <p>Ooops! Something's wrong! Please go back and try again.</p>
  %end
  <table>
    <tr>
      <td><input value="Go Back" type="button" onClick="location.href='/insert-song';"></td>
      <td><input value="Go Home" type="button" onClick="location.href='/homepage';"></td>
    </tr>
  </table>
  <hr/>
</body>
</html>
