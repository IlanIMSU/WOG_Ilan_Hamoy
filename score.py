import os

# Constants
SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = -1


def calculate_points_of_winning(difficulty):
    """Calculate the points for winning based on difficulty."""
    return (difficulty * 3) + 5


def add_score(difficulty):
    """Add score to the scores file based on the difficulty level."""
    score = calculate_points_of_winning(difficulty)

    # Try to read the current score from the scores file
    try:
        if os.path.exists(SCORES_FILE_NAME):
            with open(SCORES_FILE_NAME, 'r') as file:
                content = file.read().strip()
                current_score = int(content) if content else 0
        else:
            current_score = 0
    except Exception as e:
        print(f"Failed to read the score file: {e}")
        current_score = 0

    # Add the new score to the current score
    new_score = current_score + score

    # Write the new score back to the scores file
    try:
        with open(SCORES_FILE_NAME, 'w') as file:
            file.write(str(new_score))
        print(f"New score: {new_score}")
    except Exception as e:
        print(f"Failed to write to the score file: {e}")
