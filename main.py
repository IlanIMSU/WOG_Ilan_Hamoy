from app import start_play
import threading
import main_score

if __name__ == "__main__":
    # Start the Flask server in a separate thread
    flask_thread = threading.Thread(target=main_score.app.run, kwargs={'host': '0.0.0.0', 'port': 5000})
    flask_thread.daemon = True  # This ensures the thread will exit when the main program exits
    flask_thread.start()

    # Start the game
    start_play()
