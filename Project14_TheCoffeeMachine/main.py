"""
Project Number: 14
Project Name: The Coffee Machine Program
Description:
    This program simulates a text-based coffee machine. The user can order
    one of three available drinks: espresso, latte, or cappuccino. The system
    checks if there are sufficient resources (water, milk, coffee) to prepare
    the selected drink. If resources are adequate, the user is prompted to insert
    coins (quarters, dimes, nickels, pennies), from which the program calculates
    the total payment and verifies whether the amount is sufficient to cover the
    cost. If the transaction is successful, the drink is "served," resources are
    deducted, and change is provided if applicable. The user may also request a
    resources report to check the machine’s current stock. The program continues
    running until it is manually terminated.
Author: Jonathan Eduardo Castilla Zamora
"""

from coffee_machine_data import MENU, resources  # Predefined drink menu and resource levels
from decimal import Decimal                     # Used for precise monetary calculations
from art import logo, title                     # ASCII art for visual presentation

def ask_for_coins():
    """
    Prompts the user to input the number of coins inserted.
    Ensures that all inputs are integer values.
    Returns the total count of each coin type.
    """
    quarters = str(input("How many quarters? "))
    while not quarters.isdigit():
        quarters = str(input("How many quarters? You must enter an integer number: "))
    quarters = int(quarters)

    dimes = str(input("How many dimes? "))
    while not dimes.isdigit():
        dimes = str(input("How many dimes? You must enter an integer number: "))
    dimes = int(dimes)

    nickles = str(input("How many nickles? "))
    while not nickles.isdigit():
        nickles = str(input("How many nickles? You must enter an integer number: "))
    nickles = int(nickles)

    pennies = str(input("How many pennies? "))
    while not pennies.isdigit():
        pennies = str(input("How many pennies? You must enter an integer number: "))
    pennies = int(pennies)

    return quarters, dimes, nickles, pennies

def calculate_user_payment(quarters, dimes, nickles, pennies):
    """
    Converts the number of coins to monetary value using Decimal for accuracy.
    Returns the total payment as a Decimal.
    """
    total_payment = (
        Decimal(quarters) * Decimal('0.25') +
        Decimal(dimes) * Decimal('0.10') +
        Decimal(nickles) * Decimal('0.05') +
        Decimal(pennies) * Decimal('0.01')
    )
    return total_payment

def validate_user_payment(payment, drink_selected_cost):
    """
    Compares the user's payment with the drink cost.
    Returns True if payment is sufficient, otherwise False.
    """
    if payment < drink_selected_cost:
        return False
    else:
        return True

def calculate_change(user_total_payment, drink_selected_cost):
    """
    Calculates and returns the change owed to the user,
    using Decimal for precise subtraction.
    """
    drink_cost_decimal = Decimal(str(drink_selected_cost))
    user_change = user_total_payment - drink_cost_decimal
    return user_change

def obtain_drink_cost(menu, drink_selected):
    """
    Retrieves the cost of the selected drink
    from the provided menu data structure.
    """
    drink_selected_cost = menu[drink_selected]['cost']
    return drink_selected_cost

def calculate_cost_of_resources_for_drink(menu, drink_selected):
    """
    Retrieves the ingredients (required resources) for
    the selected drink from the menu data structure.
    """
    drink_selected_resources = menu[drink_selected]['ingredients']
    return drink_selected_resources

