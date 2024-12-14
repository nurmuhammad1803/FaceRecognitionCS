import face_recognition
import os
import numpy as np
from install import DATABASE_PATH, KNOWN_FACES_PATH, KNOWN_ENCODINGS_PATH

known_face_encodings = []
known_face_names = []

for folder_name in os.listdir(DATABASE_PATH):
    folder_path = os.path.join(DATABASE_PATH, folder_name)
    print(folder_path)
    if os.path.isdir(folder_path):
        for filename in os.listdir(folder_path):
            image_path = os.path.join(folder_path, filename)
            image = face_recognition.load_image_file(image_path)
            face_encoding = face_recognition.face_encodings(image)[0]
            known_face_encodings.append(face_encoding)
            known_face_names.append(folder_name)

np.save(KNOWN_FACES_PATH, known_face_encodings)
np.save(KNOWN_ENCODINGS_PATH, known_face_names)