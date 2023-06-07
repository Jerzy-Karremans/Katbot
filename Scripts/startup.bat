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

REM Clone the GitHub repository
git clone https://github.com/Jerzy-Karremans/Katbot

REM Change directory to the cloned repository
cd Katbot
mkdir config

REM Create a virtual environment
python -m venv env

REM Activate the virtual environment
call env\Scripts\activate.bat

REM Upgrade pip
python -m pip install --upgrade pip

REM Install the requirements and dependencies
python -m pip install -r requirements.txt

REM Create the api_keys.py file
echo API_KEYS = {> config\api_keys.py
echo    'openApi': 'your_api_key_1'>> config\api_keys.py
echo }>> config\api_keys.py
echo Created a default api_keys.py file. Please update the API keys in 'config\api_keys.py' with your actual keys.

REM Deactivate the virtual environment
deactivate

REM Provide instructions for further steps
echo.
echo Katbot environment has been set up successfully!
echo To start the application, run the following command:
echo    env\Scripts\activate.bat && python src\bot.py

REM Pause the script to prevent the terminal from closing immediately
pause
