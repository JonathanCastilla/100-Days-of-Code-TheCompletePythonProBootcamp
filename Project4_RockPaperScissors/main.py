import random # Import random module for generating aleatory numbers

# ASCII art in order to represent the different states involves during the game
# Implementing a dictionary
game_states = {
"rock":'''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',

"paper":'''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''',

"scissors":'''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''}

print("Welcome to the Rock - Paper - Scissors Game!") # Print a greeting message

# Obtaining the choice from player and printing it
player_choice = str(input("Firstly, What do you choose? Type 'Rock', 'Paper' or 'Scissors': ")).lower()
print(game_states[player_choice])

# By means of random module we can generate the choice from computer and printing it
computer_choice = random.choice(['rock', 'paper', 'scissors'])
print(f"Computer chose: {computer_choice.title()}")
print(game_states[computer_choice])

# The logic behind Rock - Paper - Scissors Game
if computer_choice == player_choice:
    print("It's a tie!")
elif computer_choice == 'rock' and player_choice == 'scissors' or computer_choice == 'scissors' and player_choice == 'paper' or computer_choice == 'paper' and player_choice == 'rock':
    print("Computer wins!")
else:
    print("You win!")