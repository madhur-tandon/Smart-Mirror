from PyDictionary import PyDictionary
from subprocess import call
import speechRecAI
from textToSpeechAI import speak

def meaning():
    # S = speechRecAI.SpeechAI()
    dictionary=PyDictionary()
    # speak("Say the Word ")
    # record,audio = S.ears()
    # word = S.recognize(record,audio)
    word = input()
    d = dictionary.meaning(word)
    print()
    print()
    call(["reset"])
    for i in d:
        print(i)
        for j in d[i]:
            print(j)
        print()
if __name__=="__main__":
    meaning()
