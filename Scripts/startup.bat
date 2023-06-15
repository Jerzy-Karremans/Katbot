@echo off

REM Check if Python is installed
python --version 2>nul
if errorlevel 1 (
    echo Python 3 is required but not found. Please install Python 3.
    exit /b 1
)

REM Check if pip is installed
pip --version 2>nul
if errorlevel 1 (
    echo pip is required but not found. Please install pip.
    exit /b 1
)

REM Check if the Katbot directory exists
if not exist ..\..\Katbot\ (
    REM Clone the GitHub repository
    git clone https://github.com/Jerzy-Karremans/Katbot
    cd Katbot
) else (
    REM Change directory to the cloned repository
    cd ..\
)

REM Change directory to the cloned repository
mkdir config

REM Create a virtual environment
python -m venv env

REM Activate the virtual environment
call env\Scripts\activate.bat

REM Upgrade pip
python -m pip install --upgrade pip

REM Install the requirements and dependencies
python -m pip install -r requirements.txt

REM Create the api_keys.json file
echo {> config\api_keys.json
echo    "openApi": "your_api_key_1">> config\api_keys.json
echo }>> config\api_keys.json
echo Created a default api_keys.json file. Please update the API keys in 'config\api_keys.json' with your actual keys.

REM Deactivate the virtual environment
deactivate

REM Pause the script to prevent the terminal from closing immediately
pause