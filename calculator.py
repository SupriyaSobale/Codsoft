# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    return x / y

# Get user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Choose an operation (+, -, *, /): ")

# Perform calculation based on operation choice
if operation == '+':
    result = add(num1, num2)
elif operation == '-':
    result = subtract(num1, num2)
elif operation == '*':
    result = multiply(num1, num2)
elif operation == '/':
    result = divide(num1, num2)
else:
    print("Invalid operation choice")
    exit()

print(f"Result: {result}")
