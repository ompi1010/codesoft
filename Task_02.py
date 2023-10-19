#****TASK 02****
#****CALCULATOR****
def calculator():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print("\nAvailable operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    operation = input("Choose an operation (1/2/3/4): ")

    if operation == "1":
        result = num1 + num2
        print("Result:", result)
    elif operation == "2":
        result = num1 - num2
        print("Result:", result)
    elif operation == "3":
        result = num1 * num2
        print("Result:", result)
    elif operation == "4":
        if num2 != 0:
            result = num1 / num2
            print("Result:", result)
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation choice.")

calculator()
