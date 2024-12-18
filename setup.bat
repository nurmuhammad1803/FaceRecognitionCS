@echo off
echo Setting up your Face Recognition project...

echo Creating virtual environment...
python -m venv venv

echo Activating virtual environment...
call venv\Scripts\activate

echo Upgrading pip...
pip install --upgrade pip
pip install --upgrade setuptools

echo Installing dependencies...
pip install -r requirements.txt

echo Running the project...
python main.py

pause