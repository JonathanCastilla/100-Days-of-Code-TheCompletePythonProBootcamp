# Project no. 22: Mail Merge Challenge
- Author: **Castilla Zamora Jonathan Eduardo**

## Overview

This project is an automation tool designed to simplify the process of mass letter customization using a **Mail Merge algorithm**. The script reads a list of names and a letter template to generate personalized text files for each recipient.

This repository contains the following files and directories:

- **main.py** – The primary script that handles reading, processing, and writing files.
- **Input/Names/invited_names.txt** – Contains the list of invitees.
- **Input/Letters/starting_letter.txt** – The template letter with placeholders.
- **Output/ReadyToSend/** – The destination folder for generated letters.

## ⚙️ Functionality Summary

- Reads a list of names from a text file.
- The specific placeholder [name] is replaced in the template letter.
- Generates a unique .txt file for every name in the list.
- Saves all files automatically to the output directory.

## 📁 Project Structure
```bash
📦 Mail-Merge-Challenge
│
├── main.py
├── Input
│   ├── Names
│   │   └── invited_names.txt
│   └── Letters
│       └── starting_letter.txt
└── Output
    └── ReadyToSend
        └── (Generated Letters)

```

## 📜 File Descriptions

### **main.py**
- The entry point of the program. Handles:
- Opening the input files.
- Iterating through the list of names.
- String replacement operations.
- Writing the final files to the hard drive.

### **Input/Names/invited_names.txt**

- A simple text file containing names, with each name on a new line.
- Input/Letters/starting_letter.txt
- The template file containing the message body and the [name] placeholder on the first line.

## ▶️ Running the Script

Make sure you have Python installed, then run:
``` bash
python main.py
```


## 🧩 Requirements

- No external dependencies. Uses only:
    - Python standard library (Built-in open, read, write functions).

## 📘 Author

**Jonathan Eduardo Castilla Zamora**
- Project no. 22 – Mail Merge Challenge
    - Python Automation

## 📄 License

This project is open-source and free to use for educational purposes.
