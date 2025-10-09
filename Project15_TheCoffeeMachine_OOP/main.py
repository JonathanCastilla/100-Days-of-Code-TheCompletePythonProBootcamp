"""
Project Number: 15
Project Name: The Coffee Machine Program (Object-Oriented Version)
Description:
    This program implements an object-oriented version of the Coffee Machine simulation.
    It integrates three primary classes: Menu, CoffeeMaker, and MoneyMachine, each
    responsible for a specific functionality within the system. The user is able to
    select a beverage (espresso, latte, or cappuccino), and the program ensures that
    sufficient resources (water, milk, and coffee) are available to prepare it.

    The MoneyMachine class manages all monetary transactions, including payment
    validation and change calculation. The CoffeeMaker class handles resource
    management and beverage preparation, while the Menu class provides access to
    available drinks and their corresponding information.

    The system operates interactively via the terminal, allowing the user to:
    - Request a drink.
    - Generate a report of current machine resources and total profit.
    - Exit the program gracefully.

    This modular design enhances readability, scalability, and maintainability by
    encapsulating each functionality into independent classes.

Author: Jonathan Eduardo Castilla Zamora
"""

# Importing necessary modules and classes.
# These modules are expected to define the main components of the coffee machine system:
# - Menu: Handles available drink options.
# - CoffeeMaker: Manages resources (water, milk, coffee) and prepares drinks.
# - MoneyMachine: Processes payments and tracks profit.
# - art: Contains visual ASCII banners used for better presentation.
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from art import logo, title

# ---------------------------------------------------------------
# INITIALIZATION OF MAIN OBJECTS
# ---------------------------------------------------------------

# The boolean flag that keeps the coffee machine operational.
operating_machine_coffee = True

# Instantiate the main system components.
menu = Menu()                       # Manages the list of drink items and drink retrieval.
coffee_maker = CoffeeMaker()        # Handles drink preparation and resource validation.
money_machine = MoneyMachine()      # Manages all monetary transactions.

# ---------------------------------------------------------------
# MAIN EXECUTION LOOP
# ---------------------------------------------------------------
# This loop maintains continuous operation of the coffee machine.
# It will only terminate when the user explicitly requests to exit.

while operating_machine_coffee:
    print(title)  # Displays the ASCII-art title of the application.
    print(logo)   # Displays the decorative logo for aesthetic purposes.

    menu_item = None  # Variable used to store the selected drink item.

    # ---------------------------------------------------------------
    # USER INPUT VALIDATION
    # ---------------------------------------------------------------
    # This nested loop ensures that the user's input corresponds to an
    # available menu item or a valid command ("report" or "exit").
    while menu_item is None:
        # Prompt the user to select a beverage from the available menu.
        user_input = str(input(f"What would you like? Type correctly ({menu.get_items()}): "))

        # If the user requests a report, display current resources and total profit.
        if user_input in ['report']:
            coffee_maker.report()     # Display resource levels: water, milk, coffee.
            money_machine.report()    # Display financial information (profit, balance).

        # If the user requests to exit, break the input loop.
        elif user_input in ['exit']:
            break

        # Otherwise, search for the drink in the menu database.
        else:
            menu_item = menu.find_drink(user_input)

    # If the user typed 'exit', terminate the main program loop.
    if user_input in ['exit']:
        break

    # ---------------------------------------------------------------
    # RESOURCE AND PAYMENT VALIDATION
    # ---------------------------------------------------------------
    # If a valid drink is selected, verify that resources are sufficient.
    if coffee_maker.is_resource_sufficient(menu_item):
        # Display the cost of the selected beverage.
        print(f"It will be: ${menu_item.cost}")

        # Request payment from the user and validate the transaction.
        successful_payment = money_machine.make_payment(menu_item.cost)

        # If payment succeeds, proceed with drink preparation.
        if successful_payment:
            coffee_maker.make_coffee(menu_item)

    # ---------------------------------------------------------------
    # INSUFFICIENT RESOURCE HANDLING
    # ---------------------------------------------------------------
    # If resources are insufficient to prepare the requested drink,
    # inform the user and suggest terminating the program.
    else:
        print("Type 'exit' to exit. Thank you! Hope you enjoy!")

# ---------------------------------------------------------------
# END OF PROGRAM EXECUTION
# ---------------------------------------------------------------
# Upon exiting, all resources and data remain managed by their
# respective classes, maintaining an encapsulated and modular design.
