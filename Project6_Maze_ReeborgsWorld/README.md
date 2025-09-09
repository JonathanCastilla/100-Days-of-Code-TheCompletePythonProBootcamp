# Reeborg's World - Maze Challenge

This project is part of my Python Bootcamp.  
The goal was to solve the **Maze challenge** in [Reeborg's World](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json).

---

## Challenge Description
Reeborg is a robot trapped inside a maze. The objective is to program its movements so that it can find the goal without getting stuck.

The constraints:
- Reeborg can only use the provided functions (`move()`, `turn_left()`, `front_is_clear()`, `right_is_clear()`, etc.).
- The algorithm must work for different maze configurations.

---

## My Solution
I implemented a **right-hand wall following algorithm**, where Reeborg always checks the right side first:
1. If there is no wall to the right → turn right and move.
2. If the front is clear but the right is blocked → keep moving forward.
3. Otherwise → turn left.

### Python Code
```python
def turn_right(steps):
    for step in range(steps):
        turn_left()

while not at_goal():
    while not right_is_clear():
        turn_left()
    if right_is_clear():
        turn_right(steps = 3)
        move()
        while front_is_clear() and not right_is_clear():
            move()
