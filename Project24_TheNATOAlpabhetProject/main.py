"""
=============================================================
 File: main.py
 Project no. 24: The NATO Alphabet Project
 Author: Jonathan Eduardo Castilla Zamora

 Description:
    This project implements a Python-based application that converts a user-provided
    name into its corresponding NATO phonetic alphabet representation.

    The program reads structured data from a CSV file containing the NATO alphabet,
    where each letter is mapped to its standardized phonetic code (e.g., A → Alpha,
    B → Bravo). Using the Pandas library, this data is loaded into a DataFrame and
    transformed into a dictionary for efficient lookup operations.

    The application prompts the user to enter their name, ensures the input is
    converted to uppercase to maintain consistency with the dataset, and then
    translates each character into its phonetic equivalent. The result is returned
    as a dictionary that maps each letter of the name to its NATO phonetic code.

    Key Features:
    - CSV data handling using the Pandas library.
    - Dictionary comprehension for efficient data transformation.
    - User input validation through case normalization.
    - Modular function design for converting text to phonetic representations.
    - Clear separation between data loading, processing, and user interaction.

    This project demonstrates fundamental data processing techniques in Python,
    practical usage of external libraries, and clean, readable code design following
    best programming practices.

=============================================================
"""



import pandas as pd

# ================================
# Load NATO Phonetic Alphabet CSV
# ================================

# Open the CSV file that contains the NATO phonetic alphabet
with open('nato_phonetic_alphabet.csv', 'r') as alphabet_file:
    # Read the CSV file into a Pandas DataFrame
    alphabet_data_frame = pd.read_csv(alphabet_file)

    # Create a dictionary where:
    # - key   = letter (A, B, C, ...)
    # - value = corresponding NATO phonetic code (Alpha, Bravo, Charlie, ...)
    alphabet_dict = {
        row.letter: row.code
        for (index, row) in alphabet_data_frame.iterrows()
    }

    # Print the generated dictionary (for verification/debugging)
    print(alphabet_dict)


# ==========================================
# Function: Convert Name to Phonetic Alphabet
# ==========================================

def list_phonetic_alphabet(name, alphabet_dictionary):
    """
    Converts each letter of the given name into its NATO phonetic equivalent.

    Parameters:
        name (str): The input name (already in uppercase)
        alphabet_dictionary (dict): Dictionary mapping letters to phonetic codes

    Returns:
        dict: A dictionary mapping each letter in the name to its phonetic code
    """

    # Convert the name into a list of individual letters
    list_of_letters_name = [letter for letter in name]

    # Create and return a dictionary:
    # key   = letter from the name
    # value = NATO phonetic code for that letter
    return {
        letter: alphabet_dictionary[letter]
        for letter in list_of_letters_name
    }


# =========================
# User Input and Processing
# =========================

# Ask the user to enter their name and convert it to uppercase
# Uppercase is required to match the dictionary keys
user_input = str(input('Enter your name: ')).upper()

# Convert the user's name into the NATO phonetic alphabet
name_user_phonetic_alphabet = list_phonetic_alphabet(user_input, alphabet_dict)

# Print the resulting phonetic alphabet mapping
print(name_user_phonetic_alphabet)
