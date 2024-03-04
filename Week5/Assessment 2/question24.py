# Implement the game rock, paper, scissors
# Rock smashes scissors.
# Paper covers rock.
# Scissors cut paper.

import random

def get_user_choice(player_name):
    while True:
        try:
            user_input = input(f"{player_name}, enter your choice (rock, paper, or scissors): ").lower()
            if user_input in ["rock", "paper", "scissors"]:
                return user_input
            else:
                print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
        except KeyboardInterrupt:
            print("\nGame interrupted. Exiting.")
            exit()

def get_opponent_choice(is_computer, opponent_name):
    if is_computer:
        return random.choice(["rock", "paper", "scissors"])
    else:
        return get_user_choice(opponent_name)

def play_game(player_name, play_with_computer, opponent_name=None):
    player_score = 0
    opponent_score = 0
    rounds = int(input("Enter the number of rounds you want to play: "))

    print("\nWelcome to the Rock, Paper, Scissors Game!")

    if play_with_computer:
        print("You are playing against the computer.")
    else:
        print(f"You are playing against {opponent_name}.")

    for round in range(1, rounds + 1):
        print(f"\nRound {round}:")
        player_choice = get_user_choice(player_name)
        opponent_choice = get_opponent_choice(play_with_computer, opponent_name)
        print(f"{player_name}'s choice: {player_choice}")
        if play_with_computer:
            print(f"Computer's choice: {opponent_choice}")
        else:
            print(f"{opponent_name}'s choice: {opponent_choice}")

        if player_choice == opponent_choice:
            print("It's a tie!")
        elif (player_choice == 'rock' and opponent_choice == 'scissors') or \
             (player_choice == 'paper' and opponent_choice == 'rock') or \
             (player_choice == 'scissors' and opponent_choice == 'paper'):
            print(f"{player_name} wins!")
            player_score += 1
        else:
            if play_with_computer:
                print("Computer wins!")
            else:
                print(f"{opponent_name} wins!")
            opponent_score += 1

    print("\nGame Over!")
    print(f"{player_name}'s score: {player_score}")
    if play_with_computer:
        print("Computer's score: ", opponent_score)
    else:
        print(f"{opponent_name}'s score: {opponent_score}")

    if player_score > opponent_score:
        print(f"Congratulations, {player_name} wins!")
    elif player_score < opponent_score:
        print(f"Sorry, {opponent_name} wins. Better luck next time!")
    else:
        print("It's a tie overall!")

def main():
    player_name = input("Enter your name: ")
    while True:
        try:
            play_with_computer_input = input("Do you want to play with the computer? (y/n): ").lower()
            if play_with_computer_input not in ['y', 'n']:
                raise ValueError("Invalid input. Please enter 'y' or 'n'.")
            play_with_computer = play_with_computer_input == "y"
            break
        except ValueError as e:
            print(e)

    if not play_with_computer:
        opponent_name = input("Enter your opponent's name: ")
        play_game(player_name, play_with_computer, opponent_name)
    else:
        play_game(player_name, play_with_computer)

if __name__ == "__main__":
    main()