def ask_for_availability_for_drink_resources(
    drink_selected,
    availability_for_drink,
    actual_resources,
    resources_for_user_drink
):
    """
    Checks whether the coffee machine has enough resources to prepare
    the user-selected drink. Espresso does not require milk; all other
    drinks do. Returns True if resources are sufficient, otherwise False.
    """
    if drink_selected != 'espresso':
        if (actual_resources['water'] // resources_for_user_drink['water'] >= 1
            and actual_resources['milk'] // resources_for_user_drink['milk'] >= 1
            and actual_resources['coffee'] // resources_for_user_drink['coffee'] >= 1):
            availability_for_drink = True
        else:
            availability_for_drink = False
    else:
        # Espresso only requires water and coffee
        if (actual_resources['water'] // resources_for_user_drink['water'] >= 1
            and actual_resources['coffee'] // resources_for_user_drink['coffee'] >= 1):
            availability_for_drink = True
        else:
            availability_for_drink = False

    return availability_for_drink

def calculate_actual_resources(actual_resources, resources_for_user_drink):
    """
    Deducts the resources used for preparing the drink
    from the coffee machine's current resources.
    Returns the updated resource dictionary.
    """
    actual_resources['water'] = actual_resources['water'] - resources_for_user_drink['water']
    actual_resources['milk'] = actual_resources['milk'] - resources_for_user_drink['milk']
    actual_resources['coffee'] = actual_resources['coffee'] - resources_for_user_drink['coffee']
    return actual_resources

def print_coffee_machine_resources(actual_resources):
    """
    Displays a report of the coffee machine's current resources:
    water, milk, coffee, and money.
    """
    print("\n")
    print(" ===================================== ")
    print("      Coffee Machine Resources         ")
    print(f"  - Water: {actual_resources['water']} [ml]")
    print(f"  - Milk: {actual_resources['milk']} [ml]")
    print(f"  - Coffee: {actual_resources['coffee']} [g]")
    print(f"  - Money: ${actual_resources['money']}")
    print(" ===================================== ")
    print("\n")


# Copy the initial resources so that we do not modify the original data
actual_resources_in_coffee_machine = resources.copy()
available_resources_for_a_drink = True
operating_machine_coffee = True

print(title)  # Display the program's title

# Main loop that continues the coffee machine operation
while operating_machine_coffee:
    print(logo)  # Display the coffee machine ASCII logo
    user_input = str(input("What would you like? Type (espresso/latte/cappuccino): "))

    # Input validation for user's drink selection or report request
    while user_input not in (list(MENU.keys()) + ['report']):
        user_input = str(input("What would you like? Type correctly (espresso/latte/cappuccino): "))

    # If the user requests a drink
    if user_input in list(MENU.keys()):
        # Determine the resources needed for the selected drink
        resources_for_selected_drink = calculate_cost_of_resources_for_drink(
            menu=MENU,
            drink_selected=user_input
        )

        # Check availability of required ingredients
        available_resources_for_a_drink = ask_for_availability_for_drink_resources(
            drink_selected=user_input,
            availability_for_drink=available_resources_for_a_drink,
            actual_resources=actual_resources_in_coffee_machine,
            resources_for_user_drink=resources_for_selected_drink
        )

        if available_resources_for_a_drink:
            # Provide drink cost and prompt user to insert coins
            drink_cost = obtain_drink_cost(menu=MENU, drink_selected=user_input)
            print(f"It will cost: ${drink_cost}")
            print("Please, insert coins. ")

            quarters, dimes, nickles, pennies = ask_for_coins()
            user_payment = calculate_user_payment(quarters, dimes, nickles, pennies)

            # Validate payment
            user_payment_validation = validate_user_payment(
                payment=user_payment,
                drink_selected_cost=drink_cost
            )

            if user_payment_validation:
                # Successful transaction
                print(f"Your payment was ${user_payment}")
                print(f"Your change is ${calculate_change(user_total_payment=user_payment, drink_selected_cost=drink_cost)}")

                # Deduct used resources
                actual_resources_in_coffee_machine = calculate_actual_resources(
                    actual_resources=actual_resources_in_coffee_machine,
                    resources_for_user_drink=resources_for_selected_drink
                )

                # Update machine's money
                actual_resources_in_coffee_machine['money'] += drink_cost
            else:
                # Payment insufficient
                print(f"Your payment was ${user_payment}")
                print(f"Sorry, that is not enough money. Money refunded.")
        else:
            # Insufficient resources to prepare the selected drink
            print("\n" * 100)  # Simulated screen clearing
            print(title)
            print(f"Sorry, there is no available resources for this drink.")
            print(logo)
            print_coffee_machine_resources(actual_resources=actual_resources_in_coffee_machine)

    else:
        # The user requested a resources report
        print("\n" * 100)
        print(title)
        print(logo)
        print_coffee_machine_resources(actual_resources=actual_resources_in_coffee_machine)
