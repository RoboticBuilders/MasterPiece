
import os
import cv2
import numpy as np
import math
from transformers import DPTFeatureExtractor, DPTForDepthEstimation
from PIL import Image
import torch
from stl import mesh

imgName = 'Images/Shilshole.jpg'
fileName = os.path.basename(imgName).split('/')[-1].split('.')[-2]

if not os.path.exists('out'):
    os.mkdir('out')

folder = 'out/' + fileName

if not os.path.exists(folder):
    os.mkdir(folder)

img = cv2.imread(imgName)
pil_image = image = Image.open(imgName)

aspect_ratio = img.shape[0] / img.shape[1]

yp = math.sqrt(75000 / aspect_ratio)
scale_ratio = yp / img.shape[1]


def Canny(img, t1, t2):
    # Convert to graycsale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Blur the image for better edge detection
    img_blur = cv2.GaussianBlur(img_gray, (3,3), 0) 

    edges = cv2.Canny(image=img_blur, threshold1=t1, threshold2=t2) # Canny Edge Detection
    final = cv2.merge([edges, edges, edges])    

    fileName = os.path.basename(imgName).split('/')[-1]

    p1 = os.path.join(folder, "Canny.jpeg")

    cv2.imwrite(p1, final)

    return final

def Resize(img, scale_ratio):

    width = int(img.shape[1] * scale_ratio)
    height = int(img.shape[0] * scale_ratio)
    dim = (width, height)
    
    # resize image
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_CUBIC)

    return resized

def DepthMap(image):
    feature_extractor = DPTFeatureExtractor.from_pretrained("Intel/dpt-large")
    model = DPTForDepthEstimation.from_pretrained("Intel/dpt-large")

    pixel_values = feature_extractor(image, return_tensors="pt").pixel_values

    with torch.no_grad():
        outputs = model(pixel_values)
        predicted_depth = outputs.predicted_depth

    # interpolate to original size
    prediction = torch.nn.functional.interpolate(
                        predicted_depth.unsqueeze(1),
                        size=image.size[::-1],
                        mode="bicubic",
                        align_corners=False,
                ).squeeze()
    output = prediction.cpu().numpy()

    max = np.max(output)
    min = np.min(output)
    range = max - min

    formatted = ((output - min) * 255.0 / range).astype('uint8')
    grayDepth = Image.fromarray(formatted)

    p2 = os.path.join(folder, "DepthMap_Original.jpeg")
    grayDepth.save(p2)

    resized = Resize(cv2.imread(p2), scale_ratio)
    
    p1 = os.path.join(folder, "DepthMap.jpeg")
    cv2.imwrite(p1, resized)
    SaveAsThermal(p1, "DepthMap_Thermal.jpeg")

    return resized

def SaveAsThermal(inputFileName, outFileName):
    image = cv2.imread(inputFileName)

    colorized = cv2.applyColorMap(image, cv2.COLORMAP_INFERNO)
    colorized_rgb = cv2.cvtColor(colorized, cv2.COLOR_BGR2RGB)
    depth = Image.fromarray(colorized_rgb)

    p3 = os.path.join(folder, outFileName)
    depth.save(p3)


def SaveAsStl(depthImg, edgeImg, maxHeight = 5, invertHeight = False):
    img = cv2.addWeighted(depthImg, 1 - edgeRatio, edgeImg, edgeRatio, 0)

    max = np.max(img)
    min = np.min(img)
    delta = max - min

    p1 = os.path.join(folder, "Model.stl")

    y = 0
    rows = img.shape[1]
    columns = img.shape[0]
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

    if invertHeight:
        p1 = os.path.join(folder, "Model.inverted.stl")
    else:
        p1 = os.path.join(folder, 'Model.stl')

    # Write the mesh to file "cube.stl"
    cube.save(p1)
    print('Saved: ', p1)

# Resume

d = os.path.join(folder, "Original.jpeg")
cv2.imwrite(d, img)

resized = Resize(img, scale_ratio)
d = os.path.join(folder, "Resized.jpeg")
cv2.imwrite(d, resized)

edgeRatio = 0.075
edgeImg = Canny(resized, 60, 160)
depthImg = DepthMap(pil_image)

img = cv2.addWeighted(depthImg, 1 - edgeRatio, edgeImg, edgeRatio, 0)

p2 = os.path.join(folder, "Final.jpeg")
cv2.imwrite(p2, img)

SaveAsThermal(p2, "Final_Thermal.jpeg")

SaveAsStl(depthImg, edgeImg, maxHeight = 10)