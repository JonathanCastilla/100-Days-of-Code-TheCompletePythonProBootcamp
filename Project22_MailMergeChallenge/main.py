"""
=============================================================
 File: main.py
 Project no. 22: Mail Merge Challenge
 Author: Jonathan Eduardo Castilla Zamora

 Description:
     This program automates the creation of personalized letters
     using a simple mail-merge algorithm. The script reads a list
     of names, loads a template letter containing a placeholder
     "[name]", and generates a customized output file for each
     person on the list.
=============================================================
"""

# ===== Read the list of invited names =====
# Opens the file containing all names, reads all lines,
# and stores them as a list (each item is one name).
with open("Input/Names/invited_names.txt") as list_of_names:
    names = list_of_names.read().splitlines()  # splitlines() removes newline characters
    print(names)  # Debug print: shows all names loaded

# ===== Read the template letter and generate personalized letters =====
# Opens the letter template, reads it line by line.
with open("Input/Letters/starting_letter.txt") as letter_text:
    letter = letter_text.readlines()  # Entire template stored as a list of lines

    # Iterate through every name in the list to create one letter per person
    for name in names:

        # Replace the placeholder "[name]" in the first line with the actual name
        fixed_name = letter[0].replace("[name]", name)

        # Build the full letter:
        # Concatenate the modified first line + the rest of the template
        fixed_letter = fixed_name + "".join(letter[1:])

        # print(fixed_letter)  # Debug print: shows the generated letter

        # ===== Save the final personalized letter =====
        # Create an output file in the "ReadyToSend" folder.
        # The file is named using the format "letter_for_<name>.txt"
        with open("Output/ReadyToSend/" + "letter_for_" + name + ".txt", "w") as letter_file:
            letter_file.write(fixed_letter)  # Write the completed letter
