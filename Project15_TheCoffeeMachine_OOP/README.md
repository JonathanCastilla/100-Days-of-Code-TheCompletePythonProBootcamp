# ☕ The Coffee Machine Program (OOP Version)

### 🧾 Project Information
**Project Number:** 15  
**Author:** Jonathan Eduardo Castilla Zamora  
**Programming Language:** Python 3  
**Paradigm:** Object-Oriented Programming (OOP)  

---

## 📖 Description

This project implements a **text-based coffee machine simulation** developed using **Object-Oriented Programming (OOP)** principles in Python.  
The system allows the user to order one of three available drinks — *espresso*, *latte*, or *cappuccino* — while managing internal resources such as **water, milk, and coffee**.

The program follows a modular design divided into four main classes:

- **`Menu`** — Handles available drink items and retrieves drink details.
- **`CoffeeMaker`** — Manages machine resources and validates ingredient availability.
- **`MoneyMachine`** — Simulates payment processing and coin transactions.
- **`art`** — Provides ASCII graphics for improved visual presentation in the terminal.

This project aims to demonstrate **OOP concepts** such as **encapsulation**, **class interaction**, and **state management**, while maintaining a clean and structured approach to program design.

---

## ⚙️ Features

- Selection between multiple coffee types.
- Resource availability check before drink preparation.
- Realistic coin-based payment system.
- Automatic calculation of total payment and change.
- Resource and financial reports on demand.
- Continuous operation until manual exit.
- Clean object-oriented structure.

---

## 🧩 Project Structure

```bash
coffee_machine_project/
│
├── main.py               # Main control program
├── menu.py               # Menu class (defines available drinks)
├── coffee_maker.py       # CoffeeMaker class (handles resources)
├── money_machine.py      # MoneyMachine class (handles payments)
├── art.py                # ASCII art for visual interface
└── README.md             # Project documentation
```

## 🧠 Example of Execution
``` python
What would you like? Type correctly (espresso/latte/cappuccino): latte
It will be: $2.50
Please insert coins.
How many quarters?: 10
Here is your latte ☕. Enjoy!

What would you like? Type correctly (espresso/latte/cappuccino): report
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.50
```

## 🧱 Object-Oriented Design Summary

| **Class** | **Responsibility** | **Key Methods** |
|------------|--------------------|-----------------|
| `Menu` | Defines and manages available drink items in the coffee machine. It allows retrieving menu options and locating drinks by name. | `get_items()`, `find_drink(name)` |
| `CoffeeMaker` | Manages the internal resources of the coffee machine (water, milk, coffee). It verifies if there are sufficient ingredients and performs coffee preparation. | `is_resource_sufficient(drink)`, `make_coffee(drink)`, `report()` |
| `MoneyMachine` | Handles the complete coin-based transaction system. It calculates inserted money, checks payment sufficiency, provides change, and maintains financial records. | `make_payment(cost)`, `report()` |
| `art` | Contains the ASCII visual elements such as the project logo and title, enhancing readability and user interaction in the console. | `logo`, `title` |

This table summarizes the modular organization of the system, showing how each class encapsulates a specific functionality and interacts with others to simulate a realistic coffee machine. This design promotes **encapsulation**, **abstraction**, and **code reusability** following OOP principles.


## 🧪 Academic Explanation

- This program exemplifies **Object-Oriented Programming** through:
- **Encapsulation**: Each class handles a specific subsystem (menu, payment, preparation).
- **Abstraction**: Users interact through simple commands without needing internal details.
- **Modularity**: Independent and reusable modules improve readability and testing.
- **Interaction of Objects**: Classes collaborate dynamically to perform actions (e.g., payment validation before coffee preparation).

## 🧾 License

This project is released under the MIT License, allowing open usage, modification, and distribution with proper attribution.