# This is a Band Name Generator

def band_name_generator():
    print("Welcome to the Band Name Generator!\n")
    city_name = input("Firstly, what is the name of the city you grew up in?\n")
    pet_name = input("What is your pet name?\n")
    print("Your band name could be: " + "'" + city_name + " " + pet_name + "'")


if __name__ == '__main__':
    band_name_generator()

