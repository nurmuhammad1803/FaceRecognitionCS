TOKEN = '' # write the token of your bot      type:string
ABSOLUTE_PATH = "C:\\Users\\Flexy\\Downloads\\Student_Attendance_Bot-master\\" # write absolue path to the project folder
DATABASE_PATH = ABSOLUTE_PATH + "faces"
UNKNOWN_FACES_DIR_PATH = ABSOLUTE_PATH + 'unknown_faces'
KNOWN_ENCODINGS_PATH = 'db/known_face_encodings.npy'
KNOWN_FACES_PATH = 'db/known_face_names.npy'
DEFAULT_ADMIN = '' # write the telegram ID of admin     type:string
CAMERA_IP = [0] # CAMERA IP -> IF you have access to RTSP supported cameras then put the in the following format: 'rtsp://[name]:[password]@[localIP]/stream1'
# CAMERA IP supports multiple cameras; if you have any other cameras; append their IPs or indexes to the list above