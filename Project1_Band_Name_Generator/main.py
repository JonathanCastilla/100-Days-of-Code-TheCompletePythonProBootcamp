# This is a Band Name Generator


'''
No. project: 1
Project name: Band Name Generator
Description: A simple beginner program generating funny band names.
Author: Jonathan Eduardo Castilla Zamora
'''



# Defining function to print band name generated
def band_name_generator():
    print("Welcome to the Band Name Generator!\n")
    # Obtaining data from user
    city_name = input("Firstly, what is the name of the city you grew up in?\n")
    pet_name = input("What is your pet name?\n")
    # Printing the band name generated
    print("Your band name could be: " + "'" + city_name + " " + pet_name + "'")

# Main function
if __name__ == '__main__':
    band_name_generator() # Calling the function

