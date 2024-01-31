import os
import cv2
import numpy as np

# def myOwnResize(img, pinArraySize):
#     row_win_size = int(img.shape[0]/pinArraySize[1])
#     col_win_size = int(img.shape[1]/pinArraySize[0])

#     rowSteps = int(img.shape[0]/row_win_size)
#     colSteps = int(img.shape[1]/col_win_size)

#     for rowStep in range(rowSteps):
#         for colStep in range(colSteps):

#       # Count edge density per tile
#       for rowOffset in range(row_win_size):
#         for colOffset in range(col_win_size):
#           if(contourImg[rowStep*row_win_size + rowOffset][colStep*col_win_size + colOffset] > 0):
#             edgePixelCount += 1

#       edgesComplexityTileScores.append(float(edgePixelCount))

def writeAsImage(array, imgName):
    imgArray = []
    for n in array:
        r = []
        for m in n:
            if m == 0:
                r.append(0)
            elif m == 1:
                r.append(100)
            elif m == 2:
                r.append(200)
            elif m == 3:
                r.append(255)
        imgArray.append(r)
    
    img = np.array(imgArray)
    p = imgName + '.jpeg'
    cv2.imwrite(p, img)






img = cv2.imread('/Users/ruchi/Documents/FLL/MasterPiece/innovation_project/Generate3DModel/out/GreatWave2/Canny.jpeg')

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# print(img)
# np.savetxt('img.out.txt', img, fmt='%5.0f')

resized = cv2.resize(img, (14, 14), interpolation=cv2.INTER_LINEAR_EXACT)
# resized = myOwnResize(img, (14,14))

resized = np.array(resized)
# print(resized)

newArray = []
for j in resized:
    array = []
    for i in j:
        if i <= 25:
            array.append(0)
        elif i > 25 and i <= 80:
            array.append(1)
        elif i > 80 and i <= 120:
            array.append(2)
        elif i > 120:
            array.append(3)
        else:
            print("????????????? - i=" + str(i))
        # print(z)
        
    newArray.append(array)
        
    print(array)

writeAsImage(newArray, 'img')