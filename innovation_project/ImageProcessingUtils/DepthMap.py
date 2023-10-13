import os
from transformers import DPTFeatureExtractor, DPTForDepthEstimation
from PIL import Image
import requests
import torch
import numpy as np
import cv2

feature_extractor = DPTFeatureExtractor.from_pretrained("Intel/dpt-large")
model = DPTForDepthEstimation.from_pretrained("Intel/dpt-large")

imageName = 'Images/Letter-to-Frida.jpg'
image = Image.open(imageName)

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

colorized = cv2.applyColorMap(formatted, cv2.COLORMAP_INFERNO)
colorized_rgb = cv2.cvtColor(colorized, cv2.COLOR_BGR2RGB)
depth = Image.fromarray(colorized_rgb)

fileName = os.path.basename(imageName).split('/')[-1]

if not os.path.exists('DepthMap'):
    os.mkdir('DepthMap')

p2 = os.path.join('DepthMap', fileName)
grayDepth.save(p2)

p3 = os.path.join('DepthMap', 'thermal_' + fileName)
depth.save(p3)
