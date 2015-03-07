import pycurl
import smtplib
from StringIO import StringIO
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from time import strftime

#decibel, twitter, instagram, my own simple api, uber, google
#each api has its own thread
#test runs every 15 minutes (to prevent overload)
#have a script that runs the 

buffer = StringIO()
c = pycurl.Curl()

fromEmail = "cs585finalprojectsc@gmail.com"

#enter email to send alert to
toEmail = raw_input("Enter your email: ")

#username = "cs585finalprojectsc"
#password = "restalert585"

#prompt user for a test link
testlink = raw_input("Enter URL to test: ");

msg = MIMEMultipart()
msg['From'] = fromEmail
msg['To'] = toEmail
msg['Subject'] = 'Alert! Service is Down for '+testlink

body = "The web server is down for "+testlink+", Please check if server is on or fix the issue\n"
body += "Time and Date of this issue: "+strftime("%m/%d/%Y %I:%M %p %Z")+"\n"
msg.attach(MIMEText(body, 'plain'))

c.setopt(c.URL, testlink)
c.setopt(c.WRITEDATA, buffer)

try:
	c.perform()
	c.close()
	result = buffer.getvalue()
	print result
	
except pycurl.error, error:
	#send email to user telling them that api call failed
	#s = smtplib.SMTP('smtp.gmail.com:587')
	#s.starttls()
	#s.login(username, password)
	#text = msg.as_string()
	#s.sendmail(fromEmail, toEmail, text)
	#s.quit()
	print body
	errno, errstr = error
	print 'An error occured: ',errstr