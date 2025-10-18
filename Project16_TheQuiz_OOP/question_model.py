# Question class for encapsulating the text and answer of a single quiz question.

class Question:
    """
    Class: Question
    ----------------
    This class represents a single True/False question in the Quiz Application.
    Each Question object stores the question text and the correct answer.

    Attributes:
    -----------
    question_text : str
        The textual content of the quiz question.
    answer : str
        The correct answer for the question ("True" or "False").
    """

    def __init__(self, question_text, answer):
        """
        Initialize a Question object with text and corresponding answer.

        Parameters:
        -----------
        question_text : str
            The text representing the question.
        answer : str
            The correct answer associated with the question.
        """
        # Store the question text.
        self.question_text = question_text
        # Store the correct answer.
        self.answer = answer
