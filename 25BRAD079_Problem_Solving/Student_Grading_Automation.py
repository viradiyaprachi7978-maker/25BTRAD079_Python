def calculate_average(scores):
    total = sum(scores)
    count = len(scores)
    return total / count


def assign_grade(average):
    if average >= 90:
        return "A+", "Pass"
    elif average >= 80:
        return "A", "Pass"
    elif average >= 70:
        return "B", "Pass"
    elif average >= 60:
        return "C", "Pass"
    elif average >= 50:
        return "D", "Pass"
    else:
        return "F", "Fail"


def collect_student_data():
    name = input("Enter student name: ")
    num_subjects = int(input(f"How many subjects for {name}? "))

    marks = []
    for i in range(num_subjects):
        score = float(input(f"  Enter mark for Subject {i + 1} (0-100): "))
        marks.append(score)

    return {"name": name, "marks": marks}


def run_grading_system():
    students_count = int(input("How many students to evaluate? "))
    student_records = []

    for _ in range(students_count):
        print("-" * 30)
        data = collect_student_data()
        student_records.append(data)

    # Display results table
    print("\n" + "=" * 50)
    print(f"{'Student':<15} {'Average':<10} {'Grade':<8} {'Status':<6}")
    print("=" * 50)

    for student in student_records:
        avg = calculate_average(student["marks"])
        grade, status = assign_grade(avg)
        print(f"{student['name']:<15} {avg:<10.2f} {grade:<8} {status:<6}")

    print("=" * 50)

if __name__ == "__main__":
    run_grading_system()