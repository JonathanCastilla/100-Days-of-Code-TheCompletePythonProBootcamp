# This is a Tip calculator

# Defining function to print band name generated
def tip_calculator():
    print("Welcome to the Tip Calculator!")
    bill = float(input("What was the total bill? $"))
    tip = int(input("How much tip would you like to give? 10, 12, or 15%\n"))
    people = int(input("How many people to split the bill?\n"))
    payment_for_person = (bill * (1 + (tip / 100))) / people

    print(f"Each person should pay: ${round(payment_for_person, 2)}")

# Main function
if __name__ == '__main__':
    tip_calculator() # Calling the function
