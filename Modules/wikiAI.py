import wikipedia
from speechRecAI import SpeechAI
from subprocess import call

def word_meaning():
    S = SpeechAI()
    print("Say the Word ")
    record,audio = S.ears()
    word = S.recognize(record,audio)
    #word = 'summer'
    ny = wikipedia.page(word)
    #call(["reset"])
    print(ny.content)

if __name__=="__main__":
    word_meaning()
