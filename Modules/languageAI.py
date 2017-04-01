import random
import datetime

class naturalLanguageAI(object):
    def __init__(self,userName=None):
        if userName is None:
            self.userName = ""
        else:
            self.userName = userName
        random.seed(datetime.datetime.now())

    def timeOfDay(self,date):
        phrase = ""

        if date.hour < 11:
            phrase = "morning"
        elif (date.hour >= 11) and (date.hour < 18):
            phrase = "afternoon"
        elif date.hour >= 18:
            phrase = "evening"

        return phrase

    def acknowledge(self):

        personal = [
            "What can I do for you, %s" % self.userName,
            "How can I help you today, %s" % self.userName,
            "Hi %s, what can I do for you?" % self.userName,
            "Hey %s, what can I do for you?" % self.userName,
            "How can I help you, %s" % self.userName
        ]

        simple = [
            "Yes ?",
            "What can I Do for you ?",
            "How can I help you today ?"
        ]

        selection = -1

        if len(self.userName) > 0:
            selection = random.randint(0,2)
        else:
            selection = random.randint(0,1)

        phrase = ""

        if selection == 0:
            phrase = random.choice(simple)
        elif selection == 1:
            phrase = "Good %s, What can I do for you?" % self.timeOfDay(datetime.datetime.now())
        else:
            phrase = random.choice(personal)

        return phrase

    def user_compliment(self,category="positive",property=None):
        phrase=""

        positive = [
            "good",
            "nice",
            "great",
            "fresh",
            "beautiful",
            "perfect",
            "cool"
        ]

        negative = [
            "bad",
            "terrible"
        ]

        neutral = [
            "okay",
            "alright"
        ]

        selection = positive
        if category == 'negative':
            selection = negative
        elif category == 'neutral':
            selection = neutral

        if property == "general":
            phrase = "You look %s" %(random.choice(selection))
        elif property == "clothes":
            verb = "look"
            item = random.choice(["clothes","outfit"])
            if item == "outfit":
                verb = verb + "s"
            phrase = "Your %s %s %s" %(item,verb,random.choice(selection))
        elif property == "hair":
            item = random.choice(["hair","hairstyle","up do"])
            phrase = "Your %s looks %s" %(item,random.choice(selection))
        return phrase
