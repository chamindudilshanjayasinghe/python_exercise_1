# Exercise 3: Property Tax
# A program to calculate assessment value and property tax.

# Input actual property value
actual_value = float(input("Enter the actual value of the property: $"))

# Assessment value is 60% of actual value
assessment_value = actual_value * 0.60

# Tax is $0.72 for each $100 of assessment value
tax = (assessment_value / 100) * 0.72

# Display results
print(f"Assessment value: ${assessment_value:,.2f}")
print(f"Property tax: ${tax:,.2f}")
