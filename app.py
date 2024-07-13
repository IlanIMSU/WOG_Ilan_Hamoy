import subprocess
import sys
from utils import screen_cleaner
from score import add_score
from guess_game import play as guess_game_play
from currency_roulette_game import play as currency_roulette_game_play
from memory_game import play as memory_game_play


# Function to install a package using pip
def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


try:
    import requests
except ImportError:
    print("Requests library not found. Installing...")
    install_package('requests')
    import requests


def start_play():
    while True:
        screen_cleaner()  # Clear screen before displaying game options
        print("Select a game to play:")
        print("1. Guess Game")
        print("2. Currency Roulette Game")
        print("3. Memory Game")
        print("4. Exit")

        game_choice = input("Enter the number of the game you want to play: ")

        if not game_choice.isdigit():
            print("Invalid input! Please enter a number.")
            continue

        game_choice = int(game_choice)

        if game_choice == 4:
            print("Thank you for playing! Goodbye.")
            break

        difficulty = input("Enter difficulty level (1-5): ")

        if not difficulty.isdigit() or not 1 <= int(difficulty) <= 5:
            print("Invalid difficulty level! Please enter a number between 1 and 5.")
            continue

        difficulty = int(difficulty)

        screen_cleaner()  # Clear screen before starting a new game

        if game_choice == 1:
            result = guess_game_play(difficulty)
        elif game_choice == 2:
            result = currency_roulette_game_play(difficulty)
        elif game_choice == 3:
            result = memory_game_play(difficulty)
        else:
            print("Invalid choice!")
            continue

        if result:
            print("You won!")
            add_score(difficulty)  # Call add_score when the user wins
        else:
            print("You lost!")

            play_again = input("Do you want to play again? (y/n): ").lower()
            if play_again != 'y':
                print("Thank you for playing! Goodbye.")
                break


if __name__ == "__main__":
    start_play()
