import speech_recognition as speechAI

class SpeechAI(object):
    def __init__(self,threshold=0.30,phrase="hello"):
        self.phrase = phrase
        self.threshold = threshold

    def recognize(self,recognize,audio):
        spoken = None
        transcript=""
        try:
            min_conf = 1
            spoken = recognize.recognize_google(audio,key="AIzaSyAcalCzUvPmmJ7CZBFOEWx2Z1ZSn4Vs1gg",language = "en-IN",show_all=True)
            print(spoken)
            if spoken != []:
                for i in spoken['alternative']:
                    if i['confidence']<=min_conf and i['confidence']>=self.threshold:
                        min_conf = i['confidence']
                for i in spoken['alternative']:
                    if i['confidence']==min_conf:
                        transcript = i['transcript']
                        print("YOU SAID "+i['transcript'])
                        break
            else:
                print("Couldn't Understand")
        except speechAI.UnknownValueError:
            print("Couldn't Understand")
        except speechAI.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return transcript

    def ears(self):
        micro_source = speechAI.Microphone()
        record = speechAI.Recognizer()
        with micro_source as source:
            record.adjust_for_ambient_noise(source,duration=1)
            record.dynamic_energy_threshold = True
            print("I am all Ears!")
            audio = record.listen(source)
        return record,audio

if __name__=="__main__":
    S = SpeechAI(0.30,"okay mirror")
    record,audio = S.ears()
    x = S.recognize(record,audio)
    if x==S.phrase:
        while True:
                record,audio = S.ears()
                S.recognize(record,audio)
    else:
        print("Say The Launching Phrase")
