import face_recognition
import os
import cv2
import pickle


print("[INFO] quantifying faces...")
exe='/home/guilherme/Imagens/Webcam'

imagePaths = os.listdir(exe)

for (i, imagePath) in enumerate(imagePaths):

    print('[INFO] processing image {}/{}'.format(i+1, len(imagePaths)))

    image = cv2.imread(exe+'/'+imagePath)
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    boxes = face_recognition.face_locations(rgb, model='cnn')

    encodings = face_recognition.face_encodings(rgb, boxes)

print("[INFO] serializing encodings...")
data = {'encodings': encodings, 'names': exe.split('/')[-1]}

try:
    f = open('/home/guilherme/Documentos/projetos/my_projects/reconhecimento_facial/models/59ab5acd359e92af0f25ece8db2cc196/299557b8532c8ff0e52d6ac15c6048ba.pickle', "wb")
    f.write(pickle.dumps(data))
finally:
    f.close()