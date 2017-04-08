import requests
import json
import time
import random
from textToSpeechAI import speak
from speechRecAI import SpeechAI
import faceAI
import time
import weatherAI
import newsAI
import mapsAI
import traceback
import languageAI
from server import sendToClient, sendJSON

wit_token = "Bearer A5YKQ3WVJPMYBDUA655USHMZ3HHJ4ZQE"
launchPhrases = ["ok mirror","ok a mirror","okay mirror","okey mirror","ok mera","okay mera","uk mirror"]
useLaunchPhrase = False
myName = "Master"

def respond(toSpeak, toSend = False):
    if not toSend && not toSpeak:
        return
    elif not toSend:
        toSend = toSpeak

    if toSpeak:
        speak(toSpeak)

    if (isinstance(toSend), str):
        sendToClient(toSend)
    else:
        sendJSON(toSend)

class mirror(object):
    def __init__(self):
        self.speech = SpeechAI(0.30)
        self.face = faceAI.faceAI(camera=0)
        self.weather = weatherAI.weather()
        self.news = newsAI.news()
        self.maps = mapsAI.maps()
        self.lang = languageAI.naturalLanguageAI(myName)
        self.activeMode = False
        self.passivePoll = {
            "headlines": {
                "refresh": 60*60, #60 minutes
                "lastDone": 0
            },
            "quotes": {
                "refresh": 3*60,
                "lastDone": 0
            },
            "weather": {
                "refresh": 5*60*60,
                "lastDone": 0
            },
            "mess-meal": {
                "refresh": 3*60,
                "lastDone": 0
            }
        }

        # info of song will be sent by its thread
    def initialize(self):
        inertia = 0 # inertia for moving from active mode to passive mode
        respond(
            False, 
            {
                "type": "command",
                "command": "passive-mode"
            }
        )
        while True:
            #sendToClient("")    # Clear Screen

            if not self.activeMode:
                pass

            # inertia logic
            if inertia <= 0 and self.activeMode:
                respond(
                    False, 
                    {
                        "type": "command",
                        "command": "passive-mode"
                    }
                )
                self.activeMode = False

            if self.face.detect_face():
                inertia = 20
                print("Found Face")
                self.activeMode = True
                respond(
                    "Hi " + random.choice(["pretty", "beautiful", "sexy", "cutie", "handsome", "lovely"]),
                    {
                        "type": "command",
                        "command": "active-mode"
                    }
                )
                if useLaunchPhrase:
                    record,audio = self.speech.ears()
                    speech = self.speech.recognize(record,audio)
                    if speech is not None and speech.lower() in launchPhrases:
                        ack = self.lang.acknowledge()
                        respond(ack)
                        self.action()
                else:
                    self.action()

    def action(self):
        record, audio = self.speech.ears()
        speech = self.speech.recognize(record,audio)

        if speech is not None:
            try:
                r = requests.get('https://api.wit.ai/message?v=20170303&q=%s' % speech,
                                         headers={"Authorization": wit_token})
                print(r.text)
                response = json.loads(r.text)
                entities = None

                if 'entities' in response:
                    entities = response['entities']

                print(entities)

                """
                Takes action based on this intent
                Only maps, news, weather as of now
                """

                if "maps" in entities:
                    self.findMaps(entities)
                elif "news" in entities:
                    self.findNews(entities)
                elif "weather" in entities:
                    self.findWeather(entities)
                elif "userStatus" in entities:
                    self.userStatus(entities)
                elif "interaction" in entities:
                    self.interaction(entities)
                else:
                    respond("I'm Sorry, I couldn't understand what you meant by that")

            except Exception as e:
                print(e)
                traceback.print_exc()
                respond("I'm Sorry, I couldn't understand what you meant by that")
                return

            self.action()

    def findMaps(self,entities=None):
        if entities is not None:
            maxConf = 0
            intent = entities['maps'][0]["value"]
            location = entities['location'][0]["value"]
            for i in entities['location']:
                if i["confidence"] > maxConf:
                    maxConf = i["confidence"]
                    location = i["value"]
            print(intent)
            print(location)

            if location is not None and intent is not None:
                LJ = self.maps.getLocation(location) #@madhur why is LJ needed here?
                respond("Here is a map of " + location, {"type": "image", "src": self.maps.findMap(intent,location)})
            else:
                respond("I'm Sorry, I couldn't retrieve maps at the moment")
        else:
            respond("I'm Sorry, I couldn't understand what you meant by that")

    def findNews(self,entities=None):
        apiObject = {"type": "news"}
        if entities is not None:
            intent = entities['news'][0]["value"]
            print(intent)
            if intent is not None:
                newsList = self.news.findNews(intent)
                respond(", ".join(map(lambda x: x["title"], newsList)), {"type": "news", "items": newsList})
            else:
                respond("I'm Sorry, I couldn't retrieve news at the moment")
        else:
            respond("I'm Sorry, I couldn't understand what you meant by that")

    def findWeather(self,entities=None):
        if entities is not None:
            if "location" in entities:
                intent = entities['weather'][0]["value"]
                maxConf = 0
                location = entities['location'][0]["value"]
                for i in entities['location']:
                    if i["confidence"] > maxConf:
                        maxConf = i["confidence"]
                        location = i["value"]
                print(intent)
                print(location)
                if location is not None:
                    LJ = self.weather.get_DifferentLocation(location)
                    self.weather.findWeather(intent,LJ)
                else:
                    respond("I'm Sorry, I couldn't retrieve weather info at the moment")
            else:
                intent = entities['weather'][0]["value"]
                print(intent)
                LJ = self.weather.getLocation()
                self.weather.findWeather(intent,LJ)
        else:
            respond("I'm Sorry, I couldn't understand what you meant by that")

    def userStatus(self,entities=None):
        property = None
        if entities is not None:
            property = entities['userStatus'][0]['value']
        i = random.randint(0,2)
        category = "neutral"
        if i == 0:
            category = "positive"
        elif i==1:
            category = "negative"
        else:
            category = "neutral"
        phrase = self.lang.user_compliment(category,property)
        respond(phrase)

    def interaction(self,entities=None):
        property = None
        if entities is not None:
            property = entities['interaction'][0]['value']
        phrase = self.lang.interaction(property)
        respond(phrase)


if __name__ == "__main__":
    M = mirror()
    M.initialize()
