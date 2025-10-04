# Exercise 5: Test Average and Grade
# A program that calculates average test score and letter grades.

# Function to calculate average of 5 test scores
def calc_average(scores):
    return sum(scores) / len(scores)

# Function to determine grade
def determine_grade(score):
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score <= 89:
        return "B"
    elif 70 <= score <= 79:
        return "C"
    elif 60 <= score <= 69:
        return "D"
    else:
        return "F"

# Input 5 test scores
scores = []
for i in range(5):
    score = float(input(f"Enter test score {i+1}: "))
    scores.append(score)

# Print grade for each score
for i, s in enumerate(scores, start=1):
    print(f"Test {i}: {s} → Grade {determine_grade(s)}")

# Calculate average
average = calc_average(scores)
print(f"Average score: {average:.2f}")
print(f"Overall grade: {determine_grade(average)}")
