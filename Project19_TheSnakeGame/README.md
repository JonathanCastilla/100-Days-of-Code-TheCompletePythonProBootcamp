# 🐍 Snake Game (OOP Version)

## 🎮 Project Overview
This project implements the **classic Snake Game** using **Object-Oriented Programming (OOP)** principles in Python.  
It uses the **Turtle Graphics** library to provide a simple but interactive graphical interface.

The game demonstrates modular software design, encapsulation, and event-driven logic while allowing real-time user input for snake control.

---

## 🧩 Project Structure

```
snake_game/
│
├── main.py               # Entry point of the game
├── snake.py              # Snake class (movement, growth, collision)
├── food.py               # Food class (random spawning)
├── scoreboard.py         # Scoreboard class (display and update score)
└── game_board.py         # GameBoard class (screen setup and configuration)
```

---

## ⚙️ Dependencies

This game only requires **Python 3.x** and the **Turtle module**, which comes preinstalled with Python.


## 🧠 Class Overview

### `GameBoard` (`game_board.py`)
Sets up the game window using Turtle’s `Screen()` class.

**Main Responsibilities:**
- Defines window **width**, **height**, and **background color**.
- Displays the game **title**.
- Manages the **is_game_over** flag for game control.

```python
WIDTH = 600
HEIGHT = 600
```

---

### `Snake` (`snake.py`)
Defines the snake's body, movement logic, and collision control.

**Main Methods:**
- `generate()`: Creates the initial 3 snake segments.
- `move_segments()`: Moves each segment to the position of the previous one.
- `extend()`: Adds a new segment to the tail when the snake eats food.
- Directional methods: `up()`, `down()`, `left()`, `right()`.

**Key Constants:**
```python
STARTING_POSITIONS = [(0,0), (-20, 0), (-40, 0)]
MOVEMENT_STEP = 20
DISTANCE_TO_FOOD = 25
```

---

### `Food` (`food.py`)
Handles the food creation and random repositioning when eaten.

**Key Features:**
- Appears as a small white circle (`shape("circle")`).
- Moves instantly to a new random location using `refresh()`.

**Key Constants:**
```python
OFFSET_SCREEN = 20
```

**Random Positioning Example:**
```python
random_x = random.randint(-WIDTH // 2 + OFFSET_SCREEN, WIDTH // 2 - OFFSET_SCREEN)
random_y = random.randint(-HEIGHT // 2 + OFFSET_SCREEN, HEIGHT // 2 - OFFSET_SCREEN)
self.goto(x=random_x, y=random_y)
```

---

### `Scoreboard` (`scoreboard.py`)
Displays and updates the score dynamically during gameplay.

**Key Methods:**
- `update_score()`: Refreshes the score display.
- `increase_score()`: Increments score after eating food.
- `game_over()`: Displays a “GAME OVER” message in the center.

**Font and Layout Configuration:**
```python
ALIGNMENT = "center"
FONT = ("Courier", 14, "bold")
FONT_FOR_GAME_OVER = ("Courier", 18, "bold")
```

---

## 🕹️ Example of User Interaction

| **Key Pressed** | **Effect on Screen**                                |
| ---------------- | --------------------------------------------------- |
| `W`              | Moves the snake upward.                             |
| `S`              | Moves the snake downward.                           |
| `A`              | Turns the snake left.                               |
| `D`              | Turns the snake right.                              |
| `C`              | (Optional) Can be used to clear or reset the board. |

---

## 🚀 How to Run the Game

1. Open the project in your favorite code editor (like VSCode).

2. Run the main game file:
   ```bash
   python main.py
   ```

3. The game window will open.  
   Use **W**, **A**, **S**, **D** keys to control the snake.

---

## 🧮 Game Logic Summary

1. **Initialization:**  
   The `GameBoard` creates the window and initializes the `Snake`, `Food`, and `Scoreboard`.

2. **Gameplay Loop:**  
   - The snake moves continuously.
   - When the snake’s head collides with the food, the `extend()` method adds a new segment and the score increases.
   - If the snake collides with itself or the border, `game_over()` is triggered.

3. **Termination:**  
   The game stops, displaying “GAME OVER” in the center.

---

## 📚 Learning Outcomes

This project reinforces:
- Object-Oriented Programming (OOP)
- Event-driven programming using `turtle.listen()` and `onkey()`
- Collision detection with coordinates
- Real-time screen updates and frame control
- Code modularization and documentation

---

## 🧠 Future Improvements

Possible enhancements:
- Add **difficulty levels** (increasing speed).
- Include **sound effects** using the `winsound` module.
- Display a **high-score system** using file storage.
- Add a **pause** or **restart** feature.

---

## 🧑‍💻 Author

**Developed by:** Jonathan Eduardo Castilla Zamora  
**Language:** Python 3.x  
**IDE Recommended:** VSCode / PyCharm  
**License:** MIT License  

---