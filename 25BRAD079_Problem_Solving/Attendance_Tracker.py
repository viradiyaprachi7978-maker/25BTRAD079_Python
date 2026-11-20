students = {}

def add_student():
    name = input("Enter student name: ")
    students[name] = []

def mark_attendance():
    name = input("Enter student name: ")

    if name in students:
        status = input("Enter P for Present or A for Absent: ").upper()
        if status in ["P", "A"]:
            students[name].append(status)
        else:
            print("Invalid status!")
    else:
        print("Student not found!")

def display():
    for name, records in students.items():
        total = len(records)
        present = records.count("P")
        percent = present / total * 100 if total else 0

        print(name, records)
        print("Attendance:", round(percent, 2), "%")

def low_attendance():
    limit = float(input("Enter attendance threshold: "))

    for name, records in students.items():
        total = len(records)
        present = records.count("P")
        percent = present / total * 100 if total else 0

        if percent < limit:
            print(name, ":", round(percent, 2), "%")


while True:
    ch = input("\n1.Add 2.Mark 3.Display 4.Low Attendance 5.Exit: ")

    if ch == '1':
        add_student()
    elif ch == '2':
        mark_attendance()
    elif ch == '3':
        display()
    elif ch == '4':
        low_attendance()
    elif ch == '5':
        break
    else:
        print("Invalid choice!")