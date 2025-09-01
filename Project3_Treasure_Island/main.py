# TREASURE ISLAND

'''
No. project: 3
Name's project: Treasure Island
Description: A tex-based adventure game using conditionals
Author: Jonathan Eduardo Castilla Zamora
'''


print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# Fist decision statement
first_decision = str(input("Would you like to go to left or right? (left or right): ")).lower() # Ensuring that input from user must be lowercase letters

# IF - ELSE CONDITIONALS

# First decision condition
if not first_decision == "left":
    print("Fall into a hole. \n")
    print("Game Over.")
else:
    # Second decision statement
    second_decision = str(input("Would you like to swim or wait? (swim or wait): ")).lower() # Ensuring that input from user must be lowercase letters
    # Conditions for second decision
    if not second_decision == "wait":
        print("Attacked by trout. \n")
        print("Game Over.")
    else:
        # Third decision statement
        third_decision = str(input("Which door would you like to cross? (red, blue or yellow): ")).lower() # Ensuring that input from user must be lowercase letters
        # Conditions for third decision
        if third_decision == "red":
            print("Burned by fire. \n")
            print("Game Over.")
        elif third_decision == "blue":
            print("Eaten by beasts. \n")
            print("Game Over.")
        elif third_decision == "yellow":
            print("You win!")
        else:
            print("You lose. \n")
            print("Game Over.")