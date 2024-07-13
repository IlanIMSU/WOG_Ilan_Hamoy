from games import currency_roulette_game, guess_game, memory_game
import score

def welcome():
    user_personal_name = input("Hi, What is your name? ")
    print(f"Hi {user_personal_name} and welcome to the World of Games: The Epic Journey")


def start_play():
    while True:
        game_choice = input(""" 
Please choose a game to play:   
1. Memory Game - a sequence of numbers will appear for 1 second and you have to 
guess it back.
2. Guess Game - guess a number and see if you chose like the computer.
3. Currency Roulette - try and guess the value of a random amount of USD in ILS
""")

        if str.isdigit(game_choice) and 0 < int(game_choice) < 4:
            while True:

                difficulty_level = input("select a difficulty level between 1 and 5:")

                if str.isdigit(difficulty_level) and 0 < int(difficulty_level) < 6:
                    break
                else:
                    print("This option does not exist")

            if int(game_choice) == 1:
                if memory_game.play(int(difficulty_level)):
                    score.add_score(int(difficulty_level))

            elif int(game_choice) == 2:
                if guess_game.play(int(difficulty_level)):
                    score.add_score(int(difficulty_level))

            elif int(game_choice) == 3:
                if currency_roulette_game.play(int(difficulty_level)):
                    score.add_score(int(difficulty_level))
        else:
            print("This option does not exist, choose again")

