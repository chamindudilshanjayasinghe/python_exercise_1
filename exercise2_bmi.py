# Exercise 2: BMI Calculator
# This program calculates Body Mass Index (BMI) using weight and height.
# It also classifies the result into categories.

import math

# Input values
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

# BMI formula
bmi = weight / math.pow(height, 2)

# Display BMI value
print(f"Your BMI is: {bmi:.2f}")

# Classification
if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi <= 24.99:
    print("You have normal weight.")
elif 25 <= bmi <= 29.99:
    print("You are overweight.")
else:
    print("You have obesity.")
