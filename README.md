# 🎓 MINI PROJECT - STUDENT SCORE MANAGEMENT SYSTEM

## 1. Project Description

This is a Python console application designed to manage student scores efficiently using procedural programming techniques.

The program runs in a CLI (Command Line Interface) environment, allowing users to interact with the system through a menu-driven interface. It supports multiple features such as adding students, displaying data, searching, sorting, calculating statistics, and saving/loading data from files.

This project applies knowledge from **Programming Methods 1**, including:

* Using functions to modularize the program
* Implementing loops for continuous interaction
* Using conditional statements to control logic flow
* Managing data using lists and dictionaries
* Validating user input
* Handling file input/output (TXT & JSON)
* Presenting data in structured format

**Selected Topic:** Topic 3 – Student Score Management (Quản lý điểm sinh viên)

---

## 2. Project Objective

The main objectives of this system are:

* Manage student information (ID, name, score)
* Allow users to perform CRUD-like operations (add, view, search)
* Provide sorting and statistical analysis of student scores
* Store data for future use using TXT and JSON files
* Apply procedural programming design principles
* Practice file handling and data persistence

---

## 3. Data Structure

Each student is stored as a dictionary:

```python
{
    "id": "S001",
    "name": "Nguyen Van A",
    "score": 8.5
}
```

All students are stored in a list:

```python
students = [
    {"id": "S001", "name": "Nguyen Van A", "score": 8.5},
    {"id": "S002", "name": "Tran Thi B", "score": 7.0}
]
```

---

## 4. Technologies Used

| Component                     | Role                       |
| ----------------------------- | -------------------------- |
| Python 3                      | Main programming language  |
| TXT File (students.txt)       | Store raw student data     |
| JSON File (students.json)     | Structured data storage    |
| CLI                           | User interaction interface |
| Built-in Libraries (os, json) | File handling              |

---

## 5. Project Structure

```
STUDENT-SCORE-MANAGEMENT/
│-- app.py
│-- students.txt
│-- students.json
│-- README.md
```

| File          | Description                        |
| ------------- | ---------------------------------- |
| app.py        | Main program source code           |
| students.txt  | Stores student data in text format |
| students.json | Stores student data in JSON format |
| README.md     | Project documentation              |

---

## 6. Main Features

### 6.1 Add Student

Users can input:

* Student ID
* Name
* Score (0–10)

The program validates score input to ensure correctness.

---

### 6.2 Display Students

Displays all student records in a formatted table:

* ID
* Name
* Score

---

### 6.3 Search Student

Allows searching by:

* Exact ID
* Exact name

---

### 6.4 Sort Students

Sorts the student list by score in descending order.

---

### 6.5 Basic Statistics

Calculates:

* Average score
* Highest score
* Lowest score

---

### 6.6 Save to TXT File

Format:

```
ID,Name,Score
```

---

### 6.7 Load from TXT File

* Restores student list
* Skips invalid/corrupted lines safely

---

### 6.8 Advanced Search (Keyword Search)

Search by partial name.

**Example:**

```
Input: an
Matches: Nguyen Van An, Tran
```

---

### 6.9 Advanced Statistics (Grade Classification)

| Grade | Condition       |
| ----- | --------------- |
| A     | Score ≥ 8       |
| B     | 6.5 ≤ Score < 8 |
| C     | 5 ≤ Score < 6.5 |
| D     | Score < 5       |

---

### 6.10 Save to JSON

Exports all student data into `students.json`.

---

### 6.11 Load from JSON

Loads and restores system data.

---

## 7. Menu System

```
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
```

---

## 8. Input Validation

| Input     | Rule                      |
| --------- | ------------------------- |
| Score     | Must be between 0 and 10  |
| File Data | Invalid lines are skipped |
| JSON Data | Must be a list            |

---

## 9. Main Functions

| Function              | Description          |
| --------------------- | -------------------- |
| add_student()         | Add new student      |
| display_students()    | Show all students    |
| search_student()      | Search by ID/name    |
| sort_students()       | Sort by score        |
| statistics()          | Avg, max, min        |
| save_to_txt()         | Save TXT             |
| load_from_txt()       | Load TXT             |
| advanced_search()     | Keyword search       |
| advanced_statistics() | Grade classification |
| save_to_json()        | Export JSON          |
| load_from_json()      | Import JSON          |
| menu()                | Main loop            |

---

## 10. Usage Examples

### Add Student

```
Enter ID: S001
Enter name: Nguyen Van A
Enter score: 8.5
=> Student added successfully!
```

### Display Students

```
ID        Name                Score
----------------------------------------
S001      Nguyen Van A        8.5
S002      Tran Thi B          7.0
```

### Statistics

```
Average score: 7.75
Max score: 8.5
Min score: 7.0
```

### Grade Statistics

```
Grade statistics:
A: 1
B: 1
C: 0
D: 0
```

---

## 11. Advanced Features

### Keyword Search

Supports substring matching for flexible searching.

### JSON Storage

Structured data saving and loading.

---

## 12. How to Run

### Requirements:

* Python 3.x installed

### Run:

```bash
python app.py
```

---

## 13. Self-Assessment

| #         | Component        | Criteria              | Max      | Score    |
| --------- | ---------------- | --------------------- | -------- | -------- |
| 1         | CLI Menu         | Fully functional loop | 1.0      | 1.0      |
| 2         | Input Validation | Score validation      | 1.0      | 1.0      |
| 3         | Data Display     | Clean output          | 1.0      | 1.0      |
| 4         | Search           | ID & name             | 1.0      | 1.0      |
| 5         | Sorting          | Descending score      | 1.0      | 1.0      |
| 6         | Statistics       | Avg, max, min         | 1.0      | 1.0      |
| 7         | TXT File I/O     | Save & load           | 1.0      | 1.0      |
| 8         | Advanced Search  | Keyword search        | 1.0      | 1.0      |
| 9         | JSON Storage     | Export & import       | 1.0      | 1.0      |
| 10        | Code Structure   | Modular design        | 1.0      | 1.0      |
| **TOTAL** |                  |                       | **10.0** | **10.0** |

---

## 14. Student Information

* **Student Name:** [Your Name]
* **Student ID:** [Your ID]
* **Class:** [Your Class]
* **Course:** Programming Methods 1
* **Instructor:** [Instructor Name]
* **University:** [Your University]

---
