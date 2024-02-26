import random
# importing the random module for generating computer choices


# class encapsulates the method of the Rock, Paper, Scissors game.
class Rockpaperscissorsgame:
    def __init__(self):
        # player's username and age attributes
        self.player_username = None
        self.player_age = None

    def set_player_detail(self, name, age):
        # creating a set_player_detail method to set player's username and age using the attributes from  __init__() method
        self.player_username = name.upper()
        self.player_age = age

    def get_users_choice(self):
        """
            Get the user to enter their choice (R, P, or S) and checking if its valid entry
        """
        user_input = input("Enter your choice (R = Rock, P = Paper, S = Scissors): ").upper()
        while user_input not in ['R', 'P', 'S']:
            print("Invalid choice! Enter R, P, or S.")
            user_input = input("Enter your choice (R = Rock, P = Paper, S = Scissors): ").upper()
        return user_input

    def convert_choice(self, choice):
        """
            Convert the user's choice into the full word (Rock, Paper, or Scissors).
        """
        if choice == 'R':
            return 'Rock'
        elif choice == 'P':
            return 'Paper'
        elif choice == 'S':
            return 'Scissors'

    def get_computer_choice(self):
        """
            Generating a random choice for the computer.
        """
        return random.choice(['R', 'P', 'S'])

    def determine_winner(self, user_choice, computer_choice):
        """
            Comparing the choices and determining the winner.
        """
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == 'R' and computer_choice == 'S') or \
                (user_choice == 'P' and computer_choice == 'R') or \
                (user_choice == 'S' and computer_choice == 'P'):
            return f"You win this round {self.player_username}!"
        else:
            return "Computer wins this round!"

#     def main(self, computer_score=0, user_score=0):
#         """
#             Main function to run the game.
#             """
#         if self.player_age is None:
#             age = int(input("Enter your age: "))
#             if age < 8:
#                 print("Sorry, you must be 8 years or older to play.")
#                 return
#             else:
#                 self.player_username = input("Enter your name: ")
#
#         print(f"Let's play Rock, Paper, Scissors, {self.player_username}!")
#
#         while user_score < 3 and computer_score < 3:
#             user_choice = self.get_users_choice()
#             computer_choice = self.get_computer_choice()
#             print(
#                 f"You chose {self.convert_choice(user_choice)}. Computer chose {self.convert_choice(computer_choice)}.")
#             result = self.determine_winner(user_choice, computer_choice)
#             print(result)
#             if result == "You win!":
#                 user_score += 1
#             elif result == "Computer wins!":
#                 computer_score += 1
#             print(f"Score: {self.player_username} {user_score} - {computer_score} Computer")
#
#         if user_score == 3:
#             print(f"WHOOP WHOOPP! Congratulations, {self.player_username.upper()}! YOU WON THE GAME!")
#         else:
#             print(f"Sorry {self.player_username}! Computer won the game!")
#
#
# # Main block to create instance of RockPaperScissorsGame and run the game
# if __name__ == "__main__":
#     game = RockPaperScissorsGame()
#     game.main()
