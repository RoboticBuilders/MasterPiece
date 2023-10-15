import os
import numpy as np
from stl import mesh
import cv2
import math

depthImage = 'Merge/25.0-Mona_Lisa_Zoomed_Depth.jpg'
edgeImage = 'Merge/25.0-Mona_Lisa_Zoomed_Canny.jpg'
invertHeight = False
edgeRatio = 0.075

depthImg = cv2.imread(depthImage)
edgeImg = cv2.imread(edgeImage)

img = cv2.addWeighted(depthImg, 1 - edgeRatio, edgeImg, edgeRatio, 0)

max = np.max(img)
min = np.min(img)
delta = max - min

fileName = os.path.basename(depthImage).split('/')[-1].split('.')[-2]
p1 = os.path.join('STLs', fileName + '.stl')

y = 0
rows = img.shape[1]
columns = img.shape[0]
maxHeight = 5
verticesPerCube = 8
allVertices = np.array([[0,0,0]])
allFaces = np.array([[0,0,0]])
pixedWidth = 0.33
minThickness = 0.5

for j in range (0, columns, 1):
    y = j * pixedWidth * 2.0
    print('Processing column ', j, ' of ', columns)

    for i in range (0, rows, 1):
        
        x = i * pixedWidth * 2.0
        height = (img[j, i,0] - min) / delta * maxHeight

        if invertHeight:
            height = maxHeight - height

        # Define the 8 vertices of the cube
        vertices = np.array([\
            [x-pixedWidth, y-pixedWidth, minThickness],
            [x+pixedWidth, y-pixedWidth, minThickness],
            [x+pixedWidth, y-pixedWidth, -1 * height],
            [x-pixedWidth, y-pixedWidth, -1 * height],
            [x-pixedWidth, y+pixedWidth, minThickness],
            [x+pixedWidth, y+pixedWidth, minThickness],
            [x+pixedWidth, y+pixedWidth, -1 * height],
            [x-pixedWidth, y+pixedWidth, -1 * height]
            ])
                
        allVertices = np.concatenate((allVertices, vertices), axis = 0)
        
        offset = verticesPerCube * i + verticesPerCube * rows * j
        # Define the 12 triangles composing the cube
        faces = np.array([\
            [offset+0,offset+3,offset+1],
            [offset+1,offset+3,offset+2],
            [offset+0,offset+4,offset+7],
            [offset+0,offset+7,offset+3],
            [offset+4,offset+5,offset+6],
            [offset+4,offset+6,offset+7],
            [offset+5,offset+1,offset+2],
            [offset+5,offset+2,offset+6],
            [offset+2,offset+3,offset+6],
            [offset+3,offset+7,offset+6],
            [offset+0,offset+1,offset+5],
            [offset+0,offset+5,offset+4]
            ])
        
        allFaces = np.concatenate((allFaces, faces), axis = 0)

allVertices  =np.delete(allVertices, 0, axis = 0)
allFaces  =np.delete(allFaces, 0, axis = 0)

# Create the mesh
cube = mesh.Mesh(np.zeros(allFaces.shape[0], dtype=mesh.Mesh.dtype))
for i, f in enumerate(allFaces):
    for j in range(3):
        cube.vectors[i][j] = allVertices[f[j],:]

# Rotate the mesh to place it in the correct default orientation wrt the printer plate
cube.rotate([1, 0, 0], math.radians(180))

fileName = os.path.basename(depthImage).split('/')[-1].split('.')[-2]

if not os.path.exists('STLs'):
    os.mkdir('STLs')

if invertHeight:
    p1 = os.path.join('STLs', fileName + '.inverted.stl')
else:
    p1 = os.path.join('STLs', fileName + '.stl')

# Write the mesh to file "cube.stl"
cube.save(p1)
print('Saved: ', p1)