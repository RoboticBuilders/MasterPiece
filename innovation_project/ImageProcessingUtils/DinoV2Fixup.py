import os
from transformers import DPTFeatureExtractor, DPTForDepthEstimation
from PIL import Image
import requests
import torch
import numpy as np
import cv2

imageName = 'DinoV2/Sumatra_Depth.jpeg'
image = cv2.imread(imageName)

image_invert = cv2.bitwise_not(image)

colorized = cv2.applyColorMap(image_invert, cv2.COLORMAP_INFERNO)
colorized_rgb = cv2.cvtColor(colorized, cv2.COLOR_BGR2RGB)
depth = Image.fromarray(colorized_rgb)

fileName = os.path.basename(imageName).split('/')[-1]

if not os.path.exists('DinoV2'):
    os.mkdir('DinoV2')

p2 = os.path.join('DinoV2', 'invert_' + fileName)
cv2.imwrite(p2, image_invert)

p3 = os.path.join('DinoV2', 'thermal_' + fileName)
depth.save(p3)
