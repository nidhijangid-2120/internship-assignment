# Rock Paper Scissor Game
import random

def get_user_choice():
    choice = input("Enter your choice (rock, paper, scissors): ").lower()
    while choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please try again.")
        choice = input("Enter your choice (rock, paper, scissors): ").lower()
    return choice

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "user"
    else:
        return "computer"

print("Welcome to Rock Paper Scissors!")
user_score = 0
computer_score = 0

for round_number in range(1, 6):
    print(f"\nRound {round_number}")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You chose {user_choice}.")
    print(f"Computer chose {computer_choice}.")

    result = determine_winner(user_choice, computer_choice)
    if result == "tie":
        print("It's a tie!")
        user_score += 1
        computer_score += 1
    elif result == "user":
        print("You win this round!")
        user_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1

print(f"\nFinal Score - You: {user_score}, Computer: {computer_score}")
if user_score > computer_score:
    print("Congratulations! You won the game!")
elif user_score < computer_score:
    print("The computer won the game. Better luck next time!")
else:
    print("The game is a draw!")
