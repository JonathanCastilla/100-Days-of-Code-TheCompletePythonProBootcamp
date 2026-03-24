# Project No. 27: The Password Manager Application

**Author:** Jonathan Eduardo Castilla Zamora 🙋

## Abstract
This repository contains the source code for a localized Graphical User Interface (GUI) application designed to function as a personal credential vault. Engineered utilizing the Python standard `tkinter` framework, the system facilitates the stochastic generation of robust cryptographic keys (passwords), integrates with the host Operating System's clipboard for seamless deployment, and executes persistent data storage via structured JSON serialization. The application enforces strict input validation, employs modal dialogues to ensure structural data integrity prior to local commitment, and features a localized query mechanism for the rapid retrieval of existing cryptographic records.

## Architectural Features 🛠️
* **Stochastic Key Generation:** Utilizes Python's `random` module to synthesize high-entropy alphanumeric and symbolic password strings, mitigating the vulnerability of predictable human-generated credentials.
* **Clipboard Integration:** Integrates the third-party `pyperclip` library to programmatically inject generated passwords directly into the OS clipboard, optimizing user workflow.
* **Structured Data Persistence (JSON):** Transitions from rudimentary flat-file storage to a structured, hierarchical JSON format. File I/O operations are safeguarded utilizing `try-except-else-finally` blocks to elegantly handle `FileNotFoundError` exceptions and prevent data corruption during the serialization of new payloads.
* **Data Retrieval Mechanism:** Features a localized query algorithm that utilizes the `Website` string as a primary key to scan the deserialized JSON database, returning the associated credentials via a modal interface if an entity match is verified.
* **Input Validation & Modals:** Prevents the transcription of null or incomplete data matrices. It leverages `tkinter.messagebox` to mandate explicit user consent prior to executing irreversible file writing operations.

## System Prerequisites ⚙️💻
This application operates within a standard Python execution environment but requires the manual installation of a third-party clipboard management library.

* **Interpreter:** Python 3.6 or higher.
* **Standard Libraries:** `tkinter`, `random`, `json` (included within the standard Python distribution).
* **External Dependencies:** `pyperclip` (must be installed via a package manager).
* **Visual Assets:** A valid image file named `logo.png` must be present in the root execution directory for proper canvas rendering.

### Dependency Installation ✅
To install the requisite external clipboard library, execute the following command in your terminal:
```bash
pip install pyperclip
```

## Execution Methodology 🧩

To initialize the application, navigate to the local directory containing the source code and the requisite image asset, then execute the primary module.

1. Navigate to the project directory:
```bash
cd path/to/project-directory
```
2. Execute the script using the Python interpreter:
```bash
python main.py
```

## Operational Procedure 📋

1. **Data Acquisition**: Upon initialization, the primary graphical matrix will render. Input the target Website and your `Email/Username`. The system automatically populates a default temporal email address to expedite execution.

2. **Key Generation (Optional)**: Actuate the **Generate Password** button to synthesize a secure, randomized password. This sequence will automatically populate the `Password` entry field and copy the string to your system's clipboard.

3. **Commitment (Save)**: Actuate the Add button. The system will validate the structural completeness of the inputs. Upon explicit modal confirmation, the dictionary payload will be serialized and merged into `data.json`. The interface fields will subsequently purge to secure the GUI.

4. **Retrieval (Search)**: To query an existing record, input the target domain into the Website field and actuate the **Search** button. The system will deserialize the database and return the corresponding credentials, or generate an error dialogue if the primary key is absent.

## ⚠️ Security and Developer Note 

In its current architectural state, this application stores credentials in an unencrypted plain-text JSON format (`data.json`). This paradigm is engineered strictly for the educational demonstration of GUI state management, dictionary manipulation, and standard file I/O operations. It is strictly advised against deploying this iteration for the storage of sensitive, real-world credentials without implementing industry-standard `cryptographic` hashing or symmetric encryption algorithms (e.g., AES utilizing the cryptography library).