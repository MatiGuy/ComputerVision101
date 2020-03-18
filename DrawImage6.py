import cv2
import numpy as np
image = np.zeros((512,512,3), np.uint8)

cv2.putText(image, 'Hello World!', (75,290), cv2.FONT_HERSHEY_COMPLEX, 2, (100,170,0), 3)
cv2.imshow("Hello World!", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
Let's even add text with cv2.putText
cv2.putText(image, 'Text to Display', bottom left starting point, Font, Font Size, Color, Thickness)

FONT_HERSHEY_SIMPLEX, FONT_HERSHEY_PLAIN
FONT_HERSHEY_DUPLEX,FONT_HERSHEY_COMPLEX
FONT_HERSHEY_TRIPLEX, FONT_HERSHEY_COMPLEX_SMALL
FONT_HERSHEY_SCRIPT_SIMPLEX
FONT_HERSHEY_SCRIPT_COMPLEX
'''