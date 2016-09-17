<html>
<head><title>Insert Song Error Page</title></head>
<body>
  <h1>Insertion Error!</h1>
  <hr/>
  %if (title_error or productionYear_error):
    %if (title_error):
      <p>Giving an Title to the song is neccessary for the insertion to be completed.</p>
    %end
    %if (productionYear_error):
      <p>Giving a Production Year to the song is neccessary for the insertion to be completed.</p>
    %end
  %else:
    %if (existence_error):
      <p>A song with the Title that you entered already exists. Try editing his details.</p>
    %else:
      <p>Exception Occured!</p>
    %end
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
