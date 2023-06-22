import random

def game_stats(rounds, user_wins, computer_wins):
    print("*" * 10)

    print("Ronda", rounds, ": ")

    print("*" * 10)

    print("Victorias de user: ", user_wins, "/ 2")

    print("Victorias de computer: ", computer_wins, "/ 2")

    print("*" * 10)

    print("Elige una opcion: ") 

def player_options_selection():
    options = ("piedra", "papel", "tijeras")
    user_option = input('piedra, papel o tijeras => ')
    user_option = user_option.lower()

    while not user_option in options:
        print("Elige una opcion valida: ")
        user_option = input('piedra, papel o tijeras => ')

    computer_option = random.choice(options)

    print("*" * 10)

    print("Opcion de user: ", user_option)

    print("opcion de computer:", computer_option)

    return user_option, computer_option

def round_winner(user_option, computer_option, user_wins, computer_wins):
    win = ("piedratijeras", "tijeraspapel", "papelpiedra")

    fight = user_option + computer_option

    print("Resultado: ")

    if user_option == computer_option:
        print('Empate!')

    elif fight in win:
        print("user gana la ronda")
        user_wins +=1

    else:
        print("computer gana la ronda")
        computer_wins +=1

    print("*" * 10)

    return user_wins, computer_wins

def match_winner(user_wins, computer_wins):
    if user_wins > computer_wins:
        print("User gana la partida")

    else: 
        print("Computer gana la partida")

def run_game():
    rounds = 1

    user_wins = 0

    computer_wins = 0

    while user_wins != 2 and computer_wins != 2:

        game_stats(rounds, user_wins, computer_wins)

        user_option, computer_option = player_options_selection()

        user_wins, computer_wins = round_winner(user_option, computer_option, user_wins, computer_wins)

        rounds +=1

    match_winner(user_wins, computer_wins)

run_game()