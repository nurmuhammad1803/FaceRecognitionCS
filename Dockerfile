# Base image for Python 3.12
FROM python:3.12

# Set the working directory in the container
WORKDIR /app

# Copy all project files into the container
COPY . .

# Update and install system dependencies required for face_recognition
RUN apt-get update && \
    apt-get install -y cmake libgl1-mesa-glx libgtk2.0-dev libboost-all-dev && \
    apt-get clean

# Install Python modules globally
RUN pip install --no-cache-dir opencv-python opencv-python-headless dlib face-recognition face-recognition-models telebot numpy

# Set the default command to run the Python script
CMD python main.py
