import numpy as np
from PIL import Image
import os, cv2
from loger import log

# Method to train custom classifier to recognize face
def train_classifer(name,status):
    # Read all the images in custom data-set
    path = os.path.join("../training/users/")
    log(f"traing path:{path}",status=status)
    faces = []
    ids = []
    labels = []
    pictures = {}


    # Store images in a numpy format and ids of the user on the same index in imageNp and id lists

    for root,dirs,files in os.walk(path):
            pictures = files


    for pic in pictures :
            imgpath = path+pic
            log(pic,status)
            try:
                   img = Image.open(imgpath).convert('L')
                   imageNp = np.array(img, 'uint8')
                   id = int(pic.split(name)[0])
                   print(img,imageNp,id)
                   faces.append(imageNp)
                   ids.append(id)
            except:
                   log("Error mapping img",status)
            #names[name].append(id)

    ids = np.array(ids)
    #Train and save classifier
    clf = cv2.face.LBPHFaceRecognizer_create()
    clf.train(faces, ids)
    clf.write("../training/classifiers/"+name+"_classifier.xml")