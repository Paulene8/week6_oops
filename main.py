from functions import get_users_choice, convert_choice, get_computer_choice, determine_winner


# main() is the entry point of the program.
# Prints the introductory message, calls get_user_choice() to get the
# user's input, and convert_choice() to convert it into the full word.
# It then calls get_computer_choice() to get the
# computer's random choice and converts it similarly.
# Finally, it prints both choices and the outcome determined by
# determine_winner().

def main():
    """
    Main function to run the game.
    """
    print("Let's play Rock, Paper, Scissors!")

    user_score = 0
    computer_score = 0
    # stores the score of the game for each loop and continues until either the user or the computer
    # reaches 3 wins
    while user_score < 3 and computer_score < 3:
        user_choice = get_users_choice()
        # stores the user's input in get_users_choice() in user_choice
        computer_choice = get_computer_choice()
        # stores the generated get_computer_choice() in computer_choice
        print(f"You chose {convert_choice(user_choice)}. Computer chose {convert_choice(computer_choice)}.")
        # the choices made by the user and the computer.
        result = determine_winner(user_choice, computer_choice)
        print(result)
        # based on the choices made, the result stores the winner of the round using determine_winner
        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1
        print(f"Score: You {user_score} - {computer_score} Computer")
        # an if statement is used to add a point to either score based on the string message from
        # determine_winner() and prints the score of that round
    # the while loop is exited after either the computer or user reaches 3 and enters an if statement to
    # check who reached 3 and print a message
    if user_score == 3:
        print("WHOOP WHOOPP! You win the game!")
    else:
        print("Better luck next time! Computer wins the game!")


if __name__ == "__main__":
    main()

    # The special variable __name__ is used to determine whether a Python script is being run as the main program or
    # being imported as a module into another script.
    # if __name__ == "__main__": works is crucial, especially when you're writing reusable code that could be both run
    # as a standalone program or imported as a module into another script.
    # When Python runs a script, it sets the special variable __name__ for that script.
    # If the script is being run as the main program, Python sets __name__ to "__main__".
    # If the script is being imported as a module into another script, Python sets __name__
    # to the name of the module.
    # The if __name__ == "__main__": block allows you to separate code that should be executed only when the script is
    # run as the main program from code that should not be executed when the script is imported as a module.
