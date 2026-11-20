#Lab_Exercise_5
import random

def guess_the_number(min_num, max_num):
    """Proximity-based guessing game with directional hints."""
    print(f"\n--- Hot & Cold Guesser ({min_num} to {max_num}) ---")

    secret_number = random.randint(min_num, max_num)
    attempts = 0

    while True:
        try:
            guess = int(input(f"Attempt {attempts + 1} - Your guess: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        attempts += 1

        if guess == secret_number:
            print(f"🏆 Spot on! You found {secret_number} in {attempts} attempts.")
            break

        # Calculate distance and determine which direction the user needs to go
        distance = abs(secret_number - guess)
        direction = "higher" if guess < secret_number else "lower"

        # Provide both proximity and directional feedback
        if distance <= 3:
            print(f" Boiling! Go {direction}.")
        elif distance <= 10:
            print(f" Warm! Go {direction}.")
        elif distance <= 25:
            print(f" Chilly. Go {direction}.")
        else:
            print(f"Freezing! Way off. Go {direction}.")

# Run the game
guess_the_number(1, 100)

#Lab_Exercise_6
def is_prime(num):
    """Checks if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def factorial_recursive(n):
    """Calculates factorial using recursion instead of a loop."""
    if n < 0:
        return "Undefined for negative numbers"
    # Base case: factorial of 0 or 1 is 1
    if n in (0, 1):
        return 1
    # Recursive step: n * factorial(n-1)
    return n * factorial_recursive(n - 1)

def main():
    try:
        while True:
            print("\n1. Check Prime | 2. Find Factorial | 3. Exit")
            choice = input("Pick an option (1-3): ").strip()

            if choice == "1":
                num = int(input("Enter a number to check: "))
                status = "is" if is_prime(num) else "is not"
                print(f"{num} {status} a prime number.")

            elif choice == "2":
                num = int(input("Enter a number to find its factorial: "))
                print(f"The factorial of {num} is {factorial_recursive(num)}.")

            elif choice == "3":
                print("Goodbye!")
                break
            else:
                print("Invalid choice.")

    except ValueError:
        print("Error: Please enter a valid integer.")
    except EOFError:
        print("\nExiting.")

if __name__ == "__main__":
    main()

#Lab_Exercise_7
def fibonacci(n):
    """Returns the nth Fibonacci number using recursion."""
    # Base cases: The sequence starts with 0 and 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive step: sum of the two preceding numbers
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Program to print the sequence up to 'n' terms
try:
    terms = int(input("How many terms of the Fibonacci series do you want? "))

    if terms <= 0:
        print("Please enter a positive integer greater than 0.")
    else:
        print("Fibonacci sequence:")
        # Loop to calculate and print each term in the series
        for i in range(terms):
            print(fibonacci(i), end=" ")
        print() # Adds a clean newline at the end

except ValueError:
    print("Invalid input. Please enter a whole number.")