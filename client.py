#!/usr/bin/python

import cgi, os, sys
import cgitb; cgitb.enable()

print 'Content-type: text/html\n\n'


form = cgi.FieldStorage()
if form.has_key('login'):
	login = form.getvalue("login")
	
	client_folder_exists = os.path.isdir("../clients/"+str(login)+"")
	
	if (client_folder_exists != True):
		print ("Client folder not found.")
		sys.exit()
else:
	sys.exit()

print """
<!DOCTYPE html>
<html lang="en">

<head>
<script src="http://ajax.aspnetcdn.com/ajax/jQuery/jquery-1.11.3.min.js"></script>

    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>"""+str(login)+"""</title>

    <!-- Bootstrap Core CSS -->
    <link href="../css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom CSS -->
    <link href="../css/scrolling-nav.css" rel="stylesheet">

    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
        <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
        <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->


<script>
// Check for the various File API support.
if (window.File && window.FileReader && window.FileList && window.Blob) {
  // Great success! All the File APIs are supported.
} else {
  alert('The File APIs are not fully supported in this browser.');
}
</script>

<style type="text/css">
.bootstrap-frm {
    margin-left:auto;
    margin-right:auto;

    max-width: 1100x;
    background: #FFF;
    padding: 20px 30px 20px 30px;
    font: 12px "Helvetica Neue", Helvetica, Arial, sans-serif;
    color: #888;
    text-shadow: 1px 1px 1px #FFF;
    border:1px solid #DDD;
    border-radius: 5px;
    -webkit-border-radius: 5px;
    -moz-border-radius: 5px;
}
.bootstrap-frm h1 {
    font: 25px "Helvetica Neue", Helvetica, Arial, sans-serif;
    padding: 0px 0px 10px 40px;
    display: block;
    border-bottom: 1px solid #DADADA;
    margin: -10px -30px 30px -30px;
    color: #888;
}
.bootstrap-frm h1>span {
    display: block;
    font-size: 11px;
}
.bootstrap-frm label {
    display: block;
    margin: 0px 0px 5px;
}
.bootstrap-frm label>span {
    float: left;
    width: 20%;
    text-align: right;
    padding-right: 10px;
    margin-top: 10px;
    color: #333;
    font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
    font-weight: bold;
}
.bootstrap-frm input[type="text"], .bootstrap-frm input[type="email"], .bootstrap-frm textarea, .bootstrap-frm select{
    border: 1px solid #CCC;
    color: #888;
    height: 20px;
    line-height:15px;
    margin-bottom: 16px;
    margin-right: 6px;
    margin-top: 2px;
    outline: 0 none;
    padding: 5px 0px 5px 5px;
    width: 70%;
    border-radius: 4px;
    -webkit-border-radius: 4px;
    -moz-border-radius: 4px;    
    -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
    box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
    -moz-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.bootstrap-frm select {
    background: #FFF url('down-arrow.png') no-repeat right;
    background: #FFF url('down-arrow.png') no-repeat right;
    appearance:none;
    -webkit-appearance:none; 
    -moz-appearance: none;
    text-indent: 0.01px;
    text-overflow: '';
    width: 70%;
    height: 35px;
    line-height:15px;
}
.bootstrap-frm textarea{
    height:100px;
    padding: 5px 0px 0px 5px;
    width: 70%;
}
.bootstrap-frm .button {
    position:relative;
    left: 41%;
    background: #FFF;
    border: 1px solid #CCC;
    padding: 10px 20px 10px 20px;
    color: #333;
    border-radius: 4px;
}
.bootstrap-frm .button:hover {
    color: #333;
    background-color: #EBEBEB;
    border-color: #ADADAD;
}

</style>

<style type="text/css")>
/* layout.css Style */
.upload-drop-zone {
  height: 200px;
  border-width: 2px;
  margin-bottom: 20px;
}

/* skin.css Style*/
.upload-drop-zone {
  color: #ccc;
  border-style: dashed;
  border-color: #ccc;
  line-height: 200px;
  text-align: center
}
.upload-drop-zone.drop {
  color: #222;
  border-color: #222;
}
</style>

</head>

<!-- The #page-top ID is part of the scrolling feature - the data-spy and data-target are part of the built-in Bootstrap scrollspy function -->

<body id="page-top" data-spy="scroll" data-target=".navbar-fixed-top">

    <!-- Navigation -->
    <nav class="navbar navbar-default navbar-fixed-top" role="navigation">
        <div class="container">
            <div class="navbar-header page-scroll">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-ex1-collapse">
                    <span class="sr-only">Toggle navigation</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>"""
                


