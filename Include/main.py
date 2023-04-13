import cv2
import pyttsx3
import speech_recognition as sr
import time
import os
import datetime

#define fundamentals
addusr=['add user','update user','add new user']
listusers=["list all users","all users","users"]
freqRate=1# rate at which images needs to be clicked
#for creating log
status = False
def log(data,status):
    x = datetime.datetime.now()
    runlog= open('../logs/runtime.txt',"a")
    runlog.write(data+"-----"+str(x)+"\n")
    runlog.close()
    if status==True:
        print(data)
def Speak(command):
    #log("speak init",status)
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
Speak("This project has been initiated!")

def dataset(name):
    dataset = open('../names.txt','a')
    dataset.write(name+"\n")
    log(f"noted name:{name}",status)

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
    num_imgs=0
    new_img=None
    detector = cv2.CascadeClassifier("../training/haarcascade_frontalface_default.xml")
    foldername=name
    folderpath="../training/"
    log(f'database init of:{name}',status)
    path = r'../images/database.mp4'#has to be auto genrated dynamic replace me with 0
    ELOC= f"../training/{foldername}/{name}"
    if not os.path.exists(folderpath+foldername):
         os.mkdir(folderpath+foldername)
    try:
        while True:
            camera = cv2.VideoCapture(path)
            return_value, image = camera.read()
            new_img = None
            grayimg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            face = detector.detectMultiScale(image=grayimg, scaleFactor=1.2, minNeighbors=5)
            for x,y,w,h in face:
                print(x,y,w,h)
                log("Face detected",status)
                new_img = image[y:y+h, x:x+w]
            key = cv2.waitKey(1) & 0xFF
            try:
                cv2.imwrite(ELOC+str(num_imgs)+'.png',new_img)
                num_imgs+=1
                time.sleep(1)
            except:
                log(f"Recording failed: {name}",status)
            if key ==ord("q") or num_imgs>5:
                break
    except:
        log(f"Error in creating DB of {name}",status)
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
                dataset(name(MyCommand))
                #break and init face training and recognision 
            except:
                Speak("error creating database")
            break
        elif (validator(MyCommand,listusers)):
            log("Listing all users",status)
            readDb()#prints all the users added
            #speak all the names of users from cloud or local database
        break
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        print("unknown error occurred")
# we have to activate and deactivate the voice control as it consumes lot of resources