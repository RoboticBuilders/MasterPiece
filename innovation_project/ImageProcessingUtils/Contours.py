import os
import cv2 as cv
import numpy as np
 

imageName = 'Images/Starry_Night_Simple.jpg'

# read the image
image = cv.imread(imageName)

imgray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

final = np.zeros(image.shape, dtype = "uint8")

cv.drawContours(final, contours, -1, (128,128,128), 3)
c = cv.hconcat([image, final]) 

d = os.path.join('Contours')
if not os.path.exists(d):
    os.mkdir(d)


fileName = os.path.basename(imageName).split('/')[-1]
p1 = os.path.join('Contours', fileName)
p2 = os.path.join('Contours', 'Combined.' + fileName)

cv.imwrite(p1, final)
cv.imwrite(p2, c)

print('Saved: ', p1)