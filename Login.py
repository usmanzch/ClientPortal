#!/usr/bin/python

import cgi, os, sys

print 'Content-type: text/html\n\n'


form = cgi.FieldStorage()
login = form.getvalue("login")
password = form.getvalue("password")


with open('clients.txt','r') as clients:
	
	for line in clients:
                line = line.strip()
		splitLine = line.split(' ')
        	user_check = splitLine[0]
        	pass_check = splitLine[1]
        	
        	if ((str(user_check) == str(login)) and (str(pass_check) == str(password))):
            		print"""            		
            			<html>
		        	<head>
		            	<meta http-equiv="Refresh" content="3; client.py">
		            	</head>
		            	<body bgcolor="#D6FFEB">
		            	<p><h3>Establishing connection....</h3></p>
		           	<form name="test" action="client.py" method="post">
		            	<input type="hidden" name="login" value=\""""+str(login)+"""\">
		            	</form> 
		           	<script type="text/javascript" language="JavaScript">
		            	document.test.submit();
		            	</script>
		            	</body>
		            	</html>"""
			clients.close()   	
			sys.exit()
            		
            		
print """<html>
<head>
<meta http-equiv="Refresh" content="3; ../default.html">
</head>
<body bgcolor ="#B00000">
<p><h3>Incorrect username or password.</h3></p>
</body>
</html>"""
    	
clients.close()

    