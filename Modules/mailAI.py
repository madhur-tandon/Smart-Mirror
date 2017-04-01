import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from speechRecAI import SpeechAI
from textToSpeechAI import speak

S = SpeechAI()
D = {'2016053':'madhur16053@iiitd.ac.in','2016242':'mandeep16242@iiitd.ac.in','2016199':'siddhant16199@iiitd.ac.in','2016057':'mudit16057@iiitd.ac.in','2016245':'mayank16245@iiitd.ac.in'}

def SendMail():
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login('smart.mirrorai@gmail.com', 'smartmirror23')
    Roll = 'default'
    while Roll not in D:
        speak("Say the Roll Number of the Recipient")
        record,audio = S.ears()
        Roll = S.recognize(record,audio)
        Roll=Roll.replace(" ","")
    Recipient = D[Roll]
    speak("Send Mail to "+Recipient+" ?")

    speak("Say The Subject")
    record,audio = S.ears()
    sub = S.recognize(record,audio)
    print("Subject : "+sub)

    speak("Say The Content")
    record,audio = S.ears()
    content = S.recognize(record,audio)
    print("Content : "+content)

    msg = MIMEMultipart()
    msg['Subject'] = sub
    msg['From'] = 'smart.mirrorai@gmail.com'
    msg['To'] = Recipient

    text = MIMEText(content)
    msg.attach(text)
    s.sendmail(msg['From'], msg['To'], msg.as_string())
    speak("Mail Sent")
    s.quit()

if __name__=="__main__":
    SendMail()
