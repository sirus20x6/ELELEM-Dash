#!/bin/bash

# Define the name of the virtual environment
VENV_NAME="elvenv"

# Check if the virtual environment already exists
if [ ! -d "$VENV_NAME" ]; then
    echo "Virtual environment not found. Creating..."
    python3 -m venv "$VENV_NAME"
else
    echo "Virtual environment already exists."
fi

# Activate the virtual environment
# This method is generally for bash. Modify if using a different shell.
source "$VENV_NAME/bin/activate"

# Check if requirements.txt exists
if [ ! -f "requirements.txt" ]; then
    echo "requirements.txt not found. Exiting..."
    exit 1
fi

# Install Python packages from requirements.txt
pip install -r requirements.txt

echo "Setup complete."