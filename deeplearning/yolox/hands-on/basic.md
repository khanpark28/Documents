Yolov5 는 pytorch, 즉 python 으로 구현된 model or application

darknet 에서 ./darknet detect cfg/yolov3.cfg yolov3.weight image1.jpg 라고 했던 것처럼 yolov5 도 python 을 이용해서 아래와 같이 실행 가능함 
```
$ python detect.py --weight yolov5.pt --img 640 --conf 0.25  --source data/images
```

darknet 자체가 굉장히 범용적인 FW 이므로 cfg으로 yolo관련 설정을 명시했지만,  yolov5 는 그 자체로 yolov5 위한 모델을 구현한 파일이기 때문에 python detect.py 으로 실행이 가능함
