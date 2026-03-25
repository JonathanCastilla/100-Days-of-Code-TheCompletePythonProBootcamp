# Project No. 28: The Flashcard Application 📨🎖️

**Author:** Jonathan Eduardo Castilla Zamora 🙋

## Abstract 📋
This repository contains the source code for a localized Graphical User Interface (GUI) application engineered to facilitate cognitive retention and bilingual language acquisition via the methodology of spatial repetition. Built upon the Python standard `tkinter` framework and leveraging the `pandas` library for tabular data manipulation, the system dynamically renders bilingual flashcards. It incorporates non-blocking asynchronous temporal callbacks to flip cards automatically and continuously mutates a localized dataset to track user progression by systematically filtering out acquired vocabulary.

## Architectural Features ✅
* **Data Ingestion and Mutation Pipeline:** Utilizes `pandas` to ingest a primary tabular dataset (`french_words.csv`). As the user interacts with the application, known entities are purged from the active memory matrix. The mutated array is subsequently serialized into a secondary, persistent state file (`words_to_learn.csv`) to ensure learning continuity across discrete execution sessions.
* **Temporal State Management:** Implements asynchronous, non-blocking temporal callbacks via the `tkinter.Tk.after()` method. The interface automatically transitions from the target language (French) to the native translation (English) after a deterministic 3000-millisecond interval, mitigating the need for manual user actuation to reveal the solution.
* **Dynamic Graphical Architecture:** Features a robust Canvas-based architecture capable of overlapping graphical assets (images) and typographic layers (text). The visual hierarchy is dynamically mutated in real-time to reflect the current operational state of the flashcard sequence.

## System Prerequisites ⚙️💻
This application operates within a standard Python execution environment but requires the manual installation of the `pandas` library for data serialization and deserialization.

* **Interpreter:** Python 3.6 or higher.
* **Standard Libraries:** `tkinter`, `random` (included within the standard Python distribution).
* **External Dependencies:** `pandas` (must be installed via a package manager).
* **System Assets:** * A `data/` directory containing the foundational `french_words.csv` dataset.
  * An `images/` directory containing the requisite visual assets: `card_front.png`, `card_back.png`, `right.png`, and `wrong.png`.

### Dependency Installation 🪛
To install the requisite data manipulation library, execute the following command in your terminal:
```bash
pip install pandas
```

## Execution Methodology 🧩
To initialize the application, navigate to the local directory containing the source code and the requisite asset directories, then execute the primary module.

1. Navigate to the project directory:
```bash
cd path/to/project-directory
```
2. Execute the script using the Python interpreter:
```bash
python main.py
```
## Operational Procedure 📋
1. **Initialization**: Upon launch, the data pipeline will attempt to load historical progress (`words_to_learn.csv`). If absent, it will fall back to the primary dataset (`french_words.csv`).

2. **Cognitive Evaluation**: The GUI will present a flashcard displaying a target vocabulary word in French. The user has 3 seconds to recall the translation.

3. **Temporal Inversion**: Following the 3000-millisecond interval, the application will asynchronously mutate the canvas, altering the graphical background and displaying the English translation.

4. **Data Actuation (Feedback)**:

    - **Acquired (Known)**: Actuate the green checkmark button (`right.png`). The current entity will be permanently purged from the active learning matrix, the updated matrix will be serialized to disk, and the next card will render.

    - **Unacquired (Unknown)**: Actuate the red cross button (`wrong.png`). The entity remains in the active learning matrix for future spatial repetition, and the next card will render.