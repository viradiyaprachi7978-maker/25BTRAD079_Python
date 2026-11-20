#  Lab_Exercise_8
contacts = []

def add():
    contacts.append({
        "name": input("Name: "),
        "phone": input("Phone: "),
        "email": input("Email: ")
    })

def search(phone):
    return next((c for c in contacts if c["phone"] == phone), None)

def display():
    for c in contacts:
        print(c)

def main():
    while True:
        ch = input("\n1.Add 2.Search 3.Update 4.Delete 5.Display 6.Exit: ")

        if ch == '1':
            add()
        elif ch == '2':
            print(search(input("Phone: ")) or "Not Found")
        elif ch == '3':
            c = search(input("Phone: "))
            if c:
                c["name"] = input("New name: ")
                c["email"] = input("New email: ")
        elif ch == '4':
            c = search(input("Phone: "))
            if c:
                contacts.remove(c)
        elif ch == '5':
            display()
        elif ch == '6':
            break
        else:
            print("Invalid choice!")

main()

#Lab_Excercise_9
def grade(m):
    if m >= 90: return 'A'
    elif m >= 80: return 'B'
    elif m >= 70: return 'C'
    elif m >= 60: return 'D'
    elif m >= 50: return 'E'
    else: return 'F'

students = {}

n = int(input("Number of students: "))

for i in range(n):
    name = input("Name: ")
    marks = float(input("Marks: "))
    students[name] = marks

for name, marks in students.items():
    print(name, marks, grade(marks))

#Lab_Exercise_10
sentence = input("Enter a sentence: ")

words = sentence.lower().split()

frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print("\n--- WORD FREQUENCY ---")

for word, count in frequency.items():
    print(word, ":", count)