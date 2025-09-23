# 🎴 Blackjack Capstone Project  

## 📌 Project Information  
- **Project Number:** 11  
- **Project Name:** The Blackjack Capstone Project  
- **Author:** Jonathan Eduardo Castilla Zamora  

## 📖 Description  
This project implements a **simplified text-based version of the Blackjack card game**.  
The player competes against the computer (acting as the dealer) by drawing cards, aiming to reach a score as close to **21** as possible **without exceeding it**.  

The program includes:  
- Interactive prompts for the player.  
- Input validation to ensure correct user responses.  
- A simplified dealer strategy (dealer draws until reaching at least 16).  
- Display of results for **win, lose, draw, or bust**.  

---

## ⚙️ Features  
- 🃏 Random card drawing system.  
- 🤖 Computer follows a simplified Blackjack dealer strategy.  
- 👤 User can decide whether to draw another card or pass.  
- 🏆 Automatic evaluation of results.  
- 🎨 Includes an ASCII art logo for a better user experience.  

---

## 🛠️ Technologies Used  
- **Python 3**  
- **Random module** (for card drawing)  
- **ASCII Art (art.py)** for the project logo

---

## 🎮 Rules of the Game

- Both the **player** and the computer start with two cards.
- The **player** can choose to:
    - "y" → Draw another card.
    - "n" → Pass and keep their current hand.

- The computer (dealer) automatically draws cards until their score is 16 or more.

### **Winning Conditions**:
- Closest to 21 without going over.
- If the dealer exceeds 21, the player wins.

### Losing Conditions:
- Player exceeds 21.
- Dealer has a higher score ≤ 21.

### Draw Condition:
- Player and dealer finish with the same score.

---

## 📂 Project Structure

```
blackjack-capstone/
│── blackjack.py    # Main source code
│── art.py          # ASCII art logo
│── README.md       # Documentation file
```

## 🚀 Example Run

```
Welcome to Blackjack! 🎴
Your cards: [10, 7], current score: 17
Computer first card: 8
Type 'y' to get another card, 'n' to pass: y
Your cards: [10, 7, 3], current score: 20
Computer first card: 8
Type 'y' to get another card, 'n' to pass: n
Your final hand: [10, 7, 3], final score: 20
Computer final hand: [8, 9, 5], final score: 22
You win! 🎉
```
