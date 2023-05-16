import cv2
import pyttsx3
import speech_recognition as sr
import time
import os
import datetime
from create_dataset import create_db
from loger import log
from recogniser import recognizer
#define fundamentals
addusr=['add user','update user','add new user']
listusers=["list all users","all users","users"]
initProcess=["init",'start']
freqRate=1# rate at which images needs to be clicked
#for creating log
status = True
path = r'../images/woman.mp4'#has to be auto genrated dynamic for video
namepath='../names.txt'

def Speak(command):
    #log("speak init",status)
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
Speak("This project has been initiated!")

def dataset(name):
    try:
        dataset = open(namepath,'a')
        dataset.write(name+" ")
        log(f"noted name:{name}",status)
    except:
        log("error noting name refer line27",status)


def readDb():
    with open('../names.txt') as f:
        Speak("The users are:")
        for line in f.readlines():
            time.sleep(0.5)
            Speak(line)

def validator(myCommand,instruction):#command from user, instruction to follow its a set
    #log(f"valication init:{instruction},{myCommand}",status)
    for i in instruction:
        if(myCommand.find(i)!=-1):
            return True
    log("Validation failed",status)
    return False
#this is not a smart name identification its based on logic that name comes last in the command else this is expected to fail
def name(myCommand):
    #identifies name from user command and returns name
    name= str(myCommand.split(" ")[-1])
    log(f"identified user name: {name}",status)
    return name

def clickimg(name):
    foldername=name
    folderpath="../training/"
    log(f'database init of:{name}',status)
    ELOC= f"../training/{foldername}/"
    try:
        create_db(name=name,pathvid=path)
        return True
    except:
        return False

while(1):
    try:
        with sr.Microphone() as source2:
            r = sr.Recognizer()
            r.adjust_for_ambient_noise(source2, duration=0.2)
            #listens for the user's input
            audio2 = r.listen(source2)
            MyCommand = r.recognize_google(audio2).lower()
            log(f"Did you say:{MyCommand} ",status)
            #Speak(MyCommand)
        if (validator(MyCommand,addusr)):
            Speak('initiated add user')#implement name detection in the sentence : add user kaushik detect kaushik
            try:
                if(clickimg(name(MyCommand))):
                    log("adding name to DB: ",status)
                    dataset(name(MyCommand))
                    Speak(f"dataset created for {name(MyCommand)}!!")
                        #recognizer(vidpath='../images/woman.mp4',sourceNames='../names.txt',status=status)
                        #train_classifer(name(MyCommand),status=status) 
            except:
                Speak("error creating database")
        elif (validator(MyCommand,listusers)):
            log("Listing all users",status)
            readDb()#prints all the users added
            #speak all the names of users from cloud or local database
        elif(validator(MyCommand,initProcess)):
            log("begin recognition!",status)
            recognizer(vidpath=path,sourceNames=namepath,status=status)
        break
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        print("unknown error occurred")
# we have to activate and deactivate the voice control as it consumes lot of resources