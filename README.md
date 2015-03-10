# cs585-course-project-chensean

## To run the RESTService example

1. cd into the directory RESTService
2. type mvn spring-boot:run to start the server


## Testing Only One HTTP URL at a time 

###To run the python script testcurl.py

1. Add/Remove urls to test in the testurls.txt files
2. Type python testcurl.py onto the command line
3. When it prompts Enter Gmail Username, only enter username without @gmail.com
4. When it prompts Enter Gmail Password, enter your gmail password
5. The program will run in a loop and check for the API status
6. If server is not down, the api will return a result
7. If server is down, it will send alert email notifying the user the API is down
8. Script will check the url continuously every 60 seconds
9. To exit the app Ctrl-C

## Testing Multiple HTTP ReST urls (Twitter and Instagram GET calls included)

###To run the python script testrest.py

1. Type python testrest.py onto the command line
2. When it prompts Enter Gmail Username, only enter username without @gmail.com
3. When it prompts Enter Gmail Password, enter your gmail password
4. The program will run in a loop and check for the API status
5. If server is not down, the api will return a result
6. If server is down, it will send alert email notifying the user the API is down
7. Script will check the urls continously every 60 seconds
8. To exit the app Ctrl-C

##Source Credits
http://thomassileo.com/blog/2013/01/25/using-twitter-rest-api-v1-dot-1-with-python/

http://docs.python-requests.org/en/latest/user/quickstart/

https://shkspr.mobi/blog/2014/04/wanted-simple-apis-without-authentication/

http://stackoverflow.com/questions/18114560/python-catch-ctrl-c-command-prompt-really-want-to-quit-y-n-resume-executi
