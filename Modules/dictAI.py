from PyDictionary import PyDictionary
# from subprocess import call
import speechRecAI
from textToSpeechAI import speak

from mirror import respond

def meaning(word):
    dictionary=PyDictionary()
    d = dictionary.meaning(word)
    toRespond = []
    for i in d:
        toRespond.append({
            "type": i,
            "meanings": []
        })

        for j in d[i]:
            toRespond[-1]["meanings"].append(j)

    respond(word, {
        "type": "dictionary",
        "word": word,
        "meanings": toRespond
    })

if __name__=="__main__":
    meaning("silent")
