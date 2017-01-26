import speech_recognition as speechAI

class SpeechAI(object):
    def __init__(self,phrase="hello"):
        self.phrase = phrase;

    def recognize(self,recognize,audio):
        spoken = None
        try:
            spoken = recognize.recognize_google(audio)
            print("YOU SAID "+spoken)
        except speechAI.UnknownValueError:
            print("Couldn't Understand")
        return spoken

    def ears(self):
        micro_source = speechAI.Microphone()
        record = speechAI.Recognizer()
        with micro_source as source:
            record.adjust_for_ambient_noise(source)
            print("I am all Ears!")
            audio = record.listen(source)
        return record,audio

if __name__=="__main__":
    S = SpeechAI("ok mirror")
    record,audio = S.ears()
    x = S.recognize(record,audio)
    if x==S.phrase:
        while True:
                record,audio = S.ears()
                S.recognize(record,audio)
    else:
        print("Say The Launching Phrase")
