import random


# get_user_choice() gets the user to input their choice of 'R', 'P', or 'S' for Rock, Paper, or
# Scissors respectively, using a while loop to ensure that the user enters a valid choice and
# prompts them again if the input is not one of the specified options.The function returns the
# validated user input in uppercase.
def get_users_choice():
    """
    Get the user to enter their choice (R, P, or S).
    """
    user_input = input("Enter your choice (R = Rock, P = Paper, S = Scissors): ").upper()
    while user_input not in ['R', 'P', 'S']:
        print("Invalid choice! Enter R, P, or S.")
        user_input = input("Enter your choice (R = Rock, P = Paper, S = Scissors): ").upper()
    return user_input


# convert_choice() takes a single argument choice, which represents the user's input ('R', 'P', or 'S').
# It converts the abbreviated user choice into the full word ('Rock', 'Paper', or 'Scissors') and
# returns it.
def convert_choice(choice):
    """
    Convert the user's choice into the full word (Rock, Paper, or Scissors).
    """
    if choice == 'R':
        return 'Rock'
    elif choice == 'P':
        return 'Paper'
    elif choice == 'S':
        return 'Scissors'


# This function get_computer_choice() randomly selects one of 'R', 'P', or 'S' for the computer's choice
# (Rock, Paper, or Scissors) using random.choice() from the random module.
def get_computer_choice():
    """
    Generate a random choice for the computer.
    """
    return random.choice(['R', 'P', 'S'])


# determine_winner() compares the user's choice with the computer's choice and determines the winner
# based on the rules of Rock, Paper, Scissors.
# It returns a string indicating the outcome: either a tie, the user wins, or the computer wins.
def determine_winner(user_choice, computer_choice):
    """
    Compare the choices and determine the winner.
    """
    if user_choice == computer_choice:
        return "Tie!"
    elif (user_choice == 'R' and computer_choice == 'S') or \
            (user_choice == 'P' and computer_choice == 'R') or \
            (user_choice == 'S' and computer_choice == 'P'):
        return "You win!"
    else:
        return "Computer wins!"
