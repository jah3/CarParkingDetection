
# Import essential libraries
import requests
import cv2
import numpy as np
import imutils
  
# Replace the below URL with your own. Make sure to add "/shot.jpg" at last.
url = "http://192.168.1.3:8080/shot.jpg"
  
import cv2
capture = cv2.VideoCapture('http://192.168.1.3:8080/video')
while(True):
   ret, frame = capture.read()
   cv2.imshow('livestream', frame)
   if cv2.waitKey(1) == ord('q'):
      break
capture.release()
cv2.destroyAllWindows()