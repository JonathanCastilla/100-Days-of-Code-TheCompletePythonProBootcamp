from turtle import Turtle, Screen
import pandas as pd

# === CONSTANT DEFINITIONS ===
BEGINNING_TITLE = 'Guess the state'          # Title shown at the beginning of the game
PLAYING_TITLE = 'States Correct'             # Title shown while the game is running
PROMPT = "What's another state's name?"       # Prompt message for user input


class Map(Turtle):
    """
    This class manages the graphical map, user interaction, state validation,
    and game logic for the U.S. States guessing game.
    It inherits from the Turtle class to allow direct drawing on the screen.
    """

    def __init__(self):
        """
        Initializes the map, screen configuration, game state variables,
        and data containers for correct and missing answers.
        """
        super().__init__()

        # --- Screen configuration ---
        self.screen = Screen()
        self.screen.setup(725, 491)
        self.screen.title("U.S. States Game")

        # --- Load and display the map image ---
        self.image = "blank_states_img.gif"
        self.screen.addshape(self.image)
        self.shape(self.image)

        # --- User input and validation variables ---
        self.answer_state = None          # Stores the user's current answer
        self.correct_answer = None        # Boolean flag for answer correctness

        # --- UI text configuration ---
        self.beginning_title = BEGINNING_TITLE
        self.playing_title = PLAYING_TITLE
        self.prompt = PROMPT

        # --- Game progress tracking ---
        self.correct_guesses = []         # List of correctly guessed states
        self.missing_states = []          # States not guessed when exiting
        self.data_to_learn = None         # DataFrame for exporting missing states

        # --- Game state flag ---
        self.game_over = False

        # --- Coordinate storage ---
        self.x_coor = 0
        self.y_coor = 0


    def get_mouse_click_coor(self, x, y):
        """
        Callback function that captures mouse click coordinates.
        Useful for identifying the correct x and y positions of states.
        """
        self.x_coor = x
        self.y_coor = y
        print(f"x = {x}, y = {y}")


    def obtain_coordinates(self):
        """
        Enables mouse click listening and prints coordinates to the console.
        This method is typically used during development to collect map data.
        """
        self.screen.onscreenclick(self.get_mouse_click_coor)
        self.screen.mainloop()


    def prompt_user_input(self, title_text, prompt_text):
        """
        Displays a text input dialog to the user.

        :param title_text: Title shown in the dialog window
        :param prompt_text: Prompt message for the user
        :return: User's input as a string
        """
        return self.screen.textinput(title=title_text, prompt=prompt_text)


    def check_answer_state(self, data_from_csv):
        """
        Validates the user's input against the dataset of U.S. states.

        - If the answer is correct and not previously guessed, it is recorded
          and displayed on the map.
        - If the user types 'exit', the game ends and missing states are saved.
        - Otherwise, the answer is marked as incorrect.

        :param data_from_csv: Pandas DataFrame containing state names and coordinates
        """

        # --- Correct state guessed ---
        if str(self.answer_state).title() in list(data_from_csv['state']):
            if str(self.answer_state).title() not in self.correct_guesses:

                # Add state to correct guesses
                self.correct_guesses.append(self.answer_state)

                # Update screen title with progress
                self.playing_title = (
                    f"{len(self.correct_guesses)}/{len(data_from_csv['state'])} "
                    f"{PLAYING_TITLE}"
                )

                # Retrieve x and y coordinates for the guessed state
                self.x_coor = data_from_csv[
                    data_from_csv['state'] == self.answer_state.title()
                ]['x'].item()

                self.y_coor = data_from_csv[
                    data_from_csv['state'] == self.answer_state.title()
                ]['y'].item()

                # Write state name on the map
                self.write_correct_answer(
                    str(self.answer_state).title(),
                    self.x_coor,
                    self.y_coor
                )

                self.correct_answer = True
            else:
                # State was already guessed
                self.correct_answer = False

        # --- Exit condition ---
        elif str(self.answer_state).lower() == 'exit':
            self.game_over = True

            # Identify missing states
            for state in list(data_from_csv['state']):
                if state not in self.correct_guesses:
                    self.missing_states.append(state)

            # Save missing states to CSV file
            self.data_to_learn = pd.DataFrame(self.missing_states)
            self.data_to_learn.to_csv('states_to_learn.csv')

        # --- Incorrect guess ---
        else:
            self.correct_answer = False


    def write_correct_answer(self, state, x, y):
        """
        Writes the correctly guessed state name at its geographical position.

        :param state: Name of the state
        :param x: X-coordinate on the map
        :param y: Y-coordinate on the map
        """
        self.a_writer = Turtle()
        self.a_writer.hideturtle()
        self.home()
        self.a_writer.penup()
        self.a_writer.goto(x, y)
        self.a_writer.write(state, align="center", font=("Calibri Light", 10))
        self.home()


    def check_user_wins(self):
        """
        Checks whether the user has guessed all 50 states.
        If so, the game ends successfully.
        """
        if len(self.correct_guesses) >= 50:
            self.game_over = True
