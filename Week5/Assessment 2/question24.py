# Implement the game rock, paper, scissors
# Rock smashes scissors.
# Paper covers rock.
# Scissors cut paper.

import random

def play_game():
    choices = ['rock', 'paper', 'scissors']
    user_score = 0
    computer_score = 0
    rounds = int(input("Enter the number of rounds you want to play: "))

    for round in range(1, rounds + 1):
        print(f"\nRound {round}:")
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        computer_choice = random.choice(choices)
        print(f"Your choice: {user_choice}")
        print(f"Computer's choice: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            print("You win!")
            user_score += 1
        else:
            print("Computer wins!")
            computer_score += 1

    print("\nGame Over!")
    print(f"Your score: {user_score}")
    print(f"Computer's score: {computer_score}")

    if user_score > computer_score:
        print("Congratulations! You win!")
    elif user_score < computer_score:
        print("Sorry, you lose. Better luck next time!")
    else:
        print("It's a tie overall!")

play_game()
