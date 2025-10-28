"""
Project Number: 18
Project Name: The Turtle Race Program
Description:
    This program implements an interactive graphical racing simulation using Python's Turtle Graphics module.
    It allows the user to place a bet on a turtle based on its color and then visually observes the race as the turtles
    move randomly toward the finish line. The program employs structured, object-oriented design principles and
    integrates randomness to make each race unique.

    The system utilizes the Turtle module for graphics, NumPy for positioning turtles evenly along the Y-axis,
    and standard Python libraries for logic and randomization. It offers an engaging visual experience that
    demonstrates event-driven programming and encapsulated class-based design.

    Key Features:
    - Object-oriented design encapsulated in the `TurtleRace` class.
    - Dynamic turtle generation with distinct colors.
    - Evenly spaced starting positions using NumPy.
    - Randomized race progress for unpredictability.
    - Interactive user betting system and result display.
    - Graceful graphical termination via screen click.

    This implementation emphasizes modular programming, user interaction, and visual simulation principles.

Author: Jonathan Eduardo Castilla Zamora
"""

from turtle import Turtle, Screen
import random
import numpy as np
from logo import title


class TurtleRace:
    """Class that encapsulates the logic of the turtle race simulation."""

    def __init__(self):
        """Initializes screen parameters, turtle settings, and race configuration variables."""
        self.turtle = None
        self.list_of_turtles = []
        self.screen = Screen()
        self.screen_height = 600
        self.screen_width = 800
        self.screen.setup(width=self.screen_width, height=self.screen_height)

        self.offset_y = 100
        self.x_steps_for_turtle_in_race = range(0, 50, 10)
        self.continue_racing = True
        self.winner = None

        self.starting_positions = []
        self.number_of_turtles = 0

        # Screen appearance
        self.screen.bgcolor("white")
        self.screen.title("Turtle Race")

        # List of available turtle colors
        self.turtle_colors = [
            'LightBlue', 'CornflowerBlue', 'MediumPurple', 'Moccasin',
            'MediumAquamarine', 'NavajoWhite', 'Salmon', 'LightPink',
            'LightSteelBlue', 'DarkSeaGreen'
        ]

        self.user_bet = None
        self.list_of_turtles_colors_in_race = []

    def greeting(self):
        """Displays a textual greeting and basic instructions for the user."""
        print(title)
        print("Welcome to the Turtle Race!")
        print("Select one of the following turtles by typing its color name:\n")

    def generate_turtles(self, number_of_turtles):
        """
        Dynamically generates a user-specified number of turtles with random colors.
        Each turtle is assigned a unique color and appended to the race list.
        """
        self.number_of_turtles = number_of_turtles
        for _ in range(number_of_turtles):
            self.turtle = Turtle()
            self.turtle.shape("turtle")
            self.turtle.color(random.choice(self.turtle_colors))
            self.turtle_colors.remove(self.turtle.color()[0])  # Ensures no repeated colors
            self.list_of_turtles.append(self.turtle)
            print(f"Generating 'The {str(self.turtle.color()[0])} turtle'... ")

        for turtle in list(self.list_of_turtles):
            self.list_of_turtles_colors_in_race.append(turtle.color()[0])

        self.print_colors_names_of_turtles()

    def print_colors_names_of_turtles(self):
        """Prints all available turtle color options for user reference."""
        print("\n" * 2)
        print(f"Available color options: {self.list_of_turtles_colors_in_race}")

    def move_turtles_to_starting_point(self):
        """
        Positions turtles at evenly spaced vertical starting locations on the left side of the screen.
        NumPy's linspace is used to distribute positions uniformly.
        """
        self.starting_positions = np.linspace(
            -(self.screen_height // 2) + self.offset_y,
            self.screen_height // 2 - self.offset_y,
            self.number_of_turtles
        )

        for y, turtle in zip(self.starting_positions, self.list_of_turtles):
            turtle.penup()
            turtle.goto(x=-(self.screen_width // 2) + 20, y=y)

    def start_race(self):
        """
        Initiates the turtle race.
        Each turtle moves forward by a random step size until one crosses the finish line.
        The race continues until a winner is determined.
        """
        while self.continue_racing:
            for turtle in self.list_of_turtles:
                x_actual_pos, y_actual_pos = turtle.pos()
                # Each turtle moves randomly in the x-direction
                turtle.goto(x=x_actual_pos + random.choice(self.x_steps_for_turtle_in_race), y=y_actual_pos)

                # Check for finish line crossing
                if turtle.pos()[0] >= self.screen_width // 2:
                    self.continue_racing = False
                    self.winner = turtle
                    self.print_winner()
                    break

    def print_winner(self):
        """Announces the winning turtle's color."""
        print(f"\nThe winner was: 'The {str(self.winner.color()[0])} turtle'!")

    def obtain_user_bet(self):
        """
        Prompts the user to place a bet on a turtle by color name.
        Ensures the input matches one of the available options.
        """
        self.user_bet = self.screen.textinput(title='Bet Racing', prompt='Which turtle would you like to bet on? ')
        while self.user_bet not in self.list_of_turtles_colors_in_race:
            self.user_bet = self.screen.textinput(
                title='Bet Racing',
                prompt='Invalid input. Type correctly one of the available colors: '
            )

    def check_user_bet(self):
        """Compares the user’s bet with the winning turtle and prints the result."""
        if self.user_bet == self.winner.color()[0]:
            print("\nCongratulations! You won your bet!")
        else:
            print("\nBetter luck next time! You lost your bet.")


# Main execution
turtle_race_app = TurtleRace()
turtle_race_app.greeting()

# Define race parameters
number_of_turtles = 5
turtle_race_app.generate_turtles(number_of_turtles)

# Obtain user bet and start race
turtle_race_app.obtain_user_bet()
turtle_race_app.move_turtles_to_starting_point()
turtle_race_app.start_race()

# Evaluate result and wait for user exit
turtle_race_app.check_user_bet()
turtle_race_app.screen.exitonclick()
