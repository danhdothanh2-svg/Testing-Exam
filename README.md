# README generator for Student Score Management System

readme_content = """
🎓 MINI PROJECT - STUDENT SCORE MANAGEMENT SYSTEM

--------------------------------------------------

1. Project Description

This is a Python console application designed to manage student scores efficiently using procedural programming techniques.

The program runs in a CLI (Command Line Interface) environment, allowing users to interact with the system through a menu-driven interface. It supports multiple features such as adding students, displaying data, searching, sorting, calculating statistics, and saving/loading data from files.

This project applies knowledge from Programming Methods 1, including:

- Using functions to modularize the program
- Implementing loops for continuous interaction
- Using conditional statements to control logic flow
- Managing data using lists and dictionaries
- Validating user input
- Handling file input/output (TXT & JSON)
- Presenting data in structured format

Selected Topic: Topic 3 – Student Score Management

--------------------------------------------------

2. Project Objective

- Manage student information (ID, name, score)
- Perform operations like add, view, search
- Provide sorting and statistical analysis
- Store data using TXT and JSON files
- Practice procedural programming design

--------------------------------------------------

3. Data Structure

Each student is stored as:

{
    "id": "S001",
    "name": "Nguyen Van A",
    "score": 8.5
}

Stored in a list:

students = [
    {"id": "S001", "name": "Nguyen Van A", "score": 8.5},
    {"id": "S002", "name": "Tran Thi B", "score": 7.0}
]

--------------------------------------------------

4. Technologies Used

- Python 3
- TXT File (students.txt)
- JSON File (students.json)
- CLI interface
- Built-in libraries: os, json

--------------------------------------------------

5. Project Structure

STUDENT-SCORE-MANAGEMENT/
|-- app.py
|-- students.txt
|-- students.json
|-- README.md

--------------------------------------------------

6. Main Features

1. Add Student (ID, name, score)
2. Display Students in table format
3. Search by ID or name
4. Sort by score (descending)
5. Statistics (average, max, min)
6. Save to TXT file
7. Load from TXT file
8. Advanced search (keyword)
9. Grade classification (A, B, C, D)
10. Save to JSON
11. Load from JSON

--------------------------------------------------

7. Menu System

===== STUDENT MANAGEMENT =====
1. Add student
2. Display students
3. Search
4. Sort
5. Statistics
6. Save to file
7. Load from file
8. Advanced search
9. Advanced statistics
10. Save to JSON
11. Load from JSON
0. Exit

--------------------------------------------------

8. Input Validation

- Score must be between 0 and 10
- Invalid TXT lines are skipped
- JSON must be list format

--------------------------------------------------

9. Main Functions

- add_student()
- display_students()
- search_student()
- sort_students()
- statistics()
- save_to_txt()
- load_from_txt()
- advanced_search()
- advanced_statistics()
- save_to_json()
- load_from_json()
- menu()

--------------------------------------------------

10. Usage Examples

Add student:
Enter ID: S001
Enter name: Nguyen Van A
Enter score: 8.5
=> Student added successfully!

Display:
ID        Name                Score
----------------------------------------
S001      Nguyen Van A        8.5

Statistics:
Average score: 7.75
Max score: 8.5
Min score: 7.0

--------------------------------------------------

11. Advanced Features

- Keyword search (substring match)
- JSON export/import

--------------------------------------------------

12. How to Run

python app.py

--------------------------------------------------

13. Self-Assessment

All required features implemented successfully.
Score: 10/10

--------------------------------------------------

14. Student Information

Student Name: Đỗ Thanh Danh
Student ID: 24S7040004
Class: Tin 2E
Course: Programming Methods 1


--------------------------------------------------
"""
