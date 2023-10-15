import torch
from PIL import Image

# Model
model = torch.hub.load('ultralytics/yolov5n', 'yolov5s')
im1 = Image.open('Images/Last_Supper.jpg')  # PIL image

# Inference
results = model([im1], size=640) # batch of images

# Results
results.print()
results.show()

