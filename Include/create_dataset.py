
import cv2
import os

def create_db(name,pathvid):
     cam = cv2.VideoCapture(pathvid)
     face_detector = cv2.CascadeClassifier('../training/haarcascade_frontalface_default.xml')
    # For each person, enter one numeric face id
     print("\n [INFO] Initializing face capture. Look the camera and wait ...")
    # Initialize individual sampling face count
     count = 0
     path =f'../training/users/'
     if not os.path.exists(path):
             os.mkdir(path)
             print("path created")

     while(True):
        ret, img = cam.read()
        #img = cv2.flip(img, -1) # flip video image vertically
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 5)
        
        for (x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
            count += 1
            # Save the captured image into the datasets folder
            cv2.imwrite(path +name +".jpg", gray[y:y+h,x:x+w])
            print(f"progress...clicking {str(count)}")
            # cv2.imshow('image', img)

        k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
        if k == 27:
            break
        elif count >= 1: # Take 30 face sample and stop video
            break
    # Do a bit of cleanup
     print("\n [INFO] Exiting Program and cleanup stuff")
     cam.release()
     cv2.destroyAllWindows()


