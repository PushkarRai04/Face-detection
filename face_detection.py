from cv2 import imread
from cv2 import imshow
from cv2 import waitKey
from cv2 import destroyAllWindows
from cv2 import CascadeClassifier
from cv2 import rectangle
#photograph
pixels = imread('6.png')
#load the pre-trained model
classifier = CascadeClassifier('haarcascade_frontalface_default.xml')
bboxes = classifier.detectMultiScale(pixels)
rgb=(0,0,255)
for box in bboxes:
	x, y, width, height = box
	x2, y2 = x + width, y + height
	# draw a rectangle over the pixels
	rectangle(pixels, (x, y), (x2, y2), rgb, 1)
# show the image
imshow('face detection', pixels)
# keep the window open until we press a key
waitKey(0)
destroyAllWindows()