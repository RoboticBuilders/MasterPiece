import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

def Canny(imgName, t1, t2):
     # Read the original image
    img = cv2.imread(imgName)

    # Convert to graycsale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Blur the image for better edge detection
    img_blur = cv2.GaussianBlur(img_gray, (3,3), 0) 

    edges = cv2.Canny(image=img_blur, threshold1=t1, threshold2=t2) # Canny Edge Detection
    # Display Canny Edge Detection Image

    print('Original: ', img.shape)
    print('Original: ', edges.shape)

    final = cv2.merge([edges, edges, edges])    

    return final

def onclick(event):
    if event.xdata != None and event.ydata != None:
        t = event.inaxes.title._text
        print(t)

image = 'Process/Letter-to-Frida_Depth.jpg'
t1range = [*range(40, 140, 20)]
t2range = [*range(80, 300, 40)]

columns = len(t1range)
rows = len(t2range)

# display results
fig, ax = plt.subplots(nrows=columns, ncols=rows, figsize=(10, 8))

for i, t1 in enumerate(t1range):
    for j, t2 in enumerate(t2range):
        # Compute the Canny filter for two values of sigma
        c = Canny(image, t1, t2)

        x = ax[i, j]
        x.imshow(c, cmap='bone')
        x.set_title(("%.f" % t1) + '|' + ("%.f" % t2), fontsize=12)

        x.axis('off')

        cid = fig.canvas.mpl_connect('button_press_event', onclick)

fig.tight_layout()
plt.show()