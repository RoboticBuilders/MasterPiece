import cv2
from scipy import misc, datasets
import scipy.ndimage as nd
import matplotlib.pyplot as plt
import numpy as np

def Sobel (imageName):
    fig = plt.figure()    
    img = cv2.imread(imageName)

    ax1 = fig.add_subplot(121)  # left side
    ax2 = fig.add_subplot(122)  # right side

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Blur the image for better edge detection
    img_blur = cv2.GaussianBlur(img_gray, (3,3), 0) 

    sx = nd.sobel(img_blur, axis = 0, mode = 'constant')
    sy = nd.sobel(img_blur, axis = 1, mode = 'constant')
    sob = np.hypot(sx, sy)

    ax1.imshow(img)
    ax2.imshow(sob)

    plt.show() 

def Prewitt (imageName):

    fig = plt.figure()    
    img = cv2.imread(imageName)

    ax1 = fig.add_subplot(121)  # left side
    ax2 = fig.add_subplot(122)  # right side

    result = nd.prewitt(img, mode='constant')
    
    ax1.imshow(img)
    ax2.imshow(result)
    plt.show()

imageName = 'Images/Mona_Lisa_Zoomed.jpg'
Sobel(imageName)