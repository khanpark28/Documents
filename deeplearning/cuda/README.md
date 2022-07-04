Esstional for cuda in WSL


# NVIDA driver (might be at Window)
  - https://www.nvidia.com/Download/driverResults.aspx/190349/en-us/
  - https://developer.nvidia.com/cuda/wsl

# Nvidia CUDA toolkit
  - To compile new CUDA applications, a CUDA Toolkit for Linux x86 is needed.
  - CUDA toolkit support for WSL is still in preview stage as developer tool such as debugger and profilers are not available yet.
  - When NVIDA drvier for window is installed, CUDA becomes available within WSL2. 
  - The CUDA driver installed on Windows host will be stubbed inside the WSL2 as libcuda.so
  - https://docs.nvidia.com/cuda/wsl-user-guide/index.html

```	
	wget https://developer.download.nvidia.com/compute/cuda/repos/wsl-ubuntu/x86_64/cuda-wsl-ubuntu.pin	
	sudo mv cuda-wsl-ubuntu.pin /etc/apt/preferences.d/cuda-repository-pin-600	
	wget https://developer.download.nvidia.com/compute/cuda/11.4.0/local_installers/cuda-repo-wsl-ubuntu-11-4-local_11.4.0-1_amd64.deb	
	sudo dpkg -i cuda-repo-wsl-ubuntu-11-4-local_11.4.0-1_amd64.deb	
	sudo apt-key add /var/cuda-repo-wsl-ubuntu-11-4-local/7fa2af80.pub	
	sudo apt-get update	
	sudo apt-get -y install cuda	
```

  - reference
    - https://0verc10ck.tistory.com/43

# Nvidia cuDNN
  - https://developer.nvidia.com/cudnn 
  - https://saltcoffee.tistory.com/entry/WSL2%EB%A1%9C-CUDA-%EA%B0%9C%EB%B0%9C%ED%99%98%EA%B2%BD-%EA%B5%AC%EC%84%B1%ED%95%98%EA%B8%B0
    -> install cuDNN & related

# Install Python with Anaconda
## install Anaconda
  - https://problemsolvingwithpython.com/01-Orientation/01.05-Installing-Anaconda-on-Linux/
  - https://clouds.eos.ubc.ca/~phil/docs/problem_solving/01-Orientation/01.05-Installing-Anaconda-on-Linux.html
  - https://repo.anaconda.com/archive/
  ```
  wget https://repo.anaconda.com/archive/Anaconda3-2022.05-Linux-x86_64.sh
  ```
  ### create conda environment
  conda create -n [env_name] [python=python_version] anaconda
  ```
  conda create -n torch anaconda
  ```
  
  ### clone conda environment
  conda create -n [env_name] --clone [source_env_name]
  ```
  conda create -n torch2 --clone anaconda-backup
  ```

### install OpenCV
  - conda install -c conda-forge opencv

# Install Pytorch based on cuda
  - https://discuss.pytorch.org/t/pytorch-cuda-11-6/149647
  - (pip install torch --pre --extra-index-url https://download.pytorch.org/whl/nightly/cu116)

  - conda create -n TORCH-NAME python=3.8
  - (remove : conda env 

  - https://pytorch.org/get-started/locally/


<hr>

# Tips
## How to check Cuda Version
  - https://varhowto.com/check-cuda-version-ubuntu-18-04/
    $ nvidia-smi
  - developer.nvidia.com/rdp/cudnn-download 

## How to check Linux version
  - https://www.ionos.ca/digitalguide/server/know-how/how-to-check-your-linux-version/
  - 

## About GPGPU & Nvidia
  - https://89douner.tistory.com/158




reference
https://velog.io/@hailee98/Ubuntu-CUDA-cuDNN-%EC%84%A4%EC%B9%98
https://webnautes.tistory.com/1171
