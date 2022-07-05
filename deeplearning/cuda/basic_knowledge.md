You should have NVIDIA driver installed on your system, as well as Nvidia CUDA toolkit, aka, CUDA.

CUDA (Computed Unified Device Architecture)
-> NVIDIA 에서 개발한 GPU 개발 툴. CUDA 는 C,C++ 기반으로 짜여진 완전 기초적 H/W 접근을 해야 하는데, 많은 연구자들이
딥러닝에 사용할 수 있도록, 쉽게 설치할 수 있도록 오픈함. 
그래서 nvidia-driver / CUDA / CUDNN 만 설치하면 딥러닝 사용이 가능함.

- nvidia-driver : H/W access API
- CUDA : wrapper layer or basic handling module for nvidia-driver
- CUDNN : Neural Net 을 위한 libraries



CUDA is a general parallel computing architecture and programming model developed by NVIDIA for its graphics cards.
Using CUDA, PyTorch or TensorFlow developers will dramatically increase the performance of PyTorch or TensorFlow training models, utilizing GPU resources effectively.
