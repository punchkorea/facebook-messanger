# facebook-messenger
This application automates sending messages using Facebook. It needs sender user credentials, receiver user IDs, python and other dependencies mentioned in the repository.
Limitation: 60 messages per usage (due to Facebook safety regulations).


In order to use this repository, 
1. Clone into your device
```
git clone https://github.com/punchkorea/facebook-messanger
```

2. Change **message.txt** by writing your personal message to be sent.
3. Change the credentials in **utils/creds.py** (FB username and password).
4. Put the receiver URLs in **profile_urls.txt** file. (Please note that the format of profile URL has to contain User ID)
5. Open command line and go the the /Scripts folder.
```
cd C:\Users\YOUR ENVIRONMENT\Downloads\auto-dm\Scripts
```
6. Activate the program
```
activate
```
7. Go back to main folder (where the facebook_auto_dm.py file is located)
```
cd ..
```
8. Run python file.
```
python facebook_auto_dm.py
```
9. The program will start sending the messages. Do not close or click anything.
10. Done!
11. To close the application, go to /Scripts and deactivate
```
cd Scripts
deactivate
```

Please feel free to give some stars~ :sparkles:
