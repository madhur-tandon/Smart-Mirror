import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import speechRecAI
from textToSpeechAI import speak
import time
from cv2 import *

S = speechRecAI.SpeechAI(0.55)
D = {'2016053':'madhur16053@iiitd.ac.in','2016242':'mandeep16242@iiitd.ac.in','2016199':'siddhant16199@iiitd.ac.in','2016245':'mayank16245@iiitd.ac.in', '2016151':'harshit16151@iiitd.ac.in', '2016057':'mudit16057@iiitd.ac.in'}

def SendMail(ImgFileName,theft=False):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login('smart.mirrorai@gmail.com', 'smartmirror23')
    if theft == False:
        Roll = 'default'
        while Roll not in D:
            speak("Say your Roll Number")
            record,audio = S.ears()
            Roll = S.recognize(record,audio)
            Roll=Roll.replace(" ","")
        Recipient = D[Roll]

        msg = MIMEMultipart()
        msg['Subject'] = 'Your Sexy Picture!'
        msg['From'] = 'smart.mirrorai@gmail.com'
        msg['To'] = Recipient

        text = MIMEText('Hi Sexy!')
        msg.attach(text)
        if ImgFileName!=None:
            img_data = open(ImgFileName, 'rb').read()
            image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
            msg.attach(image)
            s.sendmail(msg['From'], msg['To'], msg.as_string())
        else:
            s.sendmail(msg['From'], msg['To'], msg.as_string())
        print("Mail Sent")
        s.quit()
    else:
        msg = MIMEMultipart()
        msg['Subject'] = 'Thief at Home!'
        msg['From'] = 'smart.mirrorai@gmail.com'
        msg['To'] = 'madhur16053@iiitd.ac.in'

        text = MIMEText('Please be alert and call Police')
        msg.attach(text)
        if ImgFileName!=None:
            img_data = open(ImgFileName, 'rb').read()
            image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
            msg.attach(image)
            s.sendmail(msg['From'], msg['To'], msg.as_string())
        else:
            s.sendmail(msg['From'], msg['To'], msg.as_string())
        print("Mail Sent")
        s.quit()
		
def getImageName():
    base = "../client/selfies/"
	try:
		file = open(base + "counter.txt", "r+")
        counter = int(file.readline())
        counter += 1
        file.seek(0)
        file.write(str(counter))
        file.truncate()
        file.close()
    except FileNotFoundError:
        file = open(base + "counter.txt", "w+")
        file.write("0")
        file.close()
        counter = 0
    return base + counter + ".jpg" # like 1.jpg, etc


def capture(theft=False):
    if theft == False:
        for i in range(3,0,-1):
            speak(str(i))
        speak("Cheese!")
        time.sleep(0.5)
        cam = VideoCapture(0)
        # cam = VideoCapture(0)
        s, img = cam.read()
        if s:
            namedWindow("cam-test")
            imshow("cam-test",img)
            waitKey(5000)
            destroyWindow("cam-test")
            imwrite(getImageName(),img)
    else:
        cam = VideoCapture(0)
        s, img = cam.read()
        if s:
            namedWindow("cam-test")
            imshow("cam-test",img)
            destroyWindow("cam-test")
            imwrite(getImageName(),img)

if __name__=="__main__":
    capture()
    SendMail('filename.jpg')
 