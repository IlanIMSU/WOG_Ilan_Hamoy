import os

SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = -1


def calculate_points_of_winning(difficulty):
    """Calculate the points for winning based on difficulty."""
    return (difficulty * 3) + 5


def add_score(difficulty):
    """Add score to the scores file based on the difficulty level."""
    score = calculate_points_of_winning(difficulty)

    try:
        if os.path.exists(SCORES_FILE_NAME):
            with open(SCORES_FILE_NAME, 'r') as file:
                current_score = int(file.read().strip())
        else:
            current_score = 0
    except Exception as e:
        print(f"Failed to read the score file: {e}")
        current_score = 0

    new_score = current_score + score

    try:
        with open(SCORES_FILE_NAME, 'w') as file:
            file.write(str(new_score))
        print(f"New score: {new_score}")
    except Exception as e:
        print(f"Failed to write to the score file: {e}")
