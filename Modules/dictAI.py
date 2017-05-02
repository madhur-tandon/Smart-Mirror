from PyDictionary import PyDictionary
from mirror import respond

def meaning(phrase):
    try:
        index = phrase.rfind(" ")
        word = phrase[index+1:]
        print(word)

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

    except Exception as e:
        respond("I'm Sorry, I couldn't understand what you meant by that")
