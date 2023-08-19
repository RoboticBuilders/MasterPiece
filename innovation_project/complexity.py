import cv2
import os

complexity = {}

path = ".\innovation_project"
files = os.listdir(path)
for file in files:
    #image= cv2.imread('.\innovation_project\house.png')
    filename = path + '\\' + file
    if not file.endswith(".png"):
        continue
    image = cv2.imread(filename)
    height, width, channels = image.shape
    gray= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    edges= cv2.Canny(gray, 50,200)

    contours, hierarchy= cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    number_of_objects_in_image= len(contours)

    # Draw the contours on the image
    #cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

    # Display the image
    #cv2.imshow('Image', image)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

    totalPixels = height * width
    #print ("The number of objects in this image: ", str(number_of_objects_in_image))

    objects_per_pixel = float(number_of_objects_in_image)/totalPixels*10000
    complexity[file] = (totalPixels, number_of_objects_in_image, objects_per_pixel)


for key, value in complexity.items():
    print(key + " : objects per pixel = " + str(value[2]))