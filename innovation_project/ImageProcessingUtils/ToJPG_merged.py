import os
import numpy as np
from stl import mesh
import cv2

depthImage = 'Merge/25.0-Mona_Lisa_Zoomed_Depth.jpg'
edgeImage = 'Merge/25.0-Mona_Lisa_Zoomed_Canny.jpg'
invertHeight = False
edgeRatio = 0.075

depthImg = cv2.imread(depthImage)
edgeImg = cv2.imread(edgeImage)

img = cv2.addWeighted(depthImg, 1 - edgeRatio, edgeImg, edgeRatio, 0)

fileName = os.path.basename(depthImage).split('/')[-1].split('.')[-2]

p2 = os.path.join('STLs', fileName + '.jpg')
cv2.imwrite(p2, img)

print('Saved: ', p2)