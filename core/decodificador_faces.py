import face_recognition
import os
import cv2
import pickle


def start_training(faction):

	print("[INFO] quantifying faces...")
	imagePaths = os.listdir(faction['path_images'])

	for (i, imagePath) in enumerate(imagePaths):
		print('[INFO] processing image {}/{}'.format(i+1, len(imagePaths)))

		image = cv2.imread(faction['path_images']+'/'+imagePath)
		rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
		boxes = face_recognition.face_locations(rgb, model=faction['method_training'])
		encodings = face_recognition.face_encodings(rgb, boxes)
	print("[INFO] serializing encodings...")
	data = {'encodings': encodings, 'names': faction['path_images'].split('/')[-1]}
	try:
	    f = open(faction['path_model'], "wb")
	    f.write(pickle.dumps(data))
	finally:
	    f.close()
