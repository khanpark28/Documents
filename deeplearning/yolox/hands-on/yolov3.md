## Hands on Jupyter notebook
Running YoloV3 with pre-trained Model

### Run Jupyter Server
```
$ jupyter notebook
(yolo3_test) hanee@DESKTOP-9PA5FSC:~$ jupyter notebook
[I 01:29:45.396 NotebookApp] Writing notebook server cookie secret to /home/hanee/.local/share/jupyter/runtime/notebook_cookie_secret
[I 2022-07-07 01:29:45.688 LabApp] JupyterLab extension loaded from /home/hanee/anaconda3/envs/yolo3_test/lib/python3.8/site-packages/jupyterlab
[I 2022-07-07 01:29:45.688 LabApp] JupyterLab application directory is /home/hanee/anaconda3/envs/yolo3_test/share/jupyter/lab
[I 01:29:45.691 NotebookApp] Serving notebooks from local directory: /home/hanee
[I 01:29:45.691 NotebookApp] Jupyter Notebook 6.4.8 is running at:
[I 01:29:45.691 NotebookApp] http://localhost:8888/?token=d18b04fda35d857337058a411784ac53e9de859901dbe39f
[I 01:29:45.691 NotebookApp]  or http://127.0.0.1:8888/?token=d18b04fda35d857337058a411784ac53e9de859901dbe39f
[I 01:29:45.691 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[C 01:29:45.697 NotebookApp]

    To access the notebook, open this file in a browser:
        file:///home/hanee/.local/share/jupyter/runtime/nbserver-16724-open.html
    Or copy and paste one of these URLs:
        http://localhost:8888/?token=d18b04fda35d857337058a411784ac53e9de859901dbe39f
     or http://127.0.0.1:8888/?token=d18b04fda35d857337058a411784ac53e9de859901dbe39f
```

### Access jupyter in brower
- localhost:xxxx 
- login with token represented in starting log of Jupyter Server

### Download YoloV3
```
$ git clone https://github.com/ultralytics/yolov3
$ cd yolov3
```

### check image before inference
```
import torch
from IPython.display import Image, clear_output
Image(filename='data/images/bug.jpg', width=600)
Image(filename='data/images/zidane.jpg', width=600)
```
![image](https://user-images.githubusercontent.com/106988650/177858610-4fb8bcfb-af9f-4a99-a5ef-ea19f33c435e.png)
![image](https://user-images.githubusercontent.com/106988650/177858593-244c609e-9855-400d-bd76-9957156aa33e.png)


### Inference with pre-trained model
```
!python detect.py --weights yolov5s.pt --img 640 --conf 0.25 --source data/images
```
![image](https://user-images.githubusercontent.com/106988650/177858405-ad0be307-1f83-45e1-bda3-d253de50b29e.png)
![image](https://user-images.githubusercontent.com/106988650/177858356-48a186a9-b3e0-4a82-b4d1-020a9c30dd3d.png)
