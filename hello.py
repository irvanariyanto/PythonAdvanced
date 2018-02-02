#!/usr/bin/python

import cgi

print "Content-type:text/html\r\n\r"
print "<html>"
print "<head><title>My First CGI Program</title></head>"
print "<body>"
print "<h1> Hello Program! </h1>"
form = cgi.FieldStorage()
if form.getValue("name"):
    name = form.getValue("name")
    print '<h1> Hello ' + name + '! Thanks for using my script!</h1><br />'
if form.getValue("happy"):
    print "<p>Yay! I'm happy too!</p>"
if form.getValue("sad"):
    print "<p> Oh no! Why are you sad?</p>"

print "<form method='post' action='hello.py'>"
print '</p> Name: <input typw="text" name="name" /></p>'
print '<input type="checkbox" name="happy" /> Happy'
print '<input type="chackbox" name="sad" /> Sad'
print '<input type="submit" value="Submit" />'
print "</form>"
print "</body>"
print "</html"
