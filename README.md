# Katbot

Welcome to Katbot! This is a Python project that utilizes the OpenAI API and comes with a convenient startup script to set up the environment and dependencies.

## Requirements

Before running the startup script, please ensure you have the following installed on your system:

- Python 3
- pip

## Getting Started

To quickly set up the Katbot environment and run the project, follow these steps:

1. Go to the [Releases](https://github.com/Jerzy-Karremans/Katbot/releases) page of this repository.

2. Download the latest release, which includes the startup script.

3. Open a terminal or command prompt and navigate to the directory where you downloaded the script.

4. Run the startup script:

   - On Unix-like systems (Linux, macOS):
     ```bash
     bash startup.sh
     ```

   - On Windows:
     ```batch
     startup.bat
     ```

5. The script will guide you through the process. It will clone the Katbot repository, set up a virtual environment, install dependencies, and prompt you to enter your OpenAI API key.

6. After the script completes, you can start using the Katbot application.

## Configuration

The startup script will create a `config.py` file that stores the OpenAI API key. You can modify this file manually if needed.

## Support

If you encounter any issues or have questions, please feel free to [open an issue](https://github.com/Jerzy-Karremans/Katbot/issues) in this repository.

Happy botting!

ps to update requirements.txt pip freeze > requirements.txt