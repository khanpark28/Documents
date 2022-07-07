(Running on Jupyter notebook)

## Running Yolov5 training & inference

### Purpose 
- Detecting pothole
- pothole dataset : https://public.roboflow.com/object-detection/pothole
 - Image from roboflow
 - 655 images

### Download Yolov5 and images
```
git clone https://github.com/ultralytics/yolov5
cd yolov5
%mkdir pothole
!curl -L "https://public.roboflow.com/ds/VFkK3jL73D?key=fcA9ufK03w" > roboflow.zip; unzip roboflow.zip; rm roboflow.zip <- exmple, would be difference for each user
```

### List up train, valid and test image files
```
from glob import glob
import yaml

train_img_list = glob('/home/hanee/workspace/yolov5/pothole/train/images/*.jpg')
valid_img_list = glob('/home/hanee/workspace/yolov5/pothole/valid/images/*.jpg')
test_img_list = glob('/home/hanee/workspace/yolov5/pothole/test/images/*.jpg')

len(train_img_list)+ len(valid_img_list)+ len(test_img_list)

with open('/home/hanee/workspace/yolov5/pothole/train.txt', 'w') as f:
    f.write('\n'.join(train_img_list) + '\n')
with open('/home/hanee/workspace/yolov5/pothole/valid.txt', 'w') as f:
    f.write('\n'.join(valid_img_list) + '\n')
with open('/home/hanee/workspace/yolov5/pothole/test.txt', 'w') as f:
    f.write('\n'.join(test_img_list) + '\n')
    
```

### Using magic function for edit files
```
from IPython.core.magic import register_line_cell_magic

@register_line_cell_magic
def writetemplate(line, cell):
    with open(line, 'w') as f:
        f.write(cell.format(**globals()))
```

```
%%writetemplate /home/hanee/workspace/yolov5/pothole/data.yaml

train: ./pothole/train/images
test: ./pothole/test/images
val: ./pothole/valid/images

nc: 1
names: ['pothole']
```

/home/hanee/workspace/yolov5/pothole/data.yaml file would be changed like
from
```
train: ../train/images
val: ../valid/images

nc: 1
names: ['pothole']
```
to 
```
train: ./pothole/train/images
test: ./pothole/test/images
val: ./pothole/valid/images

nc: 1
names: ['pothole']
```

### Customize model file (yolov5s.yaml)
The number of class is set as 80 as default values in yolov5.yaml which is a kind of model file for yolov5. But Pothole detect problem is a problem for whether detecting pothole or not.
So do not need a such big number of class but need a just 1 class. So fix it as 1 of numcer of class. 

```
import yaml
with open("/home/hanee/workspace/yolov5/pothole/data.yaml", 'r') as stream:
    num_classes = str(yaml.safe_load(stream)['nc'])
```
```
%%writetemplate /home/hanee/workspace/yolov5/models/custom_yolov5s.yaml

# Parameters
nc: {num_classes}  # number of classes
depth_multiple: 0.33  # model depth multiple
width_multiple: 0.50  # layer channel multiple
anchors:
  - [10,13, 16,30, 33,23]  # P3/8
  - [30,61, 62,45, 59,119]  # P4/16
  - [116,90, 156,198, 373,326]  # P5/32

# YOLOv5 v6.0 backbone
backbone:
  # [from, number, module, args]
  [[-1, 1, Conv, [64, 6, 2, 2]],  # 0-P1/2
   [-1, 1, Conv, [128, 3, 2]],  # 1-P2/4
   [-1, 3, C3, [128]],
   [-1, 1, Conv, [256, 3, 2]],  # 3-P3/8
   [-1, 6, C3, [256]],
   [-1, 1, Conv, [512, 3, 2]],  # 5-P4/16
   [-1, 9, C3, [512]],
   [-1, 1, Conv, [1024, 3, 2]],  # 7-P5/32
   [-1, 3, C3, [1024]],
   [-1, 1, SPPF, [1024, 5]],  # 9
  ]

# YOLOv5 v6.0 head
head:
  [[-1, 1, Conv, [512, 1, 1]],
   [-1, 1, nn.Upsample, [None, 2, 'nearest']],
   [[-1, 6], 1, Concat, [1]],  # cat backbone P4
   [-1, 3, C3, [512, False]],  # 13

   [-1, 1, Conv, [256, 1, 1]],
   [-1, 1, nn.Upsample, [None, 2, 'nearest']],
   [[-1, 4], 1, Concat, [1]],  # cat backbone P3
   [-1, 3, C3, [256, False]],  # 17 (P3/8-small)

   [-1, 1, Conv, [256, 3, 2]],
   [[-1, 14], 1, Concat, [1]],  # cat head P4
   [-1, 3, C3, [512, False]],  # 20 (P4/16-medium)

   [-1, 1, Conv, [512, 3, 2]],
   [[-1, 10], 1, Concat, [1]],  # cat head P5
   [-1, 3, C3, [1024, False]],  # 23 (P5/32-large)

   [[17, 20, 23], 1, Detect, [nc, anchors]],  # Detect(P3, P4, P5)
  ]
```

### 
