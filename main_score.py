from flask import Flask
import os

app = Flask(__name__)

# Constants
SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = -1


def read_score():
    """Read the score from the scores file."""
    try:
        if os.path.exists(SCORES_FILE_NAME):
            with open(SCORES_FILE_NAME, 'r') as file:
                content = file.read().strip()
                return int(content) if content else 0
        else:
            return 0
    except Exception as e:
        print(f"Error reading the score file: {e}")
        return BAD_RETURN_CODE


@app.route('/')
def score_server():
    """Serve the score over HTTP."""
    score = read_score()
    if score == BAD_RETURN_CODE:
        return (
            "<html><head><title>Scores Game</title></head>"
            "<body><h1>Error:</h1><div id='score' style='color:red'>{ERROR}</div></body></html>", 500
        )
    else:
        return (
            f"<html><head><title>Score Game</title></head>"
            f"<body><h1>The score is:</h1><div id='score'>{score}</div></body></html>"
        )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
