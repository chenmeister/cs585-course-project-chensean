import pycurl, smtplib, time, getpass
from StringIO import StringIO
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from time import strftime

#google maps, twitter, instagram, my own simple api, uber

#each url has its own thread

username = raw_input("Enter Gmail Username (no @gmail.com after): ")
password = getpass.getpass("Enter Gmail Password: ")

#from to email to sent alert
fromEmail = username + "@gmail.com"
toEmail = "chensean.cs@gmail.com"

#prompt user for a test link
testlink = raw_input("Enter URL to test: ");

msg = MIMEMultipart()
msg['From'] = fromEmail
msg['To'] = toEmail
msg['Subject'] = 'Alert! Service is Down for '+testlink

reported = False

while True:
	buffer = StringIO()
	c = pycurl.Curl()

	try:
		c.setopt(c.URL, testlink)
		c.setopt(c.WRITEDATA, buffer)
		c.perform()
		c.close()
		result = buffer.getvalue()
		print result
		reported = False
	
	except pycurl.error, error:

		if reported is False:
			reported = True
			errstr = error
			body = 'An error occured: ' + str(errstr) + '\n'
			body += "The web server is down for "+testlink+".\n"
			body += "Please check if server is on or contact your IT personel to resolve this issue.\n"
			body += "Time and Date of this issue: "+strftime("%m/%d/%Y %I:%M %p %Z")+"\n"
			
			msg.attach(MIMEText(body, 'plain'))
			#send email to user telling them that api call failed
			s = smtplib.SMTP('smtp.gmail.com:587')
			s.starttls()
			s.login(username, password)
			text = msg.as_string()
			s.sendmail(fromEmail, toEmail, text)
			s.quit()			
			print body

	time.sleep(60)