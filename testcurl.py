import pycurl, smtplib, time, getpass
from StringIO import StringIO
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from time import strftime

def get_result(url, reported, msg):
	buffer = StringIO()
	c = pycurl.Curl()

	try:
		c.setopt(c.URL, url)
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
			body += "The web server is down for "+url+".\n"
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


username = raw_input("Enter Gmail Username (no @gmail.com after): ")
password = getpass.getpass("Enter Gmail Password: ")

#from to email to sent alert
fromEmail = username + "@gmail.com"
toEmail = "chensean.cs@gmail.com"

#prompt user for a test link
#testlink = raw_input("Enter URL to test: ");

reported = False

testlink = ["http://localhost:8080/greeting", 
"https://api.twitter.com/1.1/statuses/mentions_timeline.json"]

while True:
	
	for u in testlink:
		
		msg = MIMEMultipart()
		msg['From'] = fromEmail
		msg['To'] = toEmail
		msg['Subject'] = 'Alert! Service is Down for '+u
		
		get_result(u, reported, msg)
	
	time.sleep(60)