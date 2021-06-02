#!/usr/bin/env python
# coding: utf-8

# # Voice Based Email for Visually Impaired

# In[ ]:


#Import Required Liberaries

import speech_recognition as sr 
import smtplib
from bs4 import BeautifulSoup
from gtts import gTTS
import pyglet
import os, time
import imaplib
import email
from email.header import decode_header
import os


# In[ ]:


#Voice Out

def voice(tsname):
    music = pyglet.media.load(tsname, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(tsname)


# In[ ]:


#Google Speech Recognizion unable to understand audio

def google_rec():
    print("Google Speech Recognition could not understand audio.")
    ts = gTTS("Google Speech Recognition could not understand audio.", lang='en')
    tsname=("C:/Users/HP/Desktop/voicemail/error.mp3")
    ts.save(tsname)
    voice(tsname)


# In[ ]:


#Re-enter Choice

def re_enter():   
    print ("Re-Enter")
    ts = gTTS("Re-Enter" , lang='en')
    tsname=("C:/Users/HP/Desktop/voicemail/re-enter.mp3")
    ts.save(tsname)
    voice(tsname)
    


# In[ ]:


#Could not request results from Google Speech Recognition Service

def google_req():
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
    ts = gTTS("Could not request results from Google Speech Recognition service; {0}", lang='en')
    tsname=("C:/Users/HP/Desktop/voicemail/req-error.mp3")
    ts.save(tsname)
    voice(tsname)


# In[ ]:


#Project Name 

ts = gTTS(text="Voice based Email for visually impaired", lang='en')
tsname=("C:/Users/HP/Desktop/voicemail/name.mp3")
ts.save(tsname)
voice(tsname)


# In[ ]:


#login Details

login = os.getlogin
print ("You are logged In from : "+login())              
ts = gTTS(text="You are logged in from "+login(), lang='en')
tsname=("C:/Users/HP/Desktop/voicemail/login.mp3")
ts.save(tsname)
voice(tsname)


# In[ ]:


#Signin Details

text="<email_id>"
print ("You are signed in from: "+text)                             
ts = gTTS(text="You are signed in from "+text , lang='en')
tsname=("C:/Users/HP/Desktop/voicemail/usr.mp3")
ts.save(tsname)
print ("Successfully Signed in!")
voice(tsname)


# ## IMAP4_SSL

#    
# IMAP4_SSL is used to establish connection to the server.  
# **Syntax:** connection = *imaplib.IMAP4_SSL(hostname, port)*  
#     Here,  
#         **hostname:** *imap.gmail.com*  
#         **port:** *993*  
#         
# Next, open connection to the email service by use of the stored credentials.  
# **Syntax:**  *imap_object.login(username,password)*    
#     Here,  
#         **username:** *unm*   
#         **password:** *psw*  

# In[ ]:


#Logging in using IMAP4_SSL

imap = imaplib.IMAP4_SSL('imap.gmail.com',993) 
unm = ('<email_id>')                   #username
psw = ('<password>')                   #password
imap.login(unm,psw)    


# ## SMTP

# The Simple Mail Transfer Protocol (SMTP) is an internet standard communication protocol for electronic mail transmission. Mail servers and other message transfer agents use SMTP to send and receive mail messages.  
# **Syntax:** *SMTP_obj= smtplib.SMTP(hostname, port)*  
# 
# **starttls():** StartTLS is a protocol command used to inform the email server that the email client wants to upgrade from an insecure connection to a secure one.  
#   
# **ehlo():** Extended HELO (EHLO) is an Extended Simple Mail Transfer Protocol (ESMTP) command sent by an email server to identify itself when connecting to another email server to start the process of sending an email.  

# In[ ]:


#Connecting to Port 587 using SMTP

mail=smtplib.SMTP('smtp.gmail.com', 587)
mail.ehlo()
mail.starttls()
sender='<email_id>'
recipient='<recipient_email_id>'
mail.login(unm,psw)


# In[ ]:


#Function to LogOut 

def log_out():    
 
    print("Do you want to log out?")
    ts=gTTS("Do you want to log out",lang='en')
    tsname=("C:/Users/HP/Desktop/voicemail/out.mp3")
    ts.save(tsname)
    voice(tsname)

    #Voice Recognition 

    def recognize():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print ("Your choice:")
            audio=r.listen(source)
            print ("ok done!!")


        try:
            global logch
            logch=r.recognize_google(audio)
            print ("You said : "+logch)
            ts = gTTS(text="You said "+logch, lang='en')
            tsname=("C:/Users/HP/Desktop/voicemail/reply.mp3")
            ts.save(tsname)
            voice(tsname)

        except sr.UnknownValueError:
            google_rec()
            re_enter()

        except sr.RequestError as e:
            google_req()
            re_enter()
        

    recognize()
    
    if logch=="yes":
        mail.close()
        imap.logout()
    
        print("You have been logged out. Thank You!")
        ts = gTTS(text="You have been logged out Thank You ", lang='en')
        tsname=("C:/Users/HP/Desktop/voicemail/exit.mp3")
        ts.save(tsname)
        voice(tsname)
        
    elif logch=="no" :
        print ("Okay");
        initial_choice()
        
    else:
        re_enter()
        log_out()


# In[ ]:


#Function to Send Mail

def sendchoice():
    
        #Voice Recognition 

        r = sr.Recognizer()                                                                    
        with sr.Microphone() as source:
            print ("Do you want to send the mail?")
            ts = gTTS("Do you want to send the mail?", lang='en')
            tsname=("C:/Users/HP/Desktop/voicemail/send_choice.mp3")
            ts.save(tsname)
            voice(tsname)
            
            audio=r.listen(source)
            print ("ok done!!")
            
        try:
            ch=r.recognize_google(audio)
            print ("You said : "+ch)
            ts = gTTS(text="Your said "+ch, lang='en')
            tsname=("C:/Users/HP/Desktop/voicemail/msg.mp3")
            ts.save(tsname)
            voice(tsname)

            if(ch=="yes") :
                print ("Congrates! Your mail has been send. ")
                ts = gTTS(text="Congrates! Your mail has been send. ", lang='en')
                tsname=("C:/Users/HP/Desktop/voicemail/send.mp3")
                ts.save(tsname)
                voice(tsname)
        
        
            elif (ch=="no"):
                compose()
                
            else :
                re_enter()
                sendchoice()
               
           
        except sr.UnknownValueError:
            google_rec()
            re_enter()
            sendchoice()
            
            
        except sr.RequestError as e:
            google_rec()
            re_enter()
            sendchoice()


# In[ ]:


#Function to Compose Mail
    
def compose():  
    
    #Enter Subject
    
    print ("Enter your Subject: ")
    ts = gTTS("Enter your Subject: ", lang='en')
    tsname=("C:/Users/HP/Desktop/voicemail/subject.mp3")
    ts.save(tsname)
    voice(tsname)

    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio=r.listen(source)
        print ("ok done!!")

    subj=r.recognize_google(audio)
    print ("Your Subject : "+subj)
    ts = gTTS("Your Subject is: "+subj, lang='en')
    tsname=("C:/Users/HP/Desktop/voicemail/subject.mp3")
    ts.save(tsname)
    voice(tsname)

    
    r = sr.Recognizer()                                                                     
    with sr.Microphone() as source:
        
        #Enter Message
        
        print ("Enter your message: ")                            
        ts = gTTS(text="Enter your message: ", lang='en')
        tsname=("C:/Users/HP/Desktop/voicemail/msg1.mp3")
        ts.save(tsname)
        voice(tsname)
        
        audio=r.listen(source)
        print ("ok done!!")
        
    try:
        text1=r.recognize_google(audio)
        print ("You said : "+text1)
        ts = gTTS("You said : "+text1, lang='en')
        tsname=("C:/Users/HP/Desktop/voicemail/msg1.mp3")
        ts.save(tsname)
        voice(tsname)
        msg = text1
        
    except sr.UnknownValueError:
        google_rec()
        re_enter()
    except sr.RequestError as e:
        google_req()
        re_enter()
    
    
    #Connecting to Port 587 and Logging In

    mail=smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login(unm,psw)
 
    sendchoice()

    header='To:'+recipient+'\n'+'From:'+sender+'\n'+'subject:'+subj+'\n'
    msg=header+msg
    mail.sendmail(sender, recipient, msg)

    log_out() 


# In[ ]:


#Function to Input Choice from User

def choice_func():
      
    #Voice Recognition 
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print ("Your choice:")
        ts = gTTS("Your Choice:", lang='en')                             
        tsname=("C:/Users/HP/Desktop/voicemail/choice.mp3")
        ts.save(tsname)
        voice(tsname)
        
        audio=r.listen(source)
    
    try:
        
        global text
        text=r.recognize_google(audio) 
        
        
        if text=="Tu":
            text=2
            print ("You said : "+str(text))
            ts = gTTS("You said :"+str(text) , lang='en')
            tsname=("C:/Users/HP/Desktop/voicemail/choice2.mp3")
            ts.save(tsname)
            voice(tsname)
            
            switch()


        elif text=="1" :
            print ("You said : "+text)
            ts = gTTS("You said :"+text , lang='en')
            tsname=("C:/Users/HP/Desktop/voicemail/choice11.mp3")
            ts.save(tsname)
            voice(tsname)
            
            compose()


        else:
            re_enter()
            choice_func()


    except sr.UnknownValueError:
        google_rec()
        re_enter()
        choice_func()

    except sr.RequestError as e:
        google_req()
        re_enter()


# In[ ]:


#Function to provide 4 Options

def switch():

    print("Option 1 Count Total number of mails.\nOption 2 Read latest mail.\nOption 3 Read N number of UNSEEN mails.\nOption 4 Read N number of SENT mails")

    ts = gTTS(text="Option 1. Count Total number of mails.  Option 2. Read latest mail.  Option 3. Read N number of UNSEEN mails.  Option 4. Read N number of SENT mails", lang='en')
    tsname=("C:/Users/HP/Desktop/voicemail/menu.mp3")
    ts.save(tsname)
    voice(tsname)

    choice_func1()


# In[ ]:


#Function to Count Total Mails in Inbox

def count_total_mails():
    
    #Host and Port Area(SSL Security)
    
    mail = imaplib.IMAP4_SSL('imap.gmail.com',993)                                                              
    mail.login(unm,psw)                                                                   
    mail.select("inbox")
    
    print("Checking for e-mails for ",unm,".", sep='')
    
    typ, messageIDs = mail.search(None, "ALL")    #Fetching ALL Mails
    
    messageIDsString = str( messageIDs[0], encoding='utf8' ) 
    listOfSplitStrings = messageIDsString.split(" ")
                                           
    print ("Number of mails in your inbox :"+str(len(listOfSplitStrings)))
    ts = gTTS(text="Total mails are :"+str(len(listOfSplitStrings)), lang='en')                              
    tsname=("C:/Users/HP/Desktop/voicemail/total.mp3")
    ts.save(tsname)
    voice(tsname)
    


# In[ ]:


#Function to Count Total Unseen Mails 

def count_unseen_mails():


    mail = imaplib.IMAP4_SSL('imap.gmail.com',993)  
    mail.login(unm,psw)
    mail.select("inbox")


    typ, messageIDs = mail.search(None, "UNSEEN")    #Fetching Unseen Mails
    
    messageIDsString = str( messageIDs[0], encoding='utf8' ) 
    listOfSplitStrings = messageIDsString.split(" ")


    if len(listOfSplitStrings) == 0:
        print("You have no new e-mails.")


        ts = gTTS(text="You have no new e-mails.", lang='en')                              
        tsname=("C:/Users/HP/Desktop/voicemail/unseen.mp3")
        ts.save(tsname)
        voice(tsname)


    elif len(listOfSplitStrings) == 1:
        print("You have",len(listOfSplitStrings),"new e-mail.")


        ts = gTTS(text="You have one unseen email", lang='en')                             
        tsname=("C:/Users/HP/Desktop/voicemail/unseen.mp3")
        ts.save(tsname)
        voice(tsname)


    else:
        print("You have",len(listOfSplitStrings),"new e-mails.")

        ts = gTTS(text="Total unseen mails are :"+str(len(listOfSplitStrings)), lang='en')            
        tsname=("C:/Users/HP/Desktop/voicemail/unseen.mp3")
        ts.save(tsname)
        voice(tsname)
        
        log_out()


# In[ ]:


#Function to read Latest(N) Unseen Mail(s)

def n_unseen_mails():

    #Creating an IMAP Object
    
    imap = imaplib.IMAP4_SSL("imap.gmail.com")
    result = imap.login(unm, psw)
    
    #Fetching Unseen Mails from All Mais

    imap.select('"[Gmail]/All Mail"',readonly = True)
    response, messages = imap.search(None,'UnSeen')    
    messages = messages[0].split()

    try:          
        latest = int(messages[-1])    #Fetching Mails From Last
        #oldest = int(messages[0])    #Fetching Mails From Start 
    
    except IndexError:
        print("No Unseen Mails")
     

    print ("Enter the number of mails to read: ")                            
    ts = gTTS(text="Enter the number of mails to read:", lang='en')
    tsname=("C:/Users/HP/Desktop/voicemail/read.mp3")
    ts.save(tsname)
    voice(tsname)

    #Voice Recognition 
        
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio=r.listen(source)

    N=r.recognize_google(audio)
    print ("Number of mails to read are "+N)
    ts = gTTS("Number of mails to read are "+N, lang='en')
    tsname=("C:/Users/HP/Desktop/voicemail/number.mp3")
    ts.save(tsname)
    voice(tsname)

    if N=="Tu":
        N=2;


    for i in range(latest, latest-int(N), -1):
        
        #Fetching Mail Information
        
        res, msg = imap.fetch(str(i), "(RFC822)")

        for response in msg:
            if isinstance(response, tuple):

                msg = email.message_from_bytes(response[1])

  
                print(msg["Date"])
                ts = gTTS(text="Date :"+str(msg["Date"]), lang='en')
                tsname=("C:/Users/HP/Desktop/voicemail/time.mp3")
                ts.save(tsname)
                voice(tsname)


                print(msg["From"])
                ts = gTTS(text="From :"+str(msg["From"]), lang='en')
                tsname=("C:/Users/HP/Desktop/voicemail/from.mp3")
                ts.save(tsname)
                voice(tsname)


                print(msg["Subject"])
                ts = gTTS(text="Subject :"+str(msg["Subject"]), lang='en')
                tsname=("C:/Users/HP/Desktop/voicemail/subject.mp3")
                ts.save(tsname)
                voice(tsname)
                
    log_out()


# In[ ]:


#Function to read Latest(N) Sent Mail(s)

def n_sent_mails():
    
    imap = imaplib.IMAP4_SSL("imap.gmail.com")
    result = imap.login(unm, psw)

    imap.select('"[Gmail]/Sent Mail"',readonly = True)   #Fetching Sent Mails

    response, messages = imap.search(None,'ALL')
    messages = messages[0].split()

              
    latest = int(messages[-1])    #Fetching Mails From Last
    #oldest = int(messages[0])    #Fetching Mails From Start


    print ("Enter the number of sent mails to read: ")                            
    ts = gTTS(text="Enter the number of sent mails to read:", lang='en')
    tsname=("C:/Users/HP/Desktop/voicemail/read.mp3")
    ts.save(tsname)
    voice(tsname)


    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio=r.listen(source)

        N=r.recognize_google(audio)
        print ("Number of sent mails to read are "+N)
        ts = gTTS("Number of sent mails to read are "+N, lang='en')
        tsname=("C:/Users/HP/Desktop/voicemail/number.mp3")
        ts.save(tsname)
        voice(tsname)

        if N=="Tu":
            N=2;


    for i in range(latest, latest-int(N), -1):

        res, msg = imap.fetch(str(i), "(RFC822)")

        for response in msg:
            if isinstance(response, tuple):

                msg = email.message_from_bytes(response[1])

                
                print(msg["Date"])
                ts = gTTS(text="Date :"+str(msg["Date"]), lang='en')
                tsname=("C:/Users/HP/Desktop/voicemail/time.mp3")
                ts.save(tsname)
                voice(tsname)


                print(msg["To"])
                ts = gTTS(text="To :"+str(msg["To"]), lang='en')
                tsname=("C:/Users/HP/Desktop/voicemail/from.mp3")
                ts.save(tsname)
                voice(tsname)


                print(msg["Subject"])
                ts = gTTS(text="Subject :"+str(msg["Subject"]), lang='en')
                tsname=("C:/Users/HP/Desktop/voicemail/subject.mp3")
                ts.save(tsname)
                voice(tsname)

    log_out()


# In[ ]:


#Function to read Latest Mail

def search_latest():


    mail = imaplib.IMAP4_SSL('imap.gmail.com',993)                                                             
    mail.login(unm,psw)                                                                  
    stat, total = mail.select('Inbox')                  

    #Search Mails
    
    result, data = mail.uid('search',None, "ALL")
    inbox_item_list = data[0].split()
    
    new = inbox_item_list[-1]         #Fetching Mails From Last      
    #old = inbox_item_list[0]         #Fetching Mails From Start  
    
    
    #Fetching Mail Information
    
    result2, email_data = mail.uid('fetch', new, '(RFC822)')                                
    raw_email = email_data[0][1].decode("utf-8")                                            
    email_message = email.message_from_string(raw_email)

    print ("From: "+email_message['From'])
    print ("Subject: "+str(email_message['Subject']))

    stat, data1 = mail.fetch(total[0], "(UID BODY[TEXT])")
    msg = data1[0][1]
    soup = BeautifulSoup(msg, "html.parser")
    txt = soup.get_text()
    print ("Body :"+txt)

    ts = gTTS(text="From: "+email_message['From']+" .Subject: "+str(email_message['Subject'])+" .Body of the mail: "+txt, lang='en')
    tsname=("C:/Users/HP/Desktop/voicemail/body.mp3")
    ts.save(tsname)
    voice(tsname)
    
    log_out()


# In[ ]:


#Function to input Choice from User 
    
def choice_func1():   

    #Voice Recognition
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print ("Your choice:")

        ts = gTTS("Your choice ", lang='en')
        tsname=("C:/Users/HP/Desktop/voicemail/hello.mp3")
        ts.save(tsname)
        voice(tsname)

        audio=r.listen(source)


    try:

        global ch
        ch=r.recognize_google(audio)



        if ch=="Tu":
            ch=2

            print ("You said : "+str(ch))
            ts = gTTS("You said :"+str(ch) , lang='en')
            tsname=("C:/Users/HP/Desktop/voicemail/choice2a.mp3")
            ts.save(tsname)
            voice(tsname)

            search_latest()



        elif ch=="1" :
            print ("You said : "+ch)
            ts = gTTS("You said :"+ch , lang='en')
            tsname=("C:/Users/HP/Desktop/voicemail/choice1a.mp3")
            ts.save(tsname)
            voice(tsname)

            count_total_mails()
            count_unseen_mails()


        elif ch=="3" :
            print ("You said : "+ch)
            ts = gTTS("You said :"+ch , lang='en')
            tsname=("C:/Users/HP/Desktop/voicemail/choice3.mp3")
            ts.save(tsname)
            voice(tsname)

            n_unseen_mails()


        elif ch=="4" :
            print ("You said : "+ch)
            ts = gTTS("You said :"+ch , lang='en')
            tsname=("C:/Users/HP/Desktop/voicemail/choice4.mp3")
            ts.save(tsname)
            voice(tsname)

            n_sent_mails()


        else:
            re_enter()
            choice_func1()


    except sr.UnknownValueError:
        google_rec()
        re_enter()
        choice_func1()

    except sr.RequestError as e:
        google_req()
        re_enter()


# In[ ]:


#Function to input Choice from User 

def initial_choice():

    print ("1. Compose a mail.")
    ts = gTTS(text="option 1. Compose a mail.", lang='en')
    tsname=("C:/Users/HP/Desktop/voicemail/hello.mp3")
    ts.save(tsname)
    voice(tsname)

    print ("2. Check your inbox")
    ts = gTTS(text="option 2. Check your inbox", lang='en')
    tsname=("C:/Users/HP/Desktop/voicemail/hello.mp3")
    ts.save(tsname)
    voice(tsname)

    choice_func()


# In[ ]:


initial_choice()

