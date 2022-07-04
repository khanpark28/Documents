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
Torchvision is also needed, but general way to install torchvision is not recommended since it override the special version for GTX 3070, which is installed already from installation for PyTorch.

## basic knowledge

## reference for pytorch learning

- https://wikidocs.net/book/2788
