# Voice-Mail-for-Blind

![image](https://user-images.githubusercontent.com/68503114/119977874-8cbc7680-bfd6-11eb-833d-25a6b57063ad.png)

Open-Source Voice Based Emailing System for Visually Impaired.

## About
An efficient input method for visually impared inividuals is dictation using speech recognition.
However, dictation systems follows a speech interaction model. This project is a python-based application for visually impaired persons using speech to text voice response, 
thus enabling everyone to control their mail accounts using their voice only and to be able to read,send, and perform all the other useful tasks.   
This system will prompt the user with voice commands to perform certain action and the user will respond to the same. 
The main benefit of this system is that the use of mouse is completely eliminated, the user will have to respond through voice only.

## Features
1. Compose and Send email.
2. Count Total number of mails.
3. Count number of unseen emails.
4. Read latest mail.
5. Fetch unseen emails.
6. Fetch sent emails.

## Windows Installation

#### Installation with Python3
```
C:\User\khushi>git clone 

C:\User\khushi>cd voice-mail-for-blind.py

C:\User\khushi>python3 -m pip install -r requirements.txt

C:\User\khushi>python3 voice-mail-for-blind.py
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
- In order to save the mp3 files in the local directory, follow the below instructions:  

- Just add your desktop directory in code where I have used path words in several lines.   
If you don't know your desktop directory then just open terminal or command prompt and paste the below code. Like: C:\Users\khushi\Desktop (this is my desktop directory).  

    `%userprofile%\Desktop`  

- Also paste your email id and password in line number 104.  

- Allow the less secure apps: ON  


## Usage  
python3 voice-mail-for-blind.py
