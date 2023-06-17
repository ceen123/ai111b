Ultralytics YOLOv5 🚀 is a cutting-edge, state-of-the-art (SOTA) model that builds upon the success of previous YOLO versions and introduces new features and 
improvements to further boost performance and flexibility. YOLOv5 is designed to be fast, accurate, and easy to use, making it an excellent choice for a wide 
range of object detection, instance segmentation and image classification tasks.

> pip install -U ultralytics

![yolo-comparison-plots](https://github.com/ceen123/ai111b/assets/79678068/d6d5d3ed-40ae-40ad-8b9b-a3b33680e58c)

# Collect dataset or use publically available dataset
The very first step of an object detection project is to obtain data for training. You can either download datasets available publicly or create your own dataset! Usually public datasets are used for education and research purposes. However, if you want to build specific object detection projects where the public datasets do not have the objects that you want to detect, you might want to build your own dataset.

## Create dataset manually
It is recomended to collect your own data depends on what you want your AI able to detect. For my project Im using [https://www.makesense.ai/](https://www.makesense.ai/)
to create the lables to train the AI how to detect Images.
![image](https://github.com/ceen123/ai111b/assets/79678068/a9b59465-7c51-4df3-be50-bc0c1bed4551)
![image](https://github.com/ceen123/ai111b/assets/79678068/4f4ff6b6-0c2f-4f6b-a335-35632ccf3b4b)

The website provide the user to manually select the object in the image, in the picture for example. I selected the object of a chicken in the image by squaring the object.
![image](https://github.com/ceen123/ai111b/assets/79678068/11b66ad8-7c08-4b9f-9c8a-eb4785477113)

Then the website will provide the user the labels to allow YOLOv5 to train the AI to recognize the object in the image, which is a chicken.
![image](https://github.com/ceen123/ai111b/assets/79678068/bdad1eeb-a010-4e1e-8866-2cdd460f517e)


![image](https://github.com/ceen123/ai111b/assets/79678068/226b6de8-e416-4742-bfaf-21ab26e3ed66)

## How does Yolov5 works?
<p>
To understand how Yolov5 improved the performance and its architecture, let us go through the following high-level Object detection architecture:
![image](https://github.com/ceen123/ai111b/assets/79678068/b1c563d0-71e3-4d67-b957-f2b40c988a3a)
</p>
<p>
General Object Detector will have a backbone for pre-training it and a head to predict classes and bounding boxes. The Backbones can be running on GPU or CPU platforms. The Head can be either one-stage (e.g., YOLO, SSD, RetinaNet) for Dense prediction or two-stage (e.g., Faster R-CNN ) for the Sparse prediction object detector. Recent Object detectors have some layers (Neck) to collect feature maps, and it is between the backbone and the Head.
</p>
<p>
In YOLOv4, CSPDarknet53 is used as a backbone and SPP block for increasing the receptive field, which separates the significant features, and there is no reduction of the network operation speed. PAN is used for parameter aggregation from different backbone levels. YOLOv3 (anchor-based) head is used for YOLOv4.
</p>
<p>
YOLOv4 introduced new methods of data augmentation Mosaic and Self-Adversarial Training (SAT). Mosaic mixes four training images. Self-Adversarial Training operates in two forward and backward stages. In the 1st stage, the network alters the only image instead of the weights. In the second stage, the network is trained to detect an object on the modified image.
</p>
![image](https://github.com/ceen123/ai111b/assets/79678068/83452e38-54a9-4589-bd15-76e07006804c)

### YOLOv5s model displayed in Netron
![image](https://github.com/ceen123/ai111b/assets/79678068/77697907-c150-46c3-a9ea-aab1f777f474)

### YOLOv5s model displayed in TensorBoard
![image](https://github.com/ceen123/ai111b/assets/79678068/8f514286-1103-4767-929d-15f617dfdead)


## Examples of project made by YOLOv5 to detect Blood Cells
![image](https://github.com/ceen123/ai111b/assets/79678068/ff82b66c-9433-49a1-bf34-f56813999125)


## YOLOv5 also uses Auto Learning Bounding Box Anchors
<p>
In the YOLOv3 PyTorch repo, Glenn Jocher introduced the idea of learning anchor boxes based on the distribution of bounding boxes in the custom dataset with K-means and genetic learning algorithms. This is very important for custom tasks, because the distribution of bounding box sizes and locations may be dramatically different than the preset bounding box anchors in the COCO dataset.
</p>
<p>
In order to make box predictions, the YOLOv5 network predicts bounding boxes as deviations from a list of anchor box dimensions.
</p>
![image](https://github.com/ceen123/ai111b/assets/79678068/8ec00169-fb54-47eb-bbc7-6e0d4be58cee)
<p>
  The most extreme difference in anchor boxes may occur if we are trying to detect something like giraffes that are very tall and skinny or manta rays that are very wide and flat. All YOLO anchor boxes are auto-learned in YOLOv5 when you input your custom data.
</p>
```
# parameters
nc: 80  # number of classes
depth_multiple: 0.33  # model depth multiple
width_multiple: 0.50  # layer channel multiple

# anchors
anchors:
  - [116,90, 156,198, 373,326]  # P5/32
  - [30,61, 62,45, 59,119]  # P4/16
  - [10,13, 16,30, 33,23]  # P3/8

# YOLOv5 backbone
```




