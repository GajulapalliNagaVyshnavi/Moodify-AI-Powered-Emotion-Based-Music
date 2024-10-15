import speech_recognition as sr     # import the library
import os
import time
import re
from playsound import playsound
r = sr.Recognizer()                 # initialize recognizer
with sr.Microphone() as source:     # mention source it will be either Microphone or audio files.
    print("Speak Anything :")
    audio = r.listen(source)        # listen to the source
    text = r.recognize_google(audio)    # use recognizer to convert our audio into text part.
    print("You said : {}".format(text))
    if(re.search("happy", text)):
        listOfFiles = os.listdir("happy")
        print ("playing Happy songs")
        for i in range (0, len(listOfFiles)):
            playsound(("happy\\"+str(listOfFiles[i])))
            time.sleep(4)
    elif(re.search("sad", text)):
        listOfFiles = os.listdir("sad")
        print ("playing sad songs")
        for i in range (0, len(listOfFiles)):
            playsound(("sad\\"+str(listOfFiles[i])))
            time.sleep(3)
    elif(re.search("angry", text)):
        listOfFiles = os.listdir("angry")
        print ("playing angry songs")
        for i in range (0, len(listOfFiles)):
            playsound(("angry\\"+str(listOfFiles[i])))
            time.sleep(2)
    elif(re.search("surprised", text)):
        listOfFiles = os.listdir("surprised")
        print ("playing surprised songs")
        for i in range (0, len(listOfFiles)):
            playsound(("surprised\\"+str(listOfFiles[i])))
            time.sleep(3)
    elif(re.search("neutral", text)):
        listOfFiles = os.listdir("neutral")
        print ("playing neutral songs")
        for i in range (0, len(listOfFiles)):
            playsound(("neutral\\"+str(listOfFiles[i])))
            time.sleep(2)
