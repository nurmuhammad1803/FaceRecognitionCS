FROM python:3.12

COPY . .

RUN apt-get update && \
    apt-get install -y cmake libgl1-mesa-glx libgtk2.0-dev libboost-all-dev && \
    apt-get clean

RUN pip install --upgrade setuptools

RUN pip install --no-cache-dir -r requirements.txt

CMD python main.py