import pycurl, smtplib, time, getpass, twitter
import signal, sys
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

def exit_gracefully(signum, frame):
    # restore the original signal handler as otherwise evil things will happen
    # in raw_input when CTRL+C is pressed, and our signal handler is not re-entrant
    signal.signal(signal.SIGINT, original_sigint)

    try:
        if raw_input("\nReally quit? (y/n)> ").lower().startswith('y'):
            sys.exit(1)

    except KeyboardInterrupt:
        print("Ok ok, quitting")
        sys.exit(1)

    # restore the exit gracefully handler here    
    signal.signal(signal.SIGINT, exit_gracefully)

if __name__ == '__main__':
	
	# store the original SIGINT handler
	original_sigint = signal.getsignal(signal.SIGINT)
	signal.signal(signal.SIGINT, exit_gracefully)
	
	#asks user for gmail account
	username = raw_input("Enter Gmail Username (no @gmail.com after): ")
	password = getpass.getpass("Enter Gmail Password: ")

	#from to email to sent alert
	fromEmail = username + "@gmail.com"
	toEmail = "chensean.cs@gmail.com"

	#set email report to false
	reported = False

	#Get the links of the URL's to Test	
	getLinks = [line.strip() for line in open('testurls.txt')]

	#keeps the link running and checks the URL's periodically		
	while True:
		for link in getLinks:
			msg = MIMEMultipart()
			msg['From'] = fromEmail
			msg['To'] = toEmail
			msg['Subject'] = 'Alert! Service is Down for '+link
			get_result(link, reported, msg)
		time.sleep(60)