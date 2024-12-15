TOKEN = '' # write the token of your bot      type:string
ABSOLUTE_PATH = "C:\\Users\\Flexy\\Desktop\\CS\\_faceid\\FaceRecognitionCS\\" # write absolue path to the project folder
DATABASE_PATH = ABSOLUTE_PATH + "students"
UNKNOWN_FACES_DIR_PATH = ABSOLUTE_PATH + 'unknown_faces'
KNOWN_ENCODINGS_PATH = 'database/known_face_encodings.npy'
KNOWN_FACES_PATH = 'database/known_face_names.npy'
DEFAULT_ADMIN = '' # write the telegram ID of admin     type:string
CAMERA_IP = [0] # CAMERA IP -> IF you have access to RTSP supported cameras then put the in the following format: 'rtsp://[name]:[password]@[localIP]/stream1'
# CAMERA IP supports multiple cameras; if you have any other cameras; append their IPs or indexes to the list above
SET_FPS = 30 #frames per second -> default value is 30 but you can lower it to minimize the load on your GPU/CPU