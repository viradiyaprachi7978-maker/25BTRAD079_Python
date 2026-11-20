#Lab_Exercise_11
def read_log():
    try:
        f = open("log.txt", "r")
        data = f.read()

        print("ERROR:", data.count("ERROR"))
        print("WARNING:", data.count("WARNING"))
        print("INFO:", data.count("INFO"))

        f.close()

    except FileNotFoundError:
        print("File not found!")

read_log()

#Lab_Exercise_12
def add():
    f = open("student.txt", "a")
    name = input("Enter name: ")
    roll = input("Enter roll number: ")
    marks = input("Enter marks: ")

    f.write(roll + "," + name + "," + marks + "\n")
    f.close()
    print("Record added!")

def display():
    f = open("student.txt", "r")
    print(f.read())
    f.close()

def search():
    roll = input("Enter roll number: ")
    f = open("student.txt", "r")

    for line in f:
        if line.startswith(roll + ","):
            print(line)
            break
    else:
        print("Record not found!")

    f.close()

def main():
    while True:
        ch = input("\n1.Add 2.Display 3.Search 4.Exit: ")

        if ch == '1':
            add()
        elif ch == '2':
            display()
        elif ch == '3':
            search()
        elif ch == '4':
            break

main()

#Lab_Exercise_13
import csv

def payroll():
    try:
        f = open("employees.csv", "r")
        reader = csv.reader(f)

        next(reader)

        for row in reader:
            name = row[0]
            basic = float(row[1])

            hra = basic * 0.20
            da = basic * 0.10
            pf = basic * 0.12

            gross = basic + hra + da
            net = gross - pf

            print("\nEmployee:", name)
            print("Gross Salary:", gross)
            print("Deduction:", pf)
            print("Net Salary:", net)

        f.close()

    except FileNotFoundError:
        print("CSV file not found!")

payroll()