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


img = cv2.imread('/Users/ruchi/Documents/FLL/MasterPiece/innovation_project/Generate3DModel/out/House2/Final.jpeg')

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# print(img)
# np.savetxt('img.out.txt', img, fmt='%5.0f')

resized = cv2.resize(img, (14, 14), interpolation=cv2.INTER_AREA)
# resized = myOwnResize(img, (14,14))

resized = np.array(resized)
# print(resized)

newArray = []
for j in resized:
    array = []
    for i in j:
        if i <= 50:
            array.append(0)
        elif i > 50 and i <= 100:
            array.append(1)
        elif i > 100 and i <= 190:
            array.append(2)
        elif i > 190:
            array.append(3)
        else:
            print("????????????? - i=" + str(i))
    newArray.append(array)
    print(array)
