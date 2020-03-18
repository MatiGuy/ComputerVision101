import cv2
import numpy as np

#Other Option to Rotate
img = cv2.imread('images/input.jpg')

rotated_image = cv2.transpose(img)

cv2.imshow('Rotated Image - Method 2', rotated_image)
cv2.waitKey()
cv2.destroyAllWindows()

'''
Notice all the black space surrounding the image.
We could now crop the image as we can calculate it's new size (we haven't learned cropping yet!).

But here's another method for simple rotations that uses the cv2.transpose function'''