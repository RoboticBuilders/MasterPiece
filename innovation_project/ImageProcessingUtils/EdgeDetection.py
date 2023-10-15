import os
import cv2
import numpy as np

def Canny(imgName):
     # Read the original image
    img = cv2.imread(imgName)

    # Convert to graycsale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Blur the image for better edge detection
    img_blur = cv2.GaussianBlur(img_gray, (3,3), 0) 

    edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200) # Canny Edge Detection
    # Display Canny Edge Detection Image

    print('Original: ', img.shape)
    print('Original: ', edges.shape)

    final = cv2.merge([edges, edges, edges])    

    combined = cv2.hconcat([img, final])

    #cv2.imshow('Canny Edge Detection', combined)
    #cv2.waitKey(0)

    fileName = os.path.basename(imgName).split('/')[-1]

    if not os.path.exists('Canny'):
        os.mkdir('Canny')

    p1 = os.path.join('Canny', 'Combined.' + fileName)
    p2 = os.path.join('Canny', fileName)

    cv2.imwrite(p1, combined)
    cv2.imwrite(p2, final)
    print('Saved: ', p1)

    return

def Sobel(imgName):
    # Read the original image
    img = cv2.imread(imgName)

    # Convert to graycsale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Blur the image for better edge detection
    img_blur = cv2.GaussianBlur(img_gray, (3,3), 0) 

    #Sobel Edge Detection
    sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5) # Sobel Edge Detection on the X axis
    sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5) # Sobel Edge Detection on the Y axis
    sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5) # Combined X and Y Sobel Edge Detection
 
    fileName = os.path.basename(imgName).split('/')[-1]
    p1 = os.path.join('Sobel', fileName)

    if not os.path.exists('Sobel'):
        os.mkdir('Sobel')

    cv2.imwrite(p1, sobelxy)
    print('Saved: ', p1)

    return
 
# Canny Edge Detection 

Canny('Images/Mona_Lisa_Zoomed.jpg')


  
cv2.destroyAllWindows()