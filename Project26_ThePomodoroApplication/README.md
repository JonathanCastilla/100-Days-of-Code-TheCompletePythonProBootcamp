# Project No. 26: The Pomodoro Application 🍅

**Author:** Jonathan Eduardo Castilla Zamora 🙋

## Abstract 📒
This repository contains a Graphical User Interface (GUI) application designed to facilitate the Pomodoro time-management methodology. Engineered utilizing the Python standard `tkinter` framework, the software implements a discrete state machine and non-blocking recursive callbacks to alternate systematically between focused cognitive execution (work intervals) and restorative pauses (break intervals). The application provides dynamic visual feedback through semantic color modulation and cumulative symbolic tracking (checkmarks) to optimize user productivity and temporal awareness.

## Architectural Overview 📋
The system relies on an asynchronous event loop rather than traditional procedural blocking (e.g., `time.sleep()`). By leveraging the `window.after()` method, the application successfully executes a recursive temporal countdown without interrupting the responsiveness of the graphical interface. 

The state machine governs four primary phases based on iterative modulo logic:
1. **Work Phase:** Standard focused interval.
2. **Short Break Phase:** Brief restorative pause following standard work intervals.
3. **Long Break Phase:** Extended restorative pause executed upon the completion of four standard cycles.
4. **Idle/Reset Phase:** The default, inactive state of the application.

## System Prerequisites 💻
This application operates within a standard Python execution environment. While it relies primarily on standard libraries, there is a strict dependency on an external image asset for visual rendering.

* **Interpreter:** Python 3.6 or higher.
* **Libraries:** `tkinter` (included within the standard Python distribution).
* **Assets:** A valid image file named `tomato.png` must be present in the root execution directory.

## Execution Methodology 🛠️
To initialize the application, navigate to the local directory containing the source code and the requisite image asset, then execute the primary module via a command-line interface.

1. Navigate to the project directory:
   ```bash
   cd path/to/project-directory
   ```

2. Execute the script using the Python interpreter:
    ```bash
    python main.py
    ```

## Operational Procedure ⚙️
1. **Initialization**: Upon launch, the graphical interface will render in its "Idle" state, displaying a digital chronometer set to `00:00`.
2. **Actuation**: Click the Start button to initiate the first Pomodoro cycle. The interface will visually shift to indicate an active "Work" phase.
3. **Cycle Progression**: The system will automatically transition between Work, Short Break, and Long Break phases upon the exhaustion of each temporal interval. A cumulative checkmark (`✅`) is appended to the interface following each completed work session.
4. **Interruption**: The cycle can be manually terminated at any juncture by actuating the Reset button, which purges the active non-blocking loop and restores all state variables to their default parameters.