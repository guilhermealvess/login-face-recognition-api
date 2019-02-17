from imutils import paths
import face_recognition
import pickle
import cv2
import os


def start_training(data):

	print("[INFO] quantifying faces...")
	imagePaths = list(paths.list_images(data["path_images"]))
	
	knownEncodings = []
	knownNames = []
	
	for (i, imagePath) in enumerate(imagePaths):
		
		print("[INFO] processing image {}/{}".format(i + 1,
			len(imagePaths)))
		name = imagePath.split(os.path.sep)[-2]
		
		image = cv2.imread(imagePath)
		rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	
		boxes = face_recognition.face_locations(rgb,
			model=data["method_training"])
		
		encodings = face_recognition.face_encodings(rgb, boxes)
		
		for encoding in encodings:
			
			knownEncodings.append(encoding)
			knownNames.append(name)
	
	
	print("[INFO] serializing encodings...")
	result = {"encodings": knownEncodings, "names": knownNames}
	try:
		f = open(data["path_model"], "wb")
		f.write(pickle.dumps(result))
	finally:
		f.close()
