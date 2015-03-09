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
5. When it prompts Enter URL, enter the api url you want to test
6. The program will run in a loop and check for the API status
7. If server is not down, the api will return a result
8. If server is down, it will send alert email notifying the user the API is down
9. Script will check the url continuously every 60 seconds
10. To exit the app Ctrl-C

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