## COCO Dataset
- Data format for machine learning
- Purpose
  - object detection
  - segmentation
  - keypoint detection. 

- object detection paper (for computer vision) COCO 2017
- 많은 라이브러리들이 COCO Dataset 으로 사전 학습된 (pre-trained) 모델 제공. 

  - training dataset : 118,000
  - validation dataset: 5,000
  - test : 41,000

## Yolo & Darknet ??
- Darknet NN framework implemented with C. Many projects might be implemented using Darknet.
```
$ ./darknet detect cfg/yolov3.cfg yolove3.weight data/dog.jpg  
```
Darknet is general fw. For using it, just pass cfg (which might be NN structure for Yolo) weight and target image.
어느정도 검증이 된 FW 이므로, Darknet 를 써서 NN 을 구현하고 테스트 하기 용이하다. 그래서 Yolo 도 darknet을 통해 구현함.

다만 Darknet 은 C 로 구현이 되었고, 다른 언어(python)들을 써서, Yolo 구현도 가능함.


https://datascience.stackexchange.com/questions/65945/what-is-darknet-and-why-is-it-needed-for-yolo-object-detection
Darknet : Open Source Nerual Network in C and CUDA (fast, easy to install??? supports CPU and GPU computation.)


## Ojbect detection
1. Based on Traditional Computer Vision
2. Two-stage deep learning based algorithms
3. The third one is Single-Stage Deep Learning based algorithms
