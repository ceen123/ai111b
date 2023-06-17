to install fastai
```
!pip install -Uqq fastai
from fastai.vision.all import *
```

to train the AI using the data I mapped in the ../data/images/training and ../data/images/validation
```
!python train.py --img 640 --batch 2 --epochs 60 --data test_data.yaml --weights yolov5s.pt --cache
```

for the detection I downloaded a random image of chicken and place it in the folder, then detect the image for an object 'chicken'
```
!python detect.py --weights yolov5s.pt --img 640 --conf 0.25 --source ../chicken.jpg
```
the image downloaded
![chicken1](https://github.com/ceen123/ai111b/assets/79678068/b6febbbb-20d8-4fa4-862c-395f924a8b65)

the image after processed
![image](https://github.com/ceen123/ai111b/assets/79678068/b9ed33cb-6c51-41ec-a04f-b5f2c61fd88c)
