# 🕹️ Pong: The Arcade Game

A modern Python implementation of the classic **Pong** arcade game using the **Turtle Graphics** library.  
This project demonstrates **object-oriented programming**, **event-driven control**, and **animation** in Python.

👨‍💻 Author: **Jonathan Eduardo Castilla Zamora**

---

## 🎯 Game Overview

The game replicates the classic Pong experience where two paddles bounce a ball across the screen.  
Each player controls a paddle — the first to reach 5 points wins.

**Key Features:**
- Continuous paddle movement (toggle direction with a single key press)
- Collision detection between the ball, walls, and paddles
- Score tracking and automatic win message display
- Modular class-based structure for clarity and scalability

---

## 🧩 Project Structure

```
Pong-Arcade-Game/
│
├── main.py                # Main game loop and event bindings
├── game_board.py          # Screen setup and configuration
├── paddle.py              # Paddle class for player movement
├── ball.py                # Ball class for motion and collision logic
├── scoreboard.py          # Scoreboard management and win condition
└── README.md              # Project documentation
```


## 🎮 Controls

| Player | Move Up | Move Down |
|:-------|:--------|:----------|
| Left Paddle | `w` | `s` |
| Right Paddle | `Up Arrow` | `Down Arrow` |

- Press once to start continuous motion.
- Press the opposite key to reverse direction.

---

## 🧠 Code Architecture

### `game_board.py`
Handles the window setup using the **Turtle** module. Sets the background, size, and title.

### `paddle.py`
Defines paddle behavior with continuous movement logic through the `ontimer()` callback mechanism.

### `ball.py`
Controls ball movement, speed increase, and bounce logic when colliding with paddles or walls.

### `scoreboard.py`
Displays player scores, checks for a winner (first to 5 points), and shows the victory message.

### `main.py`
Coordinates all components — initializes the board, paddles, and ball, then runs the main game loop.

---

## 🏁 Win Condition

The game ends automatically when one player reaches **5 points**.  
A winning message is displayed in the center of the screen.

---

## 🧰 Technologies Used

- **Python 3.8+**
- **Turtle Graphics** for rendering
- **OOP principles** (encapsulation, modularity, reusability)

---

## 📜 License

This project is released under the **MIT License** — feel free to modify and distribute.

---

## 👨‍💻 Author

Developed with ❤️ by **Jonathan Eduardo Castilla Zamora**  
📘 Example educational project showcasing **OOP** and **event-driven programming** in Python.