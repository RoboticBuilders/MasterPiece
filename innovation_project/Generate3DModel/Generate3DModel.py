import os
import cv2
import numpy as np
import math
from transformers import DPTFeatureExtractor, DPTForDepthEstimation
from PIL import Image
import torch
from stl import mesh

## Parameters

# Point to the image that you want to process
imgName = '/Users/anya/Documents/MasterPiece/MasterPiece/innovation_project/Generate3DModel/Images/Test.jpeg'

# Set to true to auto resize the image to target pixel count (default 300000). Else, will use the resolution of the original imag
autoResize = True

# The first threshold value for the Canny Edge Detection algorithm. 
# Get from our AI model.
threshold1 = 120

# The second threshold value for the Canny Edge Detection algorithm. 
# Get from our AI model.
threshold2 = 240

# Set the gaussian blur value. 
# Get from our AI model.
gaussianBlur = 3

# The pixel count of the image that you want to generate. Not typical to change this. 300000 is a good value for the BambuLab P1S 3D printer.
targetPixelCount = 300000

# Set to true to create a composite image with 4 tiles of the original image.
createComposite = False

# Set the maximum depth of the model in mm. Default is 5mm.
maxDepthMM = 5

## Processing

#  Get the image file name without the extension (e.g. 'Masterpiece.jpeg => 'Masterpiece')
fileName = os.path.basename(imgName).split('/')[-1].split('.')[-2]

# Create output folder if it doesn't exist
if not os.path.exists('out'):
    os.mkdir('out')

# Create a folder for the image if it doesn't exist
folder = 'out/' + fileName
if not os.path.exists(folder):
    os.mkdir(folder)

# Load the image
img = cv2.imread(imgName)
pil_image = image = Image.open(imgName)

# Figure out the scale ratio of the target image given the target pixel count.
# This will give you a target image of 300000 pixels without distorting it.
scale_ratio = math.sqrt(targetPixelCount/(img.shape[0]*img.shape[1]))

### Functions

# Canny Edge Detection using OpenCV
#
# Parameters:
#   img: The image to process
#   t1: The first threshold value
#   t2: The second threshold value
#   fileName: The name of the output file
# Returns: An image with edges detected
#
def Canny(img, t1, t2, fileName):

    # Convert to grayscale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Blur the image for better edge detection
    img_blur = cv2.GaussianBlur(img_gray, (gaussianBlur,gaussianBlur), 0) 

    # Canny Edge Detection using OpenCV
    edges = cv2.Canny(image=img_blur, threshold1=t1, threshold2=t2) 

    # Convert to RGB
    final = cv2.merge([edges, edges, edges])    

    # Save the image

    cv2.imwrite(fileName, final)

    return final

# Resize the image if autoResize is set to true
#
# Parameters:
#   img: The image to process
#   scale_ratio: The scale ratio to use
# Returns: The resized image
#
def Resize(img, scale_ratio):

    # If autoResize is set to false, return the original image
    if(autoResize == False):
        return img

    # Calculate the new width and height
    width = int(img.shape[1] * scale_ratio)
    height = int(img.shape[0] * scale_ratio)
    dim = (width, height)
    
    # Resize image using OpenCV
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_CUBIC)

    return resized

# Generate a depth map using the DPT model
#
# Parameters:
#   image: The image to process
# Returns: An image with the depth map
def DepthMap(image):

    # Setup the Dense Prediction Trasnformer (DPT) model for monocular depth estimation
    # This code is inspired by the sample the sample at https://huggingface.co/Intel/dpt-large

    # Setup feature extractor for preprocessing
    feature_extractor = DPTFeatureExtractor.from_pretrained("Intel/dpt-large")

    # Setup our depth estimation model
    model = DPTForDepthEstimation.from_pretrained("Intel/dpt-large")

    # Get the pixel values
    pixel_values = feature_extractor(image, return_tensors="pt").pixel_values

    # Generate depth map
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

    # Update the depth range to improve the details.
    # The actual depth range is between 5 to 10, this will update it to 0 to 255,
    # where 5 becomes 0 and 10 becomes 255, and everything else is interpolated linearly.
    max = np.max(output)
    min = np.min(output)
    range = max - min

    formatted = ((output - min) * 255.0 / range).astype('uint8')
    grayDepth = Image.fromarray(formatted)

    # Save this data as a grayscale image, where the depth is represented by the pixel brightness.
    p2 = os.path.join(folder, "DepthMap_Original.jpeg")
    grayDepth.save(p2)

    # Resize the image to match the original image
    resized = Resize(cv2.imread(p2), scale_ratio)
    
    # Save the resized image
    p1 = os.path.join(folder, "DepthMap.jpeg")
    cv2.imwrite(p1, resized)

    # Also save as a thermal image because it looks cool
    SaveAsThermal(p1, "DepthMap_Thermal.jpeg")

    return resized

