import random


def generate_number(difficulty):
    return random.randint(0, difficulty)


def get_guess_from_user(difficulty):
    return int(input(f"Guess a number between 0 and {difficulty}: "))


def compare_results(secret_number, user_guess):
    return secret_number == user_guess


def play(difficulty):
    secret_number = generate_number(difficulty)
    user_guess = get_guess_from_user(difficulty)
    result = compare_results(secret_number, user_guess)
    if result:
        print("You're right!")
    else:
        print(f"Wrong guess! The correct number was {secret_number}.")
    return result
