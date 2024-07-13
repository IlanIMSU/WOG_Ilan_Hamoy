import random
import time


def generate_sequence(difficulty_level):
    computer_list = []
    for random_num in range(difficulty_level):
        num = random.randint(1, 101)
        computer_list.append(num)
    print(computer_list, end="")
    time.sleep(0.7)
    print("", end="\r")
    return computer_list


def get_list_from_user():
    user_input = input('input a list of numbers that match the length of generated sequence,'
                      ' separate the numbers with either a space or ",":')
    user_list = user_input.replace(',', ' ').split()
    int_user_list = []
    for num in user_list:
        int_user_list.append(int(num))

    return int_user_list


def is_list_equal(computer_list, user_list):
    if computer_list == user_list:
        print("You're right!")
        return True
    else:
        print("You are wrong, maybe next time :(")
        return False


def play(difficulty):
    return is_list_equal(generate_sequence(difficulty), get_list_from_user())


