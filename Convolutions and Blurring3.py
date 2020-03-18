# Image De-noising - Non-Local Means Denoising
import numpy as np
import cv2

image = cv2.imread('images/elephant.jpg')

# Parameters, after None are - the filter strength 'h' (5-10 is a good range)
# Next is hForColorComponents, set as same value as h again
#
dst = cv2.fastNlMeansDenoisingColored(image, None, 6, 6, 7, 21)

cv2.imshow('Fast Means Denoising', dst)
cv2.waitKey(0)

cv2.destroyAllWindows()
'''
There are 4 variations of Non-Local Means Denoising:

cv2.fastNlMeansDenoising() - works with a single grayscale images
cv2.fastNlMeansDenoisingColored() - works with a color image.
cv2.fastNlMeansDenoisingMulti() - works with image sequence captured in short period of time (grayscale images)
cv2.fastNlMeansDenoisingColoredMulti() - same as above, but for color images.
'''