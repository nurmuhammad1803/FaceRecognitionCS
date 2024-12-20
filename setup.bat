@echo off
echo Setting up Face Recognition project...

echo Creating virtual environment...
python -m venv venv

echo Activating virtual environment...
call venv\Scripts\activate

echo Upgrading pip...
pip install --upgrade pip
pip install --upgrade setuptools

echo Install Cmake...
pip install cmake

echo Installing dependencies...
pip install -r requirements.txt

echo Running the project...
python main.py

REM Check if MSVC tools are installed
where cl >nul 2>nul
if %errorlevel% neq 0 (
    echo Microsoft Visual C++ Build Tools are not installed.
    echo Please install "Desktop Development with C++" via Visual Studio Installer.
    start https://visualstudio.microsoft.com/visual-cpp-build-tools/
    pause
    exit /b
)


pause