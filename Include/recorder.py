import cv2
from datetime import datetime

def capture_picture(name):
    path=f"../logs/events/"
    count=0
    x = datetime.now()
    # Open the default camera
    dt_string = x.strftime("%H-%M-%S")
    cam = cv2.VideoCapture(0)
    filename =name+dt_string
    print(filename)
    while(True):
            
            ret, img = cam.read()
            #img = cv2.flip(img, -1) # flip video image vertically
            # Save the captured image into the datasets folder
            cv2.imwrite(path +filename +".jpg",img)
            print(f"progress...clicking {str(count)}")
                # cv2.imshow('image', img)
            count+=1
            k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
            if k == 27:
                break
            elif count >= 1: # Take 30 face sample and stop video
                break
    cam.release()
# Call the function to capture the picture