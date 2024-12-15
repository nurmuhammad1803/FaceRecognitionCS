import cv2
import os
import face_recognition
import numpy as np
import telebot
from telebot import types
import threading
import queue
import shutil


from install import TOKEN, UNKNOWN_FACES_DIR_PATH, DEFAULT_ADMIN, CAMERA_IP, SET_FPS
from help import clear_directory, unknown_faces_saver, unknown_faces_sender
from bot_settings import stats_menu, confirm_add_student, settings_menu, tolerance_menu

bot = telebot.TeleBot(TOKEN)

clear_directory(UNKNOWN_FACES_DIR_PATH)

student_queue = queue.Queue()
tolerance_queue = queue.Queue()

def update_known_face_encodings():
    global unknown_face_encodings
    while True:
        try:
            student_name, encoding, index = student_queue.get(timeout=1)
            known_face_names.append(student_name)
            known_face_encodings.append(encoding)
            added_face_names.append(student_name)
            added_face_encodings.append(encoding)

            np.save('database/added_face_encodings.npy', added_face_encodings)
            np.save('database/added_face_names.npy', added_face_names)
            print(f"Added student: {student_name}")     
            print(f"Student's index: {index}")     

            shutil.move(f'unknown_faces/unknown_face_{index}.jpg', f'students/student_{student_name}.jpg')
            added_students_indexes.append(index)
        except queue.Empty:
            pass

def update_tolerance():
    global tolerance
    while True:
        try:
            tolerance = tolerance_queue.get(timeout=1)
            print(f"Tolerance changed to {tolerance}")
        except queue.Empty:
            pass

update_thread = threading.Thread(target=update_known_face_encodings)
update_thread.start()

tolerance_thread = threading.Thread(target=update_tolerance)
tolerance_thread.start()


# Registering new student:
def reg_name(message):
    global student_name
    student_name = message.text

    bot.send_message(admin, f'Name of the newly added student is {student_name}, correct?',
                     reply_markup=confirm_add_student)

############################### Initializing bot for different commands like /start; /statistics; & etc.
# React to the '/start' command
@bot.message_handler(commands=['start'])
def start(message):
    global admin
    admin = message.chat.id

    bot.reply_to(message, f"Hello! I am a bot, which will provide statistics about students' attendance")
    bot.send_message(admin, "Send me '/stats' command to open the statistics menu")

@bot.message_handler(commands=['statistics'])
def start(message):
    bot.send_message(message.chat.id, "What do you want to know?", reply_markup=stats_menu)

@bot.message_handler(commands=['settings'])
def start(message):
    bot.send_message(message.chat.id, "What setting do you want to change?", reply_markup=settings_menu)

@bot.message_handler(content_types=['text'])
def check(message):
    global add_student
    if add_student: reg_name(message)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    global add_student, unknown_face_num, tolerance, name
    if call.data == 'number_students':
        bot.send_message(admin, f'{number_of_faces} faces detected')
    elif call.data == 'number_unknowns':
        bot.send_message(admin, f'{len(unknown_face_encodings)} unknown faces are registered')
    elif call.data == 'unknown_faces':
        bot.send_message(admin, "Here is the photos of unknown faces detected:")
        for k in range(len(unknown_face_encodings)):
            if k not in added_students_indexes:
                markup_inline_name_to_unknown = types.InlineKeyboardMarkup(row_width=1)
                item_add_student = types.InlineKeyboardButton(text='Add a student', callback_data=f'add_student-{k}')
                markup_inline_name_to_unknown.add(item_add_student)

                with open(f'unknown_faces/unknown_face_{k}.jpg', 'rb') as photo:
                    bot.send_photo(admin, photo, reply_markup=markup_inline_name_to_unknown)
    elif call.data.startswith("add_student-"):
        unknown_face_num = int(call.data.split('-')[1])
        bot.send_message(admin, "Enter a name of the student")
        add_student = True

    elif call.data == "yes":
        bot.send_message(admin, 'The student is added')
        add_student = False
        print(student_name)
        student_face_encoding = unknown_face_encodings[unknown_face_num]
        student_queue.put((student_name, student_face_encoding, unknown_face_num))

    elif call.data == "no":
        bot.send_message(admin, "Enter a name of the student")

    elif call.data == "change_tolerance":
        bot.send_message(admin, f"Choose the tolerance (current is {tolerance})", reply_markup=tolerance_menu)

    elif call.data.startswith("0."):
        tolerance_queue.put(float(call.data))
        bot.send_message(admin, f"Tolerance updated to {call.data}")


add_student = False
number_of_faces = 0
student_name = ''
name = ''
admin = DEFAULT_ADMIN
unknown_face_num = -1
tolerance = 0.5
added_students_indexes = []
unknown_face_encodings = []

if os.path.exists('database/added_face_encodings.npy'):
    known_face_encodings = np.load('database/known_face_encodings.npy').tolist() + np.load('database/added_face_encodings.npy').tolist()
    known_face_names = np.load('database/known_face_names.npy').tolist() + np.load('database/added_face_names.npy').tolist()

    added_face_encodings = np.load('database/added_face_encodings.npy').tolist()
    added_face_names = np.load('database/added_face_names.npy').tolist()
else:
    known_face_encodings = np.load('database/known_face_encodings.npy').tolist()
    known_face_names = np.load('database/known_face_names.npy').tolist()

    added_face_encodings = []
    added_face_names = []

os.makedirs('unknown_faces', exist_ok=True)

############################################### FACE_RECording using multiple cameras
def face_rec():
    global face_counter, admin
    video_captures = []
    for ip in CAMERA_IP:
        video_capture = cv2.VideoCapture(ip)
        if not video_capture.isOpened():
            print(f"[ERROR] Camera {ip} is not accessible.")
            continue

        video_capture.set(cv2.CAP_PROP_FPS, SET_FPS)
        video_captures.append(video_capture)

    while True:
        for cam_index, video_capture in enumerate(video_captures):
            ret, frame = video_capture.read()
            if not ret:
                print(f"[ERROR] Camera {cam_index} is not accessible.")
                continue

            face_locations = face_recognition.face_locations(frame)
            face_encodings = face_recognition.face_encodings(frame, face_locations)
            face_counter = len(face_locations)
            i = 0

            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=tolerance)
                unknown_face_matches = face_recognition.compare_faces(unknown_face_encodings, face_encoding, tolerance=0.5)
                name = "Unknown"

                if True in matches:
                    first_match_index = matches.index(True)
                    name = known_face_names[first_match_index]

                top, right, bottom, left = face_locations[i]
                if (name == "Unknown") and not (True in unknown_face_matches):
                    face_image = frame[top:bottom, left:right]
                    unknown_face_counter = len(unknown_face_encodings)
                    unknown_faces_saver(face_image, unknown_face_counter)
                    unknown_faces_sender(unknown_face_counter, bot, admin)
                    unknown_face_encodings.append(face_encoding)

                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
                i += 1

            cv2.imshow(f'Camera {cam_index}', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    for video_capture in video_captures:
        video_capture.release()
    cv2.destroyAllWindows()



face_recognition_thread = threading.Thread(target=face_rec)
face_recognition_thread.start()

bot.polling(non_stop=True)