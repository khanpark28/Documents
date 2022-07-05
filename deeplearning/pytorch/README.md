# About PyTorch

## install pytorch

### Install Anaconda

- https://problemsolvingwithpython.com/01-Orientation/01.05-Installing-Anaconda-on-Linux/
- https://clouds.eos.ubc.ca/~phil/docs/problem_solving/01-Orientation/01.05-Installing-Anaconda-on-Linux.html
- https://repo.anaconda.com/archive/
```
wget https://repo.anaconda.com/archive/Anaconda3-2022.05-Linux-x86_64.sh
```

### Need a specific version of PyTorch for GTX 3070 for Laptop (sm_86)
```
pip install torch --pre --extra-index-url https://download.pytorch.org/whl/nightly/cu116
```

### Additional python package for running YoloV5 with PyTorch
```
pip install opencv-python
(pip install torchvision) <- NOT RECOMMENDED
```

Torchvision is also needed, but general way to install torchvision is not recommended since it override the special version for RTX 3070, which is installed already from installation for PyTorch.

#### Before install torchvision with 'pip install torchvision'
```
torch                     1.13.0.dev20220705+cu116          pypi_0    pypi
```
#### After install torchvision with 'pip install torchvision'
```
torch                     1.12.0                   pypi_0    pypi
torchvision               0.13.0                   pypi_0    pypi
```

### Install specific version of torchvision
- https://pypi.org/project/torchvision/
- https://pytorch.kr/get-started/previous-versions/
- https://discuss.pytorch.org/t/pytorch-cuda-11-6/149647
- https://discuss.pytorch.org/t/pytorch-with-cuda-11-compatibility/89254/21
- https://stackoverflow.com/questions/72012334/pytorch-cuda-version-vs-nvidia-cuda-version
```
COMMAND
```
## basic knowledge

## reference for pytorch learning

- https://wikidocs.net/book/2788
