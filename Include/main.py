import cv2
import pyttsx3
import speech_recognition as sr
import time
import os

#define fundamentals
addusr=['add user','update user','add new user']
freqRate=1# rate at which images needs to be clicked
#for creating log
status = True
def log(data,status):
    if status==True:
        print(data)
def Speak(command):
    #log("speak init",status)
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
Speak("This project has been initiated!")

def validator(myCommand,instruction):#command from user, instruction to follow its a set
    #log(f"valication init:{instruction},{myCommand}",status)
    flag =0
    for i in instruction:
        if(myCommand.find(i)!=-1):
            log("validated",status)
            flag =1
    if flag ==1:
        return True
    else:
        Speak("validation failed")
        return False
#this is not a smart name identification its based on logic that name comes last in the command else this is expected to fail
def name(myCommand):
    #identifies name from user command and returns name
    name= str(myCommand.split(" ")[-1])
    log(f"identified user name: {name}",status)
    return name

def clickimg(name):
    foldername=name+"_folder"
    folderpath="../training/"
    log(f'database init of:{name}',status)
    path = r'../images/test.mp4'#has to be auto genrated dynamic
    ELOC= f"../training/{foldername}/{name}"
    if not os.path.exists(folderpath+foldername):
         os.mkdir(folderpath+foldername)
    try:
        camera = cv2.VideoCapture(path)
        for i in range(3):
            time.sleep(freqRate)
            return_value, image = camera.read()
            cv2.imwrite(ELOC+str(i)+'.png', image)
        camera.release()
        cv2.destroyAllWindows()
    except:
        log('create database failed',status)
    del(camera)

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
                clickimg(name(MyCommand))
                #break and init face training and recognision 
            except:
                Speak("error creating database")
            break
        break
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        print("unknown error occurred")
# we have to activate and deactivate the voice control as it consumes lot of resources