# Save the image as a thermal image
#
# Parameters:
#   inputFileName: The image to process
#   outFileName: The name of the output file
#  
def SaveAsThermal(inputFileName, outFileName):
    image = cv2.imread(inputFileName)

    colorized = cv2.applyColorMap(image, cv2.COLORMAP_INFERNO)
    colorized_rgb = cv2.cvtColor(colorized, cv2.COLOR_BGR2RGB)
    depth = Image.fromarray(colorized_rgb)

    p3 = os.path.join(folder, outFileName)
    depth.save(p3)


# Save the depth & edge map as a 3D model that can be printed. 
#
# Parameters:
#   img: Image with he depth information
#   modelFileame: The name to use in the output file. The file will be saved as Model.<modelFileame>.stl
#   max: The maximum depth value in the image
#   min: The minimum depth value in the image
#   halfPixelWidth: The half-width of a pixel in mm. Default is 0.33mm.
#   maxHeight: The maximum height of the model. Default is 5mm.
#   invertHeight: Set to true to invert the height of the model. If true, the farthest parts are higher than the lower ones. Default is false.
# 
def SaveAsStl(img, modelFileame, max, min, halfPixelWidth = 0.33, maxHeight = 5, invertHeight = False):

    # Normalize the depth
    delta = max - min

    # Some initializations
    y = 0
    rows = img.shape[1]
    columns = img.shape[0]
    verticesPerCube = 8

    # Collect vertices from all pixels here. We will use this to create the mesh.
    allVertices = np.array([[0,0,0]])

    # Collect faces from all pixels here. We will use this to create the mesh.
    allFaces = np.array([[0,0,0]])

    # The minimum thickness of the model in mm. This is to prevent the model from being too thin.
    minThickness = 0.5

    # Loop through each colum
    for j in range (0, columns, 1):

        # Calculate the y position of this column
        y = j * halfPixelWidth * 2.0
        print('Processing column ', j, ' of ', columns)

        # Loop through each row of this column
        for i in range (0, rows, 1):
            
            # Calculate the x position of this row
            x = i * halfPixelWidth * 2.0

            # Calculate the height of this pixel
            height = ((img[j, i,0] - min) / delta) * maxHeight

            # Invert the height if needed
            if invertHeight:
                height = maxHeight - height

            # Try to draw a 3D pixel for a point
            
            # A cube has 8 vertices. Save these in an array.
            vertices = np.array([\
                [x-halfPixelWidth, y-halfPixelWidth, minThickness],
                [x+halfPixelWidth, y-halfPixelWidth, minThickness],
                [x+halfPixelWidth, y-halfPixelWidth, -1 * height],
                [x-halfPixelWidth, y-halfPixelWidth, -1 * height],
                [x-halfPixelWidth, y+halfPixelWidth, minThickness],
                [x+halfPixelWidth, y+halfPixelWidth, minThickness],
                [x+halfPixelWidth, y+halfPixelWidth, -1 * height],
                [x-halfPixelWidth, y+halfPixelWidth, -1 * height]
                ])
                    
            allVertices = np.concatenate((allVertices, vertices), axis = 0)
            
            offset = verticesPerCube * i + verticesPerCube * rows * j
            
            # STL objects are composed of triangles. A cube which has 6 faces is made of 12 triangles.
            # Define the 12 triangles composing the cube. We got the vertices offset from a online sample.
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
            
            # Concatenate the set of faces from this 3D pixel to the allFaces array
            allFaces = np.concatenate((allFaces, faces), axis = 0)

    # Clear the first item from both arrays. It was just a placeholder.
    allVertices  =np.delete(allVertices, 0, axis = 0)
    allFaces  =np.delete(allFaces, 0, axis = 0)

    # Create the mesh with all the vertices and faces
    cube = mesh.Mesh(np.zeros(allFaces.shape[0], dtype=mesh.Mesh.dtype))
    for i, f in enumerate(allFaces):
        for j in range(3):
            cube.vectors[i][j] = allVertices[f[j],:]

    # Rotate the mesh to place it in the correct default orientation wrt the printer plate
    # Not strictly necessary, but it avoid having to rotate the model in the slicer.
    cube.rotate([1, 0, 0], math.radians(180))

    # Save the mesh to a STL file
    p1 = os.path.join(folder, "Model." + modelFileame + ".stl")
    
    if invertHeight:
        p1 = os.path.join(folder, "Model." + modelFileame + ".inverted.stl")
    else:
        p1 = os.path.join(folder, "Model." + modelFileame + '.stl')

    cube.save(p1)
    print('Saved: ', p1)

