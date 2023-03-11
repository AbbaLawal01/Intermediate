# Tittle: CGPA Calculator
# CGPA Calculator with 5-point grading scale

# Step 1: Get the number of courses from the user
num_of_courses = int(input("Enter the number of courses: "))

# Step 2: Initialize variables for total credits and total grade points
total_credits = 0
total_grade_points = 0

# Step 3: Loop through each course to get the credit hours and grade
for i in range(num_of_courses):
    credits = int(input(f"Enter the credit units for course {i+1}: "))
    grade = input(f"Enter the grade for course {i+1}: ").upper()

    # Step 4: Calculate the grade points for each course based on the 5-point grading scale
    if grade == "A":
        grade_points = 5.0
    elif grade == "B":
        grade_points = 4.0
    elif grade == "C":
        grade_points = 3.0
    elif grade == "D":
        grade_points = 2.0
    elif grade == "E":
        grade_points = 1.0
    else:
        grade_points = 0.0

    # Step 5: Update the total credits and total grade points for all courses
    total_credits += credits
    total_grade_points += (credits * grade_points)

# Step 6: Calculate the CGPA using the formula: CGPA = Total Grade Points / Total Credits
cgpa = total_grade_points / total_credits

# Step 7: Print the CGPA
print(f"Your CGPA is {cgpa:.2f}")