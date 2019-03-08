import cv2 
import numpy as np
import argparse
# Read image given by user
parser = argparse.ArgumentParser(description='Code for Changing the contrast and brightness of an image! tutorial.')
parser.add_argument('--input', help='Path to input image.', default='lena.jpg')
args = parser.parse_args()

i=0


cap=cv2.VideoCapture(1)


while True:


	ret,frame=cap.read()

	if i==40:


		cv2.imwrite("frame.jpg",frame)

		new_image = np.zeros(frame.shape, frame.dtype)

		alpha = 0.2 #contrast 
		beta = 0  #brightness

		new_image = cv2.convertScaleAbs(frame, alpha=alpha, beta=beta)

		cv2.imshow('Original Image', frame)
		cv2.imshow('New Image', new_image)


	if cv2.waitKey(1)  & 0xFF==ord('q'):
	 break
	i+=1;


cap.release()
cv2.destroyAllWindows()
