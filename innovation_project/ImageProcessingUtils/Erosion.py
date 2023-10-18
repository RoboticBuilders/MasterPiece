import cv2 as cv
import numpy as np

img = cv.imread('STLs/0-Sumatra_Depth.jpg', cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"
kernel = np.ones((5,5),np.uint8)
gradient = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)

cv.imshow('gradient', gradient)

cv.waitKey(0)