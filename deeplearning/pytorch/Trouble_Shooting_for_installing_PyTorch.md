# Ubuntu-20.04-clean

## Situation
```
>>> torch.tensor([1,2], device='cuda')
/home/hanee/anaconda3/envs/torch/lib/python3.8/site-packages/torch/cuda/__init__.py:146: UserWarning:
NVIDIA GeForce RTX 3070 Laptop GPU with CUDA capability sm_86 is not compatible with the current PyTorch installation.
The current PyTorch install supports CUDA capabilities sm_37 sm_50 sm_60 sm_70.
If you want to use the NVIDIA GeForce RTX 3070 Laptop GPU GPU with PyTorch, please check the instructions at https://pytorch.org/get-started/locally/

  warnings.warn(incompatible_device_warn.format(device_name, capability, " ".join(arch_list), device_name))
tensor([1, 2], device='cuda:0')

>>> torch.cuda.get_device_name()
/home/hanee/anaconda3/envs/torch/lib/python3.8/site-packages/torch/cuda/__init__.py:146: UserWarning:
NVIDIA GeForce RTX 3070 Laptop GPU with CUDA capability sm_86 is not compatible with the current PyTorch installation.
The current PyTorch install supports CUDA capabilities sm_37 sm_50 sm_60 sm_70.
If you want to use the NVIDIA GeForce RTX 3070 Laptop GPU GPU with PyTorch, please check the instructions at https://pytorch.org/get-started/locally/

  warnings.warn(incompatible_device_warn.format(device_name, capability, " ".join(arch_list), device_name))
'NVIDIA GeForce RTX 3070 Laptop GPU'

(torch) hanee@DESKTOP-9PA5FSC:/usr/local/cuda-11.4/bin$ ./nvcc --version
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2021 NVIDIA Corporation
Built on Wed_Jun__2_19:15:15_PDT_2021
Cuda compilation tools, release 11.4, V11.4.48
Build cuda_11.4.r11.4/compiler.30033411_0

(torch) hanee@DESKTOP-9PA5FSC:/usr/lib/wsl/lib$ ./nvidia-smi
Tue Jul  5 09:53:56 2022
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 510.73.08    Driver Version: 512.96       CUDA Version: 11.6     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  NVIDIA GeForce ...  On   | 00000000:01:00.0  On |                  N/A |
| N/A   38C    P8    12W /  N/A |   1399MiB /  8192MiB |      1%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+

+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|  No running processes found                                                 |
+-----------------------------------------------------------------------------+
```

## Problems & expected reasons

0. toolkit을 설치할 때 일반 패키지로 설치하는 바람에 driver 가 자동으로 설치되어 unexpected behavior 가 발생함. 
1. windows 에 설치된 driver 의 cuda version (11.6) 과 wsl 안에 설치된 cuda toolkit 의 version (11.4) 이 다르다. 
2. Torchvision  설치한 후부터 compatibility 이슈가 다시 나기 시작함. RTX 3070 Laptop CUDA capability 가 sm_86 으로 정의되어 있는데, PyTorch 의 특정 라이브러리 혹은 전체가 torchvision 을 설치할 때 override 되면서 지원하지 않는 것으로 바뀌는 듯
3. 새로 설치되는 pytorch 버전은 sm_37, sm_50, sm_60, sm_70 만 지원하며, sm_80 은 지원하지 않음. 

## To do 
1. Check what is sm_60, sm_70, sm_80, ...
2. install torchvision with specific version <= apt install torchvision 은 자동으로 pytorch 를 override 함.  그렇다면 더 높은 버전을 강제로 설치하게 하거나, ..
3. install toolkit with 11.6 version <= 현재 11.4 로 잘못 설치중. 


## Result
1. 기본 이미지로 다시 세팅 
2. Windows 에 Nvidia GPU driver 설치(Done already)
3. Ubuntu 에서 cuda 11.6 버전 cuda toolkit for WSL 버전 설치함
4. PyTorch 를  CUDA, WSL 버전으로 설치
5. pip install opencv-python 으로 opencv 설치
6. Torchvision 을 source build 로 설치
7. 테스트 OK 
