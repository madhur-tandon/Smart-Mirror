from PyDictionary import PyDictionary

def meaning(phrase):
    try:
        index = phrase.rfind(" ")
        word = phrase[index+1:]
        print(word)

        dictionary=PyDictionary()
        d = dictionary.meaning(word)
        print(d)
        for i in d:
            print(i)
            for j in d[i]:
                print(j)
            print()

    except Exception as e:
        print("I'm Sorry, I couldn't understand what you meant by that")
