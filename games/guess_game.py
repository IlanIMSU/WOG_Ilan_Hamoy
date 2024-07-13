import random


def generate_number(difficulty_level):
    secret_number = random.randint(0, difficulty_level)
    print(f"the number is {secret_number}")
    return secret_number


def get_guess_from_user(difficulty_level):
    while True:
        user_guess = input(f"Guess a number between 0 and {difficulty_level}: ")
        if str.isdigit(user_guess) and 0 <= int(user_guess) <= difficulty_level:
            return int(user_guess)
        else:
            print("You have chosen an impossible number or sign")


def compare_results(secret_number, user_gues):
    if secret_number == user_gues:
        print("You're right!")
        return True
    else:
        print("You are wrong, maybe next time :(")
        return False


def play(difficulty):
    print("Welcome to the Guess Game")
    return compare_results(generate_number(difficulty), get_guess_from_user(difficulty))
