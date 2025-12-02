# Turtle Crossing Game (Python Turtle Graphics)

## Overview
This project is an implementation of the classic **Frogger-style Turtle Crossing Game** using Python's `turtle` graphics module. The player controls a turtle attempting to cross a busy highway filled with moving cars. Each successful crossing increases the game difficulty by adding more cars and increasing their speed.

This repository contains modular, well‑structured Python files with clear object‑oriented design:
- **player.py** – Handles player movement and collision detection  
- **car_manager.py** – Spawns and manages cars  
- **scoreboard.py** – Tracks and displays score/level  
- **game_board.py** – Configures the screen  
- **main.py** – Controls the game loop  

---

## 🕹️ Gameplay Summary
- Press **Up Arrow** to move the turtle forward.
- Avoid all the cars moving horizontally across the screen.
- Each time you reach the finish line, the level increases:
  - More cars are added  
  - All cars move faster  
- Collision with a car ends the game.

---

## 📁 Project Structure
```
📦 turtle-crossing-game
│
├── main.py
├── player.py
├── car_manager.py
├── scoreboard.py
├── game_board.py
└── README.md
```

---

## 📜 File Descriptions

### **main.py**
The entry point of the program. Handles:
- Screen initialization  
- Player input setup  
- Car spawning  
- Game loop logic  
- Collision detection  
- Level progression  

### **player.py**
Defines the `Player` class:
- Turtle character starting at bottom of the screen  
- Moves upward with the Up key  
- Detects collisions with cars  
- Detects when finish line is reached  

### **car_manager.py**
Manages all aspects of car creation and movement:
- Random car colors  
- Random spawn positions  
- Movement speed scaling per level  

### **scoreboard.py**
Displays:
- Current level  
- “GAME OVER” message  

### **game_board.py**
Responsible for the window setup:
- Size  
- Background color  
- Title  

---

## ▶️ Running the Game
Make sure you have Python installed, then run:

```
python main.py
```

---

## 🧩 Requirements
No external dependencies. Uses only:
- Python standard library
- `turtle` module (included with Python)

---

## 📘 Author
**Jonathan Eduardo Castilla Zamora**  
Project no. 21 – Turtle Crossing Game  
Python Turtle Graphics

---

## 📄 License
This project is open‑source and free to use for educational purposes.
