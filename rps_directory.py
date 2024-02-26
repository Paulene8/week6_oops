def player_converter(user_input):
    if user_input == "R":
        tool = 0
        print("You chose Rock")
    elif user_input == "P":
        tool = 1
        print("You chose Paper")
    elif user_input == "S":
        tool = 2
        print("You chose Scissors")
    else:
        tool = None
        print('ERROR! Input "R" for Rock, "P" for Paper and "S" for Scissors')
    return tool


def comp_converter(comp_input):
    if comp_input == 0:
        tool = 0
        print("Computer chose Rock")
    elif comp_input == 1:
        tool = 1
        print("Computer chose Paper")
    else:
        tool = 2
        print("Computer chose Scissors")
    return tool


def outcome(self, comp_input, user_choice):
    self.comp = comp_input
    self.user = user_choice
#
#     def winlose(self, comp_input, user_choice):
#         win =
#         elif user_choice == 0 and comp_input == 2:
#             print("You win!")
#             # wins += 1
#         elif user_choice == 1 and comp_input == 0:
#             print("You win!")
#             # wins += 1
#         elif user_choice == 2 and comp_input == 1:
#             print("You win!")
#             # wins += 1
#         else:
#             print("You lose")


    # def draw(comp_input, user_choice):
    #     if comp_input == user_choice:
    #         return "it's a draw"


# def outcome(computer_input, user_input, wins):
#     if user_input == "R" and computer_input == 0:
#         print(f"You chose {user_input}, computer chose Rock. It's a draw!")
#     elif user_input == "P" and computer_input == 1:
#         print(f"You chose {user_input}, computer chose Paper. It's a draw!")
#     elif user_input == "S" and computer_input == 2:
#         print(f"You chose {user_input}, computer chose Scissors. It's a draw!")
#     else:
#         player_lose(computer_input, user_input) or player_wins(computer_input, user_input, wins=0)
#
#
# def player_wins(computer_input, user_input, wins):
#     if user_input == "R" and computer_input == 2:
#         print(f"You chose {user_input}, computer chose Scissors. You win!")
#         wins += 1
#     elif user_input == "P" and computer_input == 0:
#         print(f"You chose {user_input}, computer chose Rock. You win!")
#         wins += 1
#     elif user_input == "S" and computer_input == 1:
#         print(f"You chose {user_input}, computer chose Paper. You win!")
#         wins += 1
#
# def player_lose(computer_input, user_input):
#     if user_input == "R" and computer_input == 1:
#         print(f"You chose {user_input}, computer chose Paper. You lose!")
#     elif user_input == "P" and computer_input == 2:
#         print(f"You chose {user_input}, computer chose Scissors. You lose!")
#     elif user_input == "S" and computer_input == 0:
#         print(f"You chose {user_input}, computer chose Rock. You lose!")







