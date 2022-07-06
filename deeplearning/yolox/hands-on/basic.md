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
### result of Object detection
- box
- position
- class
- confidence

### application
- autonomous car
- medical : x-ray, MRI, ...
- robot in manufactual 
- security : counting number of people. CCTV, ...

### Bounding Box
- smallest box which capture object

### IOU (Intersection over Union)

IOU = Area of Overlap / Area of Union

- ground truth , real object -> how exactly predict the boundbox? 
- Intersection value check
- Highter IOU value is good 
- 정답과 예측값이 얼마나 겹치는지 확인-> 값이 크면 클수록 성능이 좋은 것임
- 전체 합 대비 얼마나 IOU 를 가지냐 -> 이것이 모델의 성능


### NMS (Non-maximum Suppression, 비최대값 억제)
- 확률이 가장 높은 상자와 겹치는 상자들을 제거하는 과정
- 최대값을 갖지 않는 상자들을 제거
- (box 가 여러개 나올 때, 가장 놓은 것만 놔 두고, 나머지는 제거하는 과정)
- 확률 기준으로 모든 상자를 정렬 / 그중에 높은 것만 취한다. 


## Evaluation of model performance
### Precision(정밀도)  & Recall(재현율)

- True Positive (TP: 예측이 동일 클래스의 실제 상자와 일치하는지 측정)
- False Positive (FP : 예측이 실제 상자와 일치하지 않는지 측정)
- False Negative (FN : 실제 분류값이 그와 일치하는 예측을 갖지 못하는지 측정=> 아니라고 했는데 실제 맞는 경우, Negative 를 실패함) 

- Precision = TP (TP + FP)
- recall = Tp (TP + FN)
모델이 안정적이지 않은 특징을 기반으로 객체 존재를 예측하면, 거짓긍정(FP) 이 많아져서 정밀도가 낮아짐. 즉 아닌데도 자꾸 맞다고 하니까 정확도가 떨어짐.
- 모델이 너무 엄격해서 정확한 조건을 만족할 때만 객체가 탐지된 것으로 간주하면, 거짓부정(FN) 이 많아져서 재현율이 낮아짐 , 즉 엄격해서 적당히 맞는데로 불구하고 아니라고 하니까 recall 즉 재현율이 낮아짐. 

### Precision-Recall Curve (정밀도-재현율 곡선)
- 신뢰도 임계값마다 모델의 정밀도와 재현율을 시각화
- 모든 bbox  와 함께 모델이 예측의 정확성을 얼마나 확실하는지 0~1 사이의 숫자로 나타냄
- 임계값 T 에 따라서 정밀도와 재현율이 달라짐
 - 임계값 T 이하의 예측은 제거함
 - T 가 1에 가까우면 정밀도는 높지만 재현율은 낮음, 재현율은 낮아지지만 정밀도가 높아짐
 - T 가 0에 가까우면 정밀도는 낮지만 재현율은 높음. 재현율이 높아지고 거짓 긍정이 많아짐
- 목적에 따라 임계값이 달라져야 함 
 - 자율주행일 경우, 보행자를 예측하는 값. 가능한 재현율이 높아야 함. 사고나면 큰일남
 - 투자기회 탐지일 경우: 기회를 놓치더라도 정확도가 높은 모델을 만들어야 함, 잘못된 기회에 돈을 투자하면 안되기 때문에 

### AP (Average Precision 평균 정밀도), 와 mAP(ean Average Precision)
- 곡선 아래의 영역을 의미
- 단일 클래스에 대한 모델 성능 정보를 제공함 -> 여기서 클래스는 각 분류
 - 각 모델을 얼마나 잘 분류하는가. 
- 전역 점수를 얻기 위해서 mAP 를 사용. 데이터셋이 10개의 클래스로 구분된다면, 각 클래스에 대한 AP 를 계산하고, 그 숫자들의 평균을 다시 구함. 
- 최소 2개 이상의 객체를 탐지하는 대회인 곳에서 (PASCAL visual object classes ) 에서 mAP 사용됨
- COCO dataset 이 더 많은 클래스를 포함하고 있기 때문에 보통 Pascal VOC 보다 점수가 더 낮게 나옴.
- COCO (Common Object in Context)
    
## Dataset 
### VOC dataset
- 2005~2012
- object detection 의 benchmark 로 간주
- 20개의 클래스 존재

### COCO dataset
- 굉장히 방대한 데이터
- 200,000 images
- 80 categories, over 500,000 object annotation

## Yolo
- 가장 빠른 객체 검출 알고리즘 중 하나
- 작은 물체 탐지 어려움


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

