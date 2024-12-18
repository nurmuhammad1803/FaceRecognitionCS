#!/bin/bash

echo "Setting up your Face Recognition project..."

# Create a virtual environment
echo "Creating virtual environment..."
python3 -m venv venv

# Activate the virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip and setuptools
echo "Upgrading pip..."
pip install --upgrade pip
pip install --upgrade setuptools

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Run the project
echo "Running the project..."
python3 main.py

# Pause equivalent for Linux/macOS
read -p "Press any key to exit..."
