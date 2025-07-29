#basic calculator program
# This is a simple calculator that performs basic arithmetic operations.
# It takes two numbers and an operation as input from the user and outputs the result.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2
else:
    result = "Invalid operation"

print(f"{num1} {operation} {num2} = {result}")
# End of Calculator.py

#advanced calculator program
# This is an advanced calculator that performs various mathematical operations.
import math

def advanced_calculator():
    print("Advanced Calculator")
    print("Select operation:")
    print("1. Square Root")
    print("2. Power")
    print("3. Logarithm")
    print("4. Sine")
    print("5. Cosine")
    print("6. Tangent")

    choice = input("Enter choice (1-6): ")

    if choice in ['1', '2', '3', '4', '5', '6']:
        num = float(input("Enter number: "))
        if choice == '1':
            result = math.sqrt(num)
        elif choice == '2':
            power = float(input("Enter power: "))
            result = math.pow(num, power)
        elif choice == '3':
            result = math.log(num)
        elif choice == '4':
            result = math.sin(num)
        elif choice == '5':
            result = math.cos(num)
        elif choice == '6':
            result = math.tan(num)
    else:
        result = "Invalid operation"

    print(f'Result: {result}')
# Call the advanced calculator function
advanced_calculator()