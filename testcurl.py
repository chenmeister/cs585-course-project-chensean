import pycurl, smtplib, time, getpass, twitter
from StringIO import StringIO
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from time import strftime
from requests_oauthlib import OAuth1

#function that runs and returns the curl calls
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

if __name__ == '__main__':
	#asks user for gmail account
	username = raw_input("Enter Gmail Username (no @gmail.com after): ")
	password = getpass.getpass("Enter Gmail Password: ")

	#from to email to sent alert
	fromEmail = username + "@gmail.com"
	toEmail = "chensean.cs@gmail.com"

	#set email report to false
	reported = False

	testlink = raw_input("Enter HTTP Call: ")
		
	while True:
	
		msg = MIMEMultipart()
		msg['From'] = fromEmail
		msg['To'] = toEmail
		msg['Subject'] = 'Alert! Service is Down for '+testlink
		
		get_result(testlink, reported, msg)
			
		time.sleep(60)