# 🔼 The Higher Lower Game

## 📌 Project Information
- **Project Number:** 13  
- **Project Name:** The Higher Lower Game  
- **Author:** Jonathan Eduardo Castilla Zamora  

## 📖 Description
This project is a **text-based comparison game** where the player is shown two randomly selected public figures. Each is described by name, profession, and country. The player must guess which of the two has the higher follower count.  

- A correct guess increases the player's score and continues the game.  
- An incorrect guess ends the round and displays the final score.  
- At the end of a session, the player can choose to start a new game.

---

## ⚙️ Features
- ✅ Random selection of comparison pairs  
- ✅ Input validation for user choices  
- ✅ Automatic scoring system  
- ✅ Replay option after each game  
- ✅ Clear and interactive console feedback  
- ✅ Uses ASCII art for better UX  

---

## 🛠️ Technologies Used
- **Python 3**
- **Random module**
- **Custom modules:**
  - `art.py` → contains the `logo` and `vs` ASCII graphics
  - `game_data.py` → contains a predefined list of public figure dictionaries

---

## ▶️ How to Run the Project

1. Ensure that the following files are in the same folder:
    - main.py (or your script filename)
    - art.py
    - game_data.py
2. Run the script:
    ``` bash
    python main.py
    ```

## 🎮 How the Game Works

- Two individuals are displayed as:
    - Compare A
    - Compare B
- Each entry includes:
    - Name
    - Description (profession/role)
    - Country of origin

- The player types:
    - "A" if they believe A has more followers
    - "B" if they believe B has more followers

- If correct:
    - Score increases
    -A new pair is shown
- If incorrect:
    - The game ends
    - The final score is displayed
    - The user can choose to play again by typing "y" or "n"

## 📂 Project Structure
``` bash
higher-lower-game/
│── main.py          # Main game logic
│── art.py           # ASCII art (logo and vs)
│── game_data.py     # Dataset of public figures
│── README.md        # Project documentation
```

## 🚀 Example Run

``` python
Compare A: Selena Gomez, a musician and actress, from United States.
vs
Compare B: Cristiano Ronaldo, a footballer, from Portugal.
Who has more followers? Type 'A' or 'B': A

Congratulations! You got it! Current score: 1
```

``` python
Compare A: Elon Musk, an entrepreneur, from South Africa.
vs
Compare B: Beyoncé, a musician, from United States.
Who has more followers? Type 'A' or 'B': B

Sorry, that's not the right answer. Final score: 1
Would you like to start a new game? Type 'y' or 'n':
```

## 📜 License
This project is released under the MIT License. You may use, modify, and distribute it with proper attribution.