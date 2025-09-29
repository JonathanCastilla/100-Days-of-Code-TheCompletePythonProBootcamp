# ☕ Coffee Machine Program

## 📌 Project Information
**Project Number:** 14  
**Project Name:** The Coffee Machine Program  
**Author:** Jonathan Eduardo Castilla Zamora  

## 📝 Description
This program simulates a text-based coffee machine. Users can order one of three drinks:
- **Espresso**
- **Latte**
- **Cappuccino**

The system verifies whether sufficient resources (water, milk, and coffee) are available to prepare the drink. If resources are adequate, the user is asked to insert coins, and the payment is calculated using precise decimal arithmetic.

If the transaction is successful:
- The drink is "served"
- Resources are deducted
- Change is returned if necessary

The user may also type **`report`** to display the current stock of resources, including accumulated money.  
The program continues running until it is manually terminated.

---

## 📂 Project Structure
```bash
project_root/
│
├── coffee_machine_data.py # Contains MENU and initial resources
├── art.py # Contains title and logo ASCII art
├── main.py # Main program logic

```
---

## ▶️ How to Run the Program

1. Ensure the following files exist in the same directory:
   - `main.py`
   - `coffee_machine_data.py`
   - `art.py`

2. Run the program using:
    - `python main.py`
3. Follow the interactive prompts in the terminal.

---

## ✅ Features

- Order drinks: `espresso`, `latte`, or `cappuccino`
- Coin-based payment using:
- Quarters ($0.25)
- Dimes ($0.10)
- Nickles ($0.05)
- Pennies ($0.01)
- Automatic change calculation
- Resource availability checks
- Report current machine resources with the `report` command
- Persistent resource tracking and revenue collection

---

## 🧮 Example Interaction
```python

What would you like? Type (espresso/latte/cappuccino): latte
It will cost: $2.5
Please, insert coins.
How many quarters? 8
How many dimes? 0
How many nickles? 0
How many pennies? 0
Your payment was $2.00
Sorry, that is not enough money. Money refunded.

```

---

## 📜 License
This project is provided for educational purposes and is not licensed for commercial use unless stated otherwise.

---