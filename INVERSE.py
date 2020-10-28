import cv2
import numpy as np

#reading imagae from file
img = cv2.imread("cat.png")

#INVERSE EFFECT
inv = 255-img
print('Negative Image created.')

#comparing original vs resized
cv2.imshow('ORIGINAL',img)
cv2.imshow('INVERSE',inv)
cv2.waitKey(0)
cv2.destroyAllWindows()
