# The U.S. States Game 🗺️🐢

An interactive educational game built with **Python Turtle Graphics** and **Pandas**, where the player must correctly guess all 50 U.S. states by name. Each correct answer is displayed directly on the map at its geographical location.

This project combines **graphical user interaction**, **data-driven programming**, and **object-oriented design**, making it an excellent example of applied Python fundamentals.

## 👨‍💻 Author

- **Jonathan Eduardo Castilla Zamora**
- Bionics Engineering | Python Developer | Embedded Systems & AI Enthusiast

## 🎯 Project Objective

The goal of the game is to:
- Guess as many U.S. states as possible.
- Visually reinforce geographical learning by placing state names on a real map.
- Generate a personalized learning file containing the states the user failed to guess.

The game ends when:
- The player correctly guesses all **50 states**, or
- The player types **`exit`**, triggering the generation of a study file.

---

## 🧠 How the Game Works

1. A blank map of the United States is displayed.
2. The user is prompted to enter the name of a U.S. state.
3. If the answer is correct:
   - The state name is written at its correct coordinates.
   - The score counter updates (e.g., `15/50 States Correct`).
4. If the user types **`exit`**:
   - The game ends.
   - A CSV file named `states_to_learn.csv` is generated with all missing states.
5. If all 50 states are guessed correctly:
   - The game ends automatically 🎉.

---

## 🗂️ Project Structure
```bash
U.S_States_Game/
│
├── main.py # Main game loop and control logic
├── map.py # Map class (game logic, validation, rendering)
├── 50_states.csv # Dataset with state names and coordinates
├── blank_states_img.gif # Background image of the U.S. map
├── states_to_learn.csv # Generated after exiting (if applicable)
└── README.md # Project documentation
```
---

## 🧩 Object-Oriented Design

### 📌 `Map` Class Responsibilities
- Manages the Turtle screen and background map.
- Prompts user input using GUI dialogs.
- Validates answers using CSV data.
- Displays correct state names on the map.
- Tracks correct guesses and missing states.
- Generates a learning CSV file when exiting.

### 📌 `main.py`
- Loads state data using Pandas.
- Controls the game loop.
- Communicates user input to the `Map` class.
- Ends the game based on win or exit conditions.

This modular structure improves:
- ✔ Readability  
- ✔ Maintainability  
- ✔ Scalability  

---

## 🛠️ Technologies Used

- 🐍 **Python 3**
- 🐢 **Turtle Graphics**
- 📊 **Pandas**
- 📁 **CSV Data Handling**
- 🧠 **Object-Oriented Programming (OOP)**

---

## ⌨️ User Interaction Example
```python
Guess the state:
- Texas ✅

States Correct:
- 15/50 States Correct

- California ✅

States Correct:
- 16/50 States Correct
```
After exiting, a file named `states_to_learn.csv` is created automatically 📄.

---

## 📄 Generated Learning File

If the user exits early, the program creates: 
- **states_to_learn.csv**

This file contains:
- All states that were **not guessed**
- A personalized study guide for future practice 📚

---

## 🎓 Educational Value

This project reinforces:
- Data manipulation with Pandas 📊
- Event-driven programming 🧠
- GUI interaction with Turtle 🐢
- Clean object-oriented design 📐
- File generation and I/O 📁

## 👨‍💻 Author

- Jonathan Eduardo Castilla Zamora
- Bionics Engineering | Python Developer | Embedded Systems & AI Enthusiast