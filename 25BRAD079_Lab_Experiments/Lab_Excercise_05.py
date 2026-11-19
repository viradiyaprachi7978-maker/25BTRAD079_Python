#Lab_Excercise_14
class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited!")
        else:
            print("Invalid amount!")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn!")
        else:
            print("Insufficient balance or invalid amount!")

    def display(self):
        print("Name:", self.name)
        print("Balance:", self.balance)


b = Bank("Rahul", 5000)

b.deposit(2000)
b.withdraw(1000)
b.display()

#Lab_Exercise_15
class Book:
    def __init__(self, title):
        self.title = title
        self.available = True

    def issue(self):
        if self.available:
            self.available = False
            print("Book issued!")
        else:
            print("Book not available!")

    def return_book(self):
        if not self.available:
            self.available = True
            print("Book returned!")
        else:
            print("Book was not issued!")

    def display(self):
        print(self.title, "-", "Available" if self.available else "Issued")


b1 = Book("Python Programming")

b1.display()
b1.issue()
b1.display()
b1.return_book()
b1.display()

#Lab_Exercise_16
import random

n = int(input("Enter number of dice: "))
rolls = int(input("Enter number of times to roll: "))

frequency = {}

for i in range(rolls):
    dice = []

    for j in range(n):
        dice.append(random.randint(1, 6))

    total = sum(dice)

    print("Dice:", dice, "Total:", total)

    frequency[total] = frequency.get(total, 0) + 1

print("\n--- FREQUENCY COUNTER ---")

for total, count in frequency.items():
    print(total, ":", count)