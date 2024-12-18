# FaceRecognitionCS :robot:
*Face Recognition Project for CS Polito for registering new students using Telegram Bot and multiple camera sources*


## Features:
1. **Face Recognition** (Tracks multiple faces from video source in real-time and recognizes registered faces)
2. **Registering new personas via Telegram Bot**
3. **Saves the images of registered & unknown people to proper folders** (students&unknown_faces)
4. **RTSP protocol is supported**
5. **Support of multiple camera** sources at the same time
6. **Dockerized container**

## BEFORE LAUNCHING
1. Make sure you have changed variables in install.py
2.  Download [Microsoft Visual Studio Build Tools C++](https://visualstudio.microsoft.com/ru/visual-cpp-build-tools/) and install module **Desktop Development with C++**
3.  Install Python 3 and pip

## HOW TO RUN:
Windows :window: : RUN ```setup.bat``` file

MACOS/Linux :apple: : Open terminal and navigate to the project folder. Then execute ```sh setup.sh ```

VIA DOCKER :whale: : Open terminal and navigate to the repository folder. RUN ```docker compose up```

## Setting up :gear:
Change the values of variables inside the install.py file to set your bot up:
1. **TOKEN** - token of telegram bot you want to use
2. **ABSOLUTE_PATH** - absolute path to the project folder (note that you must use double backslash \\ instead of slash or backslash)
3. **DEFAULT_ADMIN** - the id of admin telegram account (bot will be sending messages to this address) ```(type: string)```
4. **CAMERA_IP** - ```[default = 0]``` *optional: insert IPs of RTSP supported cameras or local cameras. Separate by commas. ``` (Format for RTSP: 'rtsp://[name][password]@[localIP]/stream1')*```
5. **SET_FPS** - set number of frames per second of each video. (Tip: set lower than average if you want to lower the load on your GPU/CPU) ```(type: int)```

## Customizing bot
> You can play with settings of bot in order to customize by modifying bot_settings.py file

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

## Credentials:
*This project has been built with face_recognition module developeed by ageitgey and open-source face_id_attendance project on github.*

Thank you!# FaceRecognitionCS :robot:
*Face Recognition Project for CS Polito for registering new students using Telegram Bot and multiple camera sources*


## Features:
1. **Face Recognition** (Tracks multiple faces from video source in real-time and recognizes registered faces)
2. **Registering new personas via Telegram Bot**
3. **Saves the images of registered & unknown people to proper folders** (students&unknown_faces)
4. **RTSP protocol is supported**
5. **Support of multiple camera** sources at the same time
6. **Dockerized container**

## Setting up
Change the values of variables inside the install.py file to set your bot up:
1. **TOKEN** - token of telegram bot you want to use
2. **ABSOLUTE_PATH** - absolute path to the project folder (note that you must use double backslash \\ instead of slash or backslash)
3. **DEFAULT_ADMIN** - the id of admin telegram account (bot will be sending messages to this address) ```(type: string)```
4. **CAMERA_IP** - ```[default = 0]``` *optional: insert IPs of RTSP supported cameras or local cameras. Separate by commas. ``` (Format for RTSP: 'rtsp://[name][password]@[localIP]/stream1')*```
5. **SET_FPS** - set number of frames per second of each video. (Tip: set lower than average if you want to lower the load on your GPU/CPU) ```(type: int)```

## Customizing bot
> You can play with settings of bot in order to customize by modifying bot_settings.py file

## HOW TO USE:
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

## Credentials:
*This project has been built with face_recognition module developeed by ageitgey and open-source face_id_attendance project on github.*

Thank you!