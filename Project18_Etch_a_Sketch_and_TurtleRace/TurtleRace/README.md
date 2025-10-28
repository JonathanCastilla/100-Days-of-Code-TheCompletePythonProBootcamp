# 🐢 The TurtleRace Program

## 📘 Project Overview
**Project Number:** 18  
**Project Name:** The TurtleRace Program  

The **TurtleRace Program** is a fun and interactive Python-based graphical application that simulates a race between multiple turtles using the **Turtle Graphics** library.  
The user places a **bet** on a turtle by color and watches the race unfold in real time. The program demonstrates the integration of object-oriented programming, randomization, and event-driven user interaction using Python’s built-in modules.

This project highlights **modular OOP design**, **user interaction**, and **basic computer graphics**, making it ideal for learning the fundamentals of interactive programming with graphical visualization.

---

## 🎯 Key Features
- 🐢 **Object-Oriented Design:** Encapsulates race logic and attributes in the `TurtleRace` class.  
- 🎨 **Colorful Turtles:** Each turtle is randomly assigned a color from a predefined palette.  
- 🏁 **User Betting:** The user places a bet on which turtle will win before the race starts.  
- 🔀 **Randomized Movement:** Each turtle moves forward by random steps, ensuring unpredictable outcomes.  
- 📏 **Automatic Setup:** Dynamic positioning of turtles according to the screen size.  
- 💬 **User Feedback:** Displays the race results and whether the user won or lost.  

---

## 🧠 OOP Design Summary

| **Class/Method** | **Responsibility** | **Description** |
|------------------|--------------------|-----------------|
| `TurtleRace` | Class | Encapsulates the entire race logic, screen setup, and user interaction. |
| `__init__()` | Constructor | Initializes the screen, turtle list, and race configuration parameters. |
| `greeting()` | UI Method | Prints a welcome message and available turtle color options. |
| `generate_turtles(number_of_turtles)` | Object Creation | Creates the specified number of turtle racers, each with a unique color. |
| `print_colors_names_of_turtles()` | Display Method | Displays all available turtle colors for user reference. |
| `move_turtles_to_starting_point()` | Positioning Method | Places each turtle at its starting Y-position along the left side of the screen. |
| `start_race()` | Simulation Method | Executes the race loop, moving each turtle forward by random steps until one wins. |
| `print_winner()` | Output Method | Prints the winning turtle’s color once the race ends. |
| `obtain_user_bet()` | Input Method | Prompts the user to bet on a turtle color through the graphical interface. |
| `check_user_bet()` | Validation Method | Compares the user’s bet with the winning turtle and displays the result. |

---

## ⚙️ Parameter Configuration

| **Parameter** | **Type** | **Default Value** | **Description** |
|---------------|----------|-------------------|-----------------|
| `screen_height` | `int` | `600` | Height of the Turtle Graphics window. |
| `screen_width` | `int` | `800` | Width of the Turtle Graphics window. |
| `offset_y` | `int` | `100` | Vertical margin for turtle placement. |
| `x_steps_for_turtle_in_race` | `range` | `range(0, 50, 10)` | Range of random movement steps for turtles during the race. |
| `turtle_colors` | `list[str]` | 10 preset colors | Predefined color palette used for assigning unique turtle colors. |
| `number_of_turtles` | `int` | `5` | Number of turtles participating in the race. |

---

## 💻 Code Execution Flow

1. **Initialize the Race**
   - The `TurtleRace` object is created.
   - The screen and race settings are configured automatically.

2. **Generate Turtles**
   - A group of turtles is created, each assigned a random color.

3. **User Interaction**
   - The user is prompted to **bet on a turtle color**.

4. **Start the Race**
   - Turtles move forward in random increments until one crosses the finish line.

5. **Display Results**
   - The program announces the winning turtle.
   - It verifies if the user's bet was correct.

6. **Exit Gracefully**
   - The window closes automatically when the user clicks on it.

---

## 🧩 Example of Program Flow

```text
Welcome to the Turtle Race!
Select one of the following turtles typing its color name:

Generating 'The LightBlue turtle'...
Generating 'The Salmon turtle'...
Generating 'The DarkSeaGreen turtle'...
Generating 'The LightPink turtle'...
Generating 'The MediumPurple turtle'...

Type any option: ['LightBlue', 'Salmon', 'DarkSeaGreen', 'LightPink', 'MediumPurple']

> User bets on 'LightPink'
...
The winner was: 'The Salmon turtle'.
You lost!
```

## 🧰 Dependencies

| **Library** | **Description** |
|--------------|-----------------|
| `turtle` | Provides the graphical interface and controls the movement of the turtle objects for rendering the race. |
| `random` | Generates random movement steps for each turtle, introducing variability and unpredictability in the race outcome. |
| `numpy` | Used to compute evenly spaced vertical positions (`linspace`) for the initial placement of turtles on the race track. |
| `logo` | Custom module that contains an ASCII art title displayed at the beginning of the program for aesthetic presentation. |


## 📁 File Structure
```bash
TurtleRace/
│
├── main.py             # Main program file (contains the race logic)
├── logo.py             # ASCII logo file displayed at the start
└── README.md           # Project documentation
```

## 👨‍💻 Author

**Jonathan Eduardo Castilla Zamora**

- This project demonstrates structured programming, randomness, and interactive graphics with Python Turtle.