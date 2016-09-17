<html>
<head><title>Insert Artist Error Page</title></head>
<body>
  <h1>Insertion Error!</h1>
  <hr/>
  %if (id_error or name_error or surname_error or birthYear_error):
    %if (id_error):
      <p>Giving an ID to the artist is neccessary for the insertion to be completed.</p>
    %end
    %if (name_error):
      <p>Giving a Name to the artist is neccessary for the insertion to be completed.</p>
    %end
    %if (surname_error):
      <p>Giving a Surname to the artist is neccessary for the insertion to be completed.</p>
    %end
    %if (birthYear_error):
      <p>Giving a Birth Year to the artist is neccessary for the insertion to be completed.</p>
    %end
  %else:
    %if (existence_error):
      <p>An artist with the ID that you entered already exists. Try editing his details.</p>
    %else:
      <p>Exception Occured!</p>
    %end
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
