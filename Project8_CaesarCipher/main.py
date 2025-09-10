'''
Project No.: 8
Project Name: Caesar Cipher
Description:
    This program implements a text-based version of the classic Caesar Cipher,
    a substitution cipher where each letter in the plaintext is shifted by a
    user-defined number of positions in the alphabet. The program allows the
    user to either encrypt (encode) or decrypt (decode) a given message.
    Non-alphabetical characters (e.g., spaces, punctuation) are preserved.
    The user can repeatedly perform operations until they choose to exit.
Author: Jonathan Eduardo Castilla Zamora
'''

# Import ASCII art logo for visual presentation
from art import logo

# Define the alphabet used for shifting.
# Only lowercase English letters are supported in this implementation.
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

def caesar_cipher(direction, original_text, shift_amount):
    """
    Applies the Caesar Cipher encryption or decryption to the given text.

    Parameters:
        direction (str): 'encode' to encrypt, 'decode' to decrypt.
        original_text (str): The message to be processed.
        shift_amount (int): The number of positions to shift in the alphabet.

    Behavior:
        - If direction is 'encode', letters are shifted forward.
        - If direction is 'decode', letters are shifted backward.
        - Non-alphabet characters (e.g., spaces, numbers, symbols) remain unchanged.
    """
    output_text = ""

    # Reverse shift if the user chose "decode"
    if direction == "decode":
        shift_amount *= -1

    # Iterate through each character in the input text
    for character in original_text:
        if character in alphabet:
            # Find the new shifted index within the alphabet
            shifted_position = alphabet.index(character) + shift_amount
            # Wrap around using modulo to stay within the alphabet length
            shifted_position %= len(alphabet)
            # Append the shifted character to the output
            output_text += alphabet[shifted_position]
        else:
            # Preserve non-alphabetic characters (spaces, symbols, etc.)
            output_text += character

    # Display the result
    print(f"Here is the {direction}d result: {output_text}")

# Main loop control variable
restart_flag = True

# Main program loop
while restart_flag:
    # Display the ASCII art logo
    print(logo)

    # Ask user for the operation mode
    flow_direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    # Validate user input until a correct option is provided
    while flow_direction not in ["encode", "decode"]:
        flow_direction = input("Type correctly 'encode' to encrypt or type 'decode' to decrypt:\n").lower()

    # Request the message and shift number from the user
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # Call the Caesar Cipher function with the provided inputs
    caesar_cipher(original_text=text, shift_amount=shift, direction=flow_direction)

    # Ask the user whether to restart or exit
    restart_indication = input("Type 'yes' if you would like to restart the program. Otherwise, type 'no':\n").lower()

    # Validate restart input until a correct option is provided
    while restart_indication not in ["yes", "no"]:
        restart_indication = input("Type correctly 'yes' if you would like to restart the program. Otherwise, type 'no':\n").lower()

    # Decide whether to loop again or exit
    if restart_indication == "yes":
        restart_flag = True
    else:
        restart_flag = False
        print("Goodbye! Hope you enjoyed using the Caesar Cipher!")
