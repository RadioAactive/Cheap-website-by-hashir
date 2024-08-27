#!/bin/sh

venv_name=".venv"

echo "What operating system are you using? (linux/mac/windows)"
read os

if [ -d "$venv_name" ]; then
  echo "Virtual environment '$venv_name' already exists. Skipping creation."
else
  echo "Creating virtual environment '$venv_name'..."
  python3 -m venv "$venv_name"
fi
echo "error?"
# Activate virtual environment based on OS
if [[ "$os" == "linux" ]]; then
  source "$venv_name/bin/activate"
  echo "Installing Flask and Pandas..."
  pip install flask pandas

elif [[ "$os" == "mac" ]]; then
  source "$venv_name/bin/activate"
  echo "Installing Flask and Pandas..."
  pip install flask pandas

elif [[ "$os" == "windows" ]]; then
  source "$venv_name\Scripts\activate"
  echo "Installing Flask and Pandas..."
  pip install flask pandas
else
  echo "Invalid operating system entered. Activation skipped."
fi

echo "Starting main.py..."
python main.py


# Deactivate the virtual environment (optional)
# deactivate