import numpy as np
import cv2

#capture one frame
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
cv2.imwrite("myImg.jpg", frame)
cap.release()