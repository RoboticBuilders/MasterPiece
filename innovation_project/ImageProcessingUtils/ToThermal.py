import os
from transformers import DPTFeatureExtractor, DPTForDepthEstimation
from PIL import Image
import requests
import torch
import numpy as np
import cv2


imageName = 'STLs/Letter-to-Frida_Depth.jpg'
image = cv2.imread(imageName)

colorized = cv2.applyColorMap(image, cv2.COLORMAP_INFERNO)
colorized_rgb = cv2.cvtColor(colorized, cv2.COLOR_BGR2RGB)
depth = Image.fromarray(colorized_rgb)

fileName = os.path.basename(imageName).split('/')[-1]

if not os.path.exists('DinoV2'):
    os.mkdir('DinoV2')

p3 = os.path.join('DinoV2', 'thermal_' + fileName)
depth.save(p3)
print('Saved: ', p3)
