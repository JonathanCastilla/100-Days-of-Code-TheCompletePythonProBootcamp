# 🕵️ Secret (Blind) Auction

## 📌 Project Information
- **Project No.:** 9  
- **Project Name:** Secret (Blind) Auction  
- **Author:** Jonathan Eduardo Castilla Zamora  

## 📝 Description
This project implements a **text-based blind auction system** where multiple bidders can submit their bids without seeing the others'. Each participant enters their **name** and **bid amount**, which are stored securely in a dictionary. After all bidders have finished, the program determines the **highest bid** and announces the winner.  

The auction mimics the traditional blind auction process by "clearing the console" between turns, ensuring secrecy of bids.  

---

## ⚙️ Features
- Accepts multiple bidders with names and bid amounts.  
- Validates inputs for restart options (`yes` / `no`).  
- Uses a dictionary to store bids securely.  
- Automatically determines the **highest bidder**.  
- Handles ties: if multiple bidders place the same maximum bid, the **first one entered** is declared winner.  
- Console-clearing simulation to preserve confidentiality of bids.  

---

## 📂 Project Structure
```
secret-auction/
│── main.py             # Main program logic
│── art.py              # ASCII art (logo)
│── README.md           # Project documentation
```

## 📖 Example Usage
```
Welcome to the Secret Auction program.
What is your name?: Alice
What is your bid?: $150
Are there any other bidders? Type 'yes' or 'no'. yes

What is your name?: Bob
What is your bid?: $200
Are there any other bidders? Type 'yes' or 'no'. no
```

✅ Output:
```
The winner is Bob with a bid of $200
```

---

## 🛠️ Technologies Used
- **Python 3.x**  
- Dictionary data structures  
- Basic control flow (`if`, `while` loops)  
- ASCII Art (from `art.py`)  

---

## 🌟 Learning Objectives
- Practice with Python **dictionaries** for key-value storage.  
- Strengthen understanding of **loops**, **input validation**, and **conditionals**.  
- Implement a simple but effective **decision-making algorithm** (finding maximum values).  
- Explore user interaction design in text-based programs.  

---
