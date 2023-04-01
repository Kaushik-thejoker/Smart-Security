import cv2
import pyttsx3
import speech_recognition as sr

def Speak(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
Speak("This project has been initiated!")

def clickimg(name):
    print('creating data base of:', name)
    path = r'E:\minor project\smart_security\Smart-Security\project\images\test.mp4'#has to be auto genrated
    ELOC= r'E:\minor project\smart_security\Smart-Security\project\training\{}'.format(name)
    camera = cv2.VideoCapture(path)
    for i in range(4):
        return_value, image = camera.read()
        cv2.imwrite(ELOC+str(i)+'.png', image)
    print("dataset created:",name)
    del(camera)
addusr=['add user','update user','add new user']
while(1):
    try:
        with sr.Microphone() as source2:
            r = sr.Recognizer()
            r.adjust_for_ambient_noise(source2, duration=0.2)
            #listens for the user's input
            audio2 = r.listen(source2)
            MyCommand = r.recognize_google(audio2)
            MyCommand = MyCommand.lower()
            print("Did you say ",MyCommand)
            #Speak(MyCommand)
        if MyCommand in addusr:
            Speak('initiated add user')
            clickimg('rohit')
        
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
         
    except sr.UnknownValueError:
        print("unknown error occurred")
# we have to activate and deactivate the voice control as it consumes lot of resources