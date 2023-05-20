import face_recognition
import cv2
import numpy as np
import csv
import os
from datetime import datetime
from loger import log
from recorder import capture_picture
def recognizer(vidpath,sourceNames,status):

    #captures video 
    video_capture = cv2.VideoCapture(vidpath)
    #list of encoders
    known_face_encoding = []
    #opens list of saved peoples names
    with open(sourceNames) as f:
        contents = f.readlines()[0].split(" ")
    for i in range(len(contents)-1):
        var_img=contents[i]+"_img"
        var_encoding=contents[i]+"_encoding"
        try:
            var_img =face_recognition.load_image_file(f"../training/users/{contents[i]}.jpg") #test it
            var_encoding=face_recognition.face_encodings(var_img)[0]
            known_face_encoding.append(var_encoding)
            log(f"{var_encoding},{var_img}",status=status)
        except:
            log("Error recogniser file line 22",status=status)
    #makes a list of all known names
    known_faces_names = contents
    students = known_faces_names.copy() 
    face_locations = []
    face_encodings = []
    face_names = []
    s=True
    
    now = datetime.now()
    current_date = now.strftime("%Y-%m-%d")
    log(current_date,status)
    
    f = open("../logs/"+current_date+'.csv','a')
    lnwriter = csv.writer(f)
    
    while True:
        _,frame = video_capture.read()
        small_frame = cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
        rgb_small_frame = np.ascontiguousarray(small_frame[:,:,::-1])
        if s:
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame,face_locations)
            face_names = []
            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(known_face_encoding,face_encoding)
                name=""
                face_distance = face_recognition.face_distance(known_face_encoding,face_encoding)
                best_match_index = np.argmin(face_distance)
                if matches[best_match_index]:
                    name = known_faces_names[best_match_index]
                else:
                    print("unknown face detected line 59")
                    capture_picture("unknown")#call alert
                face_names.append(name)
                if name in known_faces_names:
                    log(f"found :{name} ",status)
                    if name in students:
                        capture_picture(name)
                        students.remove(name)# this name needs to be updated into cloud with a pic
                        log(students,status)
                        current_time = now.strftime("%H:%M:%S")
                        print('data needed: ',[name,current_time])
                        lnwriter.writerow([name,current_time])
                else:
                    print("unknown found line 72")
        cv2.imshow("attendence system",frame)# needs to be turned off while deploying
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    video_capture.release()
    cv2.destroyAllWindows()
    f.close()
# recognizer(vidpath='../images/woman.mp4',sourceNames='../names.txt',status=False)