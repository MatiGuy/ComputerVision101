import cv2
import numpy as np

# Let's now to a horizontal flip.
#Other Option to Rotate
img = cv2.imread('images/input.jpg')
flipped = cv2.flip(img, 1)
cv2.imshow('Horizontal Flip', flipped)
cv2.waitKey()
cv2.destroyAllWindows()