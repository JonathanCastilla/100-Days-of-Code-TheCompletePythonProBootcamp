"""
=============================================================
 File: main.py
 Project no. 29: Automated Email Birthday Wisher
 Author: Jonathan Eduardo Castilla Zamora

 Description:
    This module implements an automated, batch-processing script
    designed to verify chronological events (birthdays) against
    the current temporal state and execute the transmission of
    personalized electronic mail via the Simple Mail Transfer
    Protocol (SMTP). It leverages the `pandas` library for tabular
    data extraction, the `datetime` module for temporal evaluation,
    and the `os` module for the secure retrieval of system-level
    environment variables to protect cryptographic credentials.
=============================================================
"""

import os
import smtplib
import datetime as dt
import pandas as pd
import random

# ----------------------- CRYPTOGRAPHIC CREDENTIALS ----------------------- #
# Data Security: Acquiring authentication credentials from host environment
# variables to prevent the hardcoding of sensitive cryptographic keys within
# the source repository.
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

# Configuration payload dictating the operational parameters for the SMTP protocol.
EMAIL = {
    "address": MY_EMAIL,
    "password": MY_PASSWORD,
    "subject": 'Happy Birthday!'
}

# ----------------------- TEMPORAL EVALUATION ----------------------------- #
# Acquire the current discrete temporal state (date) from the local system clock.
current_date = dt.date.today()

# ----------------------- DATA INGESTION & ACTUATION ---------------------- #
# Utilize a context manager to securely ingest the localized tabular database.
with open('birthdays.csv', newline='') as csvfile:
    # Deserialize the CSV file into a pandas DataFrame, subsequently coercing
    # it into a standardized list of dictionary records for iterative processing.
    birthdays_data = pd.read_csv(csvfile)
    birthdays_data = birthdays_data.to_dict('records')

    # Iterate systematically through the localized data matrix.
    for birthday in birthdays_data:
        # Chronological Validation: Evaluate if the historical day and month
        # parameters match the current temporal state.
        if birthday['month'] == current_date.month and birthday['day'] == current_date.day:

            # ----------------------- TEMPLATE MUTATION ----------------------- #
            # Stochastically select a base text template (1 through 3) for the message payload.
            with open('letter_templates/letter_'+ str(random.randint(1,3)) + '.txt') as file:
                letter_template = file.read()
                # Dynamically mutate the placeholder substring with the target entity's nomenclature.
                letter_template = letter_template.replace('[NAME]', birthday['name'])

            # ----------------------- SMTP TRANSMISSION ----------------------- #
            # Instantiate an SMTP connection utilizing Google's designated server and port (587).
            with smtplib.SMTP('smtp.gmail.com', 587) as connection:
                # Initiate Transport Layer Security (TLS) to encrypt the data stream.
                connection.starttls()
                # Authenticate against the remote server utilizing the injected environment variables.
                connection.login(user=EMAIL['address'], password=EMAIL['password'])

                # Execute the transmission of the personalized electronic payload.
                connection.sendmail(
                    from_addr=EMAIL['address'],
                    to_addrs=birthday['email'],
                    msg=f'Subject: {EMAIL["subject"]}\n\n{letter_template}'
                )