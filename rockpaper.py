import random

# Available choices
choices = ['rock', 'paper', 'scissors']

# Score tracking
user_score = 0
computer_score = 0

def get_user_choice():
    while True:
        user_input = input("Choose rock, paper, or scissors: ").lower()
        if user_input in choices:
            return user_input
        else:
            print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")

def get_computer_choice():
    return random.choice(choices)

def determine_winner(user, computer):
    global user_score, computer_score
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        user_score += 1
        return "You win!"
    else:
        computer_score += 1
        return "Computer wins!"

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    global user_score, computer_score

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        print(result)
        print(f"\nScore => You: {user_score} | Computer: {computer_score}")

        play_again = input("\nDo you want to play another round? (yes/no): ").lower()
        if play_again not in ['yes', 'y']:
            print("\nThanks for playing! Final Score => You: {} | Computer: {}".format(user_score, computer_score))
            break

# Start the game
play_game()