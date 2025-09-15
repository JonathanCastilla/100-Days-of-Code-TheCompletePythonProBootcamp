'''
No. project: 9
Name project: Secret (Blind) Auction
Description: This program implements a text-based version of a secret (blind) auction.
             Multiple bidders can enter their names and bids without seeing others’ inputs.
             The program stores all bids in a dictionary and determines the highest bidder.
             At the end, it announces the winner with the highest bid.
Author: Jonathan Eduardo Castilla Zamora
'''

# Importing the logo from the external art module for UI purposes
from art import logo

def findBidderWithMaxBid(dictionary):
    """
    Finds the highest bid and corresponding bidder(s).

    Args:
        dictionary (dict): A dictionary where keys are bidder names (str)
                           and values are bid amounts (float).

    Returns:
        tuple: (max_bid, bidder_with_max_bid)
               - max_bid: the highest bid (float)
               - bidder_with_max_bid: list of bidder(s) who placed that bid
    """
    # Find the maximum bid among all dictionary values
    max_bid = max(dictionary.values())

    # Find all bidders who placed the maximum bid
    # (to handle cases where more than one person places the same highest bid)
    bidder_with_max_bid = [key for key, value in dictionary.items() if value == max_bid]

    return max_bid, bidder_with_max_bid


# Display ASCII art logo and program introduction
print(logo)
print("Welcome to the Secret Auction program.")

# Dictionary to store bids in format { "Name": amount }
dictionary = {}

# Flag to control whether new bidders should be allowed
restart_flag = True

# Main program loop: continues until no more bidders remain
while restart_flag:
    # Ask bidder for their name
    name = str(input("What is your name?: ")).title()  # .title() formats name with capital initials

    # Ask bidder for their bid and ensure it's stored as a float
    bid = float(input("What is your bid?: $"))

    # Store bidder name and bid into the dictionary
    dictionary[name] = bid

    # Ask if there are more bidders
    restart_indicator = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()

    # Validate the input: only "yes" or "no" are accepted
    while restart_indicator not in ["yes", "no"]:
        restart_indicator = input("Are there any other bidders? Type correctly 'yes' or 'no'. ").lower()

    # If there are more bidders, "clear the screen" by printing many blank lines
    if restart_indicator == "yes":
        print("\n" * 100)  # Simulates clearing the console for bid secrecy
        restart_flag = True
    else:
        # No more bidders: exit the loop
        print("\n" * 100)
        restart_flag = False

# Once no more bidders remain, find the highest bid and winner(s)
maxBid, bidderWithMaxBid = findBidderWithMaxBid(dictionary)

# Print the final winner
# If multiple bidders tie with the same max bid, the first one in the list is chosen
print(f"The winner is {bidderWithMaxBid[0]} with a bid of ${maxBid}")
