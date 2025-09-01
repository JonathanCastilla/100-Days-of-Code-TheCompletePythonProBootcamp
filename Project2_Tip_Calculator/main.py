# This is a Tip calculator

'''
No. project: 2
Project name: Tip Calculator
Description: Small utility to calculate tip and split bills
Author: Jonathan Eduardo Castilla Zamora
'''



# Defining function in order to calculate the payment for each person
def tip_calculator():
    print("Welcome to the Tip Calculator!") # Adding a greeting for this code
    # Obtaining the data from user in order to calculate the bill for each one
    bill = float(input("What was the total bill? $"))
    tip = int(input("How much tip would you like to give? 10, 12, or 15%\n"))
    people = int(input("How many people to split the bill?\n"))

    # Calculating the payment for each person
    payment_for_person = (bill * (1 + (tip / 100))) / people

    # Printing the result
    print(f"Each person should pay: ${round(payment_for_person, 2)}")

# Main function
if __name__ == '__main__':
    tip_calculator() # Calling the function
