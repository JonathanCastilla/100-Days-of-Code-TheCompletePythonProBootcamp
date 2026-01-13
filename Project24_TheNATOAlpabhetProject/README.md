# 📡 Project 24: NATO Alphabet Project

## 📘 Description
This project converts a user's name into its **NATO Phonetic Alphabet** representation using Python and Pandas.  
Each letter is mapped to its standardized NATO code (e.g., A → Alpha, B → Bravo).

### ✍️ Author
- **Jonathan Eduardo Castilla Zamora**


## 🎯 Objectives
- Read structured data from a CSV file
- Use Pandas to process tabular data
- Apply dictionary comprehensions
- Practice clean, readable Python code
- Reinforce functional programming concepts

## 🗂️ Project Structure
```
Project_24_NATO_Alphabet/
│
├── main.py
├── nato_phonetic_alphabet.csv
└── README.md
```

## ⚙️ How It Works
1. The program loads the NATO alphabet from a CSV file.
2. A dictionary is created where:
   - Key → Letter
   - Value → NATO phonetic word
3. The user inputs their name.
4. Each letter is converted into its NATO equivalent.
5. The result is printed as a dictionary.

## 🧠 Example
**Input**
```
Enter your name: Alex
```

**Output**
```
{'A': 'Alpha', 'L': 'Lima', 'E': 'Echo', 'X': 'X-ray'}
```

## 🛠️ Technologies Used
- Python 🐍
- Pandas 📊

## 🚀 How to Run
```bash
python main.py
```
