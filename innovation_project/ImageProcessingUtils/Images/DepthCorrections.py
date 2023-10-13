import os
from transformers import DPTFeatureExtractor, DPTForDepthEstimation
from PIL import Image
import requests
import torch
import numpy as np
import cv2
import matplotlib.pyplot as plt

feature_extractor = DPTFeatureExtractor.from_pretrained("Intel/dpt-large")
model = DPTForDepthEstimation.from_pretrained("Intel/dpt-large")

imageName = 'Docs/Mona_Lisa/Original.jpg'
fileName = os.path.basename(imageName).split('/')[-1]

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

np.save('DepthMap/' + fileName + '.data', output)

output = np.clip(output, 0, 30)
output = np.log(output)



formatted = (output * 255 / np.max(output)).astype('uint8')
depth = Image.fromarray(formatted)

fileName = os.path.basename(imageName).split('/')[-1]

if not os.path.exists('DepthMap'):
    os.mkdir('DepthMap')

p2 = os.path.join('DepthMap', fileName)
depth.save(p2)

flat_output = output.flatten()
flat_output = np.clip(flat_output, 0, 1000)

cv2.imshow('Depth Map', formatted)

plt.hist(flat_output, bins='auto')
plt.show()