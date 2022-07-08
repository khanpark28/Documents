# Hard Hat detection
- https://public.roboflow.com/object-detection/hard-hat-workers
- 7041 images

## Dataset download
- download resize images
- only contains train and test images
```
curl -L "https://public.roboflow.com/ds/LCyi29rUCY?key=Y1KktqzoGI" > roboflow.zip; unzip roboflow.zip; rm roboflow.zip
```

## Preparation
- split image for validation since downloaded dataset does not contain validation set
```
from glob import glob
import yaml

train_img_list = glob('/home/hanee/workspace/yolov5/hardhat/train/images/*.jpg')
test_img_list = glob('/home/hanee/workspace/yolov5/hardhat/test/images/*.jpg')
print(len(train_img_list), len(test_img_list))

from sklearn.model_selection import train_test_split
test_img_list, val_img_list = train_test_split(test_img_list, test_size=0.5, random_state=777)
print(len(tetst_img_list), len(val_img_list))

with open('/home/hanee/workspace/yolov5/hardhat/train.txt', 'w') as f:
  f.write('\n'.join(train_img_list) + '\n')
  
with open('/home/hanee/workspace/yolov5/hardhat/val.txt', 'w') as f:
  f.write('\n'.join(val_img_list) + '\n')
  
with open('/home/hanee/workspace/yolov5/hardhat/test.txt', 'w') as f:
  f.write('\n'.join(test_img_list) + '\n')
```

