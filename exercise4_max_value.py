# Exercise 4: Maximum of Two Values
# Function that returns the maximum of two numbers

def evaluate_max(a, b):
    """Return the greater of two numbers"""
    return a if a > b else b

# Ask for input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Get max value
result = evaluate_max(num1, num2)

# Display result
print(f"The greater value is: {result}")
