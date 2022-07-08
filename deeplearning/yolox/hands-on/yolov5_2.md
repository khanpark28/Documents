# Wildfire Smoke Dataset
- https://public.roboflow.com/object-detection/wildfire-smoke
- 737 images

## Download images
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


## Inference
```
!python detect.py --weights runs/train/wildsmoke_results/weights/best.pt --img 640 --conf 0.4 --source ./wildsmoke/test/images

```


