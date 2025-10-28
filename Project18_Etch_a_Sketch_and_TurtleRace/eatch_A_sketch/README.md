# 🖊️ The Etch-A-Sketch Program

### 📘 Project Number: 18  
### 👨‍💻 Author: Jonathan Eduardo Castilla Zamora  

---

## 🧩 Project Description

The **Etch-A-Sketch Program** is a digital recreation of the classic drawing toy, implemented using **Python’s Turtle Graphics** library.  
The user can draw interactively on the screen by controlling a virtual turtle through keyboard inputs.  

This program applies **Object-Oriented Programming (OOP)** and **event-driven design principles** to encapsulate movement, drawing behavior, and interaction logic within a structured class.  
The design promotes modularity, clarity, and expandability — making it suitable for educational purposes in programming and computer graphics courses.

---

## 🎯 Key Features

- **Interactive Drawing Controls** using keyboard input:
  - `W` → Move forward  
  - `S` → Move backward  
  - `A` → Turn left  
  - `D` → Turn right  
  - `C` → Clear and reset the screen  

- **Event-Driven Programming** with keyboard listeners bound to movement methods.  
- **Customizable Parameters** for pen color, background, step size, and rotation angle.  
- **Graphical Interface** powered by the `turtle` module.  
- **Encapsulation** of logic in an `EtchASketch` class for readability and reusability.  

---

## ⚙️ Object-Oriented Design Summary

| **Class / Function** | **Responsibility** | **Attributes / Parameters** | **Description** |
|----------------------|-------------------|-----------------------------|-----------------|
| `EtchASketch` | Defines the Etch-A-Sketch system and its behavior. | `pencolor`, `bgcolor`, `pensize`, `steps_by_type`, `angle_rotation_by_type`, `keys`, `turtle`, `screen` | Initializes drawing environment and manages configuration. |
| `move_forwards()` | Moves the turtle forward. | – | Moves by `steps_by_type` units. |
| `move_backwards()` | Moves the turtle backward. | – | Moves backward by `steps_by_type` units. |
| `turn_left()` | Rotates the turtle counterclockwise. | – | Turns by `angle_rotation_by_type` degrees. |
| `turn_right()` | Rotates the turtle clockwise. | – | Turns by `angle_rotation_by_type` degrees. |
| `restart_app()` | Clears the screen and resets position. | – | Emulates shaking the Etch A Sketch to erase drawing. |
| `draw(app, movement, key_activator)` | Binds keys to movement functions. | `app`, `movement`, `key_activator` | Implements keyboard-event linkage for movement control. |

---

## 🧠 Program Workflow

1. **Initialization**  
   The program creates an instance of the `EtchASketch` class and configures the drawing environment.  

2. **Key Binding**  
   The `draw()` function binds specific keys (`w`, `s`, `a`, `d`, `c`) to movement methods.  

3. **User Interaction**  
   The user controls the turtle’s movement using the assigned keys to create free-form sketches.  

4. **Reset Functionality**  
   Pressing `C` clears the drawing area and re-centers the turtle.  

5. **Termination**  
   The program waits for a mouse click to close the window (`exitonclick()`).

---

## ⚙️ Parameter Configuration

| **Parameter** | **Default Value** | **Description** |
|----------------|-------------------|-----------------|
| `pencolor` | `"white"` | Color of the drawing line. |
| `bgcolor` | `"black"` | Background color of the drawing canvas. |
| `pensize` | `2` | Thickness of the drawing line. |
| `steps_by_type` | `10` | Distance moved with each key press. |
| `angle_rotation_by_type` | `15` | Angle of rotation for left and right turns. |

---

## 📦 Dependencies

To run this project, ensure you have the following installed:

```bash
Python 3.x
No external libraries are required beyond the standard Python Turtle module.
```

## ▶️ Execution Example

### Expected Output

A graphical window opens with a black background and a white pen.
The user can move the turtle using:

- W → Move forward
- S → Move backward
- A → Turn left
- D → Turn right
- C → Clear and reset

The drawing persists until the user closes the window by clicking it.

## 🧩 Example of User Interaction

| **Key Pressed** | **Effect on Screen**                                |
|-----------------|----------------------------------------------------|
| `W`             | Moves turtle forward, drawing a line upward.       |
| `S`             | Moves turtle backward, drawing a line downward.    |
| `A`             | Turns turtle counterclockwise (left).              |
| `D`             | Turns turtle clockwise (right).                    |
| `C`             | Clears the entire drawing area and resets position.|


## 🧱 Software Design Principles Demonstrated

- `Encapsulation`: All drawing logic is enclosed within the EtchASketch class.
- `Event-Driven Programming`: The onkey() method binds user input to specific actions.
- `Abstraction`: The user interacts with simple controls without managing internal logic.
- `Reusability`: The architecture can easily be expanded (e.g., change pen colors dynamically).