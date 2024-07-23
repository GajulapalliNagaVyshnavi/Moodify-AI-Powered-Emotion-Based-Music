import re
import os
from playsound import playsound
import time
import sys
txt = input("Enter mode of expression :")
if(re.search("happy", txt)):
    listOfFiles = os.listdir("happy")
    print ("playing Happy songs")
    for i in range (0, len(listOfFiles)):
        playsound(("happy\\"+str(listOfFiles[i])))
        time.sleep(2)
elif(re.search("sad", txt)):
    listOfFiles = os.listdir("sad")
    print ("playing Sad songs")
    for i in range (0, len(listOfFiles)):
        playsound(("Sad\\"+str(listOfFiles[i])))
        time.sleep(2)
elif(re.search("angry", txt)):
    listOfFiles = os.listdir("angry")
    print ("playing Angry songs")
    for i in range (0, len(listOfFiles)):
        playsound(("angry\\"+str(listOfFiles[i])))
        time.sleep(2)
elif(re.search("surprised", txt)):
    listOfFiles = os.listdir("surprised")
    print ("playing surprised songs")
    for i in range (0, len(listOfFiles)):
        playsound(("surprised\\"+str(listOfFiles[i])))
        time.sleep(3)
elif(re.search("neutral", txt)):
    listOfFiles = os.listdir("neutral")
    print ("playing neutral songs")
    for i in range (0, len(listOfFiles)):
        playsound(("neutral\\"+str(listOfFiles[i])))
        time.sleep(2)
sys.exit()