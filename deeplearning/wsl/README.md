# How to install WSL


## WSL & WSL2
## working nvida cuda
## testing with cuda
## install Ubuntu with non-default location
https://kontext.tech/article/308/how-to-install-windows-subsystem-for-linux-on-a-non-c-drive

```Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux```
```Invoke-WebRequest -Uri https://aka.ms/wsl-ubuntu-1804 -OutFile Ubuntu.appx -UseBasicParsing```
```move .\Ubuntu.appx .\Ubuntu.zip```
```Expand-Archive .\Ubuntu.zip```
```cd .\Ubuntu\```
 ```.\ubuntu1804.exe```


# How to delete WSL
https://pinggoopark.tistory.com/109

### WSL image list
wslconfig /l

### WSL image delete
wslconfig /u <name of distribution>  


### install more than one instance from one image
https://blog.naver.com/techshare/222596544852
https://www.sysnet.pe.kr/2/0/12569
