import os

# Variables
SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = -1


# Functions
def screen_cleaner():
    """Clears the console screen."""
    # Clear the console screen based on the operating system
    if os.name == 'nt':  # For Windows
        _ = os.system('cls')
    else:  # For macOS and Linux (posix)
        _ = os.system('clear')
