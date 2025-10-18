"""
Project Number: 15
Project Name: The Quiz (Object-Oriented Version)
Description:
    This program implements a professional, object-oriented Quiz Application.
    It uses three primary classes: Question, QuizBrain, and a data source
    containing question-answer pairs. The user is presented with a series of
    True/False questions and interacts with the system through the console.

    Key features include:
    - Encapsulation of questions into Question objects.
    - QuizBrain class manages quiz flow, user input, score tracking, and
      correctness verification.
    - User input validation ensures that only "True" or "False" responses
      are accepted.
    - Final score display at the end of the quiz provides clear feedback.

    This design promotes readability, modularity, and scalability, adhering
    to Object-Oriented Programming principles.

Author: Jonathan Eduardo Castilla Zamora
"""

# Import the Question class for encapsulating question text and answer.
from question_model import Question
# Import the question data from a separate data source file.
from data import question_data
# Import the QuizBrain class which controls the quiz flow and scoring.
from quiz_brain import QuizBrain

# Initialize an empty list to hold Question objects.
question_bank = []

# Iterate through the question_data list to create Question objects.
for question_item in question_data:
    # Extract the question text.
    question_text = question_item['text']
    # Extract the correct answer.
    answer = question_item['answer']
    # Instantiate a Question object and append it to the question_bank list.
    question_bank.append(Question(question_text=question_text, answer=answer))


# Instantiate the QuizBrain object with the list of Question objects.
quiz = QuizBrain(question_list=question_bank)

# Main loop: continue asking questions until the quiz is complete.
while quiz.still_has_questions():
    # Retrieve the next question and handle user interaction internally.
    next_question = quiz.next_question()

# Once all questions have been asked, print the user's final score.
quiz.print_final_score()
