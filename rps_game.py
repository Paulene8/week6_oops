import random, rps_directory

options = {0: "Rock", 1: "Paper", 2: "Scissors"}

# comp_input = random.choice(list(options.items()))
comp_input = random.randint(0, 2)
print(comp_input)

user_choice = input("Choose your weapon: ")

rps_directory.outcome(rps_directory.player_converter(user_choice), rps_directory.comp_converter(comp_input))

