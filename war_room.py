"""
This script is going to become a calculator with multiple features
Multiple team members are going to work here together
To deliver different features
"""
# Declaration
num_1 = 0
num_2 = 0
operator = ""
result = 0

# Input
num_1 = input("Enter 1st Number: ")
operation = input("Enter the Operator: ")
num_2 = input("Enter 2nd Number: ")

# Process

if operation == "+":
    result = int(num_1) + int(num_2)
elif operation == "-":
    result = int(num_1) - int(num_2)  # Storing Subtraction Result
elif operation == "*":
    result = int(num_1) * int(num_2)  # Storing Subtraction Result
elif operation == "/":
    result = int(num_1) / int(num_2)  # Storing Subtraction Result
elif operation == "fac":
    answer = 1
    limit = int(num_1)
    while limit > 0:
        answer = answer * limit
        limit = limit - 1
    result = answer
elif operation == "**":
    result = int(num_1) ** int(num_2)  # Storing Subtraction Result

# Output
print("Result is:", result)