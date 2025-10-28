"""
Project Number: 18
Project Name: The Etch-A-Sketch Program
Description:
    This program implements a digital version of the classic "Etch A Sketch" drawing toy
    using Python’s Turtle Graphics library. Through keyboard interaction, the user can
    control a virtual turtle to draw on the screen. Movements include forward, backward,
    left, and right rotations, while a clear/reset function allows the user to erase
    the drawing and return to the initial position.

    The implementation encapsulates the behavior of the drawing system within a class,
    following object-oriented design principles. The interaction between keyboard inputs
    and corresponding movement functions demonstrates event-driven programming.

    Key Features:
    - Object-oriented encapsulation of turtle configuration and movement logic.
    - Interactive drawing via keyboard controls:
        * 'w' → move forward
        * 's' → move backward
        * 'a' → rotate left
        * 'd' → rotate right
        * 'c' → clear screen and reset position
    - Adjustable parameters for step distance and rotation angle.
    - Clean and responsive graphical interface.

    This program serves as an educational demonstration of real-time input handling,
    event-driven design, and procedural drawing using the Turtle Graphics library.

Author: Jonathan Eduardo Castilla Zamora
"""

# Import the Turtle and Screen classes from the turtle graphics library
from turtle import Turtle, Screen


class EtchASketch:
    """
    The EtchASketch class defines the structure and behavior of the digital drawing system.
    It configures the turtle’s appearance, movement properties, and the key bindings
    that enable user control through keyboard interaction.
    """
    def __init__(self):
        # Define drawing and control parameters
        self.pencolor = "white"           # Color of the drawing line
        self.bgcolor = "black"            # Background color of the window
        self.pensize = 2                  # Thickness of the drawing line
        self.steps_by_type = 10           # Distance moved per key press
        self.angle_rotation_by_type = 15  # Degrees turned per rotation key press
        self.keys = ['w', 's', 'a', 'd', 'c']  # List of active control keys

        # Initialize Turtle and Screen instances
        self.turtle = Turtle()
        self.screen = Screen()

        # Apply graphical configuration
        self.turtle.pen(pencolor=self.pencolor, pensize=self.pensize)
        self.screen.bgcolor(self.bgcolor)

    # Movement and control methods
    def move_forwards(self):
        """Moves the turtle forward by a fixed number of steps."""
        self.turtle.forward(self.steps_by_type)

    def move_backwards(self):
        """Moves the turtle backward by a fixed number of steps."""
        self.turtle.backward(self.steps_by_type)

    def turn_right(self):
        """Rotates the turtle clockwise by a fixed angle."""
        self.turtle.right(self.angle_rotation_by_type)

    def turn_left(self):
        """Rotates the turtle counterclockwise by a fixed angle."""
        self.turtle.left(self.angle_rotation_by_type)

    def restart_app(self):
        """
        Clears the screen and resets the turtle to its home position.
        This function simulates shaking an Etch A Sketch to erase the drawing.
        """
        self.turtle.penup()
        self.turtle.home()
        self.turtle.clear()
        self.turtle.pendown()


def draw(app, movement, key_activator):
    """
    Binds a specific keyboard key to a movement function.

    Parameters:
        app (EtchASketch): Instance of the EtchASketch class.
        movement (function): The movement function to be executed when the key is pressed.
        key_activator (str): The keyboard key that triggers the movement.
    """
    app.screen.onkey(movement, key_activator)  # Assign the key to the corresponding function
    app.screen.listen()  # Listen for keypress events


# Instantiate the main application
etch_a_sketch_app = EtchASketch()

# Define key bindings for interactive movement
draw(app=etch_a_sketch_app, movement=etch_a_sketch_app.move_forwards, key_activator=etch_a_sketch_app.keys[0])  # 'w'
draw(app=etch_a_sketch_app, movement=etch_a_sketch_app.move_backwards, key_activator=etch_a_sketch_app.keys[1])  # 's'
draw(app=etch_a_sketch_app, movement=etch_a_sketch_app.turn_left, key_activator=etch_a_sketch_app.keys[2])       # 'a'
draw(app=etch_a_sketch_app, movement=etch_a_sketch_app.turn_right, key_activator=etch_a_sketch_app.keys[3])      # 'd'
draw(app=etch_a_sketch_app, movement=etch_a_sketch_app.restart_app, key_activator=etch_a_sketch_app.keys[4])     # 'c'

# Keep the window open until user clicks to exit
etch_a_sketch_app.screen.exitonclick()
