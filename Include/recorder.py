import cv2
from datetime import datetime
from loger import log
from cloud import upload_image

def capture_picture(name,pathvid):
    dt_string = x.strftime("%H-%M-%S")
    filename =name+dt_string
    print(filename)
    destination_path = f'images/{filename}'
    path=f"../logs/events/"
    count=0
    x = datetime.now()
    # Open the default camera
    cam = cv2.VideoCapture(pathvid)
    while(True):
            ret, img = cam.read()
            cv2.imwrite(path +filename +".jpg",img)
            log(f"progress...clicking {str(count)}",status=True)
            count+=1
            upload_image(destination_path=destination_path,file_path=path+filename+".jpg")
            k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
            if k == 27:
                break
            elif count >= 1: # Take 30 face sample and stop video
                break
    cam.release()
# Call the function to capture the picture