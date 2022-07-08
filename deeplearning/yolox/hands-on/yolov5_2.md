# Wildfire Smoke Dataset
- https://public.roboflow.com/object-detection/wildfire-smoke
- 737 images

## Download Datasets
- Make directory in yolov5 and download under it. 
```
$ curl -L "https://public.roboflow.com/ds/38ig6f2JWr?key=CDpIvfNGdg" > roboflow.zip; unzip roboflow.zip; rm roboflow.zip
```

## Datasets
- Detect smoke in the image <br>
![image](https://user-images.githubusercontent.com/106988650/178039946-56282ab9-bfeb-4055-b42e-2bc1244de950.png)
![image](https://user-images.githubusercontent.com/106988650/178040027-a848ccad-2265-46b2-9cb0-08bc54799be3.png)


## preparation
### modify data.yaml file
- to add test section

### customize the model file ( ./models/yolov5s.yaml')
- modify nc (number of classes) value to 1 since this problem just detect the smoke 

## training 
```
$ python train.py --img 640 --batch 8 --epochs 100 --data ./wildsmoke/data.yaml --cfg ./models/custom_yolov5s.yaml --weight '' --name wildsmoke_results  [ --cache]
```

## Review the result log (in jupyter notebook)
### log with tensorboard
![image](https://user-images.githubusercontent.com/106988650/178040927-032ff032-3709-41fa-b5f1-3d63c39839ea.png)

```
from IPython.display import Image
Image(filename='./runs/train/wildsmoke_results/results.png', width=1000)
```
![image](https://user-images.githubusercontent.com/106988650/178041044-563ebe56-5a05-4130-af3e-f7f742386af5.png)

```
Image(filename='./runs/train/wildsmoke_results/train_batch0.jpg', width=1000)
```
![image](https://user-images.githubusercontent.com/106988650/178041426-3169c1ac-3adb-4815-bf68-c24523ce0c97.png)


```
Image(filename='./runs/train/wildsmoke_results/val_batch0_labels.jpg', width=1000)
```
![image](https://user-images.githubusercontent.com/106988650/178041491-3f3c7839-31d7-4e7b-b844-3f262067490e.png)


```
Image(filename='./runs/train/wildsmoke_results/val_batch0_labels.jpg', width=1000)
```
![image](https://user-images.githubusercontent.com/106988650/178041539-9a927e5e-d01f-4722-b486-34bec8c7edf3.png)

## Validation
```
$ python val.py --weights runs/train/wildsmoke_results/weights/best.pt --data ./wildsmoke/data.yaml --img 640 --iou 0.65 --half
val: data=./wildsmoke/data.yaml, weights=['runs/train/wildsmoke_results/weights/best.pt'], batch_size=32, imgsz=640, conf_thres=0.001, iou_thres=0.65, task=val, device=, workers=8, single_cls=False, augment=False, verbose=False, save_txt=False, save_hybrid=False, save_conf=False, save_json=False, project=runs/val, name=exp, exist_ok=False, half=True, dnn=False
YOLOv5 🚀 v6.1-280-g27d831b Python-3.8.13 torch-1.13.0.dev20220705+cu116 CUDA:0 (NVIDIA GeForce RTX 3070 Laptop GPU, 8192MiB)

Fusing layers...
custom_YOLOv5s summary: 213 layers, 7012822 parameters, 0 gradients
val: Scanning '/home/hanee/workspace/yolov5/wildsmoke/valid/labels.cache' images and labels... 147 found, 0 missing, 0 empty, 0 corrupt: 100%|██████████| 147/147 [00:00<?, ?it/s]
               Class     Images     Labels          P          R     mAP@.5 mAP@.5:.95: 100%|██████████| 5/5 [00:02<00:00,  1.97it/s]
                 all        147        147      0.848       0.87      0.888       0.45
Speed: 0.5ms pre-process, 2.4ms inference, 3.4ms NMS per image at shape (32, 3, 640, 640)
Results saved to runs/val/exp3
```
```
$ python val.py --weights runs/train/wildsmoke_results/weights/best.pt --data ./wildsmoke/data.yaml --img 640 --task test
val: data=./wildsmoke/data.yaml, weights=['runs/train/wildsmoke_results/weights/best.pt'], batch_size=32, imgsz=640, conf_thres=0.001, iou_thres=0.6, task=test, device=, workers=8, single_cls=False, augment=False, verbose=False, save_txt=False, save_hybrid=False, save_conf=False, save_json=False, project=runs/val, name=exp, exist_ok=False, half=False, dnn=False
YOLOv5 🚀 v6.1-280-g27d831b Python-3.8.13 torch-1.13.0.dev20220705+cu116 CUDA:0 (NVIDIA GeForce RTX 3070 Laptop GPU, 8192MiB)

Fusing layers...
custom_YOLOv5s summary: 213 layers, 7012822 parameters, 0 gradients
test: Scanning '/home/hanee/workspace/yolov5/wildsmoke/test/labels' images and labels...74 found, 0 missing, 0 empty, 0 corrupt: 100%|██████████| 74/74 [00:00<00:00, 4007.06it/s]
test: New cache created: /home/hanee/workspace/yolov5/wildsmoke/test/labels.cache
               Class     Images     Labels          P          R     mAP@.5 mAP@.5:.95: 100%|██████████| 3/3 [00:01<00:00,  1.53it/s]
                 all         74         74      0.943      0.878      0.935        0.5
Speed: 0.5ms pre-process, 3.3ms inference, 3.5ms NMS per image at shape (32, 3, 640, 640)
Results saved to runs/val/exp4
```

## Inference
```
!python detect.py --weights runs/train/wildsmoke_results/weights/best.pt --img 640 --conf 0.4 --source ./wildsmoke/test/images

```


