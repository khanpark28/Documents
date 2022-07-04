# Yolo X

## how to install yolox
## how to see the demo?

## reference



## Yolo Family history
https://pyimagesearch.com/2022/04/04/introduction-to-the-yolo-family/

### simple test Yolo v5
```
import torch
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # or yolov5m, yolov5l
img = 'https://ultralytics.com/images/zidane.jpg'  # or file, Path, PIL, OpenCV
results = model(img)
results.print()  # or .show(), .save()
```

### require pre-installed library
- pip install -U numpy
- pip install opencv-python
- pip install pandas
- pip install requests
- pip install pyyaml
- pip install Pillow
- pip install tqdm
- pip install torchvision
- pip install matplotlib
- pip install seaborn
