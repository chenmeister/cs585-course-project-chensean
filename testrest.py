import requests, smtplib, time, getpass, twitter
import signal, sys
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from time import strftime
from requests_oauthlib import OAuth1


#api keys needed to run the applications
#please do not misuse them
inst_keys = {'client_secret': '329a3d6c2d544e929c64b0ab4adf3c18',
						 'client_id': '446407160f25466584b2a90fe3854f77'}
							 
twit_keys = {'request_token_url': 'https://api.twitter.com/oauth/request_token',
						 'authorize_url': 'https://api.twitter.com/oauth/authorize?oauth_token=',
						 'access_token_url': 'https://api.twitter.com/oauth/access_token',
						 'consumer_key': 'NjYhIoDkXJDlmJCZsxslZzLCU',
						 'consumer_secret': 'DHF71EdxwxwbF8NvEpIndYaYTKNqrVI8i1J3L5Vmf5QHddRCIT',
						 'oauth_token': '794116050-7444OWkH8mnTJ16Oxq3lB87H9v32C0NNObeSlYhV',
						 'oauth_secret_token': 'hCh4EyndipcEVLvZxPtjIk2wuZCx1gak4DNUtZmax6afH'}

instacred = "?client_secret="+inst_keys['client_secret']+"&client_id="+inst_keys['client_id']

def get_oauth_twitter():
	oauth = OAuth1(twit_keys['consumer_key'],
							client_secret=twit_keys['consumer_secret'],
							resource_owner_key=twit_keys['oauth_token'],
							resource_owner_secret=twit_keys['oauth_secret_token'])
	return oauth

#function that runs and returns the curl calls
def get_result(url, reported, msg, api, type):
	try:
		if type is "GET":
			if api is "twitter":
				print "Twitter Result:\n"
				oauthtwitter = get_oauth_twitter()
				r = requests.get(url=url, auth=oauthtwitter)
			elif api is "instagram":
				print "Instagram Result:\n"
				r = requests.get(url+instacred)
			else:
				print "Result:\n"
				r = requests.get(url)
			print r.text
			
		elif type is "POST":
			if api is "twitter":
				oauthtwitter = get_oauth_twitter()
				r = requests.post(url=url, auth=oauthtwitter)
			elif api is "instagram":
				r = requests.post(url+instacred)
			else:
				r = requests.post(url)
			print r.text
		
		elif type is "PUT":
			if api is "twitter":
				oauthtwitter = get_oauth_twitter()
				r = requests.put(url=url, auth=oauthtwitter)
			elif api is "instagram":
				r = requests.put(url+instacred)
			else:
				r = requests.put(url)
			print r.text
			
		elif type is "DELETE":
			if api is "twitter":
				oauthtwitter = get_oauth_twitter()
				r = requests.delete(url=url, auth=oauthtwitter)
			elif api is "instagram":
				r = requests.delete(url+instacred)
			else:
				r = requests.delete(url)	
			print r.text

		else:
			print "not a valid HTTP call"
		
		reported = False

	except requests.exceptions.RequestException, error:
		
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
	testlink = [{"url":"http://localhost:8080/greeting","api":"other","type":"GET"}, 
	{"url":"https://api.twitter.com/1.1/statuses/user_timeline.json","api":"twitter","type":"GET"},
	{"url":"https://api.instagram.com/v1/media/popular","api":"instagram","type":"GET"}]
	
	while True:
		for u in testlink:
			msg = MIMEMultipart()
			msg['From'] = fromEmail
			msg['To'] = toEmail
			msg['Subject'] = 'Alert! Service is Down for '+u["url"]
		
			get_result(u["url"], reported, msg, u["api"], u["type"])
	
		time.sleep(60)