print("<a class=\"navbar-brand page-scroll\" href=\"#page-top\"><img src=\"../img/default.png\" style=\"width:35px;height:30px;\"></a>")

print """    <a class="navbar-brand page-scroll" href="#page-top">"""+str(login)+"""</a>
  
	    </div>           
              
            

            <!-- Collect the nav links, forms, and other content for toggling -->
            <div class="collapse navbar-collapse navbar-ex1-collapse">
                <ul class="nav navbar-nav">
                    <!-- Hidden li included to remove active class from about link when scrolled up past about section -->
                    <li class="hidden">
                        <a class="page-scroll" href="#page-top"></a>
                    </li>
                    <li>
                        <a class="page-scroll" href="#about">Upload</a>
                    </li>
                    <li>
                        <a class="page-scroll" href="#contact">Contact</a>
                    </li>
                    <li>
                        
                        <a class="page-scroll" href="#services">...</a>
                    </li>
                </ul>
            </div>
            <!-- /.navbar-collapse -->
        </div>
        <!-- /.container -->
    </nav>

    <!-- Intro Section -->
    <section id="intro" class="intro-section">
        <div class="container">
            <div class="row">
                <div class="col-lg-12">
                     <div class="panel panel-default">
        		<div class="panel-heading"><h1>Files:</h1></div>
       			 <div class="panel-body">
                    <p> <code>Files put in the client's folder will appear below, example:</code> </p>
                    
                """

# Open a file
path = "../clients/"+str(login)
dirs = os.listdir(path)



# This would print all the files and directories
for file in dirs:
	file_extension = os.path.splitext(file)[1]
	
	if (file_extension == ".docx" or file_extension == ".doc"):
		print ("<img src=\"../img/word.png\" style=\"width:30px;height:30px;\">")
	elif (file_extension == ".pdf"):
		print ("<img src=\"../img/pdf.png\" style=\"width:30px;height:30px;\">")
	else:
		print ("<img src=\"../img/unknown.png\" style=\"width:30px;height:30px;\">")
	print """<code><a href=\""""   +str(path)+   """/"""   +str(file)+   """\">"""   +str(file)+   """</a></code>"""

	print ("<p></p>")          
    

print """      	   <p></p> 
		   <!-----<a class="btn btn-default page-scroll" href="#about">Click Me to Scroll Down!</a>--->
		</div>
            </div>
        </div>
    </section>
<!--------------------------------------------------------------------------------------------------------------->
    <!-- About Section -->
    <section id="about" class="about-section">
        <div class="container">
            <div class="row">
                <div class="col-lg-12">
                    


      <div class="panel panel-default">
        <div class="panel-heading"><h1>Upload a file:</h1></div>
        <div class="panel-body">

          <!-- Standar Form -->
          <h4>Select files from your computer</h4>
          <form action="client.py" method="post" enctype="multipart/form-data" >
            <div class="form-inline">
              <div class="form-group">
                <input type="file" name="files[]" multiple>
                <input type="hidden" name="login" value=\""""+str(login)+"""\">
              </div>
              <button type="submit" class="btn btn-sm btn-primary" >Upload files</button>
            </div>
          </form>

          <!-- Drop Zone -->
          <h4>Or drag and drop files below</h4>
          
                     
          	<div class="upload-drop-zone" id="drop_zone"><h1>Drop files here<h1></div>
		<output id="list"></output>
		
		<script>
		  function handleFileSelect(evt) {
		    evt.stopPropagation();
		    evt.preventDefault();
		
		    var files = evt.dataTransfer.files; // FileList object.
		
		    // files is a FileList of File objects. List some properties.
		    var output = [];
		    for (var i = 0, f; f = files[i]; i++) {
		      output.push('<li><strong>', escape(f.name), '</strong> (', f.type || 'n/a', ') - ',
		                  f.size, ' bytes, last modified: ',
		                  f.lastModifiedDate ? f.lastModifiedDate.toLocaleDateString() : 'n/a',
		                  '</li>');
		    }
		    document.getElementById('list').innerHTML = '<ul>' + output.join('') + '</ul>';
		  }
		
		  function handleDragOver(evt) {
		    evt.stopPropagation();
		    evt.preventDefault();
		    evt.dataTransfer.dropEffect = 'copy'; // Explicitly show this is a copy.
		  }
		
		  // Setup the dnd listeners.
		  var dropZone = document.getElementById('drop_zone');
		  dropZone.addEventListener('dragover', handleDragOver, false);
		  dropZone.addEventListener('drop', handleFileSelect, false);
		</script>
          

          <!-- Progress Bar -->
          <div class="progress">
            <div class="progress-bar" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" style="width: 0%;">
              <span class="sr-only">60% Complete</span>
            </div>
          </div>

          <!-- Upload Finished -->
          <div class="js-upload-finished">
            <h3>Processed files</h3>
            <div class="list-group">
              <a href="../clients/client@choudhryconsolidated.com/Contract.docx" class="list-group-item list-group-item-success"><span class="badge alert-success pull-right">Success</span>contract.pdf</a>
              <a href="../clients/client@choudhryconsolidated.com/balancesheet.pdf" class="list-group-item list-group-item-success"><span class="badge alert-success pull-right">Success</span>balancesheet.pdf</a>
            </div>
          </div>
        </div>
      </div>
    </div> <!-- /container -->







<!--<input type="submit" name="submit" value="Upload" id="submit" /> 
                
<form enctype="multipart/form-data" action="client.py" method="post">
<p>File:</p>
<input type="file" name="files[]" multiple />
<input type="hidden" name="login" value=\""""+str(login)+"""\">
<p><input type="submit" class="btn btn-default page-scroll" value="Upload"></p>

</form>-->
                </div>
           
"""

