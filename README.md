# Voice-Mail-for-Blind

<img src="https://user-images.githubusercontent.com/54893688/120467228-928ecf00-c3bd-11eb-9efa-24858b488b90.png" border="0" width="260" height="280" /></p>

Open-Source Voice Based Emailing System for Visually Impaired.

## About
An efficient input method for visually impared inividuals is dictation using speech recognition.
However, dictation systems follows a speech interaction model. [This project](https://github.com/KhushiiKumar/Voice-Mail-for-Blind/blob/main/Voice%20Mail%20For%20Blind%20.ipynb) is a python-based application for visually impaired persons using speech to text voice response, 
thus enabling everyone to control their mail accounts using their voice only and to be able to read,send, and perform all the other useful tasks.   
This system will prompt the user with voice commands to perform certain action and the user will respond to the same. 
The main benefit of this system is that the use of mouse is completely eliminated, the user will have to respond through voice only.

## Features
1. [Compose and Send Mail](https://github.com/KhushiiKumar/Voice-Mail-for-Blind/blob/main/Send%20and%20Compose%20Mail.ipynb)
2. [Count Total Mails](https://github.com/KhushiiKumar/Voice-Mail-for-Blind/blob/main/Count%20Total%20Mails.ipynb)
3. [Count Unseen Mails](https://github.com/KhushiiKumar/Voice-Mail-for-Blind/blob/main/Count%20Unseen%20Mails.ipynb)
4. [Read Latest Mail](https://github.com/KhushiiKumar/Voice-Mail-for-Blind/blob/main/Read%20Latest%20Mail.ipynb)
5. [Read Unseen Mails](https://github.com/KhushiiKumar/Voice-Mail-for-Blind/blob/main/Read%20Unseen%20Mails.ipynb)
6. [Read Send Mails](https://github.com/KhushiiKumar/Voice-Mail-for-Blind/blob/main/Read%20Send%20Mails.ipynb)

## Windows Installation

#### Installation with Python3
```
C:\User\khushi>git clone https://github.com/KhushiiKumar/Voice-Mail-for-Blind.git

C:\User\khushi>cd Voice-Mail-for-Blind.py

C:\User\khushi>python3 -m pip install -r requirements.txt

C:\User\khushi>python3 Voice-Mail-for-Blind.py
```

## Needed Imports


- ###  speech_recognition
    Library for performing speech recognition, with support for several engines and APIs, online and offline.

    #### Python Installation
    `pip install SpeechRecognition`

    #### Conda run Installation
    `conda install -c conda-forge speechrecognition`



- ### smtplib
    The smtplib module defines an SMTP client session object that can be used to send mail to any Internet machine with an SMTP or ESMTP listener daemon.

    #### Python Installation  
    `pip install smtplib`

    #### Conda run Installation  
    `conda install -c conda-forge aiosmtplib`



- ### BeautifulSoup
    Beautiful Soup is a Python library for pulling data out of HTML and XML files.

    #### Python Installation  
    `pip install beautifulsoup4`

    #### Conda run Installation  
    `conda install -c anaconda beautifulsoup4`



- ### gTTS
    gTTS (Google Text-to-Speech), a Python library and CLI tool to interface with Google Translate's text-to-speech API.

    #### Python Installation  
    `pip install pyglet`

    #### Conda run Installation  
    `conda install -c tdido gtts-token`



- ### pyglet
    pyglet is a cross-platform windowing and multimedia library for Python.It supports windowing, user interface event handling, loading images, videos, playing sounds and music.

    #### Python Installation  
    `pip install pyglet`

    #### Conda run Installation  
    `conda install -c conda-forge pyglet`



- ### imaplib
    Imaplib is used for accessing emails over imap protocol. IMAP stands for Internet Mail Access Protocol.

    #### Python Installation  
    `pip install python-imap`

    #### Conda run Installation    
    `conda install -c conda-forge imapclient`



## Modification
- Add your desktop directory in the code where I have used file paths in several lines, like: C:/Users/HP/Desktop/folder/file.mp3 (this is my desktop directory). 
- If you don't know your desktop directory then just open terminal or command prompt and paste the below code. 

    `%userprofile%\Desktop`  

- Paste your email id in line 134, 104 and 156 and password in line 135.  
- Paste recipient email id in line 157.

- Allow the less secure apps: ON  


## Usage  
python3 Voice-Mail-for-Blind.py
