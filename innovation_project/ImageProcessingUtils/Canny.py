
import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage as ndi
from skimage.util import random_noise
from skimage import feature

# Generate noisy image of a square
image = np.zeros((128, 128), dtype=float)
image[32:-32, 32:-32] = 1

imageName = 'Images/Mona_Lisa_Zoomed.jpg'

# read the image
image = cv2.imread(imageName)[:,:,0]

image = ndi.gaussian_filter(image, 4)
image = random_noise(image, mode='speckle', mean=0.1)

itemsPerRow = 6

sigmaSteps = np.arange(0, 1.4, 0.1)

# display results
fig, ax = plt.subplots(nrows=int(sigmaSteps.size / itemsPerRow) + 1, ncols=itemsPerRow, figsize=(10, 8))

for i, sigma in enumerate(sigmaSteps):
    # Compute the Canny filter for two values of sigma
    edge = feature.canny(image, sigma=sigma)


    x = ax[int(i / itemsPerRow), i % itemsPerRow]
    x.imshow(edge, cmap='gray')
    x.set_title('σ =' + ("% .2f" % sigma), fontsize=12)

    x.axis('off')


fig.tight_layout()
plt.show()