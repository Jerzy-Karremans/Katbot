#!/bin/bash

# Check if Python is installed
python3 --version >/dev/null 2>&1
if [[ $? -ne 0 ]]; then
    echo "Python 3 is required but not found. Please install Python 3."
    exit 1
fi

# Check if pip is installed
pip --version >/dev/null 2>&1
if [[ $? -ne 0 ]]; then
    echo "pip is required but not found. Please install pip."
    exit 1
fi

# Check if the Katbot directory exists
if [ ! -d "../..//Katbot" ]; then
    # Clone the GitHub repository
    git clone https://github.com/Jerzy-Karremans/Katbot
    cd Katbot
else
    # Change directory to the cloned repository
    cd ../..
fi

# Change directory to the cloned repository
mkdir config

# Create a virtual environment
python3 -m venv env

# Activate the virtual environment
source env/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install the requirements and dependencies
pip install -r requirements.txt

# Create the api_keys.json file
echo '{' > config/api_keys.json
echo '   "openApi": "your_open_api_key",' >> config/api_keys.json
echo '   "elevenlabs": "your_eleven_api_key",' >> config/api_keys.json
echo '   "usingEleven": false' >> config/api_keys.json
echo '}' >> config/api_keys.json
echo "Created a default api_keys.json file. Please update the API keys in 'config/api_keys.json' with your actual keys."

# Deactivate the virtual environment
deactivate

# Pause the script to prevent the terminal from closing immediately
read -p "Press Enter to exit."
