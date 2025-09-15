'''
No. project: 10
Name project: Calculator
Description: This program implements a text-based calculator.
             The user can perform addition, subtraction, multiplication,
             and division operations on numbers. After each operation,
             the user can choose to continue calculating with the current result
             or start a new calculation. The program ensures input validation
             and displays results interactively in the console.
Author: Jonathan Eduardo Castilla Zamora
'''

# Import ASCII art logo for visual presentation
from art import logo

# -------------------- Functions for arithmetic operations --------------------

# Function to add two numbers
def add(n1, n2):
    return n1 + n2

# Function to subtract the second number from the first
def subtract(n1, n2):
    return n1 - n2

# Function to multiply two numbers
def multiply(n1, n2):
    return n1 * n2

# Function to divide the first number by the second
def divide(n1, n2):
    return n1 / n2

# Dictionary mapping arithmetic symbols to their corresponding functions
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# -------------------- Main Program Loop --------------------

# This flag controls whether the user wants to start a completely new calculation
new_calculation = True
while new_calculation:
    print(logo)  # Display the calculator logo at the start of each session

    # Initialize input numbers
    n1 = 0
    n2 = 0

    # Ask for the first number with input validation
    while str(n1).isdigit():
        try:
            n1 = float(input("What's the first number?: "))
        except ValueError:
            print("Please enter a valid number.")

    # Flag to determine if the user wants to continue with the current calculation
    continue_calculating = True
    while continue_calculating:
        # Display available operations
        for operation in operations:
            print(operation)

        # Ask the user to select an operation (+, -, *, /)
        type_of_operation = str(input("Please, pick an operation. Type '+', '-', '*' or '/': ")).lower()

        # Input validation: make sure user picks a correct operation
        while type_of_operation not in operations:
            type_of_operation = str(input("Please, pick an operation correctly. Type '+', '-', '*' or '/': ")).lower()

        # Ask for the next number with input validation
        while str(n2).isdigit():
            try:
                n2 = float(input("What's the next number?: "))
            except ValueError:
                print("Please enter a valid number.")

        # Perform the operation using the dictionary of functions
        actual_result = operations[type_of_operation](n1 = n1, n2 = n2)
        print(f"{n1} {type_of_operation} {n2} = {actual_result}")

        # Ask if the user wants to continue calculating with the current result
        decision_of_calculating = str(input(
            f"Type 'y' to continue calculating with {actual_result}. Otherwise, type 'n' to start a new calculation: "))

        # Input validation for decision
        while decision_of_calculating not in ["y", "n"]:
            decision_of_calculating = str(input(
                f"Type 'y' to continue calculating with {actual_result}. Otherwise, type 'n' to start a new calculation: "))

        # If user chooses to continue, update n1 with the result
        if decision_of_calculating == "y":
            continue_calculating = True
            n1 = actual_result
        else:
            # Otherwise, break and start a new calculation cycle
            continue_calculating = False
            print("\n" * 100)  # Simulate clearing the console for clarity
