# Converting Monocular Images to 3D Models

## Step 1 - Find an Image

![alt text](Docs/Mona_Lisa/Original.jpg "Mona Lisa")

## Step 2 - Get a depth map of the image

Use `DepthMap.py` to generate the depth map.

![alt text](Docs/Mona_Lisa/DepthMap.jpg "Depth map of the Mona Lisa")

## Step 3 - Get the edges of the original image

Use the `Canny` or `Sobel` function in `EdgeDetection.py` to get the edges of the images.

![alt text](Docs/Mona_Lisa/Edges.jpg "Canny edges of the Mona Lisa")

## Get the weighted merge of the two images

This step is not a separate step and is included in `ToSTL_memrged.py`. However, if you just want to see just the image form of this data, you can use `ToJPG_merged.py`.

![alt text](Docs/Mona_Lisa/Combined.jpg "Depth + Edge details of the Mona Lisa")

## Convert it to an STL with height proportional to the intensity of the corresponding pixel

Use `ToSTL_memrged.py` to get convert the depth map and edge data into a 3D model.

![alt text](Docs/Mona_Lisa/STL_Preview.jpg "3D model of the Mona Lisa")

## 3D Print your model

Use your favorite 3D printer to print your model.

![alt text](Docs/Mona_Lisa/3D_Print.jpg "Tactile 3D print of the Mona Lisa")

# Other examples

## [The Great Wave of Kanagawa](Docs/Great_Wave/README.md)

![alt text](Docs/Great_Wave/Great_Wave.jpg "Great Wave")   ![alt text](Docs/Great_Wave/Great_Wave_Depth_Combined.jpg "Depth + Edge details of the Great Wave")

Image caption: `the great wave off kanagawa`

## [Starry Night](Docs/Starry_Night/)

![alt text](Docs/Starry_Night/Starry_Night.jpg "Starry Night")   ![alt text](Docs/Starry_Night/Starry_Night_Combined.jpg "Depth + Edge details of Starry Night")

Image caption: `the starry night by van gogh`

## [Starry Night Simple](Docs/Starry_Night_Simple/)

![alt text](Docs/Starry_Night_Simple/Starry_Night_Simple.jpg "Starry Night Simple" )   ![alt text](Docs/Starry_Night_Simple/Starry_Night_Simple_Combined.jpg "Depth + Edge details of Starry Night Simple")

Image caption: `the starry night by van gogh`

## [Starry Night Simplest](Docs/Starry_Night_Simplest/)

![alt text](Docs/Starry_Night_Simplest/StarryNight_Simplest.jpg "Starry Night Simplest" )   ![alt text](Docs/Starry_Night_Simplest/StarryNight_Simplest_Combined.jpg "Depth + Edge details of Starry Night Simplest")

Image caption: `the art of the simpsons`
