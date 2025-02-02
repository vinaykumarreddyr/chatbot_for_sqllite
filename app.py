from flask import Flask, request, jsonify, render_template # type: ignore
import sqlite3
import re

app = Flask(__name__)

def connect_to_db():
    return sqlite3.connect('company.db')

def execute_query(query, params=()):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute(query, params)
    result = cursor.fetchall()
    conn.close()
    return result

def show_all_employees(department):
    query = "SELECT Name FROM Employees WHERE Department = ?"
    result = execute_query(query, (department,))
    return [row[0] for row in result]

def get_manager(department):
    query = "SELECT Manager FROM Departments WHERE Name = ?"
    result = execute_query(query, (department,))
    return result[0][0] if result else None

def list_employees_hired_after(date):
    query = "SELECT Name FROM Employees WHERE Hire_Date > ?"
    result = execute_query(query, (date,))
    return [row[0] for row in result]

def total_salary_expense(department):
    query = "SELECT SUM(Salary) FROM Employees WHERE Department = ?"
    result = execute_query(query, (department,))
    return result[0][0]

def handle_query(user_input):
    if "show me all employees in the" in user_input.lower():
        department = re.search(r'in the (.*) department', user_input, re.IGNORECASE).group(1)
        employees = show_all_employees(department)
        return f"Employees in {department}: {', '.join(employees)}" if employees else "No employees found."

    elif "who is the manager of the" in user_input.lower():
        department = re.search(r'of the (.*) department', user_input, re.IGNORECASE).group(1)
        manager = get_manager(department)
        return f"The manager of {department} is {manager}." if manager else "Department not found."

    elif "list all employees hired after" in user_input.lower():
        date = re.search(r'after (.*)', user_input, re.IGNORECASE).group(1)
        employees = list_employees_hired_after(date)
        return f"Employees hired after {date}: {', '.join(employees)}" if employees else "No employees found."

    elif "what is the total salary expense for the" in user_input.lower():
        department = re.search(r'for the (.*) department', user_input, re.IGNORECASE).group(1)
        total = total_salary_expense(department)
        return f"Total salary expense for {department}: {total}" if total else "Department not found."

    else:
        return "Sorry, I don't understand that query."

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query():
    user_input = request.json.get('query')
    response = handle_query(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)