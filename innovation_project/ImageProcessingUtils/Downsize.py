import os
import cv2
import numpy as np


def PyrDown(imageName):
    image = cv2.imread(imageName)

    fileName = os.path.basename(imageName).split('/')[-1]

    if not os.path.exists('Downsampled'):
        os.mkdir('Downsampled')

    print("Size of image before pyrDown: ", image.shape)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    for i in range(1, 8, 1):
        image = cv2.pyrDown(image)
        print("Size of image after pyrDown: ", image.shape)

        d = os.path.join('Downsampled', fileName)
        if not os.path.exists(d):
            os.mkdir(d)

        p1 = os.path.join(d, str(i) + ' - ' + str(image.shape[0]) + 'x' + str(image.shape[1])  + '.jpg')
        cv2.imwrite(p1, image)

        print('Saved: ', p1)

def Resize(imageName, scale_percent):

    fileName = os.path.basename(imageName).split('/')[-1]

    if not os.path.exists('Downsampled'):
        os.mkdir('Downsampled')

    img = cv2.imread(imageName, cv2.IMREAD_UNCHANGED)
    
    print('Original Dimensions : ',img.shape)
    
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    
    # resize image
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_CUBIC)
    
    print('Resized Dimensions : ',resized.shape)

    # # Create the sharpening kernel
    # kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    
    # # Sharpen the image
    # sharpened_image = cv2.filter2D(resized, -1, kernel)

    # define the contrast and brightness value
    # contrast = 127. # Contrast control ( 0 to 127)
    # brightness = 100. # Brightness control (0-100)

    # # call addWeighted function. use beta = 0 to effectively only
    # out = cv2.addWeighted(sharpened_image, contrast, sharpened_image, 0, brightness)

    d = os.path.join('Downsampled', fileName)
    if not os.path.exists(d):
        os.mkdir(d)

    d = os.path.join(d, str(scale_percent) + '-' + fileName)
    cv2.imwrite(d, resized)

    print('Saved: ', d)

def ResizeMany(imageName):
    scale = 100
    for i in range(0, 5, 1):
        Resize(imageName, scale)
        scale = scale / 2

imageName = 'Images/Mona_Lisa_Zoomed.jpg'
ResizeMany(imageName)