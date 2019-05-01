import numpy as np
import os
import cv2
import time
import RPi.GPIO as gpio

gpio.setwarnings(True)
gpio.setmode(gpio.BOARD)
gpio.setup(12, gpio.IN, pull_up_down=gpio.PUD_DOWN)

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
start = time.time()

while (cap.isOpened()):
	ret, frame = cap.read()
	
	if ret:
		frame = cv2.flip(frame, 0)
		out.write(frame)
		cv2.imshow('frame', frame)
		end = time.time()
		
		if end - start > (60 * 8) or cv2.waitKey(1) & 0xFF == ord('q') or gpio.input(12) == gpio.HIGH:
			break
	else:
		break
		
cap.release()
out.release()
cv2.destroyAllWindows()
