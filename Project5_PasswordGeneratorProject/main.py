'''
No. project: 5
Name project: Password Generator
Description: This is a password generator program written in Python. It obtains the number of characters selected by the user
             for each type (letters, numbers, and symbols) and automatically shuffles them to generate a password.
Author: Jonathan Eduardo Castilla Zamora
'''

import random # Importing module for generating aleatory numbers

# List of characters for generating the password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Printing a greeting message to user
print("Welcome to the PyPassword Generator!")

# Obtaining the length of each type of character in order to generate their password
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Defining 'password' variable
password = ""

# Selecting aleatory characters from lists
# by means of number of characters chose and random module from Python

for number_of_letters in range(nr_letters):
    password += random.choice(letters)
for number_of_symbols in range(nr_symbols):
    password += random.choice(symbols)
for number_of_numbers in range(nr_numbers):
    password += random.choice(numbers)

# Shuffling the password
password_in_list = list(password) # Converting string to a list of characters
random.shuffle(password_in_list) # Shuffling the elements of list
shuffled_password = "".join(password_in_list) # Converting list to a string again already shuffled

# Printing result
print("Your password generated is: ", shuffled_password)