import os

students = []

# ================= BASIC FEATURES =================
def add_student():
    student_id = input("Enter ID: ")
    name = input("Enter name: ")

    try:
        score = float(input("Enter score (0-10): "))
        if score < 0 or score > 10:
            print("Score must be between 0 and 10!")
            return
    except:
        print("Invalid score!")
        return

    student = {
        "id": student_id,
        "name": name,
        "score": score
    }

    students.append(student)
    print("Student added successfully!")

def display_students():
    if not students:
        print("No student found.")
        return
    
    print(f"{'ID':<10}{'Name':<20}{'Score':<10}")
    print("-"*40)
    
    for s in students:
        print(f"{s['id']:<10}{s['name']:<20}{s['score']:<10}")

def search_student():
    keyword = input("Enter ID or Name: ")
    found = False
    
    for s in students:
        if s["id"] == keyword or s["name"] == keyword:
            print(s)
            found = True
    
    if not found:
        print("No student found!")

def sort_students():
    students.sort(key=lambda x: x["score"], reverse=True)
    print("Students sorted by score (descending).")

def statistics():
    if not students:
        print("No student found.")
        return
    
    scores = [s["score"] for s in students]
    avg = sum(scores) / len(scores)
    
    print("Average score:", round(avg, 2))
    print("Max score:", max(scores))
    print("Min score:", min(scores))

def save_to_txt(filename="students.txt"):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            for s in students:
                line = f"{s['id']},{s['name']},{s['score']}\n"
                f.write(line)
        print("Saved to TXT file successfully!")
    except Exception as e:
        print("Error saving file:", e)

def load_from_txt(filename="students.txt"):
    if not os.path.exists(filename):
        print("File not found!")
        return

    try:
        with open(filename, "r", encoding="utf-8") as f:
            students.clear()
            for line in f:
                parts = line.strip().split(",")

                if len(parts) != 3:
                    continue  # skip bad lines

                student_id, name, score = parts

                students.append({
                    "id": student_id,
                    "name": name,
                    "score": float(score)
                })

        print("Loaded from TXT file successfully!")
    except Exception as e:
        print("Error loading file:", e)

# ================= ADVANCED FEATURES =================
def advanced_search():
    keyword = input("Enter keyword: ").lower()
    results = [s for s in students if keyword in s["name"].lower()]
    
    if results:
        for s in results:
            print(s)
    else:
        print("No match found!")

def advanced_statistics():
    grade_count = {"A":0, "B":0, "C":0, "D":0}
    
    for s in students:
        score = s["score"]
        if score >= 8:
            grade_count["A"] += 1
        elif score >= 6.5:
            grade_count["B"] += 1
        elif score >= 5:
            grade_count["C"] += 1
        else:
            grade_count["D"] += 1
    
    print("Grade statistics:")
    for k, v in grade_count.items():
        print(f"{k}: {v}")

import json

def save_to_json(filename="students.json"):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(students, f, indent=4, ensure_ascii=False)
        print("Saved to JSON successfully!")
    except Exception as e:
        print("Error saving JSON:", e)

def load_from_json(filename="students.json"):
    if not os.path.exists(filename):
        print("File not found!")
        return

    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)

            if not isinstance(data, list):
                print("Invalid file format!")
                return

            students.clear()
            students.extend(data)

        print("Loaded from JSON successfully!")
    except Exception as e:
        print("Error loading JSON:", e)

# ================= MENU =================
def menu():
    while True:
        print("\n===== STUDENT MANAGEMENT =====")
        print("1. Add student")
        print("2. Display students")
        print("3. Search")
        print("4. Sort")
        print("5. Statistics")
        print("6. Save to file")
        print("7. Load from file")
        print("8. Advanced search")
        print("9. Advanced statistics")
        print("10. Save to JSON")
        print("11. Load from JSON")
        print("0. Exit")
        
        choice = input("Choose: ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            sort_students()
        elif choice == "5":
            statistics()
        elif choice == "6":
            save_to_txt()
        elif choice == "7":
            load_from_txt()
        elif choice == "8":
            advanced_search()
        elif choice == "9":
            advanced_statistics()
        elif choice == "10":
            save_to_json()
        elif choice == "11":
            load_from_json()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

# ================= RUN =================
if __name__ == "__main__":
    menu()