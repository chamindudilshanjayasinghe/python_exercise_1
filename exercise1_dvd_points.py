# Exercise 1: DVD Club Points
# This program asks the user for the number of DVDs purchased in a month
# and calculates how many points they earn.

# Get input from user
dvd_count = int(input("Enter the number of DVDs purchased this month: "))

# Determine points
if dvd_count == 0:
    points = 0
elif dvd_count == 1:
    points = 2
elif dvd_count == 2:
    points = 5
elif dvd_count == 3:
    points = 10
else:
    points = 25

# Display result
print(f"You earned {points} points this month.")
