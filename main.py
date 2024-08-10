from app import start_play
import threading
import main_score
import subprocess
import logging

def start_docker():
    try:
        print("Building Docker image...")
        subprocess.run(["docker", "build", "-t", "flask_app_image", "."], check=True)

        print("Running Docker container...")
        subprocess.run(["docker", "run", "-d", "--name", "flask_app_container", "-p", "8777:5000", "flask_app_image"], check=True)

        print("Container is up and running!")
    except subprocess.CalledProcessError as e:
        print(f"Failed to start Docker container: {e}")

if __name__ == "__main__":
    start_docker()  # Ensure Docker container is ready before starting the Flask server and the game

    # Start the Flask server in a separate thread
    #flask_thread = threading.Thread(target=main_score.app.run, kwargs={'host': '0.0.0.0', 'port': 5000})
    #flask_thread.daemon = True  # This ensures the thread will exit when the main program exits
    #flask_thread.start()

    # Start the game
    start_play()
