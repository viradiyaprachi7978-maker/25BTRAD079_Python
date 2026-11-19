def simple_calculator():
    """Perform basic arithmetic based on user input."""
    print("\nSimple Calculator")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Choose an operator (+, -, *, /): ").strip()

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2
    else:
        print("Invalid operator.")
        return

    print(f"Result: {num1} {operator} {num2} = {result}")


def area_calculator():
    """Calculate the area of common shapes."""
    print("\nArea Calculator")
    shape = input("Choose a shape (rectangle/circle/triangle): ").strip().lower()

    if shape == "rectangle":
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        area = length * width
        print(f"Area of rectangle = {area}")
    elif shape == "circle":
        radius = float(input("Enter radius: "))
        area = 3.14 * radius * radius
        print(f"Area of circle = {area}")
    elif shape == "triangle":
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        area = 0.5 * base * height
        print(f"Area of triangle = {area}")
    else:
        print("Invalid shape selection.")

try:
    while True:
        print("\n--- What would you like to do? ---")
        print("1. Simple Calculator")
        print("2. Area Finder")
        print("3. Exit")

        choice = input("Pick an option (1-3): ").strip()

        if choice == "1":
            simple_calculator()
        elif choice == "2":
            area_calculator()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")
except EOFError:
    print("No input available. Exiting.")