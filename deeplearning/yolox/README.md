# Material Yolo

## how to install yolox
## how to see the demo?

## reference
https://www.linkedin.com/pulse/object-detection-yolo-x-veeranjaneyulu-toka/
https://curt-park.github.io/2017-03-26/yolo/
https://blog.naver.com/sogangori/220993971883
https://blog.naver.com/PostView.nhn?isHttpsRedirect=true&blogId=ehdrndd&logNo=222368500800&categoryNo=0&parentCategoryNo=0&viewDate=&currentPage=1&postListTopCurrentPage=1&from=postView
https://pjreddie.com/darknet/yolo/
https://pjreddie.com/darknet/install/#cuda
https://robocademy.com/2020/05/01/a-gentle-introduction-to-yolo-v4-for-object-detection-in-ubuntu-20-04/


## Install Yolo
https://1-1-2-3.tistory.com/7
https://1-1-2-3.tistory.com/5?category=784190
https://velog.io/@bangsy/Yolo-%EC%84%A4%EC%B9%98%ED%95%98%EA%B8%B0
https://cloudxlab.com/blog/object-detection-yolo-and-python-pydarknet/


## Implementation Yolo 
https://deep-learning-study.tistory.com/422
https://velog.io/@minkyu4506/PyTorch%EB%A1%9C-YOLOv1-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0
https://herbwood.tistory.com/14

## Yolo4 / Darknet
https://github.com/AlexeyAB/darknet
https://velog.io/@jhlee508/Object-Detection-YOLOv4-Darknet-%ED%95%99%EC%8A%B5%ED%95%98%EC%97%AC-Custom-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EC%9D%B8%EC%8B%9D-%EB%AA%A8%EB%8D%B8-%EB%A7%8C%EB%93%A4%EA%B8%B0-feat.-AlexeyABdarknet
https://sj-d.tistory.com/10
https://github.com/Tianxiaomo/pytorch-YOLOv4
https://github.com/argusswift/YOLOv4-pytorch
https://medium.com/analytics-vidhya/faster-real-time-object-detection-yolov4-in-pytorch-6eef8436ba75
https://models.roboflow.com/object-detection/yolov4-pytorch



## Yolo v5  (official https://docs.ultralytics.com/tutorials/pytorch-hub/)
https://ropiens.tistory.com/44
https://pytorch.org/hub/ultralytics_yolov5/
https://docs.ultralytics.com/tutorials/pytorch-hub/
https://www.section.io/engineering-education/object-detection-with-yolov5-and-pytorch/



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
