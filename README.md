# FaceRecognitionCS :robot:
*Face Recognition Project for CS Polito for registering new students using Telegram Bot and multiple camera sources*

## MENU:
1. [Features](#features)
2. [Example](#example)
3. [Before Launching](#before-launching)
4. [Settings](#setting-up)
5. [Customizing](#customizing-bot)
6. [Dependencies](#dependencies)
7. [Thank you )](#credentials)

## Features:
1. **Face Recognition** (Tracks multiple faces from video source in real-time and recognizes registered faces)
2. **Registering new personas via Telegram Bot**
3. **Saves the images of registered & unknown people to proper folders** (students&unknown_faces)
4. **RTSP protocol is supported**
5. **Support of multiple camera** sources at the same time
6. **Dockerized container**

## Example:
![faceid_cam](https://cloud.githubusercontent.com/assets/896692/24430398/36f0e3f0-13cb-11e7-8258-4d0c9ce1e419.gif)
![tg_bot](https://i.postimg.cc/Lsf9BNcN/image.png)

## BEFORE LAUNCHING
1. Make sure you have changed variables in install.py
2. RUN vs_BuildTools.exe by [Microsoft Visual Studio Build Tools C++](https://visualstudio.microsoft.com/ru/visual-cpp-build-tools/)  and install module **Desktop Development with C++**
3. Install Python 3 and pip

## HOW TO RUN:
Windows :window: : RUN ```setup.bat``` file

MACOS/Linux :apple: : Open terminal and navigate to the project folder. Then execute ```sh setup.sh ```

VIA DOCKER :whale: (Currently not available) : Open terminal and navigate to the repository folder. RUN ```docker compose up```

If you cannot launch program correctly, check out [Troubleshooting section](#troubleshooting)

## Setting up :gear:
Change the values of variables inside the install.py file to set your bot up:
1. **TOKEN** - token of telegram bot you want to use
2. **ABSOLUTE_PATH** - absolute path to the project folder (note that you must use double backslash \\ instead of slash or backslash)
3. **DEFAULT_ADMIN** - the id of admin telegram account (bot will be sending messages to this address) ```(type: string)```
4. **CAMERA_IP** - ```[default = 0]``` *optional: insert IPs of RTSP supported cameras or local cameras. Separate by commas. ``` (Format for RTSP: 'rtsp://[name][password]@[localIP]/stream1')*```
5. **SET_FPS** - set number of frames per second of each video. (Tip: set lower than average if you want to lower the load on your GPU/CPU) ```(type: int)```

## Customizing bot
> You can play with settings of bot in order to customize by modifying ```bot_settings.py``` file

## Dependencies:
```
opencv
face-recognition
face-recognition-models
dlib
cmake
numpy
telebot (pyTelegramBot)
```

## Troubleshooting
1. ![Token error](https://i.postimg.cc/9My3np2p/image.png)
This error depicts that Bot's Token or Admin user's ID is not defined. Please visit install.py and change according variables to get things done :)

2. ![no module named cv2 error](https://i.postimg.cc/RhTkMZNJ/image.png)
Error's related to unfound modules (Like cv2) might arise due to c++ package. Please run ```vs_BuildTools.exe``` and install ```Desktop Development with C++``` package using Visual Studio :) 

3. **Camera Not found error**
Default camera index for most Laptop's built-in camera is 0. However if this option didn't open camera, you may try 1, or go to Google and search for your camera index. RTSP cameras always work fine )

## Credentials:
*This project has been built with face_recognition module developeed by ageitgey and open-source face_id_attendance project on github.*

Thank you!# FaceRecognitionCS :robot:
*Face Recognition Project for CS Polito for registering new students using Telegram Bot and multiple camera sources*
