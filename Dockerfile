# # Base image for Python 3.12
FROM python:3.12

COPY . .

# # Update and install system dependencies required for face_recognition
RUN apt-get update && \
    apt-get install -y cmake libgl1-mesa-glx libgtk2.0-dev libboost-all-dev && \
    apt-get clean

RUN pip install --upgrade setuptools

RUN pip3 install --no-cache-dir -r requirements.txt

RUN pip install --no-cache-dir git+https://github.com/ageitgey/face_recognition_models

CMD python main.py