if form.has_key('files[]'):

	try: # Windows needs stdio set for binary mode.
		    import msvcrt
		    msvcrt.setmode (0, os.O_BINARY) # stdin  = 0
		    msvcrt.setmode (1, os.O_BINARY) # stdout = 1
	except ImportError:
		    pass

	
	# A nested FieldStorage instance holds the file
	fileitem = form['files[]']
	
	# Test if the file was uploaded
	if fileitem.filename:
	   
	  	# strip leading path from file name to avoid directory traversal attacks
	   	fn = os.path.basename(fileitem.filename)
	   	open('../cgi-bin/' + fn, 'wb').write(fileitem.file.read())
	   	print ("<script>alert('Upload successful.');</script>")
	   
	else:
	   	print ("<script>alert('Error occured during upload, please try again.');</script>")
print """    </div>


        </div>
    </section>
<!--------------------------------------------------------------------------------------------------------------->

    <!-- Contact Section -->
    <section id="contact" class="contact-section">
        <div class="container">
            <div class="row">
                <div class="col-lg-12">
                          <div class="panel panel-default">
        		<div class="panel-heading"><h1>Contact firm:</h1></div>
       			 <div class="panel-body">

                    <form action="client.py" method="post" class="bootstrap-frm">

    <label>
        <span>Your Name :</span>
        <input id="email" type="email" name="email" value=\""""+str(login)+"""\" />
    </label>
    
    <label>
        <span>Email Topic :</span>
        <input id="name" type="text" name="name" placeholder="Email Topic" />
    </label>
    
    <label>
        <span>Message :</span>
        <textarea id="message" name="message" placeholder="Your message to us."></textarea>
    </label> 
     <label>
        <span>Subject :</span><select name="selection">
        <option value="General Question">General Question</option>
        </select>
    </label>
    <input type="hidden" name="login" value=\""""+str(login)+"""\">    
     

        <input type="submit" class="button" value="Submit">
       
</form>
                </div>
            </div>
        </div>
    </section>
"""
if form.has_key('email'):
	email = form.getvalue("email")
	message = form.getvalue("message")
	print ("<script>alert('Your email was received, thank you and have a nice day.');</script>")
	

print """

    <!-- Services Section -->
    <section id="services" class="services-section">
        <div class="container">
            <div class="row">
                <div class="col-lg-12">
                    <h1>...</h1>
                </div>
            </div>
        </div>
    </section>

    <!-- jQuery -->
    <script src="../js/jquery.js"></script>

    <!-- Bootstrap Core JavaScript -->
    <script src="../js/bootstrap.min.js"></script>

    <!-- Scrolling Nav JavaScript -->
    <script src="../js/jquery.easing.min.js"></script>
    <script src="../js/scrolling-nav.js"></script>
    <a href="index.html">here</a>

</body>

</html>



"""