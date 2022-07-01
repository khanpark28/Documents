## Step 1. WSL ubuntu 이미지를 디폴트가 아닌 다른 경로에 설치 방법
1. WSL 설치
2. Ubuntu 를 Appstore 를 통해 기본 루트에 설치하면 C 드라이브의 용량제한으로 사용이 불가하니, Store 에서 받지 않고, 이미지를 직접 다운로드하여 설치함.
(https://hacktiming.tistory.com/61)

-> 이미지를 다운로드 한 다음에, 파일 이름 바꾸고, 압축을 풀어서 환경을 만듦. 
그 다음에 Ubuntu.exe 를 실행하면 wsl 에 등록이 되면서? 사용 가능해짐
이때 id /passwd 도 설정.  hanee/hanee


## Ubuntu 인스턴스를 WSL 에서 삭제하는 방법
https://positivemh.tistory.com/584
# wslconfig.exe /u Ubuntu 


## Step 2. WSL ubuntu 이미지를 반복해서 사용하는 방법
(윈도우 WSL 환경에서 같은 종류의 리눅스를 다중으로 설치하는 방법)
https://blog.naver.com/techshare/222596544852

1. 처음 설치한 clean 한 상태의 Ubuntu 에서  (Step 1) 이미지를 extract 함. 
$ wsl --export Ubuntu-20.04 Ubuntu-20.04-clean.tar

2. extract 한 이미지를 특정 위치에 설치함. 
$ wsl.exe --import Ubuntu-20.04-clean .\Ubuntu-20.04-clean .\Ubuntu-20.04-clean.tar

3. 설치한 뒤에, 실행 명령어를 window terminal 의 새로운 profile 에 등록함
 (wsl -d [instance 이름] 이렇게 연결하면 됨)

- wsl.exe --import [instance name] [파일 시스템 만들 곳] [저장해 놓은 이미지 위치]
- wsl.exe --import Ubuntu-20.04-clearn f:\backup\Ubuntu-20.04-clean F:\Ubuntu20.04-backup\Ubuntu-20.04-clear.tar
- su hanee

##ETC.
root password 바꾸는 법
wsl -d [distribute name] -u root
#passwd

