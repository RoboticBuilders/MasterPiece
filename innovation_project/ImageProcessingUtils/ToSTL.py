import os
import numpy as np
from stl import mesh
import cv2

imageName = 'Downsampled/Starry_Night_Even_Simpler.jpg/2 - 134x214.jpg'
img = cv2.imread(imageName)
invertHeight = False

max = np.max(img)
min = np.min(img)
delta = max - min

fileName = os.path.basename(imageName).split('/')[-1].split('.')[-2]
p1 = os.path.join('STLs', fileName + '.stl')

y = 0
rows = img.shape[1]
columns = img.shape[0]
maxHeight = 10
verticesPerCube = 8
allVertices = np.array([[0,0,0]])
allFaces = np.array([[0,0,0]])

for j in range (0, columns, 1):
    y = j * 2.0
    print('Processing row ', j)

    for i in range (0, rows, 1):
        
        x = i * 2.0
        height = (img[j, i,0] - min) / delta * maxHeight

        if invertHeight:
            height = maxHeight - height

        # Define the 8 vertices of the cube
        vertices = np.array([\
            [x-1, -1, y-1],
            [x+1, -1, y-1],
            [x+1, height, y-1],
            [x-1, height, y-1],
            [x-1, -1, y+1],
            [x+1, -1, y+1],
            [x+1, height, y+1],
            [x-1, height, y+1]
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

fileName = os.path.basename(imageName).split('/')[-1].split('.')[-2]

if not os.path.exists('STLs'):
    os.mkdir('STLs')

if invertHeight:
    p1 = os.path.join('STLs', fileName + '.inverted.stl')
else:
    p1 = os.path.join('STLs', fileName + '.stl')

# Write the mesh to file "cube.stl"
cube.save(p1)
print('Saved: ', p1)