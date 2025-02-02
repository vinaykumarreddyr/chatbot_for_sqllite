# chatbot_for_sqllite
Assignment
# SQLite Chat Assistant

A Python-based chat assistant that interacts with an SQLite database to answer user queries. Built with Flask for the web interface.

---

## Features
- Accepts natural language queries.
- Converts queries into SQL to fetch data from the SQLite database.
- Responds to the user with clear, formatted answers.
- Supports the following types of queries:
  - "Show me all employees in the [department] department."
  - "Who is the manager of the [department] department?"
  - "List all employees hired after [date]."
  - "What is the total salary expense for the [department] department?"

---

## Prerequisites
- Python 3.x
- Flask
- SQLite3

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/sqlite-chat-assistant.git
cd sqlite-chat-assistant

2. Install Dependencies
Install the required Python packages:
pip install flask

3. Set Up the Database
Ensure the SQLite database (company.db) is in the project directory. If it doesn't exist, create it using the following SQL commands:
CREATE TABLE Employees (
    ID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Department TEXT NOT NULL,
    Salary INTEGER NOT NULL,
    Hire_Date TEXT NOT NULL
);

CREATE TABLE Departments (
    ID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Manager TEXT NOT NULL
);

INSERT INTO Employees (ID, Name, Department, Salary, Hire_Date) VALUES
(1, 'Alice', 'Sales', 50000, '2021-01-15'),
(2, 'Bob', 'Engineering', 70000, '2020-06-10'),
(3, 'Charlie', 'Marketing', 60000, '2022-03-20');

INSERT INTO Departments (ID, Name, Manager) VALUES
(1, 'Sales', 'Alice'),
(2, 'Engineering', 'Bob'),
(3, 'Marketing', 'Charlie');


4. Run the Application
Start the Flask application:
python app.py

5. Access the Chat Assistant
Open your browser and go to:
http://127.0.0.1:5000

6.Folder Structure
sqlite-chat-assistant/
│
├── app.py                # Flask application
├── company.db            # SQLite database
├── templates/            # Folder for HTML templates
│   └── index.html        # Chat interface HTML file
└── README.md             # Project documentation

7.Usage
Open the chat assistant in your browser.

Type your query in the input box and click "Send".

The assistant will respond with the appropriate answer.


8.Expected Output
Here’s an example of how the chat assistant will respond:
You: Show me all employees in the Sales department.
Assistant: Employees in Sales: Alice

You: Who is the manager of the Engineering department?
Assistant: The manager of Engineering is Bob.

You: List all employees hired after 2021-01-01.
Assistant: Employees hired after 2021-01-01: Charlie

You: What is the total salary expense for the Marketing department?
Assistant: Total salary expense for Marketing: 60000

9.Known Limitations
The chat assistant uses simple string matching and regular expressions for natural language processing, which may not handle complex queries well.

Error handling is basic and may not cover all edge cases.

10.Suggestions for Improvement
Implement more advanced natural language processing using libraries like NLTK or spaCy.

Add more complex queries and error handling.

Improve the user interface with a more interactive design.

