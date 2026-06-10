# sk-student-management

A lightweight, terminal-based database application built using **Python** and **MySQL**. I developed this project during my pre-college break to bridge the gap between high school computer science and professional software engineering.


## 🚀 About the Project
This system allows educational administrators to manage student records dynamically through a command-line interface. Instead of using temporary file handling, it connects directly to a relational database management system (RDBMS) to ensure data persistence.



### Key Features:
*   **Secure Connection:** Built-in exception handling to manage database connection states cleanly.
*   **Data Insertion:** Allows users to input new student details (Roll Number, Name, Board Marks) and saves them securely in SQL tables.
*   **Data Retrieval:** Fetches and displays records using structured table indexes.
*   **Interactive CLI Menu:** A continuous loop menu driven entirely by user input numbers.

---



## 🛠️ Tech Stack & Concepts Used
*   **Language:** Python 3
*   **Database:** MySQL (Structured Query Language)
*   **Libraries:** `mysql-connector-python`
*   **Core Concepts:** Conditional statements (`if-elif-else`), indefinite loops (`while True`), Exception Handling (`try-except`), and Tuple/List indexing.

---

## 💻 How to Run This Locally

### 1. Database Setup
Run the following SQL commands in your local MySQL Server to set up the backend structure:

```sql
CREATE DATABASE school_db;
USE school_db;

CREATE TABLE students (
    roll_no INT PRIMARY KEY,
    name VARCHAR(100),
    marks DECIMAL(5,2)
);
```

### 2. Python Setup
Download the project ZIP file, open your terminal inside the project folder, and install the required connector:
```bash
pip install mysql-connector-python
```

### 3. Execution
Open the `app.py` file, replace the database connection placeholders with your local MySQL credentials, and run:
```bash
python app.py
```




---

## 🧑‍💻 About the Author
I am an incoming **B.Tech Computer Science and Engineering (CSE)** student. I am passionate about core coding, database management, and backend development. I built this project to master the fundamentals of Python-SQL connectivity.


----Updated README Description
