def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "❌ Error: Cannot divide by zero."
    return a / b

def get_number(prompt):
    # Repeat this block of code forever, unless we manually return or break from inside
    # So the function will keep looping until the user gives a valid number.
    while True: 
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    while True:
        print("Select an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Quit (q)")

        operation = input("Enter the operation: ")

        num1=get_number("Enter the first number: ")
        num2=get_number("Enter the second number: ")
 

        if operation == "q":
            break
        elif operation == "1":
            result = add(num1, num2)
        elif operation == "2":
            result = subtract(num1, num2)
        elif operation == "3":
            result = multiply(num1, num2)
        elif operation == "4":
            result = divide(num1, num2)
        
        print("Result:", result)


if __name__ == "__main__":
    main()