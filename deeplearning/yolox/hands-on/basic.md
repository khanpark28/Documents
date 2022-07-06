## Basic YoloV5
Yolov5 는 pytorch, 즉 python 으로 구현된 model or application

darknet 에서 ./darknet detect cfg/yolov3.cfg yolov3.weight image1.jpg 라고 했던 것처럼 yolov5 도 python 을 이용해서 아래와 같이 실행 가능함 
```
$ python detect.py --weight yolov5.pt --img 640 --conf 0.25  --source data/images
```

darknet 자체가 굉장히 범용적인 FW 이므로 cfg으로 yolo관련 설정을 명시했지만,  yolov5 는 그 자체로 yolov5 위한 모델을 구현한 파일이기 때문에 python detect.py 으로 실행이 가능함


## 
https://www.youtube.com/watch?v=fdWx3QV5n44

## Object Detection
### application

### Bounding Box


### IOU (Intersection over Union)

IOU = Area of Overlap / Area of Union


### NMS (Non-maximum Suppression, 비최대값 억제)
- 확률이 가장 높은 상자와 겹치는 상자들을 제거하는 과정
- 최대값을 갖지 않는 상자들을 제거


## Evaluation of model performance
### Precision(정밀도)  & Recall(재현율)

- True Positive
- False Positive
- False Negative

### Precision-Recall Curve (정밀도-재현율 곡선)

### AP (Average Precision 평균 정밀도), 와 mAP(ean Average Precision)


## Dataset 
### VOC dataset
### COCO dataset



## Yolo
### Yolo Architecture
### Yolo layer output

## Anchor Box
- YoloV2 에서 도입
- 사전 정의된 상자
- 객체에 가장 근접한 앵커 박스를 맞추고 신경망을 사용해 앵커 박스의 크기를 조정하는 과정 때문에 tx, ty, tw, th이 필요

## Yolov3 Model 
### Model
### Inference

## Yolov5 Model
### Model
### Inference

## Porthole detect Model
### dataset download
### Model structure
### Training
### Validation
### Inference
### Model expouser

## Smoke detect Model
### dataset download
### Model structure
### Training
### Validation
### Inference
### Expose Model

## Safe Helmet detect Model
### dataset download
### Model structure
### training
### Validation
### Inference
### Expose Model

## Partlot detect Model
### dataset download
### Model structure
### training
### Validation
### Inference
### Expose Model

