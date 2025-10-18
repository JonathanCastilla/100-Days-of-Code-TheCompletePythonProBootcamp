# QuizBrain class for managing the flow and logic of the Quiz Application.

class QuizBrain:
    """
    Class: QuizBrain
    ----------------
    This class controls the overall behavior of the quiz, including question
    progression, user input handling, answer verification, score tracking, and
    final result display.

    Attributes:
    -----------
    question_number : int
        Tracks the current question index within the quiz.
    question_list : list
        A list of Question objects representing the entire quiz.
    user_input : str
        Stores the user's current response to a quiz question.
    user_score : int
        Tracks the total number of correctly answered questions.
    """

    def __init__(self, question_list):
        """
        Initialize the QuizBrain object with a list of Question objects.

        Parameters:
        -----------
        question_list : list
            The list of Question objects to be used in the quiz.
        """
        # Initialize the index of the current question.
        self.question_number = 0
        # Store the list of Question objects.
        self.question_list = question_list
        # Initialize the user's current answer as an empty string.
        self.user_input = ""
        # Initialize the user's score to zero.
        self.user_score = 0

    def still_has_questions(self):
        """
        Determine if there are remaining questions to be asked.

        Returns:
        --------
        bool
            True if there are more questions, False if the quiz is complete.
        """
        # Total number of questions in the quiz.
        number_of_questions = len(self.question_list)
        # Compare current question index with total questions to decide.
        return self.question_number < number_of_questions

    def next_question(self):
        """
        Present the next question to the user, handle input validation, and
        check if the response is correct. Updates question index and score.
        """
        # Retrieve the current question based on question_number.
        current_question = self.question_list[self.question_number]
        # Increment the question index for the next iteration.
        self.question_number += 1

        # Prompt the user for an answer and normalize capitalization.
        self.user_input = input(f"Q.{self.question_number}: " +
                                current_question.question_text +
                                " (True/False)?: ").title()

        # Validate input to ensure only 'True' or 'False' responses are accepted.
        while self.user_input not in ["True", "False"]:
            self.user_input = input(f"Q.{self.question_number}: " +
                                    current_question.question_text +
                                    " Type correctly (True/False): ").title()

        # Check the user's answer against the correct answer.
        self.check_answer(self.user_input, current_question.answer)

    def check_answer(self, user_input, correct_answer):
        """
        Compare the user's input to the correct answer and update the score.

        Parameters:
        -----------
        user_input : str
            The user's response to the question.
        correct_answer : str
            The correct answer of the current question.
        """
        # Check for correctness and provide feedback.
        if user_input == correct_answer.title():
            print("Correct! You got it!")
            # Increment the score for a correct answer.
            self.user_score += 1
        else:
            print("That's wrong.")
        # Display the correct answer.
        print(f"The correct answer was: {correct_answer.title()}.")
        # Print the user's current score after each question.
        self.print_score(self.user_score, self.question_number)

    def print_score(self, score, question_number):
        """
        Display the user's current score relative to the number of questions
        answered so far.

        Parameters:
        -----------
        score : int
            The user's current score.
        question_number : int
            The number of questions answered so far.
        """
        print(f"Your current score is: {score}/{question_number}.")
        print("\n")

    def print_final_score(self):
        """
        Display the user's final score and conclude the quiz.
        """
        print("You've completed the quiz.")
        print(f"Your final score was: {self.user_score}/{self.question_number}.")
