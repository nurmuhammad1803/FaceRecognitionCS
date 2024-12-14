import os
import shutil
import cv2
def clear_directory(directory_path):
    try:
        for file_name in os.listdir(directory_path):
            file_path = os.path.join(directory_path, file_name)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f"Error clearing file or directory {file_path}: {e}")

        print(f"Directory '{directory_path}' cleared successfully.")

    except OSError as e:
        print(f"Error: {directory_path} - {e}")

def unknown_faces_saver(face_image, unknown_face_counter):
    filename = f'unknown_faces/unknown_face_{unknown_face_counter}.jpg'
    cv2.imwrite(filename, face_image)

def unknown_faces_sender(unknown_face_counter, bot, admin):
    with open(f'unknown_faces/unknown_face_{unknown_face_counter}.jpg', 'rb') as photo:
        bot.send_photo(admin, photo)
    bot.send_message(admin, 'Unknown face detected')