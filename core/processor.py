import face_recognition
import imutils
import pickle
import cv2
import os


def recognition(factions):
	print("[INFO] loading encodings + face detector...")
	data = pickle.loads(open(factions["model_id"], "rb").read())
	detector = cv2.CascadeClassifier(os.getcwd()+'/core/'+'haarcascade_frontalface_default.xml')
	
	frame = cv2.imread(factions['image'])
	frame = imutils.resize(frame, width=500)	
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

	rects = detector.detectMultiScale(gray, scaleFactor=1.1, 
		minNeighbors=5, minSize=(30, 30),
		flags=cv2.CASCADE_SCALE_IMAGE)

	boxes = [(y, x + w, y + h, x) for (x, y, w, h) in rects]
	encodings = face_recognition.face_encodings(rgb, boxes)

	for encoding in encodings:
		matches = face_recognition.compare_faces(data["encodings"],
			encoding)

		if True in matches:
			return True

		else:
			False