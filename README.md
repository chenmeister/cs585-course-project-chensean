# cs585-course-project-chensean

## Testing Only One HTTP URL at a time 

To run the python script testcurl.py

1. Type python testcurl.py onto the command line
2. When it prompts Enter Gmail Username, only enter username without @gmail.com
3. When it prompts Enter Gmail Password, enter your gmail password
4. When it prompts Enter URL, enter the api url you want to test
5. The program will run in a loop and check for the API status
6. If server is not down, the api will return a result
7. If server is down, it will send alert email notifying the user the API is down
8. Script will check the url continously every 60 seconds
9. To exit the app Ctrl-C

## Testing Multiple HTTP ReST urls (Twitter and Instagram GET calls included)

To run the python script testrest.py

1. Type python testrest.py onto the command line
2. When it prompts Enter Gmail Username, only enter username without @gmail.com
3. When it prompts Enter Gmail Password, enter your gmail password
4. The program will run in a loop and check for the API status
5. If server is not down, the api will return a result
6. If server is down, it will send alert email notifying the user the API is down
7. Script will check the urls continously every 60 seconds
8. To exit the app Ctrl-C