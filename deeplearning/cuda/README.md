Esstional for cuda in WSL


1. NVIDA driver (might be at Window)
  - https://www.nvidia.com/Download/driverResults.aspx/190349/en-us/
  - https://developer.nvidia.com/cuda/wsl

2. Nvidia CUDA toolkit
  - To compile new CUDA applications, a CUDA Toolkit for Linux x86 is needed.
  - CUDA toolkit support for WSL is still in preview stage as developer tool such as debugger and profilers are not available yet.
  - When NVIDA drvier for window is installed, CUDA becomes available within WSL2. 
  - The CUDA driver installed on Windows host will be stubbed inside the WSL2 as libcuda.so
  - https://docs.nvidia.com/cuda/wsl-user-guide/index.html

	#######################################
	wbet https://developer.download.nvidia.com/compute/cuda/repos/wsl-ubuntu/x86_64/cuda-wsl-ubuntu.pin
	sudo mv cuda-wsl-ubuntu.pin /etc/apt/preferences.d/cuda-repository-pin-600
	wget https://developer.download.nvidia.com/compute/cuda/11.4.0/local_installers/cuda-repo-wsl-ubuntu-11-4-local_11.4.0-1_amd64.deb
	sudo dpkg -i cuda-repo-wsl-ubuntu-11-4-local_11.4.0-1_amd64.deb
	sudo apt-key add /var/cuda-repo-wsl-ubuntu-11-4-local/7fa2af80.pub
	sudo apt-get update
	sudo apt-get -y install cuda
	#######################################

  - reference
    - https://0verc10ck.tistory.com/43

3. Nvidia cuDNN
  - https://developer.nvidia.com/cudnn 

=======
4. How to check Cuda Version
  - https://varhowto.com/check-cuda-version-ubuntu-18-04/
    $ nvidia-smi
  - developer.nvidia.com/rdp/cudnn-download 

5. How to check Linux version
  - https://www.ionos.ca/digitalguide/server/know-how/how-to-check-your-linux-version/
  - 

6. About GPGPU & Nvidia
  - https://89douner.tistory.com/158