# More Processing

# Save the original image
d = os.path.join(folder, "Original.jpeg")
cv2.imwrite(d, img)

# Resize the image
resized = Resize(img, scale_ratio)

# Save the resized image
d = os.path.join(folder, "Resized.jpeg")
cv2.imwrite(d, resized)

# Generate the edge map
cannyFile = os.path.join(folder, "Canny.jpeg")
canny = Canny(resized, threshold1, threshold2, cannyFile)

# Generate the depth map
depthImg = DepthMap(pil_image)

cod = os.path.join(folder, "Canny_on_depth.jpeg")
cannyOnDepth = Canny(depthImg, 0, 200, cod)

# Take out canny edges already accounted for in the depth map
edgeImg = cv2.addWeighted(canny, 1, cannyOnDepth, -1, 0)

cc = os.path.join(folder, "Canny_corrected.jpeg")
cv2.imwrite(cc, edgeImg)

# Combine the depth map and edge map. Use the edgeRatio variable to control the amount of edge details to show.
# Say the edgeRatio is 0.1, then the final image will be 90% depth map and 10% edge map.
edgeRatio = 0.075
img = cv2.addWeighted(depthImg, 1 - edgeRatio, edgeImg, edgeRatio, 0)

# Save the final image
p2 = os.path.join(folder, "Final.jpeg")
cv2.imwrite(p2, img)

# Also save as a thermal image because it looks cool 
SaveAsThermal(p2, "Final_Thermal.jpeg")

max = np.max(img)
min = np.min(img)

if(createComposite == False):
    # Save the depth & edge map as a 3D model that can be printed.
    SaveAsStl(img, "Full", max, min, maxHeight = maxDepthMM)
else:
    # Save 4 composite models instead of one.
    (h, w) = img.shape[:2]

    (cX, cY) = (w // 2, h // 2)

    topLeft = img[0:cY, 0:cX]
    topRight = img[0:cY, cX:w]
    bottomLeft = img[cY:h, 0:cX]
    bottomRight = img[cY:h, cX:w]

    # Save images
    p2 = os.path.join(folder, "topLeft.jpeg")
    cv2.imwrite(p2, topLeft)

    p2 = os.path.join(folder, "topRight.jpeg")
    cv2.imwrite(p2, topRight)

    p2 = os.path.join(folder, "bottomLeft.jpeg")
    cv2.imwrite(p2, bottomLeft)

    p2 = os.path.join(folder, "bottomRight.jpeg")
    cv2.imwrite(p2, bottomRight)

    # Save the depth & edge map as a 3D model that can be printed.
    SaveAsStl(topLeft, "Topleft", max, min, maxHeight = maxDepthMM)
    SaveAsStl(topRight, "TopRight", max, min, maxHeight = maxDepthMM)
    SaveAsStl(bottomLeft, "BottomLeft", max, min, maxHeight = maxDepthMM)
    SaveAsStl(bottomRight, "BottomRight", max, min, maxHeight = maxDepthMM)
