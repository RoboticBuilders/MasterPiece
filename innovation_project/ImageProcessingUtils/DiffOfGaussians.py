import os
import cv2
import imageio
from skimage.data import camera
import matplotlib.pyplot as plt
import numpy as np
from skimage.data import gravel
from skimage.filters import difference_of_gaussians, window
from scipy.fft import fftn, fftshift
from skimage.io import imsave
from PIL.Image import Image as im


#image = camera()
imageName = 'Images/Mona_Lisa_Zoomed.jpg'
image = cv2.imread(imageName)[:,:,0]

wimage = image * window('hann', image.shape)  # window image to improve FFT
filtered_image = difference_of_gaussians(image, 4)
filtered_wimage = filtered_image * window('hann', image.shape)
im_f_mag = fftshift(np.abs(fftn(wimage)))
fim_f_mag = fftshift(np.abs(fftn(filtered_wimage)))

fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(8, 8))
ax[0, 0].imshow(image, cmap='gray')
ax[0, 0].set_title('Original Image')
ax[0, 1].imshow(np.log(im_f_mag), cmap='magma')
ax[0, 1].set_title('Original FFT Magnitude (log)')
ax[1, 0].imshow(filtered_image, cmap='gray')
ax[1, 0].set_title('Filtered Image')
ax[1, 1].imshow(np.log(fim_f_mag), cmap='magma')
ax[1, 1].set_title('Filtered FFT Magnitude (log)')

fileName = os.path.basename(imageName).split('/')[-1]
p1 = os.path.join('DiffOfGaussians', fileName)

if not os.path.exists('DiffOfGaussians'):
    os.mkdir('DiffOfGaussians')

final = cv2.merge([filtered_image, filtered_image, filtered_image])   
# cv2.imwrite(p1, final)

# new_p = im.(final)
# if new_p.mode != 'RGB':
#     new_p = new_p.convert('RGB')
# imsave(p1, new_p)

print('Saved: ', p1)

plt.show()