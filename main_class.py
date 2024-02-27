from username_class import Rockpaperscissorsgame


#  new class MainRPSGame, which inherits from RockPaperScissorsGame
class MainRPSGame(Rockpaperscissorsgame):
    # Defining the main method
    def main(self, user_score=0, computer_score=0):
        """
        Main function to run the game.
        """
        # checking if the player age is not provided and then invites the player to enter there age. then enter into
        # another if statement where if the player is under 8, they cant continue to the game otherwise continue to create
        # a username and play the game.
        if self.player_age is None:
            age = int(input("Enter your age: "))
            if age < 8:
                print("Sorry, you must be 8 years or older to play.")
                return
            else:
                self.player_username = input("Enter your Username: ").title()

        print(f"Let's play Rock, Paper, Scissors, {self.player_username}!")

        # while loop with the game: continue until either the user or computer reaches 3 wins
        while user_score < 3 and computer_score < 3:
            user_choice = self.get_users_choice()
            # Getting the user's choice and from get_users_choice and storing it in user_choice
            computer_choice = self.get_computer_choice()
            # stores the generated get_computer_choice() in computer_choice
            # prints the choices made by both the user and computer
            print(
                f"{self.player_username} {self.convert_choice(user_choice)}. Computer chose "
                f"{self.convert_choice(computer_choice)}.")
            result = self.determine_winner(user_choice, computer_choice)
            print(result)
            # prints the result of the current round
            # giving the new scores based on the result of the round
            if result == f"You win this round {self.player_username}!":
                user_score += 1
            elif result == "Computer wins this round!":
                computer_score += 1
            #  prints the new score
            print(f"Score: {self.player_username} {user_score} vs {computer_score} Computer")

        if user_score == 3:
            print(f"WHOOP WHOOPP! Congratulations, {self.player_username.upper()}! YOU WON THE GAME!")
        else:
            print(f"OOPS, better luck next time {self.player_username}! Computer won the game!")
        # once the conditions of while loop have been met and either player wins, then enter into an if statement to
        # who the winner is


# Python checks if it's the main program (not being imported), creates an instance of the MainRPSGame class,
# and then calls the main() method of that instance, which starts the Rock, Paper, Scissors game.
# It encapsulates the game logic within a class and easily runs it when the script is executed directly.
# Main block used to create an instance of MainRPSGame and run the game
if __name__ == "__main__":  # This condition checks if the script is being run directly by the Python interpreter
    # (as opposed to being imported as a module in another script).
    # Python sets the special variable __name__ to "__main__" in the scope of that script.
    # So, the if __name__ == "__main__":
    # block allows you to execute certain code only when the script is run directly,
    # not when it's imported into another script.
    game = MainRPSGame()
    # Creates an instance of the MainRPSGame class called game
    # In OOP a class serves as a blueprint for creating objects (instances).
    # MainRPSGame is the class, and game is the object (instance) created from that class.
    # creating an instance of the MainRPSGame class allows you to utilise its functionality, isolate its behaviour and
    # state, customise its initial state, and adhere to object-oriented programming principles.
    game.main()
    # calls the main() method of the game object.
    # In Python, a method is a function that belongs to a class.
    # main() is a method defined within the MainRPSGame class.
    # By calling game.main(), you're executing the code inside the main() method of the MainRPSGame class.
