# Project No. 25: The Mile to Kilometers Converter

**Author:** Jonathan Eduardo Castilla Zamora 🙋

## Abstract 📋
This repository contains a Graphical User Interface (GUI) application designed to execute deterministic unit conversions from miles to kilometers. Utilizing the Python standard `tkinter` library, the software establishes an event-driven interface that captures scalar input, applies the standard international conversion coefficient (1.60934), and dynamically updates the visual display with the computed metric equivalent.

## System Prerequisites 💻
This application operates within a standard Python execution environment. As it relies exclusively on standard libraries, no external dependencies or virtual environment configurations are strictly necessary.

* **Interpreter:** Python 3.6 or higher.
* **Libraries:** `tkinter` (included within the standard Python distribution).

## Execution Methodology 🧩
To initialize the application, navigate to the local directory containing the source code and execute the primary module via your terminal or command-line interface.

1. Navigate to the project directory:
   ```bash
   cd path/to/project-directory
   ```
2. Execute the script using the Python interpreter:
    ```bash
    python main.py
    ```
## Operational Procedure 🛠️
1. **Data Acquisition**: Upon initialization, the primary application window will render. Input the scalar distance (in miles) into the central text entry field.

2. **Execution**: Actuate the Calculate button to trigger the underlying conversion algorithm.

3. **Output Generation**: The corresponding distance in kilometers, quantized to three decimal places, will dynamically populate in the designated output matrix of the interface.