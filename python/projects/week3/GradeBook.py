# for handling mathematical operations
import math

# Function to validate score
def check_score(score):
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100.")
    return score

# Function to convert score to grade
def get_grade(score):
    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    else:
        return "F"

# Dictionary to hold students and scores
gradebook = {}

# Input loop
while True:
    name = input("Enter student name (or 'done' to finish): ").strip().title()
    if name.lower() == "done":
        break
    # raise error for an invalid score using a try/except block
    try:
        score = float(input(f"Enter score for {name}: "))
        score = check_score(score)
    except ValueError as e:
        print("Invalid score:", e)
        continue
    else:
        gradebook[name] = score

# Print results
for student, score in gradebook.items():
    print(f"{student:<10} {score:.1f}  {get_grade(score)}")

# Avoid floating-point precision loss using `math.fsum()`
# Avoid calculation if an empty dictionary
if gradebook:
    scores = list(gradebook.values())
    average = math.fsum(scores) / len(scores)
    highest = max(scores)
    print("Average:", round(average, 1))
    print("Highest:", round(highest, 1))
