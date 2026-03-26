# Project No. 29: Automated Email Birthday Wisher ✉️🎂

**Author:** Jonathan Eduardo Castilla Zamora 🙋

## Abstract 📋
This repository contains the source code for an automated, batch-processing script engineered to evaluate chronological data against the current temporal state and execute the transmission of personalized electronic mail. Utilizing the Python standard `smtplib` and `datetime` modules, alongside the `pandas` library for tabular data extraction, the system cross-references localized birthday records with the system clock. Upon verifying a chronological match, it stochastically selects a predefined text template, dynamically mutates it with the target's nomenclature, and securely dispatches the payload via the Simple Mail Transfer Protocol (SMTP). 

## Architectural Features 🏛️
* **Temporal Evaluation:** Leverages the `datetime` module to acquire the current discrete temporal state (month and day) and evaluates it against the localized database to trigger daily events accurately.
* **Stochastic Template Mutation:** Utilizes the `random` module to select one of several base letter templates, introducing variability to the messaging. The script dynamically replaces placeholder substrings (`[NAME]`) with the recipient's nomenclature prior to transmission.
* **Secure SMTP Transmission:** Implements Transport Layer Security (TLS) via `connection.starttls()` to encrypt the data stream between the local execution environment and the remote SMTP server (e.g., Google's smtp.gmail.com).
* **Cryptographic Credential Security:** Integrates the `os` module to retrieve authentication credentials from system-level environment variables, strictly preventing the hardcoding and accidental exposure of sensitive passwords within the source repository.

## System Prerequisites 💻
This application operates within a standard Python execution environment but requires external configuration for tabular data and environmental variables.

* **Interpreter:** Python 3.6 or higher.
* **Standard Libraries:** `os`, `smtplib`, `datetime`, `random` (included within the standard Python distribution).
* **External Dependencies:** `pandas` (must be installed via a package manager).
* **System Assets:** * A `birthdays.csv` file in the root directory containing the following column headers: `name`, `email`, `year`, `month`, `day`.
  * A `letter_templates/` directory containing text files named `letter_1.txt`, `letter_2.txt`, and `letter_3.txt`. Each file must contain the `[NAME]` placeholder.

### Dependency Installation ⚙️
To install the requisite data manipulation library, execute the following command in your terminal:
```bash
pip install pandas
```

## Security Configuration: Environment Variables 🛟
To execute this script securely, you must configure your local system's environment variables. Do not write your email or password directly into the main.py file. > ⚠️ SMTP Authentication Note: If utilizing a Gmail account, standard account passwords will be rejected due to modern security protocols. You must generate a 16-character App Password via your Google Account's 2-Step Verification settings and utilize that string for MY_PASSWORD.

- For **macOS/Linux (Bash/Zsh)**:

    - Execute the following in your terminal before running the script:
```bash
export MY_EMAIL="your_email@gmail.com"
export MY_PASSWORD="your_generated_app_password"
```
- For **Windows (Command Prompt)**:
```dos
set MY_EMAIL=your_email@gmail.com
set MY_PASSWORD=your_generated_app_password
```
