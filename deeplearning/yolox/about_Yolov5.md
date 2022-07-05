# About YoloV5
- Natively implemented in PyTorch, eliminating the Darkent framework's limitations (based on C programming language and not built with production environments perpective).
- Easy to modify the architecture and export to many deployment environments straightforwardly. (because of PyTorch)

```
import torch
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # or yolov5m, yolov5l
img = 'https://ultralytics.com/images/zidane.jpg'  # or file, Path, PIL, OpenCV
results = model(img)
results.print()  # or .show(), .save()
```

## Tutorials for YOLOV5
[Training on Custom Dataset](https://github.com/ultralytics/yolov5/wiki/Train-Custom-Data)
[Multi-GPU Training] (https://github.com/ultralytics/yolov5/issues/475)
[Exporting the trained YOLOv5 model on TensorRT, CoreML, ONNX, and TFLite] (https://github.com/ultralytics/yolov5/issues/251)
[Pruning the YOLOv5 architecture] (https://github.com/ultralytics/yolov5/issues/304)
[Deployment with TensorRT] (https://github.com/wang-xinyu/tensorrtx)
