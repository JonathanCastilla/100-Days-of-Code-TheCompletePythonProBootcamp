# Quiz (Object-Oriented Version)

## 📄 Project Description
This project implements an object-oriented Quiz Application in Python. The program presents the user with a series of True/False questions sourced from a predefined dataset. Users interact via the console, answer questions, and receive feedback on correctness. The quiz tracks the user's score and displays the final results upon completion.

Key Features:
- Object-Oriented Design using **Question** and **QuizBrain** classes.
- Modular architecture for scalability and readability.
- Input validation ensures only "True" or "False" responses are accepted.
- Final score display for clear performance feedback.

## 📂 Project Structure
``` bash
quiz-oop/
│── main.py # Main execution file for running the quiz
│── question_model.py # Class representing a single quiz question
│── quiz_brain.py # Class managing quiz logic, user input, and scoring
│── data.py # Dataset containing question text and correct answers
│── README.md # Project documentation
```

## 🛠️ Requirements
- Python 3.x
- Standard library (no external dependencies required)

## 📝 Example of Run
``` python
Q.1: The sky is blue. (True/False)?: True
Correct! You got it!
Your current score is: 1/1.

Q.2: 2 + 2 equals 5. (True/False)?: False
Correct! You got it!
Your current score is: 2/2.

... (continues until all questions are answered)

You've completed the quiz.
Your final score was: 10/10.
```

## 🧩 Object-Oriented Design Summary

| Class Name   | Responsibility                                                                 |
|--------------|-------------------------------------------------------------------------------|
| Question     | Encapsulates a single quiz question, storing its text and correct answer.     |
| QuizBrain    | Manages the quiz flow, presents questions, validates answers, and tracks score.|

