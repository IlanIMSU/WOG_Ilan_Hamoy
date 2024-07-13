import os

# Variables
SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = -1

# Functions


def screen_cleaner():
    """Clears the console screen."""

    if os.name == 'nt':  # for Windows
        _ = os.system('cls')
    else:  # for Mac and Linux (here, os.name is 'posix')
        _ = os.system('clear')
