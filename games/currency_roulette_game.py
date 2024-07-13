import random
import requests


def get_money_interval(difficulty_level):
    response = requests.get("https://v6.exchangerate-api.com/v6/3c199a046563bfbb7307af3e/pair/USD/ILS")
    ils = response.json()["conversion_rate"]
    computer_choos = random.randint(1, 100)
    print(f"Guess how much {computer_choos}$ is in shekels: ")
    highest_number = ils * computer_choos + 10 - difficulty_level
    lower_number = ils * computer_choos - 10 + difficulty_level
    return highest_number, lower_number


def get_guess_from_user():
    while True:
        user_guess = input(f"Guess: ")
        if str.isdigit(user_guess):
            return float(user_guess)
        else:
            print("You have chosen an impossible number or sign")


def compare_results(highest_number, lower_number, user_guess):
    if lower_number <= user_guess <= highest_number:
        print("You're right!")
        return True
    else:
        print("You are wrong, maybe next time :(")
        return False


def play(difficulty):
    money = get_money_interval(difficulty)
    highest = money[0]
    lower = money[1]
    return compare_results(highest, lower, get_guess_from_